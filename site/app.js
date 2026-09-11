'use strict';
const search=document.getElementById('search');
const task=document.getElementById('task');
const source=document.getElementById('source');
const cards=[...document.querySelectorAll('.prompt-card')];
const count=document.getElementById('result-count');
function filter(){let n=0;const query=search.value.trim().toLowerCase();for(const card of cards){const match=(!query||card.textContent.toLowerCase().includes(query))&&(!task.value||card.dataset.task===task.value)&&(!source.value||card.dataset.sources.split(' ').includes(source.value));card.hidden=!match;if(match)n++;}for(const group of document.querySelectorAll('.prompt-group'))group.hidden=![...group.querySelectorAll('.prompt-card')].some(x=>!x.hidden);count.textContent=n+' '+(n===1?'prompt':'prompts')+' shown';document.getElementById('no-results').hidden=n!==0;}
search.addEventListener('input',filter);task.addEventListener('change',filter);source.addEventListener('change',filter);
document.getElementById('reset').addEventListener('click',()=>{search.value='';task.value='';source.value='';filter();search.focus();});
for(const button of document.querySelectorAll('.copy-button'))button.addEventListener('click',async()=>{const text=button.closest('.prompt-card').querySelector('.prompt-text').textContent;try{await navigator.clipboard.writeText(text);button.textContent='Copied';setTimeout(()=>{button.textContent='Copy prompt';},2000);}catch{button.textContent='Select text to copy';const range=document.createRange();range.selectNodeContents(button.closest('.prompt-card').querySelector('.prompt-text'));const selection=window.getSelection();selection.removeAllRanges();selection.addRange(range);}});
function openHash(){const id=location.hash.slice(1);const target=document.getElementById(id);if(target?.classList.contains('prompt-card')){search.value='';task.value='';source.value='';filter();target.open=true;target.scrollIntoView();}}
window.addEventListener('hashchange',openHash);openHash();
