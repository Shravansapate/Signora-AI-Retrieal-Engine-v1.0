Motion Asset Provenance

Motion creation pipeline:

Source ISL Video
→ Pose / motion extraction
→ MediaPipe / Rokoko processing
→ BVH skeletal motion
→ Custom Blender Python conversion and retargeting
→ GLB
→ Metadata generation
→ Signora motion library

For every asset record:

- Motion ID
- Sign/gloss
- Original video source
- Original video owner
- Permission/license
- BVH generation method
- GLB conversion script version
- Conversion date
- Human/manual corrections
- Final GLB hash