"""Nueva comparación: buscar producto escribiendo unas letras (C0) + pop-ups C0a y C0b."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
SRCH = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5"/></svg>'
X = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
CHK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>'

# 1) bloque «Nueva comparación» con buscador
OLD = re.compile(r'<section class="card" style="border: 1.5px dashed #CFD8D2; background: #FBFCFB; align-items: center; justify-content: center; text-align: center; gap: 8px;">.*?</section>', re.S)
NEW = ('<section class="card" style="border: 1.5px dashed #CFD8D2; background: #FBFCFB; justify-content: center; gap: 10px;">'
       '<strong style="font-size: 15px; font-weight: 600;">Nueva comparación</strong>'
       '<span class="k" style="line-height: 1.5;">Escribe unas letras del producto y elige. Después te proponemos otros del mismo tipo.</span>'
       '<div class="inp" style="justify-content: flex-start; gap: 8px; color: #8A948F;">' + SRCH + 'Nombre del producto, p. ej. «ronoz»</div>'
       '<span class="k">También desde cualquier ficha, con «Comparar».</span></section>')
for f in ['UsrComparaciones.dc.html', 'CompSumario.dc.html']:
    s = open(P + f).read()
    if 'Nombre del producto, p. ej.' not in s:
        s, n = OLD.subn(NEW, s, count=1); assert n == 1, f
        open(P + f, 'w').write(s)
t = open(W + '/tools/intranet.py').read()
if 'Nombre del producto, p. ej.' not in t:
    i = t.index('+ """<section class="card" style="border: 1.5px dashed #CFD8D2; background: #FBFCFB; align-items: center;')
    j = t.index('</section>', i) + len('</section>')
    t = t[:i] + '+ """' + NEW.replace(SRCH, '""" + ic(\'search\', 16) + """') + t[j:]
    open(W + '/tools/intranet.py', 'w').write(t)

base = open(P + 'CompSumario.dc.html').read()
EXTRA = ('.pop{position:absolute;inset:0;background:rgba(15,30,22,.45);display:flex;align-items:flex-start;justify-content:center;padding-top:96px;z-index:5}'
         '.dlg{width:640px;background:#FFFFFF;border-radius:20px;box-shadow:0 24px 60px rgba(16,40,28,.25);padding:20px 22px;display:flex;flex-direction:column;gap:14px;box-sizing:border-box}'
         '.res{display:flex;align-items:center;gap:12px;padding:9px 10px;border-radius:12px}.res.hl{background:#F2F7F3}'
         '.pim{width:40px;height:40px;border-radius:10px;flex:none}.mk{background:#FFF1A8;border-radius:3px;padding:0 1px}'
         '.cap2{font-size:11px;font-weight:600;letter-spacing:.06em;color:#56615B}.dis{opacity:.45}')
def popup(fn, title, dlg):
    s = base.replace('<title>Comparador · Mis comparaciones (sumario)</title>', '<title>%s</title>' % title, 1)
    s = s.replace('</style>', EXTRA + '\n</style>', 1)
    k = s.rindex('</div>\n</x-dc>')
    s = s[:k] + '  <div class="pop">' + dlg + '</div>\n' + s[k:]
    open(P + fn, 'w').write(s)
def res(col, name, by, tipo, hl=False, extra='', dis=False):
    return ('<div class="res%s%s"><span class="pim" style="background: %s;"></span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column;"><span style="font-size: 13.5px; font-weight: 600;">%s</span><span class="k">%s · %s</span></span>%s</div>') % (
        ' hl' if hl else '', ' dis' if dis else '', col, name, by, tipo, extra)
head = lambda t, s: ('<div style="display: flex; align-items: flex-start; gap: 12px;"><div style="flex: 1; display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 19px; font-weight: 600;">%s</strong><span class="k" style="font-size: 12.5px;">%s</span></div><span style="color: #56615B; display: flex; padding-top: 4px;">%s</span></div>') % (t, s, X)

# C0a · escribir unas letras
d1 = (head('Nueva comparación', 'Busca el primer producto: con 3 letras ya te proponemos.') +
      '<div class="inp" style="border: 1.5px solid #0E5A3A; gap: 8px; justify-content: flex-start; color: #17231D;">' + SRCH + 'ronoz<span style="display: inline-block; width: 1.5px; height: 18px; background: #0E5A3A;"></span><span style="margin-left: auto;" class="k">4 resultados</span></div>'
      '<span class="cap2">PRODUCTOS</span>'
      + res('#E6F0FA', '<span class="mk">Ronoz</span>yme® HiPhos', 'DSM-Firmenich', 'Enzimas · fitasa', True, '<span class="k">↵ Elegir</span>')
      + res('#FFF4DE', '<span class="mk">Ronoz</span>yme® ProAct', 'DSM-Firmenich', 'Enzimas · proteasa')
      + res('#EEF2E6', '<span class="mk">Ronoz</span>yme® MultiGrain', 'DSM-Firmenich', 'Enzimas · carbohidrasas')
      + res('#F3EEE6', '<span class="mk">Ronoz</span>yme® WX', 'DSM-Firmenich', 'Enzimas · xilanasa') +
      '<div style="border-top: 1px solid #EEF1EE; padding-top: 10px; display: flex; flex-direction: column; gap: 6px;"><span class="cap2">VISTOS HACE POCO</span>'
      '<div style="display: flex; flex-wrap: wrap; gap: 6px;"><span class="chip">Sensor NH₃ / CO₂ · AgroNova</span><span class="chip">Aviary Pro · Zucami</span><span class="chip">Corrector CV-20 · AgroExport</span></div></div>'
      '<span class="k">Solo se comparan productos del mismo tipo: al elegir el primero, filtramos el resto.</span>')
popup('CompNueva1.dc.html', 'Comparador · Nueva comparación · buscar', '<div class="dlg">' + d1 + '</div>')

# C0b · primero elegido, añadir del mismo tipo
sel = lambda col, n, by: '<div style="border: 1.5px solid #0E5A3A; border-radius: 12px; padding: 8px; display: flex; flex-direction: column; gap: 4px; position: relative; background: #F2F7F3;"><span style="position: absolute; top: 6px; right: 6px; width: 20px; height: 20px; border-radius: 50%%; background: #FFFFFF; color: #56615B; display: flex; align-items: center; justify-content: center; font-size: 12px;">×</span><span style="height: 40px; border-radius: 8px; background: %s;"></span><span style="font-size: 12px; font-weight: 600;">%s</span><span class="k">%s</span></div>' % (col, n, by)
add = lambda: '<div style="border: 1.5px dashed #CFD8D2; border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #8A948F; font-size: 12px; min-height: 92px;">Hueco libre</div>'
d2 = (head('Nueva comparación · Enzimas', 'Añade hasta 3 productos del mismo tipo (plan Gratis).') +
      '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 8px;">' + sel('#E6F0FA', 'Ronozyme® HiPhos', 'DSM-Firmenich') + sel('#FDE9EC', 'Axtra® PHY', 'IFF') + add() + '</div>'
      '<div class="inp" style="gap: 8px; justify-content: flex-start; color: #17231D;">' + SRCH + 'fitas<span style="margin-left: auto;" class="tag">Tipo: Enzimas</span></div>'
      '<span class="cap2">DEL MISMO TIPO · SUGERIDOS</span>'
      + res('#EEF2E6', 'Quantum® Blue', 'AB Vista', 'Enzimas · <span class="mk">fitas</span>a', True, '<a href="#" class="btns" style="height: 32px; font-size: 12px;">+ Añadir</a>')
      + res('#E5F1F7', 'Natuphos® E', 'BASF', 'Enzimas · <span class="mk">fitas</span>a', False, '<a href="#" class="btns" style="height: 32px; font-size: 12px;">+ Añadir</a>')
      + res('#F1F4F1', 'Sensor NH₃ / CO₂', 'AgroNova', 'Sensores ambientales', False, '<span class="k">Otro tipo</span>', True) +
      '<div style="display: flex; align-items: center; gap: 10px; border-top: 1px solid #EEF1EE; padding-top: 12px;">'
      '<div class="inp" style="flex: 1; height: 40px; font-size: 13px;">Nombre: Enzimas · fitasas<span class="k">Editar</span></div>'
      '<label style="display: flex; align-items: center; gap: 6px; font-size: 12.5px; white-space: nowrap;"><span style="width: 16px; height: 16px; border-radius: 4px; background: #0E5A3A; display: flex; align-items: center; justify-content: center;">' + CHK + '</span>Guardar en «Nave 2»</label>'
      '<a href="#" class="btnp">Comparar (2)</a></div>')
popup('CompNueva2.dc.html', 'Comparador · Nueva comparación · añadir del mismo tipo', '<div class="dlg">' + d2 + '</div>')

c = json.load(open(P + 'canvas.json')); B = c['boards']
for k, x in [('CompVista.dc.html', 4080), ('CompOtroTipo.dc.html', 5440), ('CompSolicitar.dc.html', 6800)]:
    B[k]['x'] = x
B['CompNueva1.dc.html'] = {'h': 900, 'page': 'tableros', 'title': 'C0a · Nueva comparación · escribir unas letras', 'w': 1280, 'x': 1360, 'y': 1300}
B['CompNueva2.dc.html'] = {'h': 900, 'page': 'tableros', 'title': 'C0b · Nueva comparación · añadir del mismo tipo', 'w': 1280, 'x': 2720, 'y': 1300}
o = c['order']
for k in ['CompNueva2.dc.html', 'CompNueva1.dc.html']:
    if k not in o: o.insert(o.index('CompSumario.dc.html') + 1, k)
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [(k, B[k]['x']) for k in ['CompSumario.dc.html', 'CompNueva1.dc.html', 'CompNueva2.dc.html', 'CompVista.dc.html', 'CompOtroTipo.dc.html', 'CompSolicitar.dc.html']])
