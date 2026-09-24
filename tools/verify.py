#!/usr/bin/env python3
"""Verify publication parity, link scope, and retired-content removal."""
from pathlib import Path
from html.parser import HTMLParser
import json,re
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'catalog/prompts.json').read_text())
class Page(HTMLParser):
 def __init__(self):super().__init__();self.current=None;self.in_text=False;self.prompts={};self.ids=[];self.links=[];self.texts=[]
 def handle_starttag(self,t,a):
  a=dict(a)
  if a.get('id'):self.ids.append(a['id'])
  if t=='a':self.links.append(a.get('href',''))
  if t=='details':self.current=a.get('id');self.prompts[self.current]=''
  if t=='p' and a.get('class')=='prompt-text':self.in_text=True
 def handle_endtag(self,t):
  if t=='p':self.in_text=False
  if t=='details':self.current=None
 def handle_data(self,s):
  self.texts.append(s)
  if self.in_text and self.current:self.prompts[self.current]+=s
page=Page();page.feed((ROOT/'site/index.html').read_text())
assert len(page.ids)==len(set(page.ids)),'duplicate HTML IDs'
assert len(page.prompts)==56
for p in data['prompts']:assert page.prompts[p['id']]==p['text'],p['id']
for link in page.links:
 if link.startswith('#'):assert link[1:] in page.ids,link
 if link.startswith('https://'):assert link in {url for s in data['servers'] for url in s.get('directories',{}).values() if url} or link.startswith(('https://github.com/1102tools-dev/federal-contracting-prompts','https://github.com/1102tools-dev/federal-contracting-mcps')),link
 else:assert link.startswith(('#','/')),link
readme=(ROOT/'readme.md').read_text()
blocks=re.findall(r'```text\n(.*?)```',readme,re.S)
assert len(blocks)==56
normalize=lambda s:re.sub(r'\s+','',s)
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
for forbidden in ['universal-setup','agent-setup','federal-contracting-agents','federal-contracting-skills','August 2026','124 TOOLS','every pattern run live']:
 assert forbidden.lower() not in (text+'\n'+readme+'\n'+''.join(page.texts)).lower(),forbidden
assert 'Acquisition.gov' not in text
assert data==json.loads((ROOT/'site/prompts.json').read_text())
assert (ROOT/'docs/1102tools-mcp-prompt-guide.pdf').read_bytes()==(ROOT/'site/downloads/1102tools-prompt-guide.pdf').read_bytes()
print('PASS: 56 README/web prompts; 54 complete PDF prompts; approved links; no retired offerings; duplicate-free anchors;',len(pdf.pages),'PDF pages.')
