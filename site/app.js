'use strict';
const search=document.getElementById('search');
const task=document.getElementById('task');
const source=document.getElementById('source');
const cards=[...document.querySelectorAll('.prompt-card')];
const count=document.getElementById('result-count');
const groups=document.getElementById('prompt-groups');
const showAll=document.getElementById('show-all');
let expanded=false;
showAll.textContent='Show all '+cards.length+' prompts ↓';
function layout(){const active=search.value.trim()||task.value||source.value;const collapse=!expanded&&!active;groups.classList.toggle('collapsed',collapse);showAll.hidden=!collapse;}
function filter(){let n=0;const query=search.value.trim().toLowerCase();for(const card of cards){const match=(!query||card.textContent.toLowerCase().includes(query))&&(!task.value||card.dataset.task===task.value)&&(!source.value||card.dataset.sources.split(' ').includes(source.value));card.hidden=!match;if(match)n++;}for(const group of document.querySelectorAll('.prompt-group'))group.hidden=![...group.querySelectorAll('.prompt-card')].some(x=>!x.hidden);count.textContent=n+' '+(n===1?'prompt':'prompts')+' shown';document.getElementById('no-results').hidden=n!==0;groups.hidden=n===0;layout();}
showAll.addEventListener('click',()=>{expanded=true;layout();});layout();
search.addEventListener('input',filter);task.addEventListener('change',filter);source.addEventListener('change',filter);
document.getElementById('reset').addEventListener('click',()=>{search.value='';task.value='';source.value='';filter();search.focus();});
for(const button of document.querySelectorAll('.copy-button'))button.addEventListener('click',async()=>{const text=button.closest('.prompt-card').querySelector('.prompt-text').textContent;try{await navigator.clipboard.writeText(text);button.textContent='Copied';setTimeout(()=>{button.textContent='Copy prompt';},2000);}catch{button.textContent='Select text to copy';const range=document.createRange();range.selectNodeContents(button.closest('.prompt-card').querySelector('.prompt-text'));const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);}});
function openHash(){const id=location.hash.slice(1);const target=document.getElementById(id);if(target?.classList.contains('server-card')&&getComputedStyle(target).display==='none'){expandMcps();target.scrollIntoView();}if(target?.classList.contains('prompt-card')||target?.classList.contains('prompt-group')){expanded=true;search.value='';task.value='';source.value='';filter();if(target.classList.contains('prompt-card'))target.open=true;target.scrollIntoView();}}
const serverGrid=document.getElementById('server-grid');
const showAllMcps=document.getElementById('show-all-mcps');
showAllMcps.textContent='Show all '+serverGrid.querySelectorAll('.server-card').length+' MCPs ↓';
function expandMcps(){serverGrid.classList.remove('collapsed');showAllMcps.hidden=true;}
serverGrid.classList.add('collapsed');showAllMcps.hidden=false;showAllMcps.addEventListener('click',expandMcps);
window.addEventListener('hashchange',openHash);openHash();
// "Watch the demo" opens the video in a pop-up player on the page; without JavaScript the link plays the file directly.
const player=document.getElementById('demo-player');
if(player&&player.showModal){
  const video=player.querySelector('video');
  const stop=()=>{video.pause();video.removeAttribute('src');video.load();};
  document.addEventListener('click',e=>{const a=e.target.closest('a.demo-link');if(!a||e.metaKey||e.ctrlKey||e.shiftKey)return;e.preventDefault();video.src=a.getAttribute('href');player.showModal();video.play().catch(()=>{});});
  player.querySelector('.demo-close').addEventListener('click',()=>player.close());
  player.addEventListener('click',e=>{if(e.target===player)player.close();});
  player.addEventListener('close',stop);
}
