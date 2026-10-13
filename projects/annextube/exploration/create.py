from pathlib import Path
p=Path('/tmp/con-project-icon-proposals/annextube/revised')
concepts={
'a-playback-spool':('Playback spool','A continuous lowercase a encloses a playable triangular aperture; its tail winds back into the archive.', '''<path class="primary" fill-rule="evenodd" d="M128 28c-55.2 0-100 44.8-100 100s44.8 100 100 100h80v-36h-80c-35.3 0-64-28.7-64-64s28.7-64 64-64 64 28.7 64 64v28h36v-28c0-55.2-44.8-100-100-100Z"/><path class="accent" d="M108 88v80l64-40Z"/>'''),
'b-archive-sleeve':('Archive sleeve','An angular archive sleeve holds a triangular video aperture, with its projecting spine marking the retained copy.', '''<path class="primary" fill-rule="evenodd" d="m48 32 172 96L48 224V32Zm40 64v64l58-32-58-32Z"/><path class="accent" d="M20 72h16v112H20zM64 224h132v-28H114z"/>'''),
'c-tape-a':('Tape a','The lowercase a becomes a film spool, with a triangular play counter and an unspooling foot.', '''<path class="primary" fill-rule="evenodd" d="M132 28c-57.4 0-104 44.8-104 100s46.6 100 104 100h96v-36h-44V128c0-31-23.3-56-52-56s-52 25-52 56 23.3 56 52 56h16v-29l-32 19V82l68 40v-4c-5-29-26-50-52-50-36.5 0-66 26.9-66 60s29.5 60 66 60h52v-60c0-34-22-63-52-63V28Z"/>''')}
# replace C with clean a silhouette for comparison
concepts['c-tape-a']=('Tape a','A lowercase a is cut with a play aperture and ends in a horizontal archive tail.', '<path class="primary" fill-rule="evenodd" d="M124 28c-53 0-96 43-96 96s43 96 96 96c25 0 48-9.5 65-25v25h39v-40h-20v-56c0-53-31-96-84-96Zm-23 49 70 47-70 47V77Z"/>')
for key,(title,desc,body) in concepts.items():
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="annextube — {title}">\n  <title>annextube — {title}</title>\n  <desc>{desc}</desc>\n  <style>.primary{{fill:#3578A8}}.accent{{fill:#DC6D3E}}</style>\n  {body}\n</svg>\n'''
 (p/f'annextube-concept-{key}.svg').write_text(s)
