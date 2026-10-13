# con/tinuous logo redesign

The project retrieves CI logs, build artifacts and release assets from GitHub,
Travis, Appveyor and CircleCI. The broader promise is continuity of evidence:
a passing run leaves a record that can be kept. This is the audience's durable
benefit and remains useful if the specific hosting services change.

## Research

- [Project README](https://github.com/con/tinuous): actual functions and optional
  DataLad integration. Read the local README and official GitHub source.
- [GitHub artifact documentation](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflow-artifacts):
  artifacts carry results beyond a workflow run.
- [DataLad](https://www.datalad.org/): viewed the actual project logo from the
  selected CON site. Its orange/charcoal custom letterforms and angular joins
  are specific to the project, rather than part of a compulsory CON template.
- [DANDI](https://dandiarchive.org/): viewed the actual local CON project logo,
  whose brain/hat visual pun demonstrates a memorable independent silhouette.
- [ReproNim](https://repronim.org/): official identity reference in the adjacent
  reproducible-computing field.

The CON collection contains independent marks, not a matching set of dark
rounded app tiles. Borrow the discipline of a recognizable silhouette and a
specific story, without copying those projects' letterforms or symbols.

## Name and letter analysis

The compact lowercase `t` offers a stem/crossbar, but a lone t would be generic.
The paired `n` and `u` are complementary arches; the o/u curves suggest a strip
that turns and continues. `con/tinuous` completes "continuous" across the
namespace separator, so continuation is stronger than literal download.
The repeated curves motivated a coiled strip rather than a forced full acronym.

## Three directions

A — Record ribbon. One continuous strip coils into a retained record. Its open
end allows continuation; the wound center implies collected history. This
avoids a literal current-service logo and the generic arrow-to-tray metaphor.

B — Time vessel. A sculptural hourglass links time and retained output. Strong
at small sizes, but the conventional waiting/loading reading makes it weaker
as a unique identity.

C — Growth record. Concentric log/growth rings turn accumulating records into
an organic metaphor. The radial stem unintentionally resembles a target;
that interpretation is stronger than archival continuity, so reject as primary.

## Refinement and validation

Round one produced three distinct concepts. Round two compared the ribbon's
original soft terminals with cut terminals (physical strip) and a more open,
slightly lighter version (small-size clarity). All are original SVG geometry.

Rendered all five designs with librsvg at 16, 64, and 512 pixels on light and
dark backgrounds and in one ink. Inspected the contact sheet. At 16 pixels the
ribbon keeps its inner channel and single coiled silhouette. Larger displays
show smooth joined curves. No raster images, fonts, external resources,
filters, or fixed root dimensions are included. Each has a viewBox and
accessible title/description.

The initial CSS-variable rendering was black in librsvg; replaced variables
with interoperable color declarations before evaluating geometry. This was a
renderer compatibility repair, not an assumption that an unrendered mark passed.

## Palette and use

Primary burnt orange #BA482C (186, 72, 44); dark-background warm orange #F08B64
(240, 139, 100); monochrome #171717; reversed white #FFFFFF. Warm ink reflects
preservation and accumulated history without requiring a service-specific hue.
Use the supplied monochrome or reversed variant when a colored mark lacks
contrast. Minimum 16 pixels; 24 pixels preferred in dense navigation. Keep
clear space of one stroke width around the visible mark. Do not distort, add
shadows, or put the mark back into a compulsory rounded-square tile.

## Duct evidence

Retain the runs under
`/Users/johnlee/.local/state/con-duct/projects/orinoco-lite-dev-db65ce7ce2c2d102/`:

- `20261013T011406.033188Z-3d3318738f87438f852c1588271aaf00` initial render.
- `20261013T011413.082250Z-a57934d5138041349a01b463820992d3` color repair render.
- `20261013T011433.166699Z-792459e6ccf04bef8c14481511bcbf16` ribbon refinements.
- `20261013T011500.541780Z-3f2576ad243a4664a63ec77c40e07950` 45 renders and SVG checks.

No commits, pushes, or PR edits made by the design agent. Parent consolidates
Workshop feedback and publication.

## Peer critique and final decision

The fscacher designer reviewed the complete comparison and favored the cut-end
ribbon: a physical rolled record, with strong 16px survival. They identified
G/6 readings in the rounded versions and recommended shortening the outer
terminal. The parent preferred the softer A3, while agreeing that the ribbon
was the strongest concept. I retained A3 as the meaningful style alternative
and selected a final A2 refinement with its top end shortened from x=210 to
x=198. This reduces the almost-closed G reading and emphasizes the free strip.
The decision deliberately prioritizes physical archival character over generic
rounded software friendliness. Some abstract G/6 resemblance remains; no
trademark-clearance claim is made.

Final `assets/project-icon.svg` is the cut record ribbon; mono and white
reversed forms sit beside it. `assets/logo-concepts/` retains the open rounded
ribbon and the two different exploratory metaphors. The parent can choose to
omit weaker explorations from publication while the research remains here.
Final geometry was separately rendered and inspected at 16/64/512 pixels in
primary, black, and white forms. Six deliverable SVGs passed structural checks.
The final specimen is `final-validation.png`.

Additional duct runs:

- `20261013T011547.621131Z-8b3a199cc45d400ea375bb40fe7a690f` final refinement render.
- `20261013T011557.631197Z-e9bcf21c4a4a4e89af47b9c8b0d741bc` final deliverable validation.
