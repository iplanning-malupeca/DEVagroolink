const wait=ms=>new Promise(r=>setTimeout(r,ms)); await wait(400);
const css=document.querySelector('style').textContent;
const reset=()=>{Object.assign(__F,{q:'',esp:{},cat:[],enf:[],pais:[],marca:[],verif:false,tec:{}}); Object.assign(__UI,{abierto:null,tab:'productos',orden:'rel',capa:null,foco:{},paso:null}); document.body.classList.remove('cap');};
async function snap(name,title,capa){ __render(); await wait(150); scrollTo(0,0);
  if(capa) document.body.classList.add('cap');
  const main=document.getElementById('main'), layer=document.getElementById('layer');
  const nav=document.querySelector('nav.tabbar'); const body=document.querySelector('header.top').outerHTML+(capa?'<div id="layer">'+layer.innerHTML+'</div>':main.outerHTML+(innerWidth<900?nav.outerHTML.replace('class="tabbar"','class="tabbar" style="position:absolute;top:'+(Math.max(844,Math.ceil(document.documentElement.scrollHeight/10)*10)-84)+'px;bottom:auto"'):'')+layer.innerHTML);
  if(capa) main.style.display='none';
  const h=Math.max(innerWidth<900?844:860, Math.ceil(document.documentElement.scrollHeight/10)*10);
  main.style.display=''; document.body.classList.remove('cap');
  await fetch('/save?name='+name,{method:'POST',body:JSON.stringify({title,h,css,body,w:innerWidth})}); return name+':'+h; }
const out=[]; const M=innerWidth<900;
reset(); __UI.vista='home';
if(!M){ __UI.sesion=false; out.push(await snap('S0','Home · sin sesión')); __UI.sesion=true; __UI.abierto='q'; out.push(await snap('S0b','Home · primera búsqueda')); }
else { __UI.sesion=false; out.push(await snap('T0','Home móvil · sin sesión')); __UI.sesion=true; __UI.capa='hoja'; __UI.paso='q'; out.push(await snap('T0b','Home móvil · búsqueda',true)); }
reset(); __UI.vista='resultados'; __render();
return out.join(' ');
