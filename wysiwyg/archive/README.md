# WYSIWYG Editor Archive

This directory contains previous versions and reference implementations.

---

## Directory Structure

### `previous-versions/`
Older versions of COAIEXIST editors saved for reference and rollback capability.

**Files:**
- `coaiexist-creative-studio-backup.html` - Backup of creative studio before major changes
- `pro-editor-v1.html` - Earlier iteration of the pro editor (1785 lines, simpler version)

### `reference-editors/`
Third-party and reference WYSIWYG editors for inspiration and feature ideas.

**Contents:**
- `COMPARE WITH MOST RECENT ITERATION kidpix-editor (1).html` - Comparison reference
- `editor.html` - Generic reference editor
- `kidpix-editor-backup-20251105.html` - Pre-Phase 1 backup
- `bulma/` - Bulma CSS framework examples
- `richtexteditor/` - Rich text editor reference documentation

---

## Version History

### KidPix Editor Evolution
1. **kidpix-editor-backup-20251105.html** (Nov 5, 2025)
   - Pre-Phase 1 version
   - Canvas was a `<div>` (CSS isolation issues)
   - Original KidPix aesthetic

2. **Current: ../kidpix-editor.html** (Nov 8, 2025)
   - Post-Phase 1 (COMPLETE)
   - Iframe canvas isolation
   - UI overlap fixes
   - Simplified CSS/JS editors
   - Ready for Phase 2 transformation

### Pro Editor Evolution
1. **pro-editor-v1.html** (Archived)
   - 1785 lines
   - Earlier simpler iteration

2. **Current: ../coaiexist-pro-editor.html** (Active)
   - 2791 lines
   - Advanced features
   - Three.js integration for 3D
   - Tone.js for audio

### Creative Studio Evolution
1. **coaiexist-creative-studio-backup.html** (Archived)
   - Pre-refactor backup

2. **Current: ../coaiexist-creative-studio.html** (Active)
   - Streamlined interface
   - Focus on creative workflows

---

## When to Use Archive Versions

### Rollback Scenarios
- Current version has breaking bugs
- Need to reference old implementation
- Compare feature changes

### Research & Learning
- Understand evolution of features
- See how problems were solved
- Extract good ideas from older versions

### Code Archaeology
- Track when specific features were added
- Understand architectural decisions
- Document technical debt origins

---

## Restoration Process

To restore an archived version:

1. **Backup current version first:**
   ```bash
   cp ../kidpix-editor.html ../kidpix-editor-backup-$(date +%Y%m%d).html
   ```

2. **Copy archived version:**
   ```bash
   cp previous-versions/[archived-file].html ../kidpix-editor.html
   ```

3. **Test thoroughly before committing**

---

## Archive Maintenance

### When to Archive
- Before major refactors
- Before Phase transitions
- After significant milestones
- When deprecating features

### Naming Convention
```
[editor-name]-[version/date].html
```

Examples:
- `kidpix-editor-backup-20251105.html`
- `pro-editor-v1.html`
- `creative-studio-backup.html`

### What NOT to Archive
- Duplicate files with no meaningful changes
- Auto-generated backups
- Work-in-progress experiments (use git branches)

---

## Reference Editors

The `reference-editors/` directory contains:

### External References
- **richtexteditor/** - Full-featured rich text editor documentation
  - Useful for understanding advanced text editing features
  - API reference for complex operations
  - Event handling examples

- **bulma/** - CSS framework examples
  - Component styling inspiration
  - Responsive design patterns

### Internal Comparisons
- Comparison files to track changes between iterations
- Help identify regressions or feature additions

---

## Quick Reference

**Need to:**
- **Rollback kidpix-editor?** → Use `previous-versions/kidpix-editor-backup-20251105.html`
- **See simpler pro-editor?** → Check `previous-versions/pro-editor-v1.html`
- **Compare before/after Phase 1?** → Diff current vs `kidpix-editor-backup-20251105.html`
- **Research text editing?** → Browse `reference-editors/richtexteditor/docs/`

---

*Last updated: 2025-11-08*
*Archive policy: Keep all major version milestones indefinitely*
