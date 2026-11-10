# Generates pixel-terminal style SVGs for the profile README
BG = "#0A0F2A"; PANEL = "#0F1638"; LINE = "#2A46FF"
G = "#39FF88"; C = "#22E6FF"; M = "#FF3EA5"; Y = "#FFD23F"; T = "#DCE4FF"; D = "#7F8BC0"


def sprite(rows, colors, px=6):
    out = []
    for y, r in enumerate(rows):
        for x, ch in enumerate(r):
            if ch != '.':
                out.append(f'<rect x="{x*px}" y="{y*px}" width="{px}" height="{px}" fill="{colors[ch]}"/>')
    return ''.join(out)


SLIME = ["........", "..bbbb..", ".bbbbbb.", "bwkbbwkb", "bbbbbbbb", "bbbbbbbb", ".bbbbbb.", "........"]
ROBOT = ["..a..a..", ".gggggg.", "gcggggcg", "gggggggg", ".gaaaag.", "..gggg..", ".g.gg.g.", "gg....gg"]
KNIGHT = ["...rr...", "..pppp..", ".pwwwwp.", "..pkkp..", ".pppppp.", "pp.pp.pp", "..p..p..", ".pp..pp."]
BLOB = ["........", "...mm...", "..mmmm..", ".mmmmmm.", "mmkmmkmm", "mmmmmmmm", ".m.mm.m.", "m......m"]
cols = {'b': C, 'w': '#FFFFFF', 'k': BG, 'a': D, 'g': '#9AA6D8', 'c': G, 'r': M, 'p': '#8B6CF5', 'm': M}


def walker(sp, delay, dur, y=0):
    return (f'<g transform="translate(0,{y})"><g style="animation:walk {dur}s linear infinite {delay}s">'
            f'<g style="animation:hop .7s steps(2) infinite">{sprite(sp, cols)}</g></g></g>')


STYLE = """<style>
.t{font-family:'Courier New',Consolas,'Liberation Mono',monospace;font-weight:700}
@keyframes walk{from{transform:translateX(-80px)}to{transform:translateX(1260px)}}
@keyframes hop{50%{transform:translateY(-6px)}}
@keyframes blink{50%{opacity:0}}
@keyframes glow{50%{opacity:.55}}
</style>"""


def grid(w, h):
    s = []
    for x in range(0, w, 40):
        s.append(f'<path d="M{x} 0V{h}" stroke="{LINE}" stroke-opacity="0.12"/>')
    for y in range(0, h, 40):
        s.append(f'<path d="M0 {y}H{w}" stroke="{LINE}" stroke-opacity="0.12"/>')
    return ''.join(s)


# ---------- header ----------
W, H = 1200, 380
hdr = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Ivaylo Zhivkov - Android developer">
<defs>{STYLE}</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
{grid(W, H)}
<rect x="6" y="6" width="{W-12}" height="{H-12}" fill="none" stroke="{LINE}" stroke-width="4"/>
<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{LINE}" stroke-opacity="0.35" stroke-width="2"/>
<text x="56" y="70" class="t" font-size="20" fill="{D}" letter-spacing="4">&gt; HELLO, WORLD. I AM</text>
<text x="56" y="150" class="t" font-size="76" fill="{G}" letter-spacing="3" style="animation:glow 3s ease-in-out infinite">IVAYLO ZHIVKOV<tspan fill="{G}" style="animation:blink 1s steps(1) infinite">_</tspan></text>
<text x="56" y="196" class="t" font-size="26" fill="{C}" letter-spacing="2">[ INDEPENDENT ANDROID DEVELOPER ]</text>
<rect x="56" y="222" width="262" height="76" fill="{PANEL}" stroke="{G}" stroke-width="2"/><rect x="56" y="222" width="6" height="76" fill="{G}"/><text x="78" y="262" class="t" font-size="34" fill="{G}">6</text><text x="78" y="285" class="t" font-size="13" fill="{D}" letter-spacing="2">APPS ON GOOGLE PLAY</text>
<rect x="332" y="222" width="262" height="76" fill="{PANEL}" stroke="{C}" stroke-width="2"/><rect x="332" y="222" width="6" height="76" fill="{C}"/><text x="354" y="262" class="t" font-size="34" fill="{C}">1,300+</text><text x="354" y="285" class="t" font-size="13" fill="{D}" letter-spacing="2">TOTAL DOWNLOADS</text>
<rect x="608" y="222" width="262" height="76" fill="{PANEL}" stroke="{M}" stroke-width="2"/><rect x="608" y="222" width="6" height="76" fill="{M}"/><text x="630" y="262" class="t" font-size="34" fill="{M}">9</text><text x="630" y="285" class="t" font-size="13" fill="{D}" letter-spacing="2">PROJECT SHOWCASES</text>
<rect x="884" y="222" width="262" height="76" fill="{PANEL}" stroke="{Y}" stroke-width="2"/><rect x="884" y="222" width="6" height="76" fill="{Y}"/><text x="906" y="262" class="t" font-size="34" fill="{Y}">BG | EN</text><text x="906" y="285" class="t" font-size="13" fill="{D}" letter-spacing="2">TWO LANGUAGES</text>
<g transform="translate(0,306)">{walker(SLIME, 0, 16)}{walker(ROBOT, 4, 16)}{walker(KNIGHT, 8, 16)}{walker(BLOB, 12, 16)}</g>
<rect x="14" y="356" width="{W-28}" height="3" fill="{LINE}" opacity="0.5"/>
</svg>'''
open('assets/header.svg', 'w', encoding='utf-8').write(hdr)


# ---------- section dividers ----------
def section(fn, label, color, tag, tagcolor, W=1200, H=56):
    tw = len(tag) * 11 + 30
    lx1 = 50 + len(label) * 18
    lx2 = W - tw - 30
    s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{label}">
<defs>{STYLE}</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect x="6" y="20" width="16" height="16" fill="{color}"/>
<text x="36" y="35" class="t" font-size="22" fill="{T}" letter-spacing="4">{label}</text>
<line x1="{lx1}" y1="30" x2="{lx2}" y2="30" stroke="{D}" stroke-width="3" stroke-dasharray="2 8"/>
<rect x="{W-tw-6}" y="12" width="{tw}" height="32" fill="none" stroke="{tagcolor}" stroke-width="2"/>
<text x="{W-tw+9}" y="34" class="t" font-size="16" fill="{tagcolor}" letter-spacing="2">{tag}</text>
</svg>'''
    open(fn, 'w', encoding='utf-8').write(s)


section('assets/sec-apps.svg', 'APPS', G, 'CLICK A CARD', C)
section('assets/sec-stack.svg', 'STACK', C, 'WHAT I BUILD WITH', Y)
section('assets/sec-progress.svg', 'PROGRESS', M, 'PER THE AUTHOR', C)
section('assets/sec-contact.svg', 'CONTACT', Y, 'SAY HELLO', G)


# ---------- segmented progress ----------
def segbar(fn, rows, W=1200):
    H = 40 + len(rows) * 64
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Portfolio progress"><defs>{STYLE}</defs><rect width="{W}" height="{H}" fill="{BG}"/><rect x="6" y="6" width="{W-12}" height="{H-12}" fill="{PANEL}" stroke="{LINE}" stroke-width="3"/>']
    for i, (label, done, total, color, note) in enumerate(rows):
        y = 30 + i * 64
        parts.append(f'<text x="36" y="{y+22}" class="t" font-size="19" fill="{T}" letter-spacing="2">{label}</text>')
        parts.append(f'<text x="{W-36}" y="{y+22}" text-anchor="end" class="t" font-size="19" fill="{color}">{note}</text>')
        seg = (W - 72) / total
        for j in range(total):
            x = 36 + j * seg
            fill = color if j < done else 'none'
            anim = f' style="animation:glow 2.5s ease-in-out infinite {j*0.15:.2f}s"' if j < done else ''
            parts.append(f'<rect x="{x:.1f}" y="{y+34}" width="{seg-8:.1f}" height="16" fill="{fill}" stroke="{color}" stroke-width="2"{anim}/>')
    parts.append('</svg>')
    open(fn, 'w', encoding='utf-8').write(''.join(parts))


segbar('assets/progress.svg', [
    ('ANDROID APPS', 6, 9, G, '6 / 9 PROJECTS'),
    ('WEB AND GAMES', 3, 9, C, '3 / 9 PROJECTS'),
    ('SHOWCASED ON THIS PROFILE', 9, 9, M, '9 / 9'),
])

# ---------- footer strip ----------
W, H = 1200, 90
ft = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="footer"><defs>{STYLE}</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>
<rect x="0" y="76" width="{W}" height="4" fill="{LINE}"/>
<g transform="translate(0,26)">{walker(BLOB, 0, 14)}{walker(SLIME, 5, 14)}{walker(KNIGHT, 9, 14)}</g>
<circle cx="46" cy="22" r="7" fill="{G}" style="animation:blink 1.4s steps(1) infinite"/><text x="62" y="28" class="t" font-size="16" fill="{T}">ONLINE NOW</text>
</svg>'''
open('assets/footer.svg', 'w', encoding='utf-8').write(ft)
print('ok')

# ---------- stack panel ----------
rows=[("ANDROID",G,"Kotlin · Jetpack Compose · Hilt · Room · Media3 · WorkManager · Play Billing · AdMob"),
      ("BACKEND",C,"Firebase (Firestore, Auth, Cloud Functions in TypeScript) · Python data pipelines"),
      ("WEB",M,"Astro · Tailwind · static sites on Firebase Hosting with strict security headers"),
      ("QUALITY",Y,"Written audits · lint and unit-test gates · security-rule tests · no secrets in repos")]
W=1200;H=40+len(rows)*60
p=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Stack"><defs>{STYLE}</defs><rect width="{W}" height="{H}" fill="{BG}"/><rect x="6" y="6" width="{W-12}" height="{H-12}" fill="{PANEL}" stroke="{LINE}" stroke-width="3"/>']
for i,(k,c,t) in enumerate(rows):
    y=26+i*60
    p.append(f'<rect x="30" y="{y}" width="150" height="40" fill="none" stroke="{c}" stroke-width="2"/><rect x="30" y="{y}" width="8" height="40" fill="{c}"/><text x="112" y="{y+27}" text-anchor="middle" class="t" font-size="17" fill="{c}" letter-spacing="2">{k}</text>')
    p.append(f'<text x="204" y="{y+27}" class="t" font-size="18" fill="{T}">{t}</text>')
p.append('</svg>')
open('assets/stack.svg','w',encoding='utf-8').write(''.join(p))

# ---------- project cards ----------
import base64,os
SP=os.path.abspath('..')
cards=[("isa","ISA","Grocery prices from six chains, side by side",G),
("cdt","CRYPTODEPT TERMINAL","A multi-agent crypto intelligence terminal",C),
("tarot","TAROT OF THE DAY","A daily reading in 13 languages",M),
("sonirra","SONIRRA","A sleep-sounds mixer with timer",C),
("cleanx","CLEANX MAX","A phone cleaner turned into a game",Y),
("bgts","BG TOLL SPEED","Average-speed section control for drivers",G),
("izstudio","IZ STUDIO","The bilingual portfolio site for all of the above",M),
("nefera","NEFERA'S FORTUNE","An Egyptian slot game for the browser (in development)",Y),
("fundsite","VIDIN FUND CHITALISHTA","A bilingual website with a CMS the team edits",G)]
os.makedirs('assets/cards',exist_ok=True)
for i,(d,t,sub,c) in enumerate(cards,1):
    b64=base64.b64encode(open(f'{SP}/{d}/assets/banner.svg','rb').read()).decode()
    W,H=1200,500
    t=t.replace("'","&#39;")
    sub=sub.replace("'","&#39;")
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{t}"><defs>{STYLE}</defs>
<rect width="{W}" height="{H}" fill="{BG}"/>{grid(W,H)}
<rect x="6" y="6" width="{W-12}" height="{H-12}" fill="none" stroke="{c}" stroke-width="4"/>
<rect x="14" y="14" width="{W-28}" height="{H-28}" fill="none" stroke="{LINE}" stroke-opacity="0.45" stroke-width="2"/>
<image x="36" y="40" width="1128" height="338" href="data:image/svg+xml;base64,{b64}"/>
<rect x="36" y="40" width="1128" height="338" fill="none" stroke="{c}" stroke-opacity="0.6" stroke-width="2"/>
<rect x="36" y="402" width="14" height="14" fill="{c}"/>
<text x="62" y="416" class="t" font-size="30" fill="{T}" letter-spacing="2">{t}</text>
<text x="36" y="458" class="t" font-size="22" fill="{D}">{sub}</text>
<rect x="1058" y="392" width="106" height="40" fill="none" stroke="{c}" stroke-width="2"/>
<text x="1111" y="420" text-anchor="middle" class="t" font-size="18" fill="{c}" letter-spacing="2">#{i:02d}</text>
<text x="1164" y="468" text-anchor="end" class="t" font-size="16" fill="{c}" letter-spacing="2" style="animation:blink 1.6s steps(1) infinite">OPEN &gt;</text>
</svg>'''
    open(f'assets/cards/{d}.svg','w',encoding='utf-8').write(svg)
print('cards ok')
