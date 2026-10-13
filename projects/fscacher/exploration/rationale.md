# fscacher icon proposal: fingerprint f

Selected: `assets/project-icon.svg` — a lowercase f formed from three open fingerprint ridges. The center stroke is both the function initial and one ridge; this is one integrated mark rather than a file glyph with an attached cache symbol.

## Research and brief

The project [README](https://github.com/con/fscacher) describes persistent memoization keyed by function arguments and a file fingerprint. Identity, recognition, and remembering are therefore better starting points than storage capacity or generic circular refresh arrows. Audience: researchers and Python developers using file-dependent analyses.

The [CON projects page](https://centerforopenneuroscience.org/projects) deliberately accommodates distinct project identities. Local source logos inspected: DataLad (strong angular custom letters, orange/charcoal), pyout (code punctuation), duecredit (interlocking letters), DANDI (illustrated brain in a hat). These favor specific visual ideas over uniform app tiles. The [DataLad site](https://www.datalad.org/) provides the official context for the related data-management ecosystem. This proposal takes their specificity and typographic craft as a standard, without copying their graphics.

Letter analysis: lowercase f has an ascender, arched shoulder, and crossbar; the c forms in fscacher are open, rounded containers; the fs pair offers a moving path. The f shoulder maps naturally onto a fingerprint arch. Three candidate directions explored those structures:

- A / Fingerprint f: function identity inside repeated ridges. Recommended.
- B / Memory seed: an f cut into a cached acorn. Charming and clear silhouette, but implies finance/nature more than file identity.
- C / Recall: an architectural F with a returning terminal. Strong at small sizes, but less distinctive and can read FJ.

## Peer review and refinement

Both solidation and annextube design agents independently selected A. Critique identified small-size ridge spacing and a possible ear/paperclip reading. Two additional weight/terminal variants were rendered. The selected version increases stroke weight from 16 to 18 units while shortening the two lower returning curves by five units. This strengthens 16 px rasterization and reduces the elongated ear-like lower tail. The third 20-unit version crowded the ridges.

Color: teal #087E8B, RGB 8/126/139. The primary is inherently one-color, with dark #202020 and white reversed variants. Use the reversed mark on dark backgrounds when maximum clarity is needed. The use of fixed stroke values avoids SVG engines that do not support CSS custom properties.

## Delivery and validation

Repository assets: project-icon.svg, project-icon-mono.svg, project-icon-reversed.svg, plus the two alternatives in assets/logo-concepts/. No fonts, bitmap images, filters, dependencies, or hardcoded root dimensions. SVGs include accessible names/descriptions and a 256-unit viewBox. Each final variant renders successfully at 16, 64, and 512 px. `final-specimen.png` shows primary, dark-background, monochrome, and reversed contexts. Visually inspected the selected 512 px output and contact/specimen sheets. At 16 px it remains recognizable as a fingerprint, with the f reading more clearly at 24 px and larger. Minimum recommended mark size: 16 px; normal project-card use: 64 px or larger. Preserve the viewBox padding and allow at least one ridge-width of additional clear space. Do not add rings or compress its aspect ratio.

Duct runs (all exit 0):
- /Users/johnlee/.local/state/con-duct/projects/fscacher-ad49411292c7b308/20261013T011159.230126Z-408c23040b6049e59f94fbd92a88caf6
- /Users/johnlee/.local/state/con-duct/projects/fscacher-ad49411292c7b308/20261013T011236.775003Z-ed510034466b4650b3f14cb24fe88bfc
- /Users/johnlee/.local/state/con-duct/projects/fscacher-ad49411292c7b308/20261013T011255.312704Z-d39a6081569641f2afa6c6ed6bde9cf2

No commits, push, or PR edits performed by this agent. Parent handles Workshop feedback and publication.
