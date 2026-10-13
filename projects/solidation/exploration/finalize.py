from pathlib import Path
import subprocess, re, xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
P=Path(__file__).parent
R=Path('/tmp/con-project-icon-proposals/checkouts/solidation/assets')
s=(P/'b-editorial.svg').read_text()
s=s[:s.index('<path')]+'''<path class="primary" d="M18 18h92v22H59l29 24-29 24h51v22H18V88l30-24-30-24z"/><path class="accent" d="M88 53h22v22H88z"/></svg>'''
s=s.replace('Editorial gathering','Summary sigma').replace('Three separate discussion lines gather into one bracket, with the collected text forming an open S.','A summation sign gathers activity into a summary, with one square representing the consolidated result.')
(P/'b-editorial.svg').write_text(s)
selected=(P/'round-three-separated.svg').read_text()
selected=selected.replace('solidation — Conversation S','solidation — conversation S').replace('<style>.primary{fill:#7955B5}.accent{fill:#E87659}</style>','<style>.primary{fill:#7955B5}.accent{fill:#E87659}</style>')
# Retain only curated candidates and final production variants in repository.
R.mkdir(exist_ok=True)
C=R/'logo-concepts';C.mkdir(exist_ok=True)
for source,target in [('a-conversation.svg','solidation-concept-a-conversation.svg'),('b-editorial.svg','solidation-concept-b-summary.svg'),('c-collective.svg','solidation-concept-c-collective.svg')]:
 (C/target).write_text((P/source).read_text())
variants={'project-icon':selected,'project-icon-monochrome':selected.replace('#7955B5','#222222').replace('#E87659','#222222'),'project-icon-reversed':selected.replace('#7955B5','#FFFFFF').replace('#E87659','#FFFFFF')}
canvas=Image.new('RGB',(1080,780),'#ECEAE6');d=ImageDraw.Draw(canvas)
for i,(name,svg) in enumerate(variants.items()):
 (R/(name+'.svg')).write_text(svg)
 (P/(name+'.svg')).write_text(svg)
 root=ET.fromstring(svg)
 assert root.get('viewBox')=='0 0 128 128' and not root.get('width')
 assert root.get('role')=='img'
 assert not any(x.tag.split('}')[-1] in ['image','filter','text','script'] for x in root.iter())
 for row,bg in enumerate(['#FFFFFF','#202028']):
  if name=='project-icon-reversed' and row==0:bg='#7955B5'
  if name=='project-icon-monochrome' and row==1:bg='#DFDADC'
  tile=Image.new('RGB',(340,350),bg)
  for size,loc in [(512,(35,15)),(64,(25,283)),(16,(172,306))]:
   out=P/(name+f'-{size}.png')
   subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),str(P/(name+'.svg')),'-o',str(out)],check=True)
   im=Image.open(out).convert('RGBA')
   if size==512:im=im.resize((270,270),Image.Resampling.LANCZOS)
   tile.paste(im,loc,im)
  canvas.paste(tile,(i*360+10,row*365+40))
 d.text((i*360+18,12),name,fill='#222')
canvas.save(P/'final-validation.png')
for fp in list(R.glob('project-icon*.svg'))+list(C.glob('*.svg')):
 root=ET.parse(fp).getroot()
 assert root.get('viewBox') and root.get('role')=='img'
 assert not root.get('width') and not root.get('height')
print('Validated 6 curated SVG assets; rendered primary, monochrome and reversed at 16, 64 and 512 pixels.')
