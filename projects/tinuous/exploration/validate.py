from pathlib import Path
import subprocess, re, xml.etree.ElementTree as ET
p=Path(__file__).parent
names=['a-record-ribbon','b-time-vessel','c-growth-record','a2-record-ribbon-cut','a3-record-ribbon-open']
rows=[]
for i,name in enumerate(names):
 source=(p/f'{name}.svg').read_text()
 for j,(label,color,bg) in enumerate([('light','#BA482C','#FFFFFF'),('dark','#F08B64','#17272B'),('mono','#171717','#FFFFFF')]):
  svg=source.replace('#BA482C',color)
  root=ET.fromstring(svg)
  assert root.attrib['viewBox']=='0 0 256 256'
  assert 'width' not in root.attrib and 'height' not in root.attrib
  assert not any(x in svg for x in ['<image','<filter','<text'])
  for size in [16,64,512]:
   subprocess.run(['rsvg-convert','-b',bg,'-w',str(size),'-h',str(size),'-o',str(p/f'{name}-{label}-{size}.png')],input=svg.encode(),check=True)
  body=re.sub(r'^.*?<style>.*?</style>','',svg,flags=re.S).replace('</svg>','')
  x=j*350;y=i*350
  rows.append(f'<rect x="{x}" y="{y}" width="340" height="340" fill="{bg}"/><text x="{x+10}" y="{y+20}" fill="{color}" font-size="13">{name} / {label}</text><svg x="{x+40}" y="{y+35}" width="256" height="256" viewBox="0 0 256 256">{body}</svg><svg x="{x+30}" y="{y+270}" width="64" height="64" viewBox="0 0 256 256">{body}</svg><svg x="{x+160}" y="{y+294}" width="16" height="16" viewBox="0 0 256 256">{body}</svg>')
(p/'contact.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" width="1050" height="1750" viewBox="0 0 1050 1750">'+''.join(rows)+'</svg>')
subprocess.run(['rsvg-convert','-o',str(p/'contact.png'),str(p/'contact.svg')],check=True)
print('Validated and rendered 5 designs × 3 treatments × 3 sizes.')
