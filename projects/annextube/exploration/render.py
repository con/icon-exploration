from pathlib import Path
import subprocess
p=Path(__file__).parent
for f in p.glob('annextube-concept-*.svg'):
 for size in [16,64,512]:
  subprocess.run(['rsvg-convert','-w',str(size),'-h',str(size),'-o',str(f.with_suffix(f'.{size}.png')),str(f)],check=True)
subprocess.run(['rsvg-convert','-w','750','-o',str(p/'con-reference.png'),'/Users/johnlee/code/CON/orinoco/dev-centerforopenneuroscience.org/site-specific/static/img/con-logo.svg'],check=True)
