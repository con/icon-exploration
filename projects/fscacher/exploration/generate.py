from pathlib import Path
import subprocess
p=Path(__file__).parent
shapes={
'a-fingerprint':'''<g fill="none" stroke="var(--primary)" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"><path d="M46 144V99a82 82 0 0 1 164 0v34c0 46-23 78-47 95"/><path d="M74 176V99a54 54 0 0 1 108 0v34c0 35-15 61-33 76"/><path d="M102 205V99a26 26 0 0 1 52 0"/><path d="M102 128h46"/></g>''',
'b-memory-seed':'''<path fill="var(--primary)" d="M66 114h124v24c0 43-31 64-62 91-31-27-62-48-62-91z"/><path d="M47 93c0-37 36-58 81-58s81 21 81 58v10H47z" fill="var(--accent)"/><path d="M128 39c-4-15 0-22 15-29" fill="none" stroke="var(--primary)" stroke-width="15" stroke-linecap="round"/><path d="M112 176v-30c0-14 10-19 25-16m-37 21h40" fill="none" stroke="var(--cutout)" stroke-width="12" stroke-linecap="round"/>''',
'c-recall':'''<path d="M40 216V82c0-34 28-62 62-62h104v36H102c-14 0-26 12-26 26v23h101v36H76v75z" fill="var(--primary)"/><path d="M112 174h65v-33h39v37c0 19-16 35-35 35h-69z" fill="var(--accent)"/>'''
}
for name,shape in shapes.items():
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="fscacher {name}"><title>fscacher — {name}</title><desc>File identity and persistent reuse expressed as a distinctive project mark.</desc><style>:root{{--primary:#087E8B;--accent:#D97732;--cutout:#FFFFFF}}</style>{shape}</svg>'''
 (p/f'{name}.svg').write_text(svg)
# Compose scale/context specimen from the actual geometry.
parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="1150" viewBox="0 0 1200 1150"><rect width="1200" height="1150" fill="#ecece8"/>']
for col,(name,shape) in enumerate(shapes.items()):
 x=col*400
 parts.append(f'<text x="{x+20}" y="32" font-family="sans-serif" font-size="20">{name}</text>')
 for row,(bg,color,accent,cut) in enumerate([('#FFFFFF','#087E8B','#D97732','#FFFFFF'),('#162329','#43B6C0','#ECA66E','#162329'),('#FFFFFF','#202020','#202020','#FFFFFF')]):
  y=50+row*350
  parts.append(f'<rect x="{x+10}" y="{y}" width="380" height="330" fill="{bg}"/>')
  s=shape.replace('var(--primary)',color).replace('var(--accent)',accent).replace('var(--cutout)',cut)
  for size,px,py in [(256,x+72,y+8),(64,x+90,y+265),(16,x+220,y+282)]:
   parts.append(f'<svg x="{px}" y="{py}" width="{size}" height="{size}" viewBox="0 0 256 256">{s}</svg>')
parts.append('</svg>')
(p/'contact.svg').write_text(''.join(parts))
subprocess.run(['rsvg-convert','-o',str(p/'contact.png'),str(p/'contact.svg')],check=True)
for name in shapes:
 for size in [16,64,512]:
  subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),'-o',str(p/f'{name}-{size}.png'),str(p/f'{name}.svg')],check=True)
print('Three concepts rendered at 16, 64, and 512 px; contact sheet includes light, reversed, monochrome.')
