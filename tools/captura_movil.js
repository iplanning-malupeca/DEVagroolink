// Capturas a 390 px de los prototipos (producto, servicios, proyectos) para la página «013_Móvil».
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
if(P.indexOf('crear-producto')>-1){
  window.__demo('probiotico'); click('ir|especies'); click('espfoco|Porcino'); out.push(await snap('MP1','Especies'));
  click('ir|categoria'); out.push(await snap('MP2','Categoría'));
  click('ir|mercados'); click('madd|Europa'); out.push(await snap('MP3','Mercados'));
  click('ir|identidad'); type('#i-corta','Probiótico para lechones y pollos de engorde que mejora la salud intestinal.'); out.push(await snap('MP4','Identidad'));
  click('ir|tecnicos'); out.push(await snap('MP5','Técnicos'));
  click('ir|aplicaciones'); click('afase|Porcino › Lechones|Posdestete'); out.push(await snap('MP6','Aplicación por especie'));
  click('ir|documentos'); out.push(await snap('MP7','Fotos y documentos'));
  click('ir|certificaciones'); click('cadd|gmp_fsa'); out.push(await snap('MP8','Certificaciones'));
  click('ir|revision'); out.push(await snap('MP9','Revisión'));
  window.__cat(); out.push(await snap('ME1','Mis productos'));
  click('menu|demo1'); out.push(await snap('ME2','Menú de acciones'));
  document.body.click(); click('editar|demo1'); click('babrir|tecnicos'); type('[data-tv="proteina"]','17,5'); out.push(await snap('ME3','Editar por bloques'));
  click('baplicar'); click('bguardar'); out.push(await snap('ME4','Guardar y avisar'));
  click('cerrar'); click('babrir|traducciones'); out.push(await snap('ME5','Traducciones'));
  click('bcerrar'); click('publica'); click('fl|en'); out.push(await snap('ME6','Ficha en inglés')); click('cerrar');
  window.__demo('cero');
} else if(P.indexOf('crear-servicio')>-1){
  localStorage.removeItem('agroolink-servicios-experto-v1'); window.__t("S = nuevo(); LISTA = []; UI.vista = 'asistente'; render()");
  click('tipo|C11-01'); out.push(await snap('MS1','Tipo'));
  click('seguir'); click('esp|Avicultura'); click('prod|Avicultura|Pollos de engorde'); out.push(await snap('MS2','Especies'));
  click('seguir'); click('rama|Granja'); click('cargo|Granjero'); out.push(await snap('MS3','Dirigido a'));
  click('seguir'); type('[data-zq="pz"]','Catal'); click('pza|España › Cataluña'); const c=q('[data-sw="dist"]'); c.checked=true; c.dispatchEvent(new Event('change',{bubbles:true})); out.push(await snap('MS4','Dónde'));
  click('seguir'); type('[data-f="nombre"]','Auditoría nutricional de broilers'); type('[data-f="desc"]','Visita a granja, revisión de pienso y consumos, e informe por fase.'); out.push(await snap('MS5','Detalles'));
  click('seguir'); click('seguir'); out.push(await snap('MS6','Revisión'));
  click('publicar'); window.__t("UI.menu = LISTA[0].id; render()"); out.push(await snap('MS7','Mis servicios'));
  window.__t("const c = JSON.parse(JSON.stringify(LISTA[0])); c.id='s2'; c.nombre='Diagnóstico de coccidiosis'; c.estado='Pausado'; LISTA.push(c); UI.menu = null; render()"); click('editar|'+window.__t('LISTA[0].id')); click('edbloque|especies'); click('esp|Porcino'); click('edvolver'); out.push(await snap('MS8','Editar servicio'));
  click('edguardar'); out.push(await snap('MS9','¿Avisar?'));
  click('edconfirmar'); window.__t("LISTA[1].archivado = true; UI.vista = 'archivados'; render()"); out.push(await snap('MS10','Archivados'));
  window.__t("localStorage.removeItem('agroolink-servicios-experto-v1'); S = nuevo(); LISTA = []; UI.vista='asistente'; UI.menu=null; render()");
} else {
  localStorage.clear(); location.hash=''; 
  out.push(await snap('MJ1','Bienvenida'));
  q('#start').click(); out.push(await snap('MJ2','Primera pregunta'));
  q('#exitBtn').click(); await wait(200); q('#example').click(); out.push(await snap('MJ3','Resumen'));
  document.querySelector('[data-edit]').click(); out.push(await snap('MJ4','Editar desde el resumen'));
  localStorage.clear();
}
return out.join(' ');
