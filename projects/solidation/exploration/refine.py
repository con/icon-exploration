from pathlib import Path
import subprocess
from PIL import Image, ImageDraw
P=Path(__file__).parent
base=(P/'a-conversation.svg').read_text()
# Give each voice a clean separator; no background-colored patch is required.
body='''<path class="primary" d="M108 20H49C27 20 14 33 14 51c0 19 14 31 36 31h7l20-20H50c-8 0-12-4-12-11s4-11 12-11h38z"/>
<path class="accent" d="M20 108h59c22 0 35-13 35-31 0-19-14-31-36-31H71L51 66h27c8 0 12 4 12 11s-4 11-12 11H40z"/>'''
# Shape split stays legible when both pieces have the same fill.
variants={
'round-two-open':body,
'round-two-editorial':body.replace('M108 20','M104 20').replace('h38z','h34z').replace('M20 108','M24 108').replace('h59','h55').replace('H40z','H44z'),
}
for name,geom in variants.items():
 s=base[:base.index('<path')]+geom+'</svg>'
 (P/(name+'.svg')).write_text(s)
# All concept and refinement scale/background comparisons.
names=['a-conversation','b-editorial','c-collective']+list(variants)
canvas=Image.new('RGB',(360*len(names),900),'#ECEAE6'); draw=ImageDraw.Draw(canvas)
for x,name in enumerate(names):
 source=(P/(name+'.svg')).read_text()
 draw.text((x*360+18,12),name,fill='#222222')
 for y,(theme,bg) in enumerate([('light','#FFFFFF'),('dark','#202028'),('mono','#FFFFFF')]):
  tile=Image.new('RGB',(340,270),bg)
  s=source
  if theme=='mono':s=s.replace('#7955B5','#222222').replace('#E87659','#222222')
  if theme=='dark':s=s.replace('#7955B5','#AD8DD7').replace('#E87659','#F08D72')
  fp=P/(name+'-'+theme+'.svg');fp.write_text(s)
  for size,loc in [(512,(60,5)),(64,(35,200)),(16,(165,223))]:
   out=P/(name+f'-{theme}-{size}.png')
   subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),str(fp),'-o',str(out)],check=True)
   im=Image.open(out).convert('RGBA')
   if size==512:im=im.resize((210,210),Image.Resampling.LANCZOS)
   tile.paste(im,loc,im)
  canvas.paste(tile,(x*360+10,y*285+35))
canvas.save(P/'contact.png')
