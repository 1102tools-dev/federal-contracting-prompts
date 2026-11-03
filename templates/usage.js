'use strict';
// Reads the daily numbers file (updated at 12 a.m. Eastern) and fills the homepage stat and the /usage page.
// The file holds daily tool-call counts per app for the last 7 finished Eastern days, midnight to midnight, nothing else.
(function(){
const APPS=[['claude','Claude','#168276'],['claude-code','Claude Code','#5fae9f'],['chatgpt','ChatGPT','#2e5f94'],['codex','Codex','#7a9fd0'],['other','Other','#8a6fb0'],['perplexity','Perplexity','#d9a441']];
const FAMILIES=[['Anthropic',['claude','claude-code']],['OpenAI',['chatgpt','codex']],['Perplexity',['perplexity']],['Other',['other']]];
const COLOR=Object.fromEntries(APPS.map(a=>[a[0],a[2]]));
const fmt=n=>n.toLocaleString('en-US');
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'})[c]);
const day=s=>new Date(s+'T00:00:00Z');
const dateLabel=(s,opts)=>day(s).toLocaleDateString('en-US',Object.assign({timeZone:'UTC'},opts));

function pie(sums,grand,small){
  // On phones the slice labels would be too small to read, so the pie is drawn bare and a list of apps goes under it.
  const w=small?470:680,h=470,r=small?225:195,cx=w/2,cy=h/2,share=n=>100*n/grand<0.5?'<1%':Math.round(100*n/grand)+'%';
  const ink=c=>{const v=[1,3,5].map(i=>parseInt(c.slice(i,i+2),16));return .299*v[0]+.587*v[1]+.114*v[2]>160?'#1d2b38':'#fff'};
  const parts=[],labels=[],outside=[];let angle=-Math.PI/2;
  for(const [key,label,color] of APPS){
    const n=sums[key];if(!n)continue;
    const frac=n/grand,mid=angle+Math.PI*frac,tip=`<title>${label}: ${fmt(n)} (${share(n)})</title>`;
    if(n===grand){parts.push(`<circle cx="${cx}" cy="${cy}" r="${r}" fill="${color}">${tip}</circle>`)}
    else{
      const end=angle+2*Math.PI*frac,big=end-angle>Math.PI?1:0;
      parts.push(`<path d="M${cx},${cy} L${(cx+r*Math.cos(angle)).toFixed(2)},${(cy+r*Math.sin(angle)).toFixed(2)} A${r},${r} 0 ${big} 1 ${(cx+r*Math.cos(end)).toFixed(2)},${(cy+r*Math.sin(end)).toFixed(2)} Z" fill="${color}" stroke="#fafcfd" stroke-width="2">${tip}</path>`);
      angle=end;
    }
    if(small)continue;
    if(frac>=0.1){ // roomy enough to write on the slice itself
      const rr=n===grand?0:r*0.6,tx=cx+rr*Math.cos(mid),ty=cy+rr*Math.sin(mid),fill=ink(color);
      const rows=[[label,15,600],[fmt(n),22,750],[share(n),15,600]];let y=ty-(rows.length-1)*10;
      for(const [t,size,weight] of rows){labels.push(`<text x="${tx.toFixed(1)}" y="${(y+size*.35).toFixed(1)}" text-anchor="middle" font-size="${size}" font-weight="${weight}" fill="${fill}">${esc(t)}</text>`);y+=20}
    }else outside.push([mid,label,n]); // thin slice: label just outside with a short line
  }
  for(const side of [1,-1]){ // right side, then left; push labels apart so they never overlap
    const group=outside.filter(o=>(Math.cos(o[0])>=0)===(side===1)).sort((a,b)=>Math.sin(a[0])-Math.sin(b[0]));let last=-1e9;
    for(const [mid,label,n] of group){
      const ex=cx+r*Math.cos(mid),ey=cy+r*Math.sin(mid),ly=Math.max(cy+(r+22)*Math.sin(mid),last+44),bx=cx+(r+22)*Math.cos(mid),lx=bx+side*18,anchor=side===1?'start':'end';last=ly;
      labels.push(`<polyline points="${ex.toFixed(1)},${ey.toFixed(1)} ${bx.toFixed(1)},${ly.toFixed(1)} ${(lx-side*4).toFixed(1)},${ly.toFixed(1)}" fill="none" stroke="#8a99a8" stroke-width="1"/>`);
      labels.push(`<text x="${lx.toFixed(1)}" y="${(ly-4).toFixed(1)}" text-anchor="${anchor}" font-size="14" font-weight="600" fill="#213647">${esc(label)}</text>`);
      labels.push(`<text x="${lx.toFixed(1)}" y="${(ly+14).toFixed(1)}" text-anchor="${anchor}" font-size="14" font-weight="500" fill="#617184">${fmt(n)} · ${share(n)}</text>`);
    }
  }
  const rows=FAMILIES.map(([name,keys])=>{const n=keys.reduce((s,k)=>s+sums[k],0);return `<li style="--u:${COLOR[keys[0]]}"><span>${name}</span><b>${fmt(n)}</b><small>${share(n)}</small></li>`}).join('');
  const apps=small?'<ul class="usage-apps">'+APPS.map(([key,label,color])=>`<li><i style="background:${color}"></i><span>${label}</span><b>${fmt(sums[key])}</b><small>${share(sums[key])}</small></li>`).join('')+'</ul>':'';
  return `<div class="usage-card usage-pie-wrap"><svg class="usage-pie" viewBox="0 0 ${w} ${h}" role="img" aria-label="Tool calls by app">${parts.join('')}${labels.join('')}</svg>${apps}<ul class="usage-family">${rows}<li class="usage-family-all"><span>All</span><b>${fmt(grand)}</b><small>100%</small></li></ul></div>`;
}

function bars(days,w){ // w: drawing width, matched to the screen so the text stays readable
  const h=220,padL=48,padB=50,padT=10,slot=(w-padL)/days.length,bar=(w-padL)/12*.5;
  const most=Math.max(1,...days.map(d=>APPS.reduce((s,a)=>s+d.counts[a[0]],0)));
  const step=Math.pow(10,Math.floor(Math.log10(most)))/2,top=Math.ceil(most/step)*step; // a round top line
  const parts=[`<svg viewBox="0 0 ${w} ${h}" role="img" aria-label="Tool calls per day">`];
  for(const frac of [0,.5,1]){
    const y=padT+(h-padT-padB)*(1-frac);
    parts.push(`<line x1="${padL}" x2="${w}" y1="${y.toFixed(1)}" y2="${y.toFixed(1)}" stroke="#e3eaf0"/><text x="${padL-8}" y="${(y+4).toFixed(1)}" text-anchor="end" font-size="11" fill="#617184">${fmt(Math.round(top*frac))}</text>`);
  }
  days.forEach((d,i)=>{
    const x0=padL+i*slot+(slot-bar)/2,tx=padL+i*slot+slot/2,name=dateLabel(d.date,{weekday:'short',month:'short',day:'numeric'});let y=h-padB;
    for(const [key,label,color] of APPS){
      const n=d.counts[key];if(!n)continue;const bh=(h-padT-padB)*n/top;y-=bh;
      parts.push(`<rect x="${x0.toFixed(1)}" y="${y.toFixed(1)}" width="${bar.toFixed(1)}" height="${bh.toFixed(1)}" rx="2" fill="${color}"><title>${name} · ${label}: ${fmt(n)}</title></rect>`);
    }
    parts.push(`<text x="${tx.toFixed(1)}" y="${h-30}" text-anchor="middle" font-size="11" fill="#33414f">${dateLabel(d.date,{month:'short',day:'numeric'})}</text><text x="${tx.toFixed(1)}" y="${h-15}" text-anchor="middle" font-size="10" fill="#8695a5">${dateLabel(d.date,{weekday:'short'})}</text>`);
  });
  parts.push('</svg>');
  const legend=APPS.map(([,label,color])=>`<span><i style="background:${color}"></i>${label}</span>`).join('');
  return `<div class="usage-card usage-bars">${parts.join('')}<div class="usage-legend">${legend}</div></div>`;
}

let last=null,width=0;
function render(data){
  last=data;
  const total=data.days.reduce((s,d)=>s+APPS.reduce((t,a)=>t+d.counts[a[0]],0),0);
  document.querySelectorAll('[data-usage-total]').forEach(el=>{el.textContent=fmt(total);const box=el.closest('[hidden]');if(box)box.hidden=false});
  const page=document.getElementById('usage-charts');if(!page)return;
  const sums=Object.fromEntries(APPS.map(([k])=>[k,data.days.reduce((s,d)=>s+d.counts[k],0)]));
  document.getElementById('usage-range').textContent=dateLabel(data.start,{month:'long',day:'numeric'})+' – '+dateLabel(data.end,{month:'long',day:'numeric'});
  document.getElementById('usage-headline').textContent=fmt(total)+' tool calls in the last 7 days';
  width=page.clientWidth;const inner=Math.max(300,width-50);
  page.innerHTML=`<section><h2>Tool calls by app</h2>${pie(sums,total,inner<560)}</section><section><h2>Tool calls per day</h2>${bars(data.days,Math.min(900,Math.max(330,inner)))}</section>`;
}
let timer;addEventListener('resize',()=>{clearTimeout(timer);timer=setTimeout(()=>{const page=document.getElementById('usage-charts');if(last&&page&&Math.abs(page.clientWidth-width)>40)render(last)},200)});

fetch('/data/usage.json',{cache:'no-cache'}).then(r=>{if(!r.ok)throw new Error(r.status);return r.json()}).then(render).catch(()=>{
  const page=document.getElementById('usage-charts');
  if(page)page.innerHTML='<p class="usage-error">The numbers didn’t load. Try again in a minute.</p>';
});
})();
