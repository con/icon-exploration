from pathlib import Path
import re
P=Path(__file__).parent
base=(P/'a-conversation.svg').read_text()
body=re.search(r'<path class="accent" d="([^"]+)"',base).group(1)
defs='<defs><mask id="voice-gap"><rect width="128" height="128" fill="white"/><path d="'+body+'" fill="black" stroke="black" stroke-width="8"/></mask></defs>'
start=base.index('<path')
s=base[:start]+defs+base[start:].replace('class="primary"','class="primary" mask="url(#voice-gap)"')
(P/'round-three-separated.svg').write_text(s)
