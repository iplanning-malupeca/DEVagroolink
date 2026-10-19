"""«004b_LP_Intranet · Empresa»: Editar ficha de empresa (capturas EE1–EE3 del prototipo alta-empresa), junto al panel de empresa.
Uso: python3 tools/empresa_editar_canvas.py <canvas.json>"""
import json, os, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANVAS = sys.argv[1]; DEST = os.path.dirname(CANVAS) + '/'
src = open(W + '/tools/alta_producto_canvas.py').read(); dc_src = src[:src.index('F1 = [')]
ns = {}; exec(compile(dc_src.replace("W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))", "W = '" + W + "'"), 'dc', 'exec'), ns); dc = ns['dc']
F = [('EE1', 'EmpEditarFicha', 'EM2 · Editar ficha de empresa: por bloques, con «Cambiar» y los bloques modificados marcados; sociedades del CRM solo las cambia el superadmin'),
     ('EE2', 'EmpEditarBloque', 'EM3 · Cambiar un bloque: el mismo paso del alta y «Hecho · volver a Editar ficha»'),
     ('EE3', 'EmpEditarAvisar', 'EM4 · Antes de guardar: si cambian tipo, especies, mercados o red, se avisa del efecto en las búsquedas y a la red en Mensajes')]
c = json.load(open(CANVAS)); B = c['boards']
for p in c['pages']:
    if p['id'] == 'intempresa': p['name'] = '004b_LP_Intranet · Empresa'
x = 1360
for cap, key, t in F:
    html, h = dc(cap, 'Intranet de empresa · ' + t.split(' · ', 1)[1].split(':')[0])
    open(DEST + key + '.dc.html', 'w').write(html); open(W + '/project/' + key + '.dc.html', 'w').write(html)
    B[key + '.dc.html'] = {'w': 1280, 'h': h, 'page': 'intempresa', 'x': x, 'y': 0, 'title': t}; x += 1360
    if key + '.dc.html' not in c['order']: c['order'].append(key + '.dc.html')
c['notes']['iemEdit'] = {'fill': 'orange', 'maxH': 260, 'page': 'intempresa', 'size': 22, 'w': 1280, 'x': 1360, 'y': -420, 'text':
  'PARA DESARROLLO · Editar ficha de empresa\n\nSe abre desde el panel («Editar ficha»). Cada bloque reutiliza su paso del alta (006–010 y prototipo alta-empresa). Los cambios no se publican hasta «Guardar cambios». Sociedades y datos fiscales: solo el superadmin (CRM).\nPrototipo: https://claude.ai/artifact/GD5V5oHeH2yCRwiVcMAs2N · móvil en 004b_MB_Intranet · Empresa.'}
json.dump(c, open(CANVAS, 'w'), ensure_ascii=False, indent=1)
print('ok')
