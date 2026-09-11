#!/usr/bin/env python3
"""Generate README, printable PDF, and website from catalog/prompts.json.

Run: python tools/build.py
Validate without overwriting: python tools/build.py --check
Requires reportlab. Generated products must not be hand-edited.
"""
from pathlib import Path
import argparse,html,json,re,shutil,tempfile,hashlib,textwrap
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate,Frame,PageTemplate,Paragraph,Spacer,PageBreak,KeepTogether,Table,TableStyle
from reportlab.platypus.tableofcontents import TableOfContents
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'catalog/prompts.json').read_text())
SERVERS={s['id']:s for s in DATA['servers']}
PR='https://github.com/1102tools-dev/federal-contracting-prompts'
MR='https://github.com/1102tools-dev/federal-contracting-mcps'
ESC=html.escape
GREEN=colors.HexColor('#008766');NAVY=colors.HexColor('#172f43');MUTED=colors.HexColor('#566b71');LINE=colors.HexColor('#d4e0dd')
def names(p):return ' + '.join(SERVERS[x]['name'] for x in p['mcps'])
def linklabel(p):return ' + '.join(f"[{SERVERS[x]['name']}]({SERVERS[x]['url']})" for x in p['mcps'])
def readme():
    lines=['# Federal contracting MCP prompts','',f"**{DATA['edition']} · Copy, paste, adapt.**",'',
    'Practical questions for federal opportunities, competitor research, teaming, pricing, and regulations. Choose the work, connect the MCPs named beneath the prompt, and replace the bracketed details.','',
    '[Browse the readable website](https://1102tools.com/#prompts) · [Download the printable guide](docs/1102tools-mcp-prompt-guide.pdf) · [MCP setup instructions]('+MR+'#install)','',
    '## Start here','','1. Choose a prompt and check its **MCPs used** line.','2. Install those servers using their individual READMEs. Configure any required API keys outside chat and confirm that your client can see the tools.','3. Replace the bracketed details, then ask your assistant to run the prompt. Check source links, dates, and missing information before using the results.','',
    'The print guide contains 54 prompts for the original eight MCP sources. The online library also includes two Acquisition.gov examples for FAR Overhaul research. These examples describe available source tools; this edition is not a claim that every prompt has been re-run against live APIs.','',
    '## Browse by task','','| Task | Prompts |','|---|---|']
    for sec in DATA['sections']:
        ps=[p for p in DATA['prompts'] if p['category']==sec['id']]
        lines.append(f"| [{sec['title']}](#{sec['id']}) | {len(ps)} |")
    lines+=['','## MCPs and setup','','| Source | What it provides | Access |','|---|---|---|']
    for s in DATA['servers']:lines.append(f"| [{s['name']}]({s['url']}) | {s['description']} | {s['access']} |")
    lines+=['','The individual server READMEs contain installation instructions, configuration examples, access requirements, and testing records. A prompt does not install an MCP.','']
    for sec in DATA['sections']:
        lines += [f'<a id="{sec["id"]}"></a>',f"## {sec['title']}",'',sec['intro'],'']
        if sec['id']=='far-overhaul-and-agency-deviations':lines+=['These two examples have not been live-tested as part of this guide refresh.','']
        for p in DATA['prompts']:
            if p['category']!=sec['id']:continue
            lines += [f'<a id="{p["id"]}"></a>',f"### {p['title']}",'','```text',textwrap.fill(p['text'],width=84,break_long_words=False,break_on_hyphens=False),'```','',f"**MCPs used:** {linklabel(p)}",'']
    lines+=['## Maintaining this library','','Edit `catalog/prompts.json`, then run `python tools/build.py`. The README, PDF, and website are generated from that one file. `python tools/build.py --check` verifies that generated copies match. See [maintenance notes](MAINTAINING.md).','','MIT licensed. Built by James Jenrette. Independently developed and not affiliated with or endorsed by any federal agency.','']
    return '\n'.join(lines)
class Doc(BaseDocTemplate):
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and f.style.name=='Section':
            key='section-'+str(getattr(f,'key',''))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(f.getPlainText(),key,level=0)
            self.notify('TOCEntry',(0,f.getPlainText(),self.page,key))
def page(c,doc):
    c.setFillColor(GREEN);c.rect(0,788,612,4,fill=1,stroke=0)
    if doc.page>1:
        c.setFont('Helvetica',8);c.setFillColor(MUTED);c.drawString(52,758,'1102tools  /  MCP PROMPT GUIDE');c.drawRightString(560,758,DATA['edition'].upper())
        c.setStrokeColor(LINE);c.line(52,45,560,45);c.setFont('Helvetica',8);c.drawString(52,31,'COPY · PASTE · ADAPT');c.drawRightString(560,31,str(doc.page))
def build_pdf(dest):
    dest.parent.mkdir(parents=True,exist_ok=True)
    styles={
    'body':ParagraphStyle('Body',fontName='Times-Roman',fontSize=11.2,leading=16,textColor=NAVY,spaceAfter=10),
    'small':ParagraphStyle('Small',fontName='Helvetica',fontSize=8.7,leading=12,textColor=MUTED,spaceAfter=8),
    'section':ParagraphStyle('Section',fontName='Times-Bold',fontSize=22,leading=26,textColor=NAVY,spaceBefore=20,spaceAfter=9,keepWithNext=True),
    'intro':ParagraphStyle('Intro',fontName='Times-Roman',fontSize=11.2,leading=16,textColor=MUTED,spaceAfter=17,keepWithNext=True),
    'title':ParagraphStyle('PromptTitle',fontName='Helvetica-Bold',fontSize=10.4,leading=14,textColor=NAVY,spaceAfter=6),
    'prompt':ParagraphStyle('Prompt',fontName='Times-Italic',fontSize=11,leading=15.5,textColor=colors.HexColor('#304f5b'),spaceAfter=8),
    'label':ParagraphStyle('Label',fontName='Helvetica',fontSize=8.2,leading=11,textColor=GREEN,spaceAfter=5),
    'cover':ParagraphStyle('Cover',fontName='Times-Roman',fontSize=39,leading=42,textColor=NAVY,spaceAfter=20),
    'eyebrow':ParagraphStyle('Eyebrow',fontName='Helvetica',fontSize=9,leading=14,textColor=GREEN,spaceAfter=20),
    }
    story=[Spacer(1,15),Paragraph('COPY · PASTE · ADAPT',styles['eyebrow']),Paragraph('1102tools<br/>MCP Prompt <font color="#008766">Guide</font>',styles['cover']),Paragraph('Federal contracting research, one useful question at a time.',ParagraphStyle('Subtitle',parent=styles['body'],fontSize=17,leading=23,spaceAfter=14)),Paragraph('Prompts for opportunities, competitors, teaming, awards, labor rates, wages, travel, and regulations. Connect the named MCPs, replace the bracketed details, and work from the returned sources.',styles['body']),Spacer(1,25)]
    grid=[]
    for i in range(0,8,2):
        row=[]
        for s in DATA['servers'][i:i+2]:row.append([Paragraph(ESC(s['name']),styles['title']),Paragraph(ESC(s['description']),styles['small'])])
        grid.append(row)
    table=Table(grid,colWidths=[254,254]);table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOX',(0,0),(-1,-1),.6,LINE),('INNERGRID',(0,0),(-1,-1),.5,LINE),('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14),('TOPPADDING',(0,0),(-1,-1),13),('BOTTOMPADDING',(0,0),(-1,-1),9)]));story += [table,Spacer(1,35),Paragraph(DATA['edition'].upper()+'  ·  54 PROMPTS  ·  8 MCP SOURCES',styles['eyebrow']),Paragraph(f'<link href="{PR}" color="#008766">Federal contracting prompts</link>  /  <link href="{MR}" color="#008766">MCP servers and setup</link>',styles['small']),PageBreak()]
    story += [Paragraph('Start with the work',ParagraphStyle('Start',parent=styles['section'],spaceBefore=0)),Paragraph('1. Choose a prompt. The MCP labels tell you which sources to connect.<br/>2. Follow those servers\' GitHub READMEs for installation and any API keys.<br/>3. Replace the brackets, run the prompt, and check the sources and dates.',styles['body']),Paragraph('Ask for the exact source, data period, and retrieval date. Keep missing records, incomplete pages, and uncertain matches visible. If a required MCP is unavailable, connect it before treating the answer as retrieved research.',styles['body']),Paragraph(f'<link href="{PR}" color="#008766">Prompt repository</link>  ·  <link href="{MR}" color="#008766">MCP repository</link>  ·  <link href="{MR}#install" color="#008766">Installation instructions</link>',styles['small']),Spacer(1,12),Paragraph('Find a prompt',ParagraphStyle('IndexTitle',parent=styles['section'],spaceBefore=0))]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='Helvetica',fontSize=10,leading=18,textColor=NAVY,leftIndent=0,firstLineIndent=0,rightIndent=20,spaceBefore=3)];story+=[toc,Spacer(1,16),Paragraph('September 2026 edition. Prompt wording and source mappings have been reviewed. Provider data and tool availability can change; this is not a claim that every request was re-run live.',styles['small']),PageBreak()]
    for sec in DATA['sections']:
        ps=[p for p in DATA['prompts'] if p['category']==sec['id'] and p['in_pdf']]
        if not ps:continue
        heading=Paragraph(ESC(sec['title']),styles['section']);heading.key=sec['id'];section_start=[heading,Paragraph(ESC(sec['intro']),styles['intro'])]
        for prompt_index,p in enumerate(ps):
            label=' + '.join(f'<link href="{SERVERS[x]["url"]}" color="#008766">{ESC(SERVERS[x]["name"])}</link>' for x in p['mcps'])
            block=[Paragraph(ESC(p['title']),styles['title']),Paragraph(ESC(p['text']),styles['prompt']),Paragraph('MCPs used: '+label,styles['label'])]
            t=Table([[block]],colWidths=[508]);t.setStyle(TableStyle([('LINEBEFORE',(0,0),(0,0),1.3,LINE),('LEFTPADDING',(0,0),(-1,-1),12),('RIGHTPADDING',(0,0),(-1,-1),4),('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),5)]));story += [KeepTogether((section_start if prompt_index==0 else [])+[t,Spacer(1,11)])]
    doc=Doc(str(dest),pagesize=(612,792),leftMargin=52,rightMargin=52,topMargin=55,bottomMargin=59,title=DATA['title'],author='James Jenrette / 1102tools',subject=DATA['edition']+' MCP prompt guide',allowSplitting=1)
    doc.addPageTemplates(PageTemplate(id='all',frames=[Frame(52,59,508,678,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)],onPage=page))
    doc.multiBuild(story,canvasmaker=lambda *a,**kw:canvas.Canvas(*a,**dict(kw,invariant=1)))
    return doc.page

def website(out,pdf,pages):
    out.mkdir(parents=True,exist_ok=True);(out/'downloads').mkdir(exist_ok=True)
    shutil.copy2(pdf,out/'downloads/1102tools-prompt-guide.pdf')
    groups=[]
    for n,sec in enumerate(DATA['sections'],1):
        cards=[]
        for p in DATA['prompts']:
            if p['category']!=sec['id']:continue
            chips=''.join(f'<span class="source-chip">{ESC(SERVERS[x]["name"])}</span>' for x in p['mcps'])
            cards.append(f'<details class="prompt-card" id="{p["id"]}" data-task="{sec["id"]}" data-sources="{" ".join(p["mcps"])}"><summary><span class="prompt-name">{ESC(p["title"])}</span><span class="chips">{chips}</span></summary><div class="prompt-body"><p class="prompt-text">{ESC(p["text"])}</p><div class="copy-row"><button class="copy-button" type="button" aria-label="Copy prompt: {ESC(p["title"],quote=True)}">Copy prompt</button><span class="prompt-code">{p["id"].upper()}</span></div></div></details>')
        note='<p class="online-note">Additional online examples; not live-tested as part of this guide refresh.</p>' if sec['id'].startswith('far-overhaul') else ''
        groups.append(f'<section class="prompt-group" id="{sec["id"]}"><div class="group-heading"><span>{n:02}</span><h3>{ESC(sec["title"])}</h3></div>{note}<div class="prompt-grid">'+''.join(cards)+'</div></section>')
    cards=[]
    for i,s in enumerate(DATA['servers'],1):cards.append(f'<article class="server-card"><span>SOURCE {i:02}</span><h3>{ESC(s["name"])}</h3><p>{ESC(s["description"])}</p><small>{ESC(s["access"])}</small><a href="{s["url"]}">Setup &amp; source code ↗</a></article>')
    replacements={'EXAMPLE':ESC(next(p['text'] for p in DATA['prompts'] if p['id']=='p03')),'TASK_OPTIONS':''.join(f'<option value="{s["id"]}">{ESC(s["title"])}</option>' for s in DATA['sections']),'SOURCE_OPTIONS':''.join(f'<option value="{s["id"]}">{ESC(s["name"])}</option>' for s in DATA['servers']),'PROMPT_GROUPS':''.join(groups),'SERVER_CARDS':''.join(cards),'PDF_PAGES':str(pages)}
    template=(ROOT/'templates/index.html').read_text()
    for k,v in replacements.items():template=template.replace('{{'+k+'}}',v)
    assert '{{' not in template
    (out/'index.html').write_text(template)
    for file in ['styles.css','app.js']:shutil.copy2(ROOT/'templates'/file,out/file)
    (out/'prompts.json').write_text(json.dumps(DATA,indent=2)+'\n')
    (out/'.well-known').mkdir(exist_ok=True);shutil.copy2(ROOT/'templates/mcp-registry-auth',out/'.well-known/mcp-registry-auth')
    (out/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="12" fill="#007a59"/><text x="32" y="41" text-anchor="middle" font-family="monospace" font-size="30" font-weight="bold" fill="white">02</text></svg>')
    (out/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Cache-Control: public, max-age=0, must-revalidate\n/downloads/*\n  Content-Disposition: inline\n')
    (out/'_redirects').write_text('/tools /#mcps 302\n/tools.html /#mcps 302\n/setup /#mcps 302\n/setup.html /#mcps 302\n/examples /#prompts 302\n/examples.html /#prompts 302\n/about / 302\n/about.html / 302\n/install /#mcps 302\n/downloads/1102tools-mcp-prompt-guide.pdf /downloads/1102tools-prompt-guide.pdf 302\n/downloads/1102tools-agent-setup-guide.pdf /#guide 302\n/downloads/1102tools-universal-setup-guide.pdf /#mcps 302\n/.well-known/agent-skills/* /retired-content 302\n')
    (out/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://1102tools.com/sitemap.xml\n')
    (out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://1102tools.com/</loc><lastmod>'+DATA['date']+'</lastmod></url></urlset>')
    (out/'llms.txt').write_text('# 1102tools\n\nFederal contracting MCP servers and prompts.\n\n- [Prompt library]('+PR+')\n- [MCP catalog and setup]('+MR+')\n- [Print guide](https://1102tools.com/downloads/1102tools-prompt-guide.pdf)\n- [Structured prompts](https://1102tools.com/prompts.json)\n')
    (out/'404.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page unavailable | 1102tools</title><link rel="stylesheet" href="/styles.css"></head><body><main class="wrap" style="padding-block:100px"><a class="brand" href="/">1102<span>tools</span></a><h1 style="margin-top:60px;font-size:48px">This page is no longer available.</h1><p>Find the current MCP servers, prompts, and printable guide on the homepage.</p><a class="button primary" href="/">Open 1102tools</a></main></body></html>')

def build(out):
    out.mkdir(parents=True,exist_ok=True)
    (out/'readme.md').write_text(readme())
    pdf=out/'docs/1102tools-mcp-prompt-guide.pdf';pages=build_pdf(pdf)
    website(out/'site',pdf,pages)
    return pages

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    ids=[p['id'] for p in DATA['prompts']];assert len(ids)==len(set(ids))==56
    assert sum(p['in_pdf'] for p in DATA['prompts'])==54
    for p in DATA['prompts']:assert p['mcps'] and all(x in SERVERS for x in p['mcps'])
    with tempfile.TemporaryDirectory() as tmp:
        tmp=Path(tmp);pages=build(tmp)
        files=[p for p in tmp.rglob('*') if p.is_file()]
        if args.check:
            bad=[str(p.relative_to(tmp)) for p in files if not (ROOT/p.relative_to(tmp)).exists() or p.read_bytes()!=(ROOT/p.relative_to(tmp)).read_bytes()]
            if bad:raise SystemExit('Generated copies differ: '+', '.join(bad))
        else:
            for p in files:
                dest=ROOT/p.relative_to(tmp);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
        print(f'{"Verified" if args.check else "Built"} 56 web/repository prompts, 54 PDF prompts, {pages} PDF pages; {len(files)} generated files.')
if __name__=='__main__':main()
