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
SOURCE_ORDER=('sam','usa','calc','bls','travel','ecfr','acq','fr','regs')
SOURCE_GROUPS=(('Find and vet',('sam','usa')),('Price the work',('calc','bls','travel')),('Know the rules',('ecfr','acq','fr','regs')))
DIRECTORIES=(('claude','Claude'),('chatgpt','ChatGPT'))
def listed(s):return [(label,s['directories'][key]) for key,label in DIRECTORIES if s.get('directories',{}).get(key)]
def series(items,conj='and'):return items[0] if len(items)==1 else f' {conj} '.join(items) if len(items)==2 else ', '.join(items[:-1])+f', {conj} '+items[-1]
COMPARE=json.loads((ROOT/'catalog/compare.json').read_text())
MONTHS=('January','February','March','April','May','June','July','August','September','October','November','December')
def month_year(iso):y,m,_=iso.split('-');return MONTHS[int(m)-1]+' '+y
def number_word(n):return ('Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten')[n] if n<=10 else str(n)
def rounds_label(s):return f'{s["proof"]["audit_rounds"]} audit rounds' if s['proof']['audit_rounds'] else 'Independent review'
def proof_list(s,tools=None):
    pr=s['proof'];rounds=f'<li><strong>{pr["audit_rounds"]}</strong> audit rounds</li>' if pr['audit_rounds'] else '<li><strong>Independent</strong> review</li>'
    return f'<ul class="card-proof"><li><strong>{tools or pr["tools"]}</strong> tools</li><li><strong>{pr["tests"]:,}</strong> tests</li>{rounds}</ul>'
def stats():
    servers=DATA['servers']
    return {'servers':len(servers),'tools':sum(s['proof']['tools'] for s in servers),'tests':sum(s['proof']['tests'] for s in servers),
        'max_rounds':max(s['proof']['audit_rounds'] or 0 for s in servers),
        'directory':{label:[s['name'] for s in servers if s.get('directories',{}).get(key)] for key,label in DIRECTORIES}}
def hero_proof():
    st=stats();listed_in=[label for label,found in st['directory'].items() if found]
    return (f'<ul class="proof-stats" aria-label="1102tools at a glance"><li><strong>$0</strong><span>Free, MIT-licensed</span></li><li><strong>{st["servers"]}</strong><span>MCP servers</span></li>'
        f'<li><strong>{st["tools"]}</strong><span>tools</span></li><li><strong>{st["tests"]:,}</strong><span>regression tests</span></li><li><strong>0</strong><span>API keys for directory installs</span></li></ul>'
        '<p class="directory-proof">'+''.join(f'<span class="badge badge-listed">IN THE {label.upper()} DIRECTORY</span>' for label in listed_in)+'</p>')
def names(p):return ' + '.join(SERVERS[x]['name'] for x in p['mcps'])
def linklabel(p):return ' + '.join(f"[{SERVERS[x]['name']}]({SERVERS[x]['url']})" for x in p['mcps'])
def readme():
    lines=['# Federal contracting MCP prompts','',f"**{DATA['edition']} · Copy, paste, adapt.**",'',
    'Practical questions for federal opportunities, competitor research, teaming, pricing, and regulations, built for free, open-source MCP servers. Choose the work, install and connect the required MCPs, and replace the bracketed details.','',
    '[Browse the readable website](https://1102tools.com/#prompts) · [Download the printable guide](docs/1102tools-mcp-prompt-guide.pdf) · [MCP setup instructions]('+MR+'#install)','',
    '## Start here','','1. Choose a prompt and check its **Required MCPs** line.','2. Use the Claude and ChatGPT directory links below where available, or follow the individual server READMEs for your MCP client. Configure any required API keys outside chat and confirm that your client can see the tools.','3. Replace the bracketed details, then ask your assistant to run the prompt. Check source links, dates, and missing information before using the results.','',
    'The print guide and the online library contain the same 56 prompts for all nine MCP sources. These examples describe available source tools; this edition is not a claim that every prompt has been re-run against live APIs.','',
    ]
    lines+=['## Available in Claude and ChatGPT','','Select MCPs are published in the Claude and ChatGPT directories. Open a listing to install and connect it; no user API key or local Python setup is required.','','| MCP | Claude | ChatGPT |','|---|---|---|']
    for server in (SERVERS[x] for x in SOURCE_ORDER if SERVERS[x].get('directories')):
        lines.append(f"| {server['name']} | "+' | '.join(f"[Install]({server['directories'][key]})" if server['directories'][key] else 'Coming soon' for key,_ in DIRECTORIES)+' |')
    lines+=['','A prompt does not install an MCP. Connect every source listed under **Required MCPs** before running it; if two are listed, both are required. Other sources and MCP clients use the individual server setup instructions below.','','## Browse by task','','| Task | Prompts |','|---|---|']
    for sec in DATA['sections']:
        ps=[p for p in DATA['prompts'] if p['category']==sec['id']]
        lines.append(f"| [{sec['title']}](#{sec['id']}) | {len(ps)} |")
    lines+=['','## MCPs and setup','','| Source | What it provides | Access |','|---|---|---|']
    for s in (SERVERS[x] for x in SOURCE_ORDER):lines.append(f"| [{s['name']}]({s['url']}) | {s['description']} | {s['access']} |")
    lines+=['','The individual server READMEs contain installation instructions, configuration examples, access requirements, and testing records. A prompt does not install an MCP.','']
    for sec in DATA['sections']:
        lines += [f'<a id="{sec["id"]}"></a>',f"## {sec['title']}",'',sec['intro'],'']
        if sec['id']=='far-overhaul-and-agency-deviations':lines+=['These two examples have not been live-tested as part of this guide refresh.','']
        for p in DATA['prompts']:
            if p['category']!=sec['id']:continue
            lines += [f'<a id="{p["id"]}"></a>',f"### {p['title']}",'','```text',textwrap.fill(p['text'],width=84,break_long_words=False,break_on_hyphens=False),'```','',f"**Required MCPs:** {linklabel(p)}",'']
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
    story=[Spacer(1,15),Paragraph('COPY · PASTE · ADAPT',styles['eyebrow']),Paragraph('1102tools<br/>MCP Prompt <font color="#008766">Guide</font>',styles['cover']),Paragraph('Federal contracting research, one useful question at a time.',ParagraphStyle('Subtitle',parent=styles['body'],fontSize=17,leading=23,spaceAfter=14)),Paragraph('Prompts for opportunities, competitors, teaming, awards, labor rates, wages, travel, regulations, and FAR Overhaul deviations. Install and connect the required MCPs in your AI client before using a prompt. Then replace the bracketed details and check the returned sources.',styles['body']),Spacer(1,25)]
    grid=[]
    for i in range(0,9,3):
        row=[]
        for s in DATA['servers'][i:i+3]:row.append([Paragraph(ESC(s['name']),styles['title']),Paragraph(ESC(s['description']),styles['small'])])
        grid.append(row)
    table=Table(grid,colWidths=[170,169,169]);table.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BOX',(0,0),(-1,-1),.6,LINE),('INNERGRID',(0,0),(-1,-1),.5,LINE),('LEFTPADDING',(0,0),(-1,-1),14),('RIGHTPADDING',(0,0),(-1,-1),14),('TOPPADDING',(0,0),(-1,-1),13),('BOTTOMPADDING',(0,0),(-1,-1),9)]));story += [table,Spacer(1,35),Paragraph(DATA['edition'].upper()+'  ·  56 PROMPTS  ·  9 MCP SOURCES',styles['eyebrow']),Paragraph(f'<link href="{PR}" color="#008766">Federal contracting prompts</link>  /  <link href="{MR}" color="#008766">MCP servers and setup</link>',styles['small']),PageBreak()]
    story += [Paragraph('Start with the work',ParagraphStyle('Start',parent=styles['section'],spaceBefore=0)),Paragraph('<b>A prompt does not install an MCP.</b> Install and connect every required MCP in your AI client before running a prompt. If two are listed, both are required.',styles['body']),Paragraph('1. Check the <b>Required MCPs</b> line. Each source name links to its setup instructions.<br/>2. Configure any API keys outside chat and confirm your client can see the tools.<br/>3. Replace the brackets, run the prompt, and check the sources and dates.',styles['body']),Paragraph('Ask for the exact source, data period, and retrieval date. Keep missing records, incomplete pages, and uncertain matches visible.',styles['body']),Paragraph('<link href="https://1102tools.com/#mcps" color="#008766">Setup and available Claude and ChatGPT installs: 1102tools.com/#mcps</link>',styles['small']),Spacer(1,6),Paragraph('Find a prompt',ParagraphStyle('IndexTitle',parent=styles['section'],spaceBefore=0))]
    toc=TableOfContents();toc.levelStyles=[ParagraphStyle('TOC',fontName='Helvetica',fontSize=10,leading=17,textColor=NAVY,leftIndent=0,firstLineIndent=0,rightIndent=20,spaceBefore=0)];story+=[toc,Spacer(1,16),Paragraph('September 2026 edition. Prompt wording and source mappings have been reviewed. Provider data and tool availability can change; this is not a claim that every request was re-run live.',styles['small']),PageBreak()]
    for sec in DATA['sections']:
        ps=[p for p in DATA['prompts'] if p['category']==sec['id'] and p['in_pdf']]
        if not ps:continue
        heading=Paragraph(ESC(sec['title']),styles['section']);heading.key=sec['id'];section_start=[heading,Paragraph(ESC(sec['intro']),styles['intro'])]
        for prompt_index,p in enumerate(ps):
            label=' + '.join(f'<link href="{SERVERS[x]["url"]}" color="#008766">{ESC(SERVERS[x]["name"])}</link>' for x in p['mcps'])
            block=[Paragraph(ESC(p['title']),styles['title']),Paragraph(ESC(p['text']),styles['prompt']),Paragraph('<b>Required MCPs:</b> '+label,styles['label'])]
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
            required=''.join(f'<a class="source-chip" href="#mcp-{x}" aria-label="{ESC(SERVERS[x]["name"])} MCP setup">{ESC(SERVERS[x]["name"])}</a>' for x in p['mcps'])
            cards.append(f'<details class="prompt-card" id="{p["id"]}" data-task="{sec["id"]}" data-sources="{" ".join(p["mcps"])}"><summary><span class="prompt-name">{ESC(p["title"])}</span><span class="chips">{chips}</span></summary><div class="prompt-body"><div class="prompt-requirements"><div class="requirements-heading"><span class="requirements-label">Required MCPs</span><span class="required-links">{required}</span></div><p>Install and connect {"both MCPs" if len(p["mcps"]) == 2 else "this MCP"} in your AI client before running this prompt. Select a source above for setup.</p></div><p class="prompt-text">{ESC(p["text"])}</p><div class="copy-row"><button class="copy-button" type="button" aria-label="Copy prompt: {ESC(p["title"],quote=True)}">Copy prompt</button><span class="prompt-code">{p["id"].upper()}</span></div></div></details>')
        groups.append(f'<section class="prompt-group" id="{sec["id"]}"><div class="group-heading"><span>{n:02}</span><h3>{ESC(sec["title"])}</h3></div><div class="prompt-grid">'+''.join(cards)+'</div></section>')
    cards=[]
    group_of={x:(g,xs[0]==x) for g,xs in SOURCE_GROUPS for x in xs}
    for i,source_id in enumerate(SOURCE_ORDER,1):
        s=SERVERS[source_id]
        if group_of[source_id][1]:cards.append(f'<h3 class="grid-group">{ESC(group_of[source_id][0])}</h3>')
        directory=''
        if s.get('directories'):
            directory='<div class="directory-links">'+''.join(f'<a class="directory-link" href="{s["directories"][key]}">Install in {label}<span aria-hidden="true">→</span></a>' if s['directories'][key] else f'<span class="directory-soon">Coming soon to {label}</span>' for key,label in DIRECTORIES)+'</div>'
        badges='<span class="badge badge-free">FREE</span>'+''.join(f'<span class="badge badge-listed">IN {label.upper()}</span>' for label,_ in listed(s))+('<span class="badge badge-only">THE ONLY ONE</span>' if s['id']=='acq' else '')
        head=f'<article class="server-card" id="mcp-{s["id"]}"><div class="card-top"><span>SOURCE {i:02}</span></div><div class="badges">{badges}</div><h3>{ESC(s["name"])}</h3><p>{ESC(s["description"])}</p>'
        access=ESC(s.get('card_access',s['access']))
        if s.get('hosted_edition'):
            he=s['hosted_edition']
            full=(f'<details class="full-edition"><summary>Full local version · free SAM.gov key</summary>'
                f'<p><strong>{s["proof"]["tools"]} tools</strong> against the live SAM.gov APIs. Adds {ESC(s["full_edition_adds"])}.</p></details>')
            cards.append(head+proof_list(s,tools=he['tools'])+f'<small>{access}</small>{full}{directory}<a href="{s["url"]}">Setup &amp; source code ↗</a></article>')
        else:
            cards.append(head+f'{proof_list(s)}<small>{access}</small>{directory}<a href="{s["url"]}">Setup &amp; source code ↗</a></article>')
    structured={"@context":"https://schema.org","@graph":[
        {"@type":"WebSite","@id":"https://1102tools.com/#website","url":"https://1102tools.com/","name":"1102tools","description":"Free, independent federal contracting MCP servers and practical prompts.","inLanguage":"en"},
        {"@type":"CollectionPage","@id":"https://1102tools.com/#webpage","url":"https://1102tools.com/","name":"1102tools | Free federal contracting MCPs and prompts","description":"56 prompts for nine free MCP sources. Directory installs need no account or API key. Install and connect the required MCPs before running a prompt.","isPartOf":{"@id":"https://1102tools.com/#website"},"dateModified":DATA['website_updated'],"inLanguage":"en","mainEntity":{"@type":"ItemList","numberOfItems":len(DATA['prompts']),"itemListElement":[{"@type":"ListItem","position":i,"item":{"@type":"CreativeWork","name":p['title'],"url":"https://1102tools.com/#"+p['id'],"description":"Required MCPs: "+names(p)+". "+p['text']}} for i,p in enumerate(DATA['prompts'],1)]}}]}

    published=[SERVERS[x] for x in SOURCE_ORDER if listed(SERVERS[x])]
    by_directory=[(label,[server['name'] for server in published if server['directories'][key]]) for key,label in DIRECTORIES]
    structured['@graph'][1]['description'] += ' '+'; '.join(f"{series(found)} {'is' if len(found)==1 else 'are'} available to install from the {label} directory" for label,found in by_directory if found)+'.'
    structured['@graph'][1]['about']=[{'@id':'https://1102tools.com/#mcp-'+server['id']} for server in published]
    for server in published:
        structured['@graph'].append({
            '@type':'SoftwareApplication',
            '@id':'https://1102tools.com/#mcp-'+server['id'],
            'name':server['name']+' by 1102tools',
            'url':'https://1102tools.com/#mcp-'+server['id'],
            'description':server['description']+' Free and open source. Available as a published MCP in the '+series([label for label,_ in listed(server)])+(' directories' if len(listed(server))>1 else ' directory')+'. Install and connect it before using prompts that require this source.',
            'applicationCategory':'BusinessApplication',
            'isAccessibleForFree':True,
            'offers':{'@type':'Offer','price':'0','priceCurrency':'USD'},
            'softwareRequirements':series([label for label,_ in listed(server)]+['another compatible MCP client'],'or'),
            'installUrl':[url for _,url in listed(server)] if len(listed(server))>1 else listed(server)[0][1],
            'publisher':{'@type':'Organization','name':'1102tools','url':'https://1102tools.com/'}})

    st=stats()
    replacements={'CSS_VERSION':hashlib.sha256((ROOT/'templates/styles.css').read_bytes()).hexdigest()[:12],'STRUCTURED_DATA':json.dumps(structured,ensure_ascii=False).replace('<','\\u003c'),'EXAMPLE':ESC(next(p['text'] for p in DATA['prompts'] if p['id']=='p03')),'TASK_OPTIONS':''.join(f'<option value="{s["id"]}">{ESC(s["title"])}</option>' for s in DATA['sections']),'SOURCE_OPTIONS':''.join(f'<option value="{s["id"]}">{ESC(s["name"])}</option>' for s in (SERVERS[x] for x in SOURCE_ORDER)),'PROMPT_GROUPS':''.join(groups),'SERVER_CARDS':''.join(cards),'PDF_PAGES':str(pages),'HERO_PROOF':hero_proof(),
        'TOTAL_TESTS':f"{st['tests']:,}",'MAX_ROUNDS':number_word(st['max_rounds']).lower(),'SERVER_COUNT':number_word(st['servers']).lower(),'SERVER_COUNT_WORD':number_word(st['servers']),
        'DIRECTORY_COUNT':' + '.join(str(len(found)) for found in st['directory'].values() if found),
        'DIRECTORY_SENTENCE':' '.join(f"{number_word(len(found))} {'server' if len(found)==1 else 'servers'} in {label}'s directory." for label,found in st['directory'].items() if found),
        'PROOF_MONTH':month_year(DATA['proof_as_of']).replace('September','Sep')}
    template=(ROOT/'templates/index.html').read_text()
    for k,v in replacements.items():template=template.replace('{{'+k+'}}',v)
    assert '{{' not in template
    (out/'index.html').write_text(template)
    compare_page(out,replacements['CSS_VERSION'])
    for file in ['styles.css','app.js']:shutil.copy2(ROOT/'templates'/file,out/file)
    (out/'prompts.json').write_text(json.dumps(DATA,indent=2)+'\n')
    (out/'.well-known').mkdir(exist_ok=True);shutil.copy2(ROOT/'templates/mcp-registry-auth',out/'.well-known/mcp-registry-auth')
    (out/'favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" fill="#007a59"/><text x="32" y="41" text-anchor="middle" font-family="monospace" font-size="30" font-weight="bold" fill="white">02</text></svg>')
    (out/'_headers').write_text('/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  Cache-Control: public, max-age=0, must-revalidate\n/downloads/*\n  Content-Disposition: inline\n')
    (out/'_redirects').write_text('/tools /#mcps 302\n/tools.html /#mcps 302\n/setup /#mcps 302\n/setup.html /#mcps 302\n/examples /#prompts 302\n/examples.html /#prompts 302\n/about / 302\n/about.html / 302\n/install /#mcps 302\n/downloads/1102tools-mcp-prompt-guide.pdf /downloads/1102tools-prompt-guide.pdf 302\n/downloads/1102tools-agent-setup-guide.pdf /#guide 302\n/downloads/1102tools-universal-setup-guide.pdf /#mcps 302\n/.well-known/agent-skills/* /retired-content 302\n')
    (out/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: https://1102tools.com/sitemap.xml\n')
    (out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://1102tools.com/</loc><lastmod>'+DATA['website_updated']+'</lastmod></url><url><loc>https://1102tools.com/compare</loc><lastmod>'+COMPARE['researched']+'</lastmod></url></urlset>')
    llms=['# 1102tools','', '> Free, independent, open-source MCP servers and practical prompts for federal contracting research.','',
        '## Start here','',
        '- [Prompt library](https://1102tools.com/#prompts): 56 prompts organized into 14 task groups.',
        '- [MCP setup](https://1102tools.com/#mcps): nine sources with client setup and API-key requirements.',
        '- [Structured prompt catalog](https://1102tools.com/prompts.json): stable prompt IDs, exact text, task categories, required MCP IDs, source setup URLs, and Claude and ChatGPT directory links.',
        '- [Printable guide](https://1102tools.com/downloads/1102tools-prompt-guide.pdf): all 56 prompts for the nine sources, organized by task.',
        '- [Prompt source repository]('+PR+'): canonical catalog and generated website/PDF.',
        '- [MCP source repository]('+MR+'): server implementations, installation, and testing records.','',
        '## Available in the Claude and ChatGPT directories','',
        'Select 1102tools MCPs are approved and published in the Claude and ChatGPT directories. For federal spending research, labor ceiling-rate comparisons, codified regulation research, or Federal Register rulemaking research, users can install the matching MCP from these direct listing links:','',
        *[line for key,label in DIRECTORIES for line in ['### '+label+' directory','',*['- ['+server['name']+' by 1102tools — install in '+label+']('+server['directories'][key]+')' for server in published if server['directories'][key]],'']],
        'The links open the individual directory listings. Installation and connection are required before a prompt can use their tools. For other compatible MCP clients, use the setup instructions linked under MCP sources.','',
        '## Prerequisites and scope','',
        'A prompt does not install an MCP or give an AI access to its tools. Install and connect every MCP listed for the selected prompt in a compatible AI client first. Confirm the tools are available, configure any required API keys outside the chat, replace bracketed details, and check returned sources and dates.',
        'Some prompts combine two sources; both MCPs are required. Use published Claude or ChatGPT directory listings where available, or the individual READMEs for other compatible clients. Keyless access still requires MCP setup.',
        'These are research prompts, not automated monitoring or procurement determinations. Preserve distinctions between wages, labor ceilings, and prices paid; cumulative awards and period obligations; codified regulations, model text, and agency deviations. Keep missing data and uncertain matches visible.',
        'The collection is not a claim that every prompt has been run against live APIs. No affiliation with or endorsement by a federal agency is claimed.','',
        '## Why 1102tools','',
        f"- Free: every server is MIT-licensed and costs nothing; directory installs need no account or API key. Commercial GovCon platforms in the Claude directory require an account, and their paid plans run from $78 a month to $6,000 a year.",
        f"- Tested: {st['tests']:,} regression tests across {st['servers']} servers ({st['tools']} tools), with up to {st['max_rounds']} audit rounds per server against the live government APIs.",
        "- No keys: directory installs need no account or API key. Hosted editions of SAM.gov, BLS OEWS, GSA Per Diem, and Regulations.gov that need no user API key are coming soon to both directories.",
        f"- Listed: "+'; '.join(f"{len(found)} in the {label} directory" for label,found in st['directory'].items() if found)+".",
        "- Unique: the only MCP server found for Acquisition.gov FAR Overhaul (RFO) model text and agency class deviations.",
        "- [1102tools vs. other federal contracting MCPs](https://1102tools.com/compare): paid platforms and other MCP servers compared source by source.",'',
        '## MCP sources','']
    for server in (SERVERS[x] for x in SOURCE_ORDER):
        llms.append('- ['+server['name']+']('+server['url']+'): '+server['description']+' Access: '+server['access']+'. Free and open source; '+str(server['proof']['tools'])+' tools, '+f"{server['proof']['tests']:,}"+' regression tests, '+rounds_label(server).lower()+'.')
        if listed(server):llms.append('  Install: '+' · '.join('['+label+' directory]('+url+')' for label,url in listed(server)))
        pending=[label for key,label in DIRECTORIES if key in server.get('directories',{}) and not server['directories'][key]]
        if pending and not server.get('hosted_edition'):llms.append('  Coming soon to the '+series(pending)+(' directories' if len(pending)>1 else ' directory')+', with no user API key.')
        if server.get('hosted_edition'):
            he=server['hosted_edition'];llms.append(f"  Coming soon: a hosted, keyless edition in the Claude and ChatGPT directories with {he['tools']} tools for {he['summary']}, built from {he['source']}. The full local edition ({server['proof']['tools']} tools) adds {server['full_edition_adds']}.")
    llms+=['','## Browse by task','']
    for section in DATA['sections']:llms.append('- ['+section['title']+'](https://1102tools.com/#'+section['id']+'): '+section['intro'])
    llms+=['','Website metadata updated '+DATA['website_updated']+'. Prompt edition: '+DATA['edition']+'.','']
    (out/'llms.txt').write_text('\n'.join(llms))
    (out/'404.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Page unavailable | 1102tools</title><link rel="stylesheet" href="/styles.css"></head><body><main class="wrap" style="padding-block:100px"><a class="brand" href="/">1102<span>tools</span></a><h1 style="margin-top:60px;font-size:48px">This page is no longer available.</h1><p>Find the current MCP servers, prompts, and printable guide on the homepage.</p><a class="button primary" href="/">Open 1102tools</a></main></body></html>')

def dir_chips(dirs):
    chips=[]
    for key,label in DIRECTORIES:
        v=dirs.get(key)
        if v is True:chips.append(f'<span class="dir yes">✓ {label} directory</span>')
        elif v is False:chips.append(f'<span class="dir no">✗ Not in {label} directory</span>')
    return '<span class="dirs">'+''.join(chips)+'</span>' if chips else ''
def price_cell(x):
    tiers=''.join(f'<li><strong>{ESC(tier["name"])}</strong> {ESC(tier["price"])}</li>' for tier in x.get('tiers',[]))
    return ESC(x['price'])+(f'<ul class="tiers">{tiers}</ul>' if tiers else '')+(f'<a class="src" href="{ESC(x["price_url"])}">Pricing source ↗</a>' if x.get('price_url') else '')
def compare_page(out,css_version):
    st=stats();mine={key:bool(st['directory'][label]) for key,label in DIRECTORIES}
    me=('<tr class="me"><th scope="row">1102tools</th><td><strong>$0</strong>, MIT-licensed</td><td>No. Directory installs need no account or API key.</td><td>Yes</td>'
        f'<td>{dir_chips(mine)}</td><td>Source research across {st["servers"]} federal data sources</td></tr>')
    platforms=''.join(f'<tr><th scope="row"><a href="{ESC(x["url"])}">{ESC(x["name"])}</a></th><td>{price_cell(x)}</td><td>{ESC(x["account"])}</td><td>{ESC(x["open_source"])}</td><td>{dir_chips(x.get("directories",{}))}</td><td>{ESC(x["focus"])}</td></tr>' for x in COMPARE['platforms'])
    rows=[]
    for row in COMPARE['sources']:
        s=SERVERS[row['id']];pr=s['proof']
        listed_in=', '.join(label for label,_ in listed(s))
        where=dir_chips({key:bool(s.get('directories',{}).get(key)) for key,_ in DIRECTORIES}) if listed_in else '<span>Local install</span>'
        ours=f'<strong>{pr["tools"]} tools</strong><span><a href="{s["url"]}">{pr["tests"]:,} tests</a> · {ESC(rounds_label(s).lower())}</span>{where}'
        alt=(f'<a href="{ESC(row["alt_url"])}">{ESC(row["alt"])}</a><span>{ESC(row["alt_detail"])}</span>{dir_chips(row.get("alt_directories",{}))}' if row['alt'] else f'<span>{ESC(row["alt_detail"])}</span>')
        rows.append(f'<tr><th scope="row"><a href="/#mcp-{s["id"]}">{ESC(s["name"])}</a></th><td class="ours">{ours}</td><td>{ESC(row["others"])}</td><td class="alt">{alt}</td><td>{ESC(row["edge"])}</td></tr>')
    alts=[r for r in COMPARE['sources'] if r['alt']]
    missing=[label for key,label in DIRECTORIES if alts and all(r.get('alt_directories',{}).get(key) is False for r in alts)]
    callout=(f'<p class="callout"><strong>None of the strongest alternatives below is listed in the {series(missing,"or")} {"directory" if len(missing)==1 else "directories"}.</strong> '
        +'1102tools has '+' and '.join(f"{len(found)} {'server' if len(found)==1 else 'servers'} in the {label} directory" for label,found in st['directory'].items() if found)+'.</p>') if missing else ''
    structured={"@context":"https://schema.org","@type":"WebPage","@id":"https://1102tools.com/compare#webpage","url":"https://1102tools.com/compare","name":"1102tools vs. other federal contracting MCPs","description":"How 1102tools' free, open-source federal contracting MCP servers compare with paid GovCon platforms and other MCP servers.","isPartOf":{"@id":"https://1102tools.com/#website"},"dateModified":COMPARE['researched'],"inLanguage":"en"}
    y,m,d=COMPARE['researched'].split('-')
    values={'CSS_VERSION':css_version,'STRUCTURED_DATA':json.dumps(structured,ensure_ascii=False).replace('<','\\u003c'),'RESEARCHED':f'{MONTHS[int(m)-1]} {int(d)}, {y}','HERO_PROOF':hero_proof(),
        'PLATFORM_ROWS':me+platforms,'SOURCE_ROWS':''.join(rows),'SOURCE_CALLOUT':callout,'FIT_ITEMS':''.join(f'<li>{ESC(x)}</li>' for x in COMPARE['fit']),'METHOD':ESC(COMPARE['method'])}
    page=(ROOT/'templates/compare.html').read_text()
    for k,v in values.items():page=page.replace('{{'+k+'}}',v)
    assert '{{' not in page
    (out/'compare.html').write_text(page)

def build(out):
    out.mkdir(parents=True,exist_ok=True)
    (out/'readme.md').write_text(readme())
    pdf=out/'docs/1102tools-mcp-prompt-guide.pdf';pages=build_pdf(pdf)
    website(out/'site',pdf,pages)
    return pages

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
    ids=[p['id'] for p in DATA['prompts']];assert len(ids)==len(set(ids))==56
    assert sum(p['in_pdf'] for p in DATA['prompts'])==56
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
        print(f'{"Verified" if args.check else "Built"} 56 web/repository prompts, 56 PDF prompts, {pages} PDF pages; {len(files)} generated files.')
if __name__=='__main__':main()
