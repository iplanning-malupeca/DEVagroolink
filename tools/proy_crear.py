"""J1 · Crear proyecto: formulario completo (qué necesitas, animales y lugar, detalles)."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
H = 1920
s = open(P + 'ProyCrear.dc.html').read()
EXTRA = ('.sec{display:flex;align-items:center;gap:10px;margin:4px 0 -2px}.num{width:26px;height:26px;border-radius:50%;background:#0E5A3A;color:#FFFFFF;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none}'
         '.st2{font-size:16px;font-weight:600}.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}.g3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}'
         '.req{color:#C2410C}.drop{border:1.5px dashed #B9CBBF;border-radius:12px;background:#FBFCFB;padding:14px;display:flex;align-items:center;gap:12px;font-size:12.5px;color:#4A5650}'
         '.file{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 10px;border-radius:8px;background:#F2F5F3;font-size:12px}'
         '.sub{display:inline-flex;align-items:center;gap:4px;height:24px;padding:0 9px;border-radius:999px;font-size:11.5px;border:1px solid #C9E3C3;background:#DDF0D8;color:#0E5A3A;white-space:nowrap}'
         '.ck{display:flex;align-items:flex-start;gap:8px;font-size:12.5px;padding:8px 10px;border:1px solid #E3E8E4;border-radius:10px;background:#FFFFFF}.ck input{accent-color:#0E5A3A;margin:2px 0 0}'
         '.idx{display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:10px;font-size:12.5px}.idx .n{width:24px;height:24px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font-size:11px;font-weight:600;box-sizing:border-box}')
s = s.replace('</style>', EXTRA + '\n</style>', 1)

def opt(t, d, sel=False):
    return '<label class="opt%s"><input type="radio" name="tipo"%s><span><strong style="font-size: 13px; font-weight: 600;">%s</strong><br><span style="color: #4A5650;">%s</span></span></label>' % (' sel' if sel else '', ' defaultChecked="{{ yes }}"' if sel else '', t, d)
def ck(t, d='', on=False):
    return '<label class="ck"><input type="checkbox"%s><span><strong style="font-weight: 500;">%s</strong>%s</span></label>' % (' defaultChecked="{{ yes }}"' if on else '', t, ('<br><span class="hint">%s</span>' % d) if d else '')
def sec(n, t, d):
    return '<div class="sec"><span class="num">%d</span><span class="st2">%s</span><span class="hint">%s</span></div>' % (n, t, d)
def chip(t, on=False): return '<span class="%s">%s%s</span>' % ('on' if on else 'off', '✓ ' if on else '', t)
CLIP = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#0E5A3A" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="M21 11.5 12.5 20a5 5 0 0 1-7-7L14 4.5a3.5 3.5 0 0 1 5 5L10.5 18a2 2 0 0 1-3-3L15 7.5"/></svg>'
PIN = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>'

form = ('<form style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 12px;">'
 + sec(1, 'Qué necesitas', '· lo que buscas, en tus palabras') +
 '<section class="card" style="gap: 10px;"><p class="h">Tipo de necesidad</p><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">'
 + opt('Productos o equipos', 'Comprar o renovar', True) + opt('Un servicio', 'Asesoría, análisis, formación…') + opt('Un proyecto completo', 'Nave nueva o reforma llave en mano') + opt('No lo sé', 'Te ayuda un experto a definirlo') + '</div></section>'
 '<section class="card" style="gap: 10px;">'
 '<label class="lbl"><span>Título <span class="req">*</span> <span class="hint">· máx. 90</span></span><input class="inp" type="text" value="Sistema de alimentación para nave nueva de broilers"></label>'
 '<div class="g2"><label class="lbl"><span>Categoría principal <span class="req">*</span></span><select class="inp"><option>Equipamiento › Sistemas de alimentación automática</option></select></label>'
 '<label class="lbl">Situación<select class="inp"><option>Obra nueva</option><option>Ampliación</option><option>Reforma</option><option>Reposición</option></select></label></div>'
 '<div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;"><span class="hint">Añadir al mismo proyecto:</span>' + chip('Silos y almacenamiento', True) + chip('Bebederos') + chip('Básculas y pesaje') + chip('Montaje') + '</div>'
 '<label class="lbl"><span>Descripción <span class="req">*</span> <span class="hint">· qué quieres conseguir y qué tienes ahora</span></span><textarea class="ta" rows="4">Construimos una segunda nave de 40.000 broilers en Lleida. Buscamos un sistema de alimentación completo (2 silos de 20 t, transporte y 4 líneas de comederos) con montaje y buen servicio técnico en la zona. La nave 1 tiene comederos de otra marca y nos gustaría unificar.</textarea></label>'
 '<div class="lbl">Objetivos <span class="hint" style="margin-top: -3px;">De tus intereses · ayudan a que encajen mejor las propuestas</span><div style="display: flex; gap: 6px; flex-wrap: wrap;">' + chip('Conversión alimenticia', True) + chip('Reducción de costes', True) + chip('Bienestar animal') + chip('Eficiencia operativa') + chip('Sostenibilidad') + '</div></div>'
 '</section>'
 + sec(2, 'Para qué animales y dónde', '· para que te propongan lo adecuado') +
 '<section class="card" style="gap: 10px;">'
 '<div class="lbl"><span>Especie y producción <span class="req">*</span></span><div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;">' + chip('Avicultura', True) + '<span class="sub">✓ Pollos de engorde</span><span class="sub">✓ Broilers</span>' + chip('Porcino') + chip('Bovino') + chip('Otras…') + '</div></div>'
 '<div class="g3"><label class="lbl">Nº de animales<input class="inp" type="text" value="40.000 aves"></label><label class="lbl">Naves o instalaciones<input class="inp" type="text" value="1 nave · 2.200 m²"></label><label class="lbl">Ciclos al año<input class="inp" type="text" value="6"></label></div>'
 '<div class="g2"><label class="lbl"><span>Ubicación <span class="req">*</span></span><div class="inp" style="display: flex; align-items: center; gap: 6px;">' + PIN + 'Alcarràs · Lleida · España</div><span class="hint">Las empresas ven solo provincia y comarca.</span></label>'
 '<label class="lbl">Instalaciones actuales<select class="inp"><option>Tengo otra nave en marcha</option><option>Es la primera</option></select></label></div>'
 '</section>'
 + sec(3, 'Detalles', '· plazos, presupuesto y lo que debe incluir') +
 '<section class="card" style="gap: 10px;">'
 '<div class="g3"><label class="lbl">Presupuesto orientativo<select class="inp"><option>60.000 – 90.000 €</option><option>A consultar</option></select></label>'
 '<label class="lbl"><span>Recibir propuestas hasta <span class="req">*</span></span><input class="inp" type="text" value="14 nov 2026"></label>'
 '<label class="lbl">Quiero tenerlo<input class="inp" type="text" value="Antes de marzo de 2027"></label></div>'
 '<div class="lbl">La propuesta debe incluir<div class="g3" style="margin-top: 2px;">' + ck('Suministro', '', True) + ck('Montaje e instalación', '', True) + ck('Puesta en marcha', '', True) + ck('Mantenimiento', 'Contrato anual') + ck('Financiación o renting') + ck('Formación al personal') + '</div></div>'
 '<div class="g2"><label class="lbl">Requisitos<textarea class="ta" rows="2">Servicio técnico a menos de 100 km. Compatible con el control de la nave 1.</textarea></label>'
 '<label class="lbl">Marcas<input class="inp" type="text" placeholder="Preferidas o a evitar (opcional)"><span class="hint">Si no pones nada, abierto a todas.</span></label></div>'
 '<div class="lbl">Documentos <span class="hint" style="margin-top: -3px;">Planos, fotos, pliego… · PDF, JPG, DWG hasta 20 MB</span>'
 '<div class="drop">' + CLIP + '<span style="flex: 1;">Arrastra aquí o <a href="#">elige archivos</a></span><span class="file">📄 Plano_nave2.pdf · 2,1 MB ×</span><span class="file">🖼 Parcela.jpg ×</span></div></div>'
 '<div class="g2"><label class="lbl">Cómo quieres recibir las propuestas<select class="inp"><option>En Agroolink (Mensajes) y aviso por email</option></select></label>'
 '<label class="lbl">¿Visita a la granja?<select class="inp"><option>Sí, con cita previa</option><option>No es necesaria</option></select></label></div>'
 '</section></form>')

def step(n, label, st):
    sty = {'on': ('background: #EEF6EE; color: #0E5A3A; font-weight: 600;', 'border: 2px solid #0E5A3A;'), 'here': ('color: #17231D;', 'border: 1.5px solid #0E5A3A; color: #0E5A3A;'), 'next': ('color: #56615B;', 'border: 1.5px solid #CFD8D2; color: #8A948F;')}[st]
    return '<div class="idx" style="%s"><span class="n" style="%s">%d</span>%s</div>' % (sty[0], sty[1], n, label)
idx = ('<div style="display: flex; align-items: center; gap: 4px; background: #FFFFFF; border: 1px solid #E6EBE7; border-radius: 14px; padding: 6px;">'
 + step(1, 'Qué necesitas', 'on') + step(2, 'Animales y dónde', 'here') + step(3, 'Detalles', 'here')
 + '<span style="width: 1px; height: 24px; background: #E3E8E4; margin: 0 6px;"></span>' + step(4, 'A quién se lo enviamos', 'next') + step(5, 'Revisar y publicar', 'next')
 + '<span style="margin-left: auto; display: flex; align-items: center; gap: 8px; padding-right: 8px;" class="hint">Obligatorios 7/7<span style="width: 70px; height: 6px; border-radius: 3px; background: #E3E8E4; overflow: hidden; display: inline-block;"><span style="display: block; width: 80%; height: 100%; background: #0E5A3A;"></span></span></span>'
 '</div>')

aside = ('<aside style="width: 290px; flex: none; display: flex; flex-direction: column; gap: 12px;">'
 '<section class="card" style="gap: 8px; background: #F2F7F3; border-color: #DCE9DF;"><span style="display: flex; align-items: center; gap: 8px; color: #0E5A3A;"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg><strong style="font-size: 13.5px; color: #17231D;">Ya encajan</strong></span>'
 '<strong style="font-size: 30px; font-weight: 700; color: #0E5A3A; line-height: 1;">23 <span style="font-size: 13px; font-weight: 500; color: #2F3D36;">empresas</span> · <span style="color: #4B3BA6;">4</span> <span style="font-size: 13px; font-weight: 500; color: #2F3D36;">expertos</span></strong>'
 '<span style="font-size: 12px; color: #4A5650; line-height: 1.45;">con sistemas de alimentación para broilers y servicio en Lleida.</span></section>'
 '<section class="card" style="gap: 8px;"><p class="h" style="font-size: 13.5px;">Así lo verán</p>'
 '<div style="border: 1px solid #E6EBE7; border-radius: 12px; padding: 10px 12px; display: flex; flex-direction: column; gap: 5px; font-size: 12px;"><strong style="font-size: 13px;">Sistema de alimentación para nave nueva de broilers</strong><span class="hint">Granja de broilers · Lleida · 40.000 aves</span><span style="display: flex; gap: 5px; flex-wrap: wrap;"><span class="st ok">Obra nueva</span><span class="st dr">60–90 k€</span><span class="st wn">Hasta 14 nov</span></span><span class="hint">Incluye: suministro, montaje, puesta en marcha</span></div>'
 '<span class="hint">Tu nombre y contacto no aparecen hasta que respondes a una propuesta.</span></section>'
 '<section class="card" style="gap: 6px;"><p class="h" style="font-size: 13.5px;">Consejos</p><ul style="margin: 0; padding-left: 18px; font-size: 12px; color: #2F3D36; line-height: 1.55;"><li>Con tamaño, plazo y presupuesto recibes propuestas comparables.</li><li>Un plano o una foto evita muchas preguntas.</li><li>Puedes guardar el borrador y seguir luego.</li></ul></section>'
 '</aside>')

i = s.index('    <div style="display: flex; gap: 20px; flex: 1; min-height: 0;">'); j = s.index('    <div style="display: flex; justify-content: flex-end; gap: 10px;">')
body = '    ' + idx + '\n    <div style="display: flex; gap: 20px; flex: 1; min-height: 0; align-items: flex-start;">\n      ' + form + '\n      ' + aside + '\n    </div>\n'
s = s[:i] + body + s[j:]
s = s.replace('<button type="button" class="btnp" style="height: 42px;">Siguiente →</button>', '<button type="button" class="btnp" style="height: 42px;">Siguiente: a quién se lo enviamos →</button>', 1)
s = s.replace('Lo enviamos a empresas y expertos que encajan. Gratis y sin compromiso.', 'Cuanto más concreto, mejores propuestas. Lo enviamos a empresas y expertos que encajan; gratis y sin compromiso.', 1)
s = s.replace('<div style="width: 1280px; height: 900px; position: relative;', '<div style="width: 1280px; height: %dpx; position: relative;' % H, 1)
s = s.replace('alto="832" hint-size="256px,832px"', 'alto="%d" hint-size="256px,%dpx"' % (H - 68, H - 68), 1)
s = s.replace('"$preview":{"width":1280,"height":900}', '"$preview":{"width":1280,"height":%d}' % H)
open(P + 'ProyCrear.dc.html', 'w').write(s)

c = json.load(open(P + 'canvas.json')); B = c['boards']
B['ProyCrear.dc.html'].update(h=H, title='J1 · Crear proyecto · formulario completo (qué, animales y dónde, detalles)')
for k in ['ProyOportunidades.dc.html', 'ProyPropuesta.dc.html', 'ProyExperto.dc.html']:
    B[k]['y'] = H + 500
c['notes']['proyT2']['y'] = H + 200
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
