# solidation logo revision

Recommended: **Conversation S**, two alternating voices forming one initial.
The tapered terminals suggest conversation tails; their shared S silhouette
turns separate discussions into a single account. A narrow transparent contour
gap keeps the voices separate in monochrome. The mark has no enclosing tile.

## Research and name analysis

[The project README](https://github.com/con/solidation) identifies the real
operation: producing Markdown reports of issue and pull-request activity
across repositories. Its audience is maintainers reviewing recent work.
The visible CON project collection has varied identities rather than one icon
system: the locally inspected DataLad mark uses interlocked lettering and
angular cuts, while pyout uses a brace/prompt composition.
[GitHub's official iconography guidance](https://brand.github.com/graphic-elements/iconography)
places Octicons in a utility-interface role. The proposal avoids borrowing a
GitHub glyph or presenting a generic document icon as the project identity.
[DataLad](https://www.datalad.org/) supplies relevant ecosystem context.

The initial S offers two opposing curves and open counters. The full name's
repeated o forms and upright l/d/t strokes would make a balanced wordmark, but
an isolated S is more useful for the requested project icon. The con/solidation
name also reads as consolidation: separate voices becoming a coherent whole.
No extra lettering or font dependency is necessary.

## Concepts and refinement

- A: Conversation S. Selected for recognizability, specificity and compactness.
- B: Summary sigma. A typographic summation symbol and consolidated output
  square. Clear reduction/summary metaphor, but less specific to the name.
- C: Collected voices. A C embracing three report lines. Useful alternate,
  though less distinctive than A and more likely to read as a generic C/E.

The first editorial B read as a lowercase b or a numeral 5 and was replaced by
sigma. Peer critique from the fscacher agent favored A and identified the
monochrome overlap as its weakness. A second round shortened the center
terminals; a third tested diagonal separation, then rejected it because it
broke the S into disconnected hooks. The final contour gap preserves the
silhouette and gives each voice its own edge. The parent independently
reviewed and favored the contour-gap refinement.

## Production assets and usage

`assets/project-icon.svg` is the selected color version.
`assets/project-icon-monochrome.svg` uses charcoal.
`assets/project-icon-reversed.svg` uses white.
Three standalone alternatives are in `assets/logo-concepts/`.

Purple #7955B5 (RGB 121,85,181) and coral #E87659 (RGB 232,118,89) distinguish
solidation from the ecosystem's orange, green, and blue marks while maintaining
a warm editorial character. Use white for maximum contrast on dark surfaces.
Minimum size is 16px; at 16px the S silhouette carries recognition, while the
two-voice contour is clearer at 24px and above. Retain at least 12 viewBox units
of external clear space; never squeeze the mark or add a tile around it.

## Verification

Rendered and visually inspected the final color, charcoal, and white variants
at 16, 64, and 512 pixels on light and dark presentation surfaces. All SVGs use
responsive viewBoxes, title/description accessibility metadata, and vector
paths, with no font, raster, script, or filter dependency. A simple mask makes
the voice gap transparent. The first final render exposed librsvg's lack of
CSS variable fill support; literal fills in one style block corrected it.
Final previews: `final-validation.png`, plus individual size renders.

Successful final duct capture:
`/Users/johnlee/.local/state/con-duct/projects/orinoco-lite-dev-db65ce7ce2c2d102/20261013T011351.415446Z-2c4a055affff4d5aa8be7ae65e47c6dd/`
The temporary Pillow import failure was resolved with the bundled Python
runtime; failed capture and source files remain local for review.
No commits, pushes, or PR edits were performed by this design agent.
