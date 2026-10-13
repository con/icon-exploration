from pathlib import Path
import subprocess
P=Path(__file__).parent
concepts={
'a-conversation':('Conversation S','Two interlocking conversation forms make an S: individual discussions become one readable account.', '''<path class="primary" d="M108 20H49C27 20 14 33 14 51c0 19 14 31 36 31h13l21-20H50c-8 0-12-4-12-11s4-11 12-11h38z"/>
<path class="accent" d="M20 108h59c22 0 35-13 35-31 0-19-14-31-36-31H65L44 66h34c8 0 12 4 12 11s-4 11-12 11H40z"/>'''),
'b-editorial':('Editorial gathering','Three separate discussion lines gather into one bracket, with the collected text forming an open S.', '''<path class="primary" d="M22 20h74v20H42v14h44c17 0 28 11 28 28s-11 28-28 28H12l20-20h54c5 0 8-3 8-8s-3-8-8-8H22z"/>
<path class="accent" d="M12 20h14v20H12zm0 34h14v20H12z"/>'''),
'c-collective':('Collected voices','Three distinct speech lines nest within a single circular gathering mark.', '''<path class="primary" d="M104 34A48 48 0 1 0 104 94L86 80a26 26 0 1 1 0-32z"/>
<path class="accent" d="M62 34h48v14H62zm-8 24h60v14H54zm8 24h48v14H62z"/>''')}
for name,(title,desc,body) in concepts.items():
 s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" role="img" aria-labelledby="title desc"><title id="title">solidation — {title}</title><desc id="desc">{desc}</desc><style>.primary{{fill:#7955B5}}.accent{{fill:#E87659}}</style>{body}</svg>'''
 (P/(name+'.svg')).write_text(s)
 subprocess.run(['rsvg-convert','-w','512','-h','512',str(P/(name+'.svg')),'-o',str(P/(name+'.png'))],check=True)
