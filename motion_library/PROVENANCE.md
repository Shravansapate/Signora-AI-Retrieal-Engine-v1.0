# Motion Asset Provenance

## Signora AI – Safety-Aware Hierarchical ISL Motion Retrieval and Playback Engine

**Version:** 1.0  
**Repository:** `Signora-AI-Retrieval-Engine-v1.0`  
**Git Tag:** `copyright-v1.0`  
**Git Commit:** `14a25dc95130be41cba31a304ec660c0044c4874`  
**Release / Freeze Date:** 29 September 2026  
**Frozen Commit Date:** Tue Sep 29 13:50:03 2026 +0530

---

## 1. Purpose

This document records the origin, ownership status, metadata relationship, and use of motion assets included in the Signora AI Retrieval Engine.

Its purpose is to maintain traceability between:

- Source ISL motion assets
- Final GLB motion files
- Metadata records
- Motion-library entries
- Retrieval-system usage

This document also distinguishes project-created materials from third-party or externally sourced assets.

---

## 2. Motion Library

The Signora AI Retrieval Engine uses a structured motion library containing GLB motion assets and associated metadata.

The motion library supports retrieval at multiple semantic levels, including:

- Sentence-level motions
- Phrase-level motions
- Word-level motions
- Number motions
- Alphabet motions
- Fingerspelling fallback
- Railway-specific vocabulary

Example directory structure:

```text
motion_library/
├── glb/
├── metadata/
└── PROVENANCE.md
```

---

## 3. Motion Asset Sources

Each GLB motion asset should have a documented source.

For each asset, record:

- Motion ID
- Gloss or concept
- GLB filename
- Source owner
- Source reference
- Licence or permission status
- Whether the asset was created by the project team or obtained externally

The presence of a GLB file in this repository does not by itself establish ownership of all underlying source material.

---

## 4. Source Classification

Each motion asset should be classified using one of the following categories.

### PROJECT_OWNED

The asset was created by the Signora AI project team and the team possesses the necessary rights to use and distribute it.

### LICENSED_EXTERNAL

The asset originated from an external source, but the applicable licence or written permission allows its use.

### RESEARCH_ONLY_EXTERNAL

The asset was obtained for academic or research use, but redistribution or derivative-use rights have not yet been fully verified.

### UNKNOWN

The source or licence has not yet been verified.

Assets marked `UNKNOWN` should not be represented as exclusively owned Signora AI assets until their provenance has been resolved.

---

## 5. GLB Motion Assets

The final motion library contains GLB motion files used by the retrieval and avatar-playback system.

Examples may include:

```text
Train.glb
Arrive.glb
Platform.glb
Luggage.glb
1_One.glb
2_Two.glb
3_Three.glb
...
1000_Thousand.glb
```

Each GLB represents a motion concept available to the Signora AI retrieval engine.

The copyright and ownership status of each asset depends on its actual source and applicable licence or permission.

---

## 6. Motion Metadata

Each GLB motion may be associated with a metadata file such as:

```text
Train.metadata.json
Arrive.metadata.json
Platform.metadata.json
1_One.metadata.json
```

Metadata may contain project-created information such as:

- Motion identifier
- Canonical concept name
- Gloss
- Aliases
- Domain
- Retrieval level
- Verification status
- Motion filename
- Version information
- Search information
- Playback information

Where this metadata was independently created and organized by the Signora AI team, it may be treated as project-created material.

Externally sourced linguistic or dataset information should be separately documented where applicable.

---

## 7. Recommended Motion Record

Maintain a record for each production motion asset using the following format:

```text
Motion ID:
Gloss:
Concept:

Final GLB:
Metadata File:

Source Owner:
Source Reference:
Source Licence:
Source Classification:

Metadata Created By:
Validated By:

Final SHA-256 Hash:

Notes:
```

---

## 8. Example Motion Record

The following is an example only and must be replaced with accurate information.

```text
Motion ID: ISL_TRAIN_001

Gloss: TRAIN
Concept: TRAIN

Final GLB: Train.glb
Metadata File: Train.metadata.json

Source Owner: [INSERT OWNER]
Source Reference: [INSERT SOURCE]
Source Licence: [INSERT LICENCE]
Source Classification: [PROJECT_OWNED / LICENSED_EXTERNAL / RESEARCH_ONLY_EXTERNAL / UNKNOWN]

Metadata Created By: [INSERT NAME]
Validated By: [INSERT NAME]

Final SHA-256 Hash: [INSERT HASH]

Notes:
Railway vocabulary motion used by the Signora AI retrieval engine.
```

---

## 9. Metadata and Library Contributions

The following types of work may be original project contributions where independently created:

- Motion metadata
- Canonical concept naming
- Alias definitions
- Railway-specific categorization
- Retrieval-level classification
- Motion-library organization
- Verification status
- Version management
- Search-related metadata
- Playback-related metadata

These contributions should be distinguished from any externally sourced motion content.

---

## 10. Third-Party Assets

The Signora AI project does not automatically claim ownership over:

- Third-party GLB assets
- External ISL motion datasets
- External sign-language recordings
- External 3D assets
- Third-party animation files
- Third-party linguistic data

Such material remains subject to its respective copyright holders, licences, and permissions.

For further information, see:

```text
THIRD_PARTY_NOTICES.md
```

---

## 11. Motion Asset Copyright Scope

The software copyright claim for Signora AI primarily concerns the original source-code implementation of the retrieval system.

Motion assets are included in the project only to the extent necessary for operation, testing, demonstration, and retrieval.

Motion assets should be claimed as original project material only where the project authors possess the necessary rights.

---

## 12. Integrity and File Hashes

Important motion assets may be hashed to preserve evidence of the exact files included in the frozen release.

Example PowerShell command:

```powershell
Get-FileHash ".\motion_library\glb\Train.glb" -Algorithm SHA256
```

Example metadata hash:

```powershell
Get-FileHash ".\motion_library\metadata\Train.metadata.json" -Algorithm SHA256
```

The resulting SHA-256 values may be stored with the corresponding provenance records.

---

## 13. Frozen Copyright Version

The motion library documented here corresponds to the following frozen repository state:

```text
Project:
Signora AI – Safety-Aware Hierarchical ISL Motion Retrieval and Playback Engine

Version:
1.0

Git Tag:
copyright-v1.0-final

Git Commit:
46236f85423290ba92a2703bc4158081b044d8c5

Commit Date:
Tue Sep 29 13:50:03 2026 +0530

Release / Freeze Date:
29 September 2026
```

This repository state should be preserved as the reference version associated with copyright preparation.

---

## 14. Related Documentation

This provenance record should be reviewed together with:

```text
AUTHORS.md
COPYRIGHT_SCOPE.md
THIRD_PARTY_NOTICES.md
README.md
ARCHITECTURE_RETRIEVAL.md
```

---

## 15. Final Declaration

The Signora AI team distinguishes its original retrieval software, metadata, documentation, and project-created materials from third-party or externally sourced motion assets.

Only material for which the project authors possess appropriate rights should be represented as original Signora AI intellectual property.

Where asset ownership or licensing remains uncertain, the asset should remain classified as `UNKNOWN` or `RESEARCH_ONLY_EXTERNAL` until the issue is resolved.
