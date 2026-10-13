from pathlib import Path
p=Path(__file__).parent
concepts={
'a-record-ribbon':('Record ribbon','A continuous strip coils into a protected record and carries onward.', '''<path d="M206 43H92C57 43 34 65 34 99v65c0 34 22 55 56 55h63c39 0 69-29 69-67s-27-66-65-66h-48c-21 0-35 14-35 35s14 35 35 35h41" fill="none" stroke="var(--ink)" stroke-width="27" stroke-linecap="round" stroke-linejoin="round"/>'''),
'b-time-vessel':('Time vessel','An open hourglass catches the passing record in a lasting base.', '''<path d="M43 35h170v23c0 27-25 48-52 67 27 20 52 42 52 70v26H43v-26c0-28 25-50 52-70C68 106 43 85 43 58Zm31 29c6 15 27 32 54 50 27-18 48-35 54-50Zm54 77c-28 21-49 38-54 51h108c-5-13-26-30-54-51Z" fill="var(--ink)"/>'''),
'c-growth-record':('Growth record','Tree rings turn the log into a durable growing record, with a shared stem.', '''<path d="M128 34a94 94 0 1 0 94 94M128 73a55 55 0 1 0 55 55" fill="none" stroke="var(--ink)" stroke-width="25" stroke-linecap="round"/><path d="M128 32v96h95M128 128l67-67" fill="none" stroke="var(--ink)" stroke-width="25" stroke-linecap="round" stroke-linejoin="round"/>''')}
for name,(title,desc,body) in concepts.items():
    s=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="con/tinuous {title.lower()} logo">\n  <title>con/tinuous — {title}</title>\n  <desc>{desc}</desc>\n  <style>:root {{ --ink: #BA482C; }}</style>\n  {body}\n</svg>\n'''
    (p/f'{name}.svg').write_text(s)
