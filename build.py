#!/usr/bin/env python3
"""
Build-Skript für LINA2-Lernhilfe GitHub Pages Site.
Konvertiert Markdown-Dateien zu HTML mit MathJax, Navigation und Print-Support.

Usage: python3 build.py
"""

import os
import re
import json

def slugify(text):
    text = re.sub(r'<[^>]+>', '', text)
    text = text.lower()
    text = text.replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

BASE = os.path.dirname(os.path.abspath(__file__))
MD_DIR = os.path.join(BASE, "markdown")
DOCS_DIR = os.path.join(BASE, "docs")

# Ordered list of all pages for navigation
PAGES = [
    {"file": "index", "title": "Startseite", "icon": "🏠", "cat": "nav"},
    {"file": "00_Lernplan", "title": "9-Tage-Lernplan", "icon": "📅", "cat": "Planung"},
    {"file": "01_Komplexe_Zahlen_Vektorraeume", "title": "Komplexe Zahlen & Vektorräume", "icon": "1️⃣", "cat": "Zusammenfassungen"},
    {"file": "02_Bild_Kern_Determinanten", "title": "Bild, Kern & Determinanten", "icon": "2️⃣", "cat": "Zusammenfassungen"},
    {"file": "03_Eigenwerte_Diagonalisierung", "title": "Eigenwerte & Diagonalisierung", "icon": "3️⃣", "cat": "Zusammenfassungen"},
    {"file": "04_Skalarprodukte_GramSchmidt", "title": "Skalarprodukte & Gram-Schmidt", "icon": "4️⃣", "cat": "Zusammenfassungen"},
    {"file": "05_JNF_Minimalpolynom_CayleyHamilton", "title": "JNF, Minimalpolynom & Cayley-Hamilton", "icon": "5️⃣", "cat": "Zusammenfassungen"},
    {"file": "06_Bilinearformen_Isometrien_Gruppen", "title": "Bilinearformen, Isometrien & Gruppen", "icon": "6️⃣", "cat": "Zusammenfassungen"},
    {"file": "Vernetzung_Das_Grosse_Ganze", "title": "Das große Ganze – Vernetzung", "icon": "🌐", "cat": "Verständnis"},
    {"file": "Karteikarten", "title": "Karteikarten", "icon": "🗂️", "cat": "Lernmaterial"},
    {"file": "Checkliste_Themen", "title": "Checkliste pro Thema", "icon": "✅", "cat": "Lernmaterial"},
    {"file": "Uebungsaufgaben", "title": "Übungsaufgaben (inkl. Lösungen)", "icon": "📝", "cat": "Lernmaterial"},
    {"file": "Uebungszettel_Originale", "title": "Originale Übungszettel 1-10", "icon": "📄", "cat": "Lernmaterial"},
    {"file": "Klausur_Originale", "title": "Originale (Probe-)Klausuren", "icon": "📝", "cat": "Klausur"},
    {"file": "Klausur_Musterloesungen", "title": "Klausur-Musterlösungen", "icon": "🎯", "cat": "Klausur"},
    {"file": "Checklisten_Originale", "title": "Originale Checklisten", "icon": "✔️", "cat": "Lernmaterial"},
    {"file": "Formelblatt", "title": "Formelblatt", "icon": "📋", "cat": "Lernmaterial"},
    {"file": "Vorlesungsmaterial", "title": "Vorlesungsmaterial & Klausuren", "icon": "📄", "cat": "Dozent"},
]

def get_nav_html(current_file):
    """Generate navigation sidebar HTML."""
    nav_items = []
    current_cat = None
    for p in PAGES:
        if p["file"] == "index":
            continue
        if p["cat"] != current_cat:
            if current_cat:
                nav_items.append('</div>')
            current_cat = p["cat"]
            nav_items.append(f'<div class="nav-category"><span class="nav-cat-label">{current_cat}</span>')
        active = ' active' if p["file"] == current_file else ''
        nav_items.append(f'<a class="nav-link{active}" href="{p["file"]}.html">{p["icon"]} {p["title"]}</a>')
    nav_items.append('</div>')
    return '\n'.join(nav_items)


TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} – LINA2 Lernhilfe</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📐</text></svg>">
<script>
MathJax = {{
  tex: {{
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: true
  }},
  options: {{
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
  }}
}};
</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

  :root {{
    --primary: #4361ee;
    --primary-dark: #3a0ca3;
    --accent: #f72585;
    --bg: #f8f9fc;
    --card: #ffffff;
    --text: #1a1a2e;
    --text-muted: #6b7280;
    --border: #e5e7eb;
    --sidebar-w: 280px;
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    line-height: 1.75;
    color: var(--text);
    background: var(--bg);
    font-size: 15px;
  }}

  /* --- Top Bar --- */
  .topbar {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 100;
    background: var(--primary-dark);
    color: white;
    padding: 10px 24px;
    display: flex; align-items: center; gap: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,.15);
  }}
  .topbar a {{ color: white; text-decoration: none; font-weight: 600; font-size: 1.1em; }}
  .topbar .subtitle {{ color: rgba(255,255,255,.7); font-size: .85em; margin-left: auto; }}
  .menu-btn {{
    display: none; background: none; border: none; color: white;
    font-size: 1.5em; cursor: pointer; padding: 4px 8px;
  }}

  /* --- Sidebar --- */
  .sidebar {{
    position: fixed; top: 50px; left: 0; bottom: 0;
    width: var(--sidebar-w);
    background: var(--card);
    border-right: 1px solid var(--border);
    overflow-y: auto;
    padding: 16px 0;
    z-index: 50;
    transition: transform .3s;
  }}
  .nav-category {{ padding: 0 16px; margin-bottom: 8px; }}
  .nav-cat-label {{
    display: block; font-size: .7em; font-weight: 600;
    color: var(--text-muted); text-transform: uppercase;
    letter-spacing: .08em; padding: 12px 0 4px 0;
  }}
  .nav-link {{
    display: block; padding: 6px 16px; margin: 1px 8px;
    border-radius: 6px; text-decoration: none;
    color: var(--text); font-size: .88em;
    transition: background .15s;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
  }}
  .nav-link:hover {{ background: #f0f2ff; }}
  .nav-link.active {{
    background: var(--primary);
    color: white;
    font-weight: 600;
  }}

  /* --- Main Content --- */
  .main {{
    margin-left: var(--sidebar-w);
    margin-top: 50px;
    padding: 32px 40px 60px;
    max-width: 900px;
  }}

  h1 {{
    font-size: 1.8em; color: var(--text);
    border-bottom: 3px solid var(--primary);
    padding-bottom: 12px; margin: 24px 0 20px;
  }}
  h2 {{
    font-size: 1.35em; color: var(--primary-dark);
    margin: 28px 0 14px;
    border-left: 4px solid var(--primary);
    padding-left: 12px;
  }}
  h3 {{
    font-size: 1.1em; color: var(--primary);
    margin: 20px 0 10px;
  }}
  p {{ margin: 10px 0; }}

  blockquote {{
    border-left: 4px solid var(--accent);
    background: #fff0f6;
    padding: 12px 16px; margin: 16px 0;
    border-radius: 0 8px 8px 0;
  }}
  blockquote strong {{ color: var(--accent); }}

  .infobox {{
    border-left: 5px solid #10b981;
    background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
    padding: 20px 24px; margin: 24px 0;
    border-radius: 0 12px 12px 0;
    box-shadow: 0 2px 8px rgba(16,185,129,.1);
    font-size: .97em;
    line-height: 1.85;
  }}
  .infobox-title {{
    display: flex; align-items: center; gap: 8px;
    font-weight: 700; font-size: 1.05em;
    color: #065f46; margin-bottom: 10px;
  }}
  .infobox p {{ margin: 8px 0; color: #1a3a2a; }}

  code {{
    font-family: 'JetBrains Mono', monospace;
    background: #f0f0f5; padding: 2px 6px;
    border-radius: 4px; font-size: .9em;
  }}
  pre {{
    background: #f0f0f5; padding: 16px;
    border-radius: 8px; overflow-x: auto; margin: 12px 0;
  }}
  pre code {{ background: none; padding: 0; }}

  table {{
    border-collapse: collapse; width: 100%;
    margin: 16px 0; font-size: .92em;
  }}
  th {{
    background: var(--primary); color: white;
    padding: 10px 14px; text-align: left; font-weight: 600;
  }}
  td {{ padding: 8px 14px; border-bottom: 1px solid var(--border); }}
  tr:nth-child(even) td {{ background: #f8f9fa; }}
  tr:hover td {{ background: #e8ecff; }}

  ul, ol {{ margin: 10px 0 10px 24px; }}
  li {{ margin: 4px 0; }}
  li input[type="checkbox"] {{ margin-right: 8px; }}

  hr {{ border: none; border-top: 2px solid var(--border); margin: 30px 0; }}

  details {{
    background: #f8f9fa; border: 1px solid var(--border);
    border-radius: 8px; padding: 12px 16px; margin: 12px 0;
  }}
  details summary {{
    cursor: pointer; font-weight: 600; color: var(--primary);
  }}

  .footer {{
    margin-top: 48px; padding-top: 20px;
    border-top: 1px solid var(--border);
    color: var(--text-muted); font-size: .82em;
    text-align: center;
  }}

  /* --- Mobile --- */
  @media (max-width: 768px) {{
    .sidebar {{ transform: translateX(-100%); width: 260px; }}
    .sidebar.open {{ transform: translateX(0); box-shadow: 4px 0 20px rgba(0,0,0,.15); }}
    .main {{ margin-left: 0; padding: 24px 16px 60px; }}
    .menu-btn {{ display: block; }}
    body {{ font-size: 14px; }}
  }}

  /* --- Print --- */
  @media print {{
    .topbar, .sidebar, .menu-btn, .footer {{ display: none !important; }}
    .main {{ margin: 0; padding: 20px; max-width: 100%; }}
    body {{ font-size: 11px; background: white; }}
    h1 {{ font-size: 1.4em; }}
    h2 {{ font-size: 1.15em; break-after: avoid; }}
    table {{ break-inside: avoid; font-size: .85em; }}
    blockquote {{ break-inside: avoid; }}
    @page {{ margin: 1.5cm; }}
  }}
</style>
</head>
<body>

<div class="topbar">
  <button class="menu-btn" onclick="document.querySelector('.sidebar').classList.toggle('open')">☰</button>
  <a href="index.html">📐 LINA2 Lernhilfe</a>
  <span class="subtitle">Lineare Algebra II – FU Berlin WiSe 2025/26</span>
</div>

<nav class="sidebar">
  <div class="nav-category">
    <a class="nav-link{index_active}" href="index.html">🏠 Startseite</a>
  </div>
  {nav}
</nav>

<div class="main">
{content}
<div class="footer">
  LINA2 Lernhilfe · Lineare Algebra II · FU Berlin WiSe 2025/26 · 
  <a href="index.html">← Zurück zur Startseite</a>
</div>
</div>

<script>
// Close sidebar on mobile after link click
document.querySelectorAll('.nav-link').forEach(l => l.addEventListener('click', () => {{
  document.querySelector('.sidebar').classList.remove('open');
}}));
</script>
</body>
</html>
"""


def escape_html(text):
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def inline_format(text):
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def markdown_to_html(md_text):
    lines = md_text.split('\n')
    html_lines = []
    in_table = False
    in_list = False
    in_code_block = False
    list_type = None

    i = 0
    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                html_lines.append('</code></pre>')
                in_code_block = False
            else:
                html_lines.append('<pre><code>')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            html_lines.append(escape_html(line))
            i += 1
            continue

        # Details
        if line.strip() in ('<details>', '</details>') or line.strip().startswith('<summary>'):
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            html_lines.append(line.strip())
            i += 1
            continue

        # Horizontal rule
        if line.strip() in ('---', '***', '___') and not in_table:
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            html_lines.append('<hr>')
            i += 1
            continue

        # Headers
        m = re.match(r'^(#{1,6})\s+(.*)', line)
        if m:
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            if in_table:
                html_lines.append('</table>')
                in_table = False
            level = len(m.group(1))
            text = inline_format(m.group(2))
            html_lines.append(f'<h{level} id="{slugify(m.group(2))}">{text}</h{level}>')
            i += 1
            continue

        # Tables
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                if in_list:
                    html_lines.append(f'</{list_type}>')
                    in_list = False
                html_lines.append('<table>')
                in_table = True
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                html_lines.append('<tr>' + ''.join(f'<th>{inline_format(c)}</th>' for c in cells) + '</tr>')
                if i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i+1].strip()):
                    i += 2
                    continue
            else:
                if re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                    i += 1
                    continue
                cells = [c.strip() for c in line.strip().strip('|').split('|')]
                html_lines.append('<tr>' + ''.join(f'<td>{inline_format(c)}</td>' for c in cells) + '</tr>')
            i += 1
            continue
        elif in_table:
            html_lines.append('</table>')
            in_table = False

        # Blockquote
        if line.strip().startswith('>'):
            if in_list:
                html_lines.append(f'</{list_type}>')
                in_list = False
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith('>'):
                quote_lines.append(lines[i].strip().lstrip('> '))
                i += 1
            # Check for [!INFO] infobox
            if quote_lines and quote_lines[0].strip().startswith('[!INFO]'):
                title = quote_lines[0].replace('[!INFO]', '').strip()
                if not title:
                    title = 'Einfach erklärt'
                body_lines = quote_lines[1:]
                # Convert body to paragraphs
                paragraphs = []
                current_para = []
                for ql in body_lines:
                    if ql.strip() == '':
                        if current_para:
                            paragraphs.append(' '.join(current_para))
                            current_para = []
                    else:
                        current_para.append(ql)
                if current_para:
                    paragraphs.append(' '.join(current_para))
                body_html = ''.join(f'<p>{inline_format(p)}</p>' for p in paragraphs)
                html_lines.append(f'<div class="infobox"><div class="infobox-title">💡 {title}</div>{body_html}</div>')
            else:
                content = inline_format('<br>'.join(quote_lines))
                html_lines.append(f'<blockquote><p>{content}</p></blockquote>')
            continue

        # Unordered list
        um = re.match(r'^(\s*)[-*]\s+(\[[ x]\]\s+)?(.*)', line)
        if um:
            if not in_list or list_type != 'ul':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ul>')
                in_list = True
                list_type = 'ul'
            checkbox = um.group(2) or ''
            text = um.group(3)
            if checkbox:
                checked = 'checked' if 'x' in checkbox else ''
                html_lines.append(f'<li><input type="checkbox" {checked} disabled> {inline_format(text)}</li>')
            else:
                html_lines.append(f'<li>{inline_format(text)}</li>')
            i += 1
            continue

        # Ordered list
        om = re.match(r'^(\s*)\d+[.)]\s+(.*)', line)
        if om:
            if not in_list or list_type != 'ol':
                if in_list:
                    html_lines.append(f'</{list_type}>')
                html_lines.append('<ol>')
                in_list = True
                list_type = 'ol'
            html_lines.append(f'<li>{inline_format(om.group(2))}</li>')
            i += 1
            continue

        if in_list and line.strip():
            html_lines.append(f'</{list_type}>')
            in_list = False

        if not line.strip():
            i += 1
            continue

        # Display math block
        if line.strip().startswith('$$') and not (line.strip().endswith('$$') and len(line.strip()) > 2):
            math_lines = [line]
            i += 1
            while i < len(lines) and not lines[i].strip().endswith('$$'):
                math_lines.append(lines[i])
                i += 1
            if i < len(lines):
                math_lines.append(lines[i])
                i += 1
            html_lines.append('<p>' + '\n'.join(math_lines) + '</p>')
            continue

        html_lines.append(f'<p>{inline_format(line)}</p>')
        i += 1

    if in_table: html_lines.append('</table>')
    if in_list: html_lines.append(f'</{list_type}>')
    return '\n'.join(html_lines)


def build_page(page_file, title, content_html, nav_html):
    is_index = page_file == "index"
    return TEMPLATE.format(
        title=title,
        nav=nav_html,
        content=content_html,
        index_active=' active' if is_index else '',
    )


def build_index():
    """Build the landing page."""
    cards = []
    current_cat = None
    for p in PAGES:
        if p["file"] == "index":
            continue
        if p["cat"] != current_cat:
            if current_cat:
                cards.append('</div>')
            current_cat = p["cat"]
            cards.append(f'<h2>{current_cat}</h2><div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-bottom:8px;">')
        cards.append(f'''<a href="{p['file']}.html" style="display:block;padding:16px;background:white;border:1px solid #e5e7eb;border-radius:10px;text-decoration:none;color:#1a1a2e;transition:all .2s;box-shadow:0 1px 3px rgba(0,0,0,.05);" onmouseover="this.style.borderColor='#4361ee';this.style.boxShadow='0 4px 12px rgba(67,97,238,.15)'" onmouseout="this.style.borderColor='#e5e7eb';this.style.boxShadow='0 1px 3px rgba(0,0,0,.05)'">
  <span style="font-size:1.5em;">{p['icon']}</span><br>
  <strong style="font-size:.95em;">{p['title']}</strong>
</a>''')
    cards.append('</div>')

    return f'''
<h1>📐 LINA2 Lernhilfe</h1>
<p style="font-size:1.1em;color:#6b7280;">
  Lineare Algebra II · FU Berlin · WiSe 2025/26 · PD Dr. Marcus Weber
</p>
<blockquote>
  <p><strong>Nachklausur:</strong> 19.03.2026, 8:00 Uhr, Gr. Hörsaal Takustr. 9<br>
  Diese Seite enthält Zusammenfassungen, Karteikarten, Übungsaufgaben, Formelblätter und
  Musterlösungen zur Vorbereitung auf die LINA2-Klausur.</p>
</blockquote>
<hr>
{''.join(cards)}
<hr>
<h2>Wie benutze ich diese Seite?</h2>
<ol>
  <li><strong>Tag für Tag lernen:</strong> Folge dem <a href="00_Lernplan.html">9-Tage-Lernplan</a></li>
  <li><strong>Themen verstehen:</strong> Lies die <a href="01_Komplexe_Zahlen_Vektorraeume.html">Zusammenfassungen</a> (1-6)</li>
  <li><strong>Vernetzung:</strong> Lies <a href="Vernetzung_Das_Grosse_Ganze.html">Das große Ganze</a> – <em>jeden Tag einmal</em></li>
  <li><strong>Aktiv lernen:</strong> Bearbeite die <a href="Uebungsaufgaben.html">Übungsaufgaben</a></li>
  <li><strong>Wissen prüfen:</strong> Gehe die <a href="Karteikarten.html">Karteikarten</a> und <a href="Checkliste_Themen.html">Checkliste</a> durch</li>
  <li><strong>Klausur üben:</strong> Arbeite die <a href="Klausur_Musterloesungen.html">Musterlösungen</a> durch</li>
  <li><strong>Nachschlagen:</strong> Nutze das <a href="Formelblatt.html">Formelblatt</a></li>
  <li><strong>Original-PDFs:</strong> Alle Vorlesungs-PDFs und Klausuren unter <a href="Vorlesungsmaterial.html">Vorlesungsmaterial</a></li>
</ol>
<p style="margin-top:24px;color:#6b7280;font-size:.9em;">
  💡 <strong>PDF-Export:</strong> Jede Seite kann über <code>Cmd+P</code> (Mac) / <code>Strg+P</code> (Win) → "Als PDF speichern" exportiert werden.
  Die Druckansicht ist optimiert und blendet die Navigation aus.
</p>
'''


def main():
    os.makedirs(DOCS_DIR, exist_ok=True)

    # Collect markdown source files
    md_files = {}
    for p in PAGES:
        if p["file"] == "index":
            continue
        # Try multiple locations
        candidates = [
            os.path.join(MD_DIR, f"{p['file']}.md"),
            os.path.join(BASE, "markdown", f"{p['file']}.md"),
        ]
        for c in candidates:
            if os.path.exists(c):
                md_files[p["file"]] = c
                break

    print(f"📁 Markdown-Quellen: {len(md_files)} Dateien gefunden")
    print(f"📂 Ausgabe: {DOCS_DIR}\n")

    built = []

    for p in PAGES:
        nav_html = get_nav_html(p["file"])

        if p["file"] == "index":
            content = build_index()
        elif p["file"] in md_files:
            with open(md_files[p["file"]], 'r', encoding='utf-8') as f:
                content = markdown_to_html(f.read())
        else:
            print(f"  ⚠️  Übersprungen (nicht gefunden): {p['file']}")
            continue

        html = build_page(p["file"], p["title"], content, nav_html)
        out_path = os.path.join(DOCS_DIR, f"{p['file']}.html")
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(html)
        built.append(p["file"])
        print(f"  ✅ {p['file']}.html")

    # Create .nojekyll for GitHub Pages
    nojekyll = os.path.join(DOCS_DIR, '.nojekyll')
    if not os.path.exists(nojekyll):
        open(nojekyll, 'w').close()

    print(f"\n🎉 Fertig! {len(built)} Seiten generiert in docs/")
    print(f"📖 Lokal testen: open {os.path.join(DOCS_DIR, 'index.html')}")


if __name__ == '__main__':
    main()
