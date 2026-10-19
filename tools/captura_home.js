const wait=ms=>new Promise(r=>setTimeout(r,ms)); await wait(400);
async function snap(name,title,w){ await wait(250); scrollTo(0,0);
  const css=[...document.querySelectorAll('style')].map(s=>s.textContent).join('\n');
  const c=document.body.cloneNode(true); c.querySelectorAll('script,template').forEach(x=>x.remove());
  const h=Math.max(w<900?844:860, Math.ceil(document.documentElement.scrollHeight/10)*10);
  await fetch('/save?name='+name,{method:'POST',body:JSON.stringify({title,h,css,body:c.innerHTML,w})}); return name+':'+h; }
const W=innerWidth<900?390:1280, out=[];
__UI.vista='home'; __UI.abierto=null; __UI.capa=null; __render();
if(W===1280){ out.push(await snap('S0','Home',W)); __UI.abierto='q'; __render(); out.push(await snap('S0b','Home · primera búsqueda',W)); }
else { out.push(await snap('T0','Home móvil',W)); }
__UI.vista='resultados'; __UI.abierto=null; __render();
return out.join(' ');
