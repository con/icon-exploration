from pathlib import Path
import shutil
import subprocess
from PIL import Image, ImageDraw, ImageFont

root = Path('/tmp/con-project-icon-proposals')
out = Path('/Users/johnlee/.codex/artifacts/con-project-icons')
out.mkdir(parents=True, exist_ok=True)
shutil.copy2(root / 'logo-design-SKILL.md', out / 'logo-design-SKILL.md')
canvas = Image.new('RGB', (1280, 380), '#f4f3ef')
draw = ImageDraw.Draw(canvas)
font = ImageFont.truetype('/System/Library/Fonts/Helvetica.ttc', 22)
for i, name in enumerate(['annextube', 'fscacher', 'solidation', 'tinuous']):
    target = out / name
    target.mkdir(exist_ok=True)
    shutil.copy2(root / 'checkouts' / name / 'assets' / 'project-icon.svg', target / 'project-icon.svg')
    shutil.copy2(root / name / 'revised' / 'rationale.md', target / 'rationale.md')
    shutil.copy2(root / 'checkouts' / name / 'assets' / 'logo-concepts' / 'comparison.png', target / 'comparison.png')
    png = target / 'project-icon.png'
    subprocess.run(['rsvg-convert', '-w', '256', '-h', '256', '-o', str(png), str(target / 'project-icon.svg')], check=True)
    draw.rounded_rectangle((i*320+12, 12, i*320+308, 368), radius=12, fill='white')
    im = Image.open(png).convert('RGBA')
    canvas.paste(im, (i*320+32, 40), im)
    draw.text((i*320+32, 321), name, font=font, fill='#242a32')
canvas.save(out / 'recommended-marks.png')
print(out / 'recommended-marks.png')
