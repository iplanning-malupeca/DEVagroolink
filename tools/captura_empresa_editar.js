// Capturas de «Editar ficha de empresa» (escritorio 1280 → EE*, móvil 390 → EEM*) para 004b_LP/MB_Intranet · Empresa.
const wait=ms=>new Promise(r=>setTimeout(r,ms)); await wait(500);
const q=s=>{const e=document.querySelector(s); if(!e) throw new Error('no '+s); return e;};
const click=a=>q(`[data-act="${a}"]`).click();
const type=(sel,val)=>{const e=q(sel); e.value=val; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));};
const M=innerWidth<900, W=M?390:1280, pre=M?'EEM':'EE';
async function snap(name,title){ await wait(200); document.querySelectorAll('.toast').forEach(t=>t.remove()); scrollTo(0,0);
  const css=[...document.querySelectorAll('style')].map(s=>s.textContent).join('\n');
  const c=document.body.cloneNode(true); c.querySelectorAll('script,template').forEach(x=>x.remove());
  const h=Math.max(M?844:860, Math.ceil(document.documentElement.scrollHeight/10)*10);
  await fetch('/save?name='+name,{method:'POST',body:JSON.stringify({title,h,css,body:c.innerHTML,w:W})}); return name+':'+h; }
const out=[];
window.__t("S = nuevo(); UI.desdeRev = false; UI.vista = 'alta'; UI.edit = false; ORIG = null; render()");
type('[data-f="q"]','zucami'); click('crm|zucami'); click('seguir'); for(let i=0;i<6;i++) type(`[data-cd="${i}"]`, String((i*3+1)%10));
for(let n=0;n<12 && !document.querySelector('[data-act="publicar"]');n++) click('seguir');
window.__t("S.sobre = 'Diseñamos y fabricamos jaulas y equipos para gallinas ponedoras y reproductoras desde Valladolid.'; render()");
click('publicar'); click('editarficha'); click('edbloque|mercados'); type('[data-q="mq"]','Ital'); click('merc|Italia'); out.push(await snap(pre+'2','Cambiar un bloque'));
click('edvolver'); click('edbloque|cabecera'); click('obj|Bienestar animal'); click('edvolver'); out.push(await snap(pre+'1','Editar ficha de empresa'));
click('edguardar'); out.push(await snap(pre+'3','Antes de guardar'));
click('edconfirmar'); window.__t("UI.vista = 'alta'; S = nuevo(); ORIG = null; render()");
return out.join(' ');
