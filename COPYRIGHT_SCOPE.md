# Copyright Scope

## Signora AI – Safety-Aware Hierarchical ISL Motion Retrieval and Playback Engine

**Version:** 1.0  
**Repository:** `Signora_AI_Retrieval_Engine-v1.0`

---

## 1. Purpose

This document defines the scope of original software and related materials developed for the Signora AI Retrieval Engine.

The project implements a retrieval-based system for converting railway announcements into sequences of Indian Sign Language motion assets for playback through a 3D avatar.

The copyright claim relates to the original expression and implementation contained in the project source code, documentation, tests, schemas, and other independently authored software materials.

---

## 2. Original Software Components

Subject to authorship verification, the original project software includes implementation of the following components.

### Announcement Processing

- Railway announcement input processing
- Text normalization
- Announcement-type handling
- Structured announcement processing
- Critical entity processing
- Railway-specific processing rules

### ISL Processing

- ISL-oriented gloss processing
- Lexical normalization and recovery
- Mapping between announcement information and supported motion concepts
- Handling of railway-specific vocabulary

### Hierarchical Motion Retrieval

The system implements hierarchical motion retrieval using available representations such as:

1. Sentence-level retrieval
2. Phrase-level retrieval
3. Word-level retrieval
4. Number handling
5. Alphabet-based fingerspelling fallback

Original implementation may include:

- Retrieval policies
- Search orchestration
- Catalog lookup
- Retrieval ranking
- Matching logic
- Fallback rules
- Alias handling
- Metadata lookup
- Motion-selection logic

### Safety-Related Processing

Original software may include:

- Critical-field validation workflows
- Railway information consistency checking
- Retrieval guards
- Validation policies
- Handling of inconsistent or unsupported announcement information

### Motion Selection and Playback

Original implementation may include:

- Motion manifest handling
- Playback-sequence construction
- Motion ordering
- Transition-related selection logic
- GLB asset lookup
- Playback orchestration
- Avatar playback integration
- Rig validation

### Library and Motion Management

Original project code may include:

- Motion-library indexing
- Metadata management
- Motion version management
- Library workflows
- Asset inventory handling
- Upload/replacement workflows
- Motion lifecycle handling

### Backend and APIs

Original code may include:

- FastAPI endpoints
- Application-specific request/response schemas
- Database integration
- Retrieval APIs
- Announcement APIs
- Playback APIs
- Library APIs
- Display-routing logic
- Live delivery logic

### Frontend

Original frontend code may include:

- Announcement interface
- Avatar viewer
- Motion-library interface
- Display-control interface
- Administrative interface
- Playback controls
- Railway control-room functionality
- Project-specific client-side services

### Testing and Evaluation

Original project materials may include:

- Unit tests
- Integration tests
- Retrieval evaluation scripts
- Performance benchmarking scripts
- Safety-validation tests
- Motion-playback tests
- Scalability tests
- Research evaluation utilities

### Documentation

Original documentation may include:

- Project README
- Architecture documentation
- Setup documentation
- Technical workflow descriptions
- Testing documentation
- Original diagrams and explanatory material

---

## 3. Motion Processing Pipeline

The Signora AI project also uses a motion-processing workflow broadly involving:

```text
Sign-language video
        ↓
Pose / motion processing
        ↓
BVH skeletal motion
        ↓
Custom Blender/Python processing
        ↓
GLB motion asset
        ↓
Metadata creation
        ↓
Signora motion library
```

Original scripts independently written by project authors for processing, converting, validating, organizing, or importing these motion assets may form part of the project's copyrighted software.

Third-party tools used within this workflow remain the property of their respective copyright holders.

---

## 4. Excluded Third-Party Components

The project does not claim copyright ownership over third-party software, services, frameworks, models, or other materials.

Examples include, where applicable:

- Python
- FastAPI
- React
- Next.js
- Three.js
- MediaPipe
- Rokoko software
- Blender
- OpenAI Whisper
- Third-party Python packages
- npm packages
- Pretrained machine-learning models
- External APIs
- External fonts, icons, or UI assets

Use of these technologies does not constitute a claim of ownership over them.

See `THIRD_PARTY_NOTICES.md`.

---

## 5. Motion Asset Ownership

Motion assets must be considered separately from software source code.

For each GLB, BVH, video, or related motion asset, ownership and licensing should be determined from:

- Original video source
- Original recording ownership
- Dataset licence
- Permission to create derivative motion data
- Conversion history
- Manual modifications
- Contributor information

Motion-asset provenance is documented in:

`PROVENANCE.md`

The project does not claim exclusive ownership of source material owned by third parties merely because it was processed or converted into another file format.

---

## 6. Copyright and Ideas

Copyright protection applies to the original expression and implementation of the software.

It does not by itself provide exclusive rights over abstract ideas such as:

```text
Sentence → Phrase → Word → Number → Fingerspelling
```

or the general concept of retrieving motion clips.

Protection of a technical method or process may require separate patent analysis.

---

## 7. Copyright Filing Version

The repository version intended for copyright registration should be permanently identified.

**Software title:**  
Signora AI – Safety-Aware Hierarchical ISL Motion Retrieval and Playback Engine

**Version:** 1.0

**Git Tag:**  
`copyright-v1.0`

**Git Commit Hash:**  
`[INSERT FINAL COMMIT HASH]`

**Release Date:**  
`[INSERT DATE]`

---

## 8. Declaration

Only material independently authored by the identified project contributors should be represented as original Signora AI software.

Third-party components, externally sourced data, and externally owned assets remain subject to their respective licences, permissions, and intellectual-property rights.