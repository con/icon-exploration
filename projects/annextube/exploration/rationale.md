# annextube project icon proposal

Recommend **C — Tape a**: a custom lowercase `a` with a triangular play
counter. Its substantial continuous bowl suggests held media; the curled foot
recalls tape leaving a spool. The letter is the primary identity, and playable
video is the immediate secondary reading. Archival meaning is suggestive rather
than a claim that a new viewer will decode every operation.

## Evidence and visual direction

- [Project README](https://github.com/con/annextube): complete channel archival,
  including videos, metadata, comments and captions; incremental updates and
  offline browsing. This favors retained playable media over a download arrow.
- [git-annex](https://git-annex.branchable.com/): distributed storage, offline
  availability and long-term access ground the preservation interpretation.
- [YouTube brand resources](https://brand.youtube/): the familiar play triangle
  is useful visual vocabulary, but the red rounded player badge is too close
  to the source service. The proposal uses a letter silhouette and blue instead.
- [DataLad](https://www.datalad.org/): contextual distributed-data reference,
  not a source of borrowed geometry.
- The actual CON vector at `site-specific/static/img/con-logo.svg` was rendered
  and inspected. Its blue and negative-space brain within a letter suggest a
  restrained family relationship: meaningful counters, not identical frames.
  The CON logo uses #87AADE; the primary proposal deepens blue to #3578A8 for
  white backgrounds. A #87AADE treatment was checked on dark backgrounds.

Name analysis: the initial lowercase `a` offers an enclosed counter; the
repeated `nn` offers an arch rhythm but little unique archival meaning; `x`
suggests crossing but would overemphasize transfer; the `u` in `tube` offers a
holding trough. The `a` best combines name recognition and a video aperture.
No font is required: all lettering is custom path geometry.

## Three directions and refinement

A, **Playback spool**, places a play triangle inside an open tape loop. It has
clear retention/motion associations but risks reading as a generic player.
B, **Archive reel**, uses two reels and a tape path. It explicitly references
archival media but can read as an owl; it is the intentionally figurative
alternative, not the recommendation.
C, **Tape a**, is the strongest compact silhouette and works in one ink.

Peer critique from the fscacher design agent independently preferred C and
flagged its initial `q` reading. The second pass raised the right stem to cap
height and gave the foot a controlled curve. This made the lowercase `a`
unambiguous without reducing the play aperture. The original C iteration
remains outside the repository for comparison. A and B remain optional proposal
alternatives under `assets/logo-concepts/`.

## Deliverables and validation

`assets/project-icon.svg` is the recommended primary; monochrome and white
reversed variants are adjacent. All are transparent, responsive, accessible
SVGs with no fonts, raster images, filters or dependencies. The primary is a
single filled compound path with a genuine transparent counter.

Rendered all three concepts at 16, 64 and 512 px on light, dark and one-ink
backgrounds (27 checks). Visually inspected the large individual renders, the
contact sheet and the actual 16 px primary. At 16 px the stem remains visible
and the triangular opening survives; 24 px or larger is preferable for a
prominent project mark. Reserve at least 24 viewBox units of surrounding clear
space. Preserve the aspect ratio and the aperture; do not add a tile.

Final duct validation passed:
`/Users/johnlee/.local/state/con-duct/projects/annextube-39348a314b3c7ecf/20261013T011251.046570Z-698fb068cb7246c6ac7d75f4bdf7d0d4/`.

Palette: primary #3578A8 (53,120,168), dark-display blue #87AADE
(135,170,222), monochrome #20252B (32,37,43), reversed #FFFFFF.

This is a local project-icon proposal, not an adopted identity or trademark
clearance. No commit, push or PR modification was performed by this agent.
