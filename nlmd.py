"""Minimal markdown -> HTML for newsletter issues (paragraphs, ## headings, **bold**, [links](url), emails)."""
import html, re
EMAIL_RE = re.compile(r'(?<![\w.:/-])([\w.+-]+@[\w-]+\.[\w.-]*\w)')
def inline(t, link_style=""):
    t = html.escape(t, quote=False)
    st = f' style="{link_style}"' if link_style else ""
    links = []
    def keep(m):
        links.append(f'<a href="{html.escape(m.group(2))}"{st}>{m.group(1)}</a>'); return f"\x00{len(links)-1}\x00"
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', keep, t)
    t = EMAIL_RE.sub(lambda m: f'<a href="mailto:{m.group(1)}"{st}>{m.group(1)}</a>', t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    return re.sub(r'\x00(\d+)\x00', lambda m: links[int(m.group(1))], t)
def md_to_html(md, link_style="", h2_style="", p_style=""):
    out = []
    hs = f' style="{h2_style}"' if h2_style else ""; ps = f' style="{p_style}"' if p_style else ""
    for block in re.split(r'\n\s*\n', md.strip()):
        lines = block.strip().split("\n")
        if len(lines) == 1 and lines[0].startswith("## "):
            out.append(f"<h2{hs}>{inline(lines[0][3:], link_style)}</h2>")
        else:
            out.append(f"<p{ps}>" + "<br>\n".join(inline(l, link_style) for l in lines) + "</p>")
    return "\n".join(out)
def md_to_text(md):
    t = re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)', r'\1: \2', md.strip())
    t = re.sub(r'\*\*(.+?)\*\*', r'\1', t)
    return re.sub(r'^## (.*)$', lambda m: m.group(1).upper(), t, flags=re.M)
