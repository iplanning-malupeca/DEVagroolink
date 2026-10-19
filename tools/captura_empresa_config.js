// Capturas a 390 px de los prototipos (alta de empresa) para la página «013_Móvil».
const wait=ms=>new Promise(r=>setTimeout(r,ms)); await wait(500);
const q=s=>{const e=document.querySelector(s); if(!e) throw new Error('no '+s); return e;};
const click=a=>q(`[data-act="${a}"]`).click();
const type=(sel,val)=>{const e=q(sel); e.value=val; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));};
async function snap(name,title){ await wait(200); document.querySelectorAll('.toast').forEach(t=>t.remove()); scrollTo(0,0);
  const css=[...document.querySelectorAll('style')].map(s=>s.textContent).join('\n');
  const c=document.body.cloneNode(true); c.querySelectorAll('script,template').forEach(x=>x.remove());
  const h=Math.max(844, Math.ceil(document.documentElement.scrollHeight/10)*10);
  await fetch('/save?name='+name,{method:'POST',body:JSON.stringify({title,h,css,body:c.innerHTML,w:390})}); return name+':'+h; }
const out=[]; const P=location.pathname;
const reset=()=>window.__t("S = nuevo(); UI.desdeRev = false; render()");
const codigo=()=>{ for(let i=0;i<6;i++) type(`[data-cd="${i}"]`, String((i*3+1)%10)); };
// Una captura por configuración: tipo de empresa, red (quién vende) y contacto (a quién llega la solicitud).
const paso=p=>window.__t("S.paso = '"+p+"'; render()");
for (const [id,q,pre] of [['dsm','dsm','CD'],['bd','big dutchman','CS'],['newfarms','newfarms','CX']]) {
  reset(); type('[data-f="q"]',q); click('crm|'+id); click('seguir'); codigo();
  paso('tipo'); out.push(await snap(pre+'1','Tipo de empresa'));
  paso('red'); out.push(await snap(pre+'2','Red'));
  paso('contacto'); out.push(await snap(pre+'3','Contacto'));
}
reset(); type('[data-f="q"]','dsm'); click('crm|dsm'); click('seguir'); codigo();
window.__t("S.espModo.Avicultura = 'excluir'; S.esp.Avicultura = ['Codornices']; S.paso = 'especies'; render()"); out.push(await snap('CD4','Especies · Excluir'));
reset();
return out.join(' ');
