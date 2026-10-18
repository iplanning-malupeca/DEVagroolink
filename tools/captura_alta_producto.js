const wait=ms=>new Promise(r=>setTimeout(r,ms)); await wait(500);
const click=a=>{const b=document.querySelector(`[data-act="${a}"]`); if(!b) throw new Error('no '+a); b.click();};
const demo=v=>window.__demo(v);
const type=(sel,val)=>{const e=document.querySelector(sel); e.value=val; e.dispatchEvent(new Event('input',{bubbles:true})); e.dispatchEvent(new Event('change',{bubbles:true}));};
const css=document.querySelector('style').textContent;
async function snap(name,title,conLayer){ await wait(150); document.querySelectorAll('.toast').forEach(t=>t.remove()); scrollTo(0,0);
  const h=Math.max(900, Math.ceil(document.documentElement.scrollHeight/10)*10);
  const body=document.querySelector('header.top').outerHTML+document.querySelector('.wrap').outerHTML+(conLayer?document.getElementById('layer').innerHTML:'');
  await fetch('/save?name='+name,{method:'POST',body:JSON.stringify({title,h,css,body})}); return name+':'+h; }
async function img(name,color,w,h){ const c=document.createElement('canvas'); c.width=w; c.height=h; const g=c.getContext('2d'); g.fillStyle=color; g.fillRect(0,0,w,h); g.fillStyle='rgba(255,255,255,.85)'; g.font='600 90px sans-serif'; g.fillText(name,70,h/2+30); return new File([await new Promise(r=>c.toBlob(r,'image/jpeg',.8))], name.replace(/ /g,'_')+'.jpg', {type:'image/jpeg'}); }
async function fotos(){ const dt=new DataTransfer(); dt.items.add(await img('Foto 1','#3E6C8F',1600,1200)); dt.items.add(await img('Foto 2','#5C7F5A',1600,1200)); dt.items.add(await img('Foto 3','#7C6A4A',1600,1200)); const inp=document.getElementById('inFotos'); inp.files=dt.files; inp.dispatchEvent(new Event('change',{bubbles:true})); await wait(900); }
const out=[];
demo('probiotico'); click('ir|documentos'); await fotos(); click('ir|especies'); click('espfoco|Porcino'); out.push(await snap('E1','Especies'));
click('ir|categoria'); out.push(await snap('G1','Categoría'));
click('ir|mercados'); click('madd|Europa'); out.push(await snap('G2','Mercados'));
click('ir|identidad'); out.push(await snap('G3','Identidad'));
click('ir|tecnicos'); out.push(await snap('G4','Técnicos'));
click('ir|aplicaciones'); click('afase|Porcino › Lechones|Posdestete'); click('afase|Avicultura › Pollos de engorde|Inicio'); out.push(await snap('GA','Aplicaciones'));
click('ir|enfermedad'); out.push(await snap('G5','Enfermedad'));
click('ir|variantes'); out.push(await snap('G6','Variantes'));
click('ir|documentos'); const u=document.getElementById('vurl'); u.value='https://www.youtube.com/watch?v=ejemplo'; u.dispatchEvent(new Event('input',{bubbles:true})); click('vlink'); type('[data-vt="0"]','Cómo se aplica (ejemplo)'); click('vcap|0'); type('[data-vcm="0|0"]','00:00'); type('[data-vct="0|0"]','Presentación'); click('ir|documentos'); out.push(await snap('G7','Documentos'));
click('ir|certificaciones'); click('cadd|gmp_fsa'); click('cdoc|0'); type('[data-cf="0|entidad"]','Entidad certificadora (ejemplo)'); type('[data-cf="0|hasta"]','2027-12-31'); click('cadd|eco_apto_alimentacion'); click('ir|certificaciones'); out.push(await snap('GC','Certificaciones'));
click('ir|revision'); out.push(await snap('G8','Revisión'));
demo('ordeno'); out.push(await snap('H1','Ordeño'));
demo('vacuna'); out.push(await snap('H2','Vacuna enfermedad'));
click('ir|aplicaciones'); out.push(await snap('H3','Vacuna aplicación'));
demo('pienso'); out.push(await snap('H4','Pienso'));
demo('molino'); click('ir|especies'); out.push(await snap('H5','Sin especie'));
click('ir|tecnicos'); out.push(await snap('H6','Molino'));
demo('ordeno'); click('ir|categoria'); click('fam|C02'); out.push(await snap('H7','No aplica'));
demo('probiotico'); click('ir|mercados'); click('madd|Todo el mundo'); click('mit|0|Asia-Pacífico'); click('mit|0|África'); click('mit|0|Rusia'); out.push(await snap('H8','Mercados excluir'));
demo('cero'); click('ir|categoria'); click('fam|C06'); click('cat|C06-01-OTRO'); type('#catotro','Bacteriófagos'); click('ir|categoria'); click('fam|C06'); out.push(await snap('H9','Otro'));
demo('probiotico'); click('ir|tecnicos'); type('[data-t="cepa"]','Cepa de ejemplo'); type('[data-t="viabilidad"]','Según ficha técnica'); click('ir|categoria'); click('cat|C06-01-04'); click('ir|tecnicos'); out.push(await snap('H10','Ocultos'));
demo('pienso'); click('ir|documentos'); await fotos(); click('ir|certificaciones'); click('cadd|gmp_fsa'); click('cdoc|0'); type('[data-cf="0|hasta"]','2027-12-31'); click('ir|revision'); click('publica'); out.push(await snap('H11','Ficha pública',true)); click('cerrar');
click('comparar'); out.push(await snap('H12','Comparador',true)); click('cerrar');
demo('cero');
out.join(' ')