#!/usr/bin/env python3
"""Verify publication parity, link scope, and retired-content removal."""
from pathlib import Path
from html.parser import HTMLParser
import json,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'catalog/prompts.json').read_text())
class Page(HTMLParser):
 def __init__(self):super().__init__();self.current=None;self.in_text=False;self.card_texts={};self.prompts={};self.ids=[];self.links=[];self.texts=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if a.get('id'):self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='details' and 'prompt-card' in (a.get('class') or ''):self.current=a.get('id');self.prompts[self.current]='';self.card_texts[self.current]=''
  if t=='p' and a.get('class')=='prompt-text':self.in_text=True
 def handle_endtag(self,t):
  if t=='p':self.in_text=False
  if t=='details':self.current=None
 def handle_data(self,s):
  self.texts.append(s)
  if self.current:self.card_texts[self.current]+=s
  if self.in_text and self.current:self.prompts[self.current]+=s
compare=json.loads((ROOT/'catalog/compare.json').read_text())
APPROVED={'https://github.com/1102tools-dev/federal-contracting-mcps','https://tango.makegov.com/','https://tango.makegov.com/subscriptions/pricing/','https://kthq.org/','https://www.youtube.com/@1102tools','https://www.youtube.com/@1102tools/shorts','https://www.war.gov/News/Contracts/','https://www.youtube.com/playlist?list=PLdrqO_0dQ1LM','https://www.youtube.com/watch?v=ybkwXEZXsaw&list=PLdrqO_0dQ1LM','https://www.youtube.com/watch?v=V8MDVOluNRg&list=PLdrqO_0dQ1LM','https://www.youtube.com/watch?v=f1623C0UoUU&list=PLdrqO_0dQ1LM'}
page=Page();page.feed((ROOT/'site/index.html').read_text())
assert len(page.ids)==len(set(page.ids)),'duplicate HTML IDs'
assert len(page.prompts)==len(data['prompts'])
for p in data['prompts']:assert page.prompts[p['id']]==p['text'],p['id']
structured=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',(ROOT/'site/index.html').read_text(),re.S).group(1))
items=next(x for x in structured['@graph'] if x['@type']=='CollectionPage')['mainEntity']['itemListElement']
descriptions={x['item']['url'].split('#')[-1]:x['item']['description'] for x in items}
for p in data['prompts']:
 if p.get('requires_local_full_sam'):
  label='This prompt needs the Local full SAM.gov edition for live API or detailed certification/integrity fields.'
  assert label in page.card_texts[p['id']] and label in descriptions[p['id']],p['id']
 if p.get('sam_edition_note'):
  assert p['sam_edition_note'] in page.card_texts[p['id']] and p['sam_edition_note'] in descriptions[p['id']],p['id']
 assert p['text'] in descriptions[p['id']],p['id']
for link in page.links:
 if link.startswith('#'):assert link[1:] in page.ids,link
 if link.startswith('https://'):assert link in APPROVED or link in {url for s in data['servers'] for url in s.get('directories',{}).values() if url} or link in {s['demo'] for s in data['servers'] if s.get('demo')} or link.startswith(('https://github.com/1102tools-dev/federal-contracting-prompts','https://github.com/1102tools-dev/federal-contracting-mcps')),link
 else:assert link.startswith(('#','/')),link
compare_page=Page();compare_page.feed((ROOT/'site/compare.html').read_text())
compare_urls={x['url'] for x in compare['platforms']}|{x['price_url'] for x in compare['platforms'] if x.get('price_url')}|{x['alt_url'] for x in compare['sources'] if x['alt_url']}
for link in compare_page.links:
 if link.startswith('https://'):assert link in APPROVED or link in compare_urls or link.startswith(('https://github.com/1102tools-dev/federal-contracting-prompts','https://github.com/1102tools-dev/federal-contracting-mcps')),link
 else:assert link.startswith(('/','#')),link
 if link.startswith('/#'):assert link[2:] in page.ids,link
 if link.startswith('#'):assert link[1:] in compare_page.ids,link
assert {x['id'] for x in compare['sources']}=={s['id'] for s in data['servers']},'compare page must cover every source'
# One page per server under /mcp/, each linked from its card.
server_files=sorted((ROOT/'site/mcp').glob('*.html'))
assert len(server_files)==len(data['servers']),'one page per server'
directory_urls={url for s in data['servers'] for url in s.get('directories',{}).values() if url}
youtube_urls={'https://www.youtube.com/watch?v='+s['youtube']['id'] for s in data['servers'] if s.get('youtube')}
server_texts=[]
for f in server_files:
 sp=Page();sp.feed(f.read_text());server_texts.append(''.join(sp.texts))
 assert len(sp.ids)==len(set(sp.ids)),f.name
 for link in sp.links:
  if link.startswith('https://'):assert link in APPROVED or link in directory_urls or link in youtube_urls or re.fullmatch(r'https://[a-z-]+\.1102tools\.com/privacy',link) or link.startswith(('https://github.com/1102tools-dev/federal-contracting-prompts','https://github.com/1102tools-dev/federal-contracting-mcps')),(f.name,link)
  elif link.startswith('#'):assert link[1:] in sp.ids,(f.name,link)
  else:assert link.startswith('/'),(f.name,link)
  if link.startswith('/#'):assert link[2:] in page.ids,(f.name,link)
  if link.startswith('/mcp/'):assert (ROOT/'site'/(link[1:]+'.html')).exists(),(f.name,link)
for link in page.links:
 if link.startswith('/mcp/'):assert (ROOT/'site'/(link[1:]+'.html')).exists(),link
assert sum(l.startswith('/mcp/') for l in page.links)==len(data['servers']),'each card links to its server page'
normalize=lambda s:re.sub(r'\s+','',s)
readme=(ROOT/'readme.md').read_text()
blocks=re.findall(r'```text\n(.*?)```',readme,re.S)
assert len(blocks)==len(data['prompts'])
for p,b in zip(data['prompts'],blocks):assert normalize(p['text'])==normalize(b),p['id']
pdf=PdfReader(ROOT/'docs/1102tools-mcp-prompt-guide.pdf')
text='\n'.join(p.extract_text() for p in pdf.pages)
for p in data['prompts']:
 if p['in_pdf']:assert normalize(p['text']) in normalize(text),'PDF missing '+p['id']
 else:assert p['title'] not in text,'online-only prompt in print'
for page_ in pdf.pages:
 for annotation in page_.get('/Annots',[]):
  action=annotation.get_object().get('/A')
  if action and action.get('/URI'):
   url=str(action['/URI']);assert url == 'https://1102tools.com/#mcps' or url.startswith(('https://github.com/1102tools-dev/federal-contracting-prompts','https://github.com/1102tools-dev/federal-contracting-mcps')),url
for forbidden in ['universal-setup','agent-setup','federal-contracting-agents','federal-contracting-skills','August 2026','124 TOOLS','every pattern run live','plain English','one click','recommended']:
 assert forbidden.lower() not in (text+'\n'+readme+'\n'+''.join(page.texts)+'\n'+''.join(compare_page.texts)+'\n'+''.join(server_texts)).lower(),forbidden
assert data==json.loads((ROOT/'site/prompts.json').read_text())
assert (ROOT/'docs/1102tools-mcp-prompt-guide.pdf').read_bytes()==(ROOT/'site/downloads/1102tools-prompt-guide.pdf').read_bytes()
print(f'PASS: {len(data["prompts"])} README/web prompts; {sum(p["in_pdf"] for p in data["prompts"])} complete PDF prompts; approved links; no retired offerings; duplicate-free anchors;',len(pdf.pages),'PDF pages.')
