from pathlib import Path
import subprocess, xml.etree.ElementTree as ET
p=Path(__file__).parent
rows=[]
for i,(name,bg) in enumerate([('project-icon','#FFFFFF'),('project-icon-mono','#FFFFFF'),('project-icon-reversed','#17272B')]):
 s=(p/f'{name}.svg').read_text(); body=s[s.index('  <path'):].replace('</svg>','')
 for size in [16,64,512]:
  subprocess.run(['rsvg-convert','-b',bg,'-w',str(size),'-h',str(size),'-o',str(p/f'{name}-{size}.png')],input=s.encode(),check=True)
 x=350*i
 rows.append(f'<rect x="{x}" width="340" height="360" fill="{bg}"/><svg x="{x+42}" y="10" width="256" height="256" viewBox="0 0 256 256">{body}</svg><svg x="{x+48}" y="280" width="64" height="64" viewBox="0 0 256 256">{body}</svg><svg x="{x+170}" y="303" width="16" height="16" viewBox="0 0 256 256">{body}</svg>')
for f in Path('/tmp/con-project-icon-proposals/checkouts/tinuous/assets').rglob('*.svg'):
 root=ET.parse(f).getroot(); assert root.attrib['viewBox']=='0 0 256 256';assert not any(x in root.attrib for x in ['width','height']);assert root.attrib['role']=='img'
(p/'final-validation.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="360">'+''.join(rows)+'</svg>')
subprocess.run(['rsvg-convert','-o',str(p/'final-validation.png'),str(p/'final-validation.svg')],check=True)
print('Six deliverable SVGs validate. Final primary, mono, reversed rendered at 16/64/512.')
