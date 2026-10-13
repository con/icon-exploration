from pathlib import Path
import subprocess,re,xml.etree.ElementTree as ET
p=Path(__file__).parent
original=(p/'a-fingerprint.svg').read_text()
variants={
'01-original':original,
'02-balanced':original.replace('stroke-width="16"','stroke-width="18"').replace('c0 46-23 78-47 95','c0 43-22 73-47 90').replace('c0 35-15 61-33 76','c0 31-15 56-33 71'),
'03-bold':original.replace('stroke-width="16"','stroke-width="20"')}
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="560"><rect width="1100" height="560" fill="white"/>']
for i,(name,svg) in enumerate(variants.items()):
 fixed=svg.replace('var(--primary)','#087E8B')
 (p/f'refinement-{name}.svg').write_text(fixed)
 inner=re.search(r'<g .*?</g>',fixed).group()
 parts.append(f'<text x="{30+i*365}" y="30" font-size="20" font-family="sans-serif">{name}</text>')
 for size,x,y in [(300,30+i*365,45),(64,45+i*365,380),(16,160+i*365,400)]:
  parts.append(f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="0 0 256 256">{inner}</svg>')
parts.append('</svg>')
(p/'refinements.svg').write_text(''.join(parts))
subprocess.run(['rsvg-convert','-o',str(p/'refinements.png'),str(p/'refinements.svg')],check=True)
