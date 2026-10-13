from pathlib import Path
import subprocess,xml.etree.ElementTree as ET,re
p=Path(__file__).parent
repo=Path('/tmp/con-project-icon-proposals/checkouts/fscacher/assets')
geometry='''<g fill="none" stroke="#087E8B" stroke-width="18" stroke-linecap="round" stroke-linejoin="round">
    <path d="M46 144V99a82 82 0 0 1 164 0v34c0 43-22 73-47 90"/>
    <path d="M74 176V99a54 54 0 0 1 108 0v34c0 31-15 56-33 71"/>
    <path d="M102 205V99a26 26 0 0 1 52 0m-52 29h46"/>
  </g>'''
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-labelledby="title desc">
  <title id="title">fscacher</title>
  <desc id="desc">A lowercase f formed from a fingerprint, representing file identity and remembered function results.</desc>
  {geometry}
</svg>
'''
for name,color in [('project-icon','#087E8B'),('project-icon-mono','#202020'),('project-icon-reversed','#FFFFFF')]:
 data=svg.replace('#087E8B',color)
 (repo/f'{name}.svg').write_text(data)
 (p/f'{name}.svg').write_text(data)
 for size in [16,64,512]:
  subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),'-o',str(p/f'{name}-{size}.png'),str(repo/f'{name}.svg')],check=True)
(repo/'logo-concepts').mkdir(exist_ok=True)
for name in ['b-memory-seed','c-recall']:
 s=(p/f'{name}.svg').read_text().replace('var(--primary)','#087E8B').replace('var(--accent)','#D97732').replace('var(--cutout)','#FFFFFF')
 s=re.sub(r'<style>.*?</style>','',s)
 (repo/'logo-concepts'/f'{name}.svg').write_text(s)
# Final image with actual selected geometry on both backgrounds, and mono.
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="650"><rect width="1440" height="650" fill="#ecece8"/>']
for i,(name,bg,color) in enumerate([('Primary','#FFFFFF','#087E8B'),('Dark background','#162329','#087E8B'),('Monochrome','#FFFFFF','#202020'),('Reversed','#162329','#FFFFFF')]):
 x=i*360
 parts += [f'<rect x="{x+8}" y="8" width="344" height="634" fill="{bg}"/>',f'<text x="{x+28}" y="40" font-family="sans-serif" font-size="18" fill="{color}">{name}</text>']
 for size,px,py in [(320,x+20,80),(64,x+40,440),(16,x+190,465)]:
  parts.append(f'<svg x="{px}" y="{py}" width="{size}" height="{size}" viewBox="0 0 256 256">{geometry.replace("#087E8B",color)}</svg>')
parts.append('</svg>')
(p/'final-specimen.svg').write_text(''.join(parts))
subprocess.run(['rsvg-convert','-o',str(p/'final-specimen.png'),str(p/'final-specimen.svg')],check=True)
for f in repo.rglob('*.svg'):
 root=ET.parse(f).getroot()
 assert root.attrib.get('viewBox')=='0 0 256 256'
 assert 'width' not in root.attrib and 'height' not in root.attrib
 assert root.attrib.get('role')=='img'
 assert '<image' not in f.read_text() and '<filter' not in f.read_text()
 assert 'var(' not in f.read_text()
print('Validated 5 self-contained SVGs; final variants rendered at 16, 64, 512 px.')
