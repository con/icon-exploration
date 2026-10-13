from pathlib import Path
import re, subprocess, xml.etree.ElementTree as ET
p=Path(__file__).parent
repo=Path('/tmp/con-project-icon-proposals/checkouts/annextube/assets')
files=sorted(p.glob('annextube-concept-*.svg'))
primary=(p/'annextube-concept-c-tape-a.svg').read_text().replace('.accent{fill:#DC6D3E}','')
(repo/'project-icon.svg').write_text(primary)
(repo/'project-icon-monochrome.svg').write_text(primary.replace('#3578A8','#20252B'))
(repo/'project-icon-reversed.svg').write_text(primary.replace('#3578A8','#FFFFFF'))
(repo/'logo-concepts').mkdir(exist_ok=True)
for f in files[:2]: (repo/'logo-concepts'/f.name).write_text(f.read_text())
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1260" viewBox="0 0 1080 1260"><rect width="1080" height="1260" fill="#ecece9"/>']
for row,(bg,color,accent,label) in enumerate([('#ffffff','#3578A8','#DC6D3E','light'),('#15242e','#87AADE','#F0A36C','dark'),('#ffffff','#20252B','#20252B','one ink')]):
 for col,f in enumerate(files):
  s=f.read_text(); body=s[s.index('</style>')+8:s.index('</svg>')].replace('class="primary"',f'fill="{color}"').replace('class="accent"',f'fill="{accent}"')
  x=col*360;y=row*420
  parts += [f'<rect x="{x+8}" y="{y+8}" width="344" height="404" fill="{bg}"/>',f'<text x="{x+20}" y="{y+32}" fill="{color}" font-family="sans-serif" font-size="14">{f.stem[17:]} · {label}</text>']
  for size,dx,dy in [(256,52,50),(64,54,326),(16,164,350)]: parts.append(f'<svg x="{x+dx}" y="{y+dy}" width="{size}" height="{size}" viewBox="0 0 256 256">{body}</svg>')
  for size in [16,64,512]:
   variant=s.replace('#3578A8',color).replace('#DC6D3E',accent)
   target=p/f'{f.stem}-{label.replace(" ","-")}-{size}.png'
   subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),'-b',bg,'-o',str(target)],input=variant.encode(),check=True)
parts.append('</svg>')
(p/'contact.svg').write_text(''.join(parts))
subprocess.run(['rsvg-convert','-o',str(p/'contact.png'),str(p/'contact.svg')],check=True)
for f in repo.glob('*.svg'):
 root=ET.parse(f).getroot()
 assert root.attrib.get('viewBox')=='0 0 256 256'
 assert 'width' not in root.attrib and 'height' not in root.attrib
 assert root.attrib.get('role')=='img'
 assert not re.search(r'<(?:image|filter|text)\b',f.read_text())
print('Rendered 27 size/background checks, contact sheet; validated scalable accessible path-only production SVGs.')
