from pathlib import Path
import subprocess

root = Path('/tmp/con-project-icon-proposals')
descriptions = {
    'annextube': ('Tape a', 'A custom lowercase a holds a transparent play aperture. The continuous bowl and curled foot suggest retained playable media and tape, reflecting complete channel archival and offline browsing.', [('Playback spool', 'An open loop enclosing play; the more abstract retention direction.'), ('Archive reel', 'Two reels and a tape path; the more figurative archival direction.')]),
    'fscacher': ('Fingerprint f', 'Three open fingerprint ridges integrate the function initial. This connects directly to persistent memoization keyed by file fingerprints.', [('Memory seed', 'An acorn with an f counter; a warmer metaphor for retained results.'), ('Recall', 'An architectural F with a returning terminal; a more abstract monogram.')]),
    'solidation': ('Conversation S', 'Two conversation forms combine into one S. A transparent contour gap preserves the separate voices in monochrome, reflecting issue and pull-request activity consolidated into a Markdown account.', [('Summary sigma', 'Summation and consolidated output; a typographic summary metaphor.'), ('Collected voices', 'A C embraces report lines; a more literal collection direction.')]),
    'tinuous': ('Record ribbon', 'A continuous strip coils into a lasting record. Cut terminals and an open upper end emphasize a physical strip and continuity, reflecting preservation of CI logs, artifacts, and release assets.', [('Open rounded ribbon', 'A softer, more open treatment of the same retention metaphor.'), ('Time vessel', 'An hourglass connecting passing time and retained output; a more literal alternative.')]),
}
for name, (title, desc, alternatives) in descriptions.items():
    if not title:
        continue
    repo = root / 'checkouts' / name
    sha = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
    owner = 'con' if name == 'solidation' else 'leej3'
    body = f'''**AI-generated draft — not reviewed by John**

Propose **{title}** as the primary project mark. {desc}

<img src="https://raw.githubusercontent.com/{owner}/{name}/{sha}/assets/logo-concepts/comparison.png" width="900" alt="Recommended {name} logo and two alternatives">

The comparison shows the recommended mark first, followed by two distinct alternatives:

'''
    body += '\n'.join(f'- **{t}**: {d}' for t, d in alternatives)
    body += '''

Includes editable standalone SVGs and monochrome/reversed treatments. Each concept was developed by an Astra agent at medium effort using the logo-design skill, project documentation, and existing CON/field logos as references, then refined through peer critique. These are proposals for maintainer selection or revision.

Validation: SVG XML parses; the selected mark was rendered and visually inspected at 16, 64, and 512 pixels on light/dark backgrounds and in monochrome. No font, raster, or external resource dependencies. Runtime behavior is unchanged.
'''
    if name != 'annextube':
        body += '\nRepository pre-commit checks pass for the added assets.\n'
    (root / f'{name}-revised-pr-body.md').write_text(body)
