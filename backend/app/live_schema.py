"""Versioned publication and display protocol; credentials never enter persisted events."""

from typing import Annotated, Literal
from uuid import UUID

from pydantic import Field, StringConstraints, model_validator

from app.announcement_schema import AnnouncementPlan
from app.lifecycle_schema import ReviewText
from app.retrieval.playback_schema import Digest, PlaybackPlan, WireModel

Label = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=160)]


class Publication(WireModel):
    station_id: Label
    source_event_id: Label
    source_revision: int = Field(ge=1, le=2147483647)
    expected_revision: int = Field(ge=0)
    preview_manifest_id: UUID | None = None
    preview_manifest_hash: Digest | None = None
    cancel: bool = False
    reason: ReviewText

    @model_validator(mode="after")
    def content(self):
        if self.cancel == bool(self.preview_manifest_id) or (
            not self.cancel and not self.preview_manifest_hash
        ):
            raise ValueError("Supply a reviewed preview or an explicit cancellation")
        return self


class LiveContext(WireModel):
    message_id: UUID
    revision: int = Field(ge=1)
    source_event_id: Label
    source_revision: int = Field(ge=1)
    priority: int = Field(ge=0, le=3)
    supersedes_revision: int | None = None


class LivePlan(AnnouncementPlan):
    schema_version: Literal[4] = 4
    purpose: Literal["PUBLISHED"] = "PUBLISHED"
    operational: Literal[True] = True
    delivery: LiveContext


class DevelopmentAnnouncement(WireModel):
    station_id: Label
    input_id: UUID


class DevelopmentLivePlan(PlaybackPlan):
    """Local development delivery, without invented linguistic review records."""

    schema_version: Literal[5] = 5
    purpose: Literal["PUBLISHED"] = "PUBLISHED"
    operational: Literal[True] = True
    development: Literal[True] = True
    announcement: DevelopmentAnnouncement
    delivery: LiveContext


class DeviceRegistration(WireModel):
    station_id: Label
    subject: Label
    name: Label
    expected_revision: int = Field(ge=0)
    enabled: bool = True


class DisplayHello(WireModel):
    type: Literal["HELLO"]
    token: Annotated[str, StringConstraints(min_length=1, max_length=512)]
    cursor: int = Field(ge=0)


class DisplayAck(WireModel):
    type: Literal["ACK", "HEARTBEAT"]
    cursor: int = Field(ge=0)
    manifest_id: UUID | None = None
    state: Literal["RECEIVED", "ASSETS_READY", "STARTED", "COMPLETED", "FAILED"] | None = None
    boundary: int = Field(default=-1, ge=-1, le=63)
    error_code: Annotated[str, StringConstraints(pattern=r"^[A-Z0-9_]{1,64}$")] | None = None
