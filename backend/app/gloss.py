"""Typed railway sign construction, distinct from English token lookup.

Default rules are a configurable engineering draft, not validated ISL grammar.
Reviewed database recipes remain authoritative when the existing compiler can use them.
"""

import re
from dataclasses import asdict, dataclass

from app.announcement_schema import DevelopmentGlossPolicy
from app.meaning import normalize


@dataclass(frozen=True)
class GlossUnit:
    token: str
    kind: str = "LEXEME"
    role: str = "event"


def construct_gloss(meaning, policy: DevelopmentGlossPolicy):
    if meaning is None:
        return []
    groups = {name: [] for name in policy.order}

    def sign(token, group, kind="LEXEME"):
        groups[group].append(
            GlossUnit(
                policy.lexical_forms.get(token, token) if kind == "LEXEME" else token, kind, group
            )
        )

    def slot(name, group, label=None):
        value = meaning.slots.get(name)
        if not value:
            return
        if label:
            sign(label, group)
        if value.kind == "NAME":
            # Display names, not configured database entity IDs, are lexical input.
            sign(normalize(value.raw)[0].upper(), group, "NAME")
        elif value.kind == "TRAIN_IDENTIFIER":
            sign(value.value, group, "IDENTIFIER")
        elif value.kind == "PLATFORM_IDENTIFIER":
            sign(value.value, group, "PLATFORM_IDENTIFIER")
        elif value.kind == "CLOCK_TIME":
            # A clock is not an arbitrary integer. Without an exact realization,
            # report it missing instead of dropping AM/PM or the colon.
            sign(value.raw.upper(), group, "CLOCK_TIME")
        else:
            sign(value.raw.upper(), group, "NUMBER")

    sign("TRAIN", "entity")
    slot("train_identifier", "entity")
    slot("train_name", "entity")
    relations = getattr(meaning, "relations", {})
    for role, marker in (("source", "FROM"), ("destination", "TO")):
        if role in meaning.slots:
            if relations.get(role) != "event_location":
                sign(marker, role)
            slot(role, role, "STATION")
    if "platform_identifier" in meaning.slots:
        relation = relations.get("platform_identifier", "location")
        if relation == "origin" and meaning.intent == "TRAIN_ARRIVAL":
            sign("FROM", "location")
        elif relation == "destination" and meaning.intent == "TRAIN_DEPARTURE":
            sign("TO", "location")
        slot("platform_identifier", "location", "PLATFORM")
    for name, marker in (("old_platform", "FROM"), ("new_platform", "TO")):
        if name in meaning.slots:
            sign(marker, "location")
            slot(name, "location", "PLATFORM")
    temporal = meaning.temporal_state
    if temporal.startswith("SCHEDULED_"):
        sign("FUTURE", "time")
    elif temporal.startswith("ALREADY_"):
        sign("ALREADY", "time")
    elif temporal in {"ARRIVING_NOW", "DEPARTING_NOW"}:
        sign("NOW", "time")
    if getattr(meaning, "time_modifier", None):
        sign(meaning.time_modifier.upper(), "time")
    slot("clock_time", "time", "TIME")
    if meaning.polarity == "NEGATIVE":
        sign("NOT", "polarity")
    sign(
        {
            "TRAIN_ARRIVAL": "ARRIVE",
            "TRAIN_DEPARTURE": "DEPART",
            "TRAIN_DELAY": "DELAY",
            "TRAIN_CANCELLATION": "CANCEL",
            "PLATFORM_CHANGE": "CHANGE",
        }[meaning.intent],
        "event",
    )
    if "delay_duration" in meaning.slots:
        duration = meaning.slots["delay_duration"]
        match = re.fullmatch(r"([0-9]+) (hours?|minutes?)", duration.value, re.IGNORECASE)
        if match:
            sign(match[1], "duration", "NUMBER")
            sign("HOUR" if match[2].lower().startswith("hour") else "MINUTE", "duration")
        else:
            sign(duration.raw.upper(), "duration", "DURATION")
    return [unit for group in policy.order for unit in groups[group]]


def translation_trace(original, normalized, meaning, issues, units, policy, *, construction=None):
    return {
        "original_input": original,
        "normalized_input": normalized,
        "english_tokens": normalized.split(),
        "semantic_parse": meaning.model_dump(mode="json") if meaning else None,
        "translation_status": "DOMAIN_DRAFT" if meaning else "UNSUPPORTED",
        "construction": construction
        or {
            "source": "STATION_DOMAIN_RULES",
            "rule_id": policy.rule_id,
            "linguistically_validated": False,
            "order": policy.order,
        },
        "translation_issues": [item.model_dump(mode="json") for item in issues],
        "gloss_tokens": [unit.token for unit in units],
        "gloss_units": [asdict(unit) for unit in units],
        "retrieval_tokens": [unit.token for unit in units],
        # Compatibility key now deliberately reflects gloss, never English.
        "tokens": [unit.token for unit in units],
    }
