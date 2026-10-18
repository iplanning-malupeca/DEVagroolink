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
if(!M){
  reset(); __F.q='micotoxinas'; out.push(await snap('S1','Resultados'));
  reset(); __F.q='micot'; __UI.abierto='q'; out.push(await snap('S2','Autocompletado'));
  reset(); __F.esp={Porcino:['Lechones']}; __UI.abierto='esp'; out.push(await snap('S3','Especie'));
  reset(); __F.esp={Porcino:['Lechones']}; __UI.abierto='cat'; __UI.foco={f1:'C06',f2:'C06-02'}; out.push(await snap('S4','Categoría'));
  reset(); __F.esp={Porcino:['Lechones'],Avicultura:['Pollos de engorde']}; __UI.abierto='enf'; out.push(await snap('S5','Enfermedad'));
  reset(); __F.esp={Porcino:['Lechones'],Avicultura:['Pollos de engorde']}; __F.cat=['C08','C06-02-01']; __F.enf=['Colibacilosis','Coccidiosis']; out.push(await snap('S6','Varios filtros'));
  reset(); __F.esp={Porcino:[]}; __F.cat=['C06-02-01']; __F.tec={toxinas:['DON']}; out.push(await snap('S7','Con categoría: filtros técnicos'));
  reset(); __F.esp={Porcino:[]}; __F.cat=['C06-02-01']; __F.tec={toxinas:['DON']}; __UI.capa='filtros'; __UI.foco={f1:'C06',f2:'C06-02'}; out.push(await snap('S8','Filtros',true));
  reset(); __F.esp={Bovino:['Vacuno de leche']}; __F.cat=['C08']; __F.enf=['Colibacilosis']; out.push(await snap('S9','Sin resultados'));
} else {
  reset(); __F.q='micotoxinas'; __F.esp={Porcino:['Lechones']}; out.push(await snap('T1','Móvil resultados'));
  reset(); __F.esp={Porcino:['Lechones']}; __UI.capa='hoja'; __UI.paso='esp'; out.push(await snap('T2','Móvil buscar especie',true));
  reset(); __F.esp={Porcino:['Lechones']}; __UI.capa='hoja'; __UI.paso='cat'; __UI.foco={f1:'C06',f2:'C06-02'}; out.push(await snap('T3','Móvil buscar categoría',true));
  reset(); __F.esp={Porcino:[]}; __F.cat=['C06-02-01']; __F.tec={toxinas:['DON']}; __UI.capa='filtros'; __UI.foco={f1:'C06',f2:'C06-02'}; out.push(await snap('T4','Móvil filtros',true));
}
reset(); __render();
return out.join(' ');
