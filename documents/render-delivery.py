from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

root = Path('/tmp/con-project-icon-proposals')
names = ['annextube', 'fscacher', 'solidation', 'tinuous']
for name in names:
    repo = root / 'checkouts' / name
    assets = repo / 'assets'
    if not (root / name / 'revised' / 'rationale.md').exists():
        continue
    files = [assets / 'project-icon.svg', *sorted((assets / 'logo-concepts').glob('*.svg'))]
    canvas = Image.new('RGB', (900, 360), '#f6f6f3')
    draw = ImageDraw.Draw(canvas)
    for i, f in enumerate(files):
        ET.parse(f)
        png = root / name / 'revised' / (f.stem + '-delivery.png')
        subprocess.run(['rsvg-convert', '-w', '256', '-h', '256', '-o', str(png), str(f)], check=True)
        draw.rounded_rectangle((i*300+10, 38, i*300+290, 330), radius=8, fill='white')
        im = Image.open(png).convert('RGBA')
        canvas.paste(im, (i*300+22, 53), im)
        draw.text((i*300+20, 15), 'Recommended' if i == 0 else f'Alternative {i}', fill='#222222')
    canvas.save(assets / 'logo-concepts' / 'comparison.png')
    for f in assets.rglob('*.svg'):
        ET.parse(f)
    print(name, 'SVG XML and comparison rendering passed')
