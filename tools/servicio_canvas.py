"""Página «Alta experto»: fila nueva con el alta de servicios del experto, capturada del prototipo (19/10/2026)."""
import json, os, sys
sys.argv = sys.argv[:1] + sys.argv[1:]
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANVAS = sys.argv[1]; DEST = os.path.dirname(CANVAS) + '/'
URL = 'https://claude.ai/artifact/XsEBeuRLjpbEpUynd4U3Tu'
import importlib.util
src = open(W + '/tools/alta_producto_canvas.py').read(); dc_src = src[:src.index('F1 = [')]
ns = {}; exec(compile(dc_src.replace("W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))", "W = '" + W + "'"), 'dc', 'exec'), ns); dc = ns['dc']
F = [('V1', 'ServExpTipo', 'SX1 · Tipo de servicio: los de la familia Servicios, con «Otro servicio…»'),
     ('V2', 'ServExpEspecies', 'SX2 · Especies y, si quieres, su producción (sin marcar = todas)'),
     ('V3', 'ServExpPublico', 'SX3 · Dirigido a: ramas de negocio y cargos del CRM'),
     ('V4', 'ServExpDonde', 'SX4 · Dónde lo prestas: presencial por zonas y a distancia con idiomas'),
     ('V5', 'ServExpDetalles', 'SX5 · Detalles: nombre, descripción, datos del tipo de servicio y «Se publica en» (traducción)'),
     ('V6', 'ServExpCondiciones', 'SX6 · Plazo de respuesta y precio; las solicitudes llegan por Mensajes'),
     ('V7', 'ServExpRevision', 'SX7 · Revisión con «Editar» por apartado y «Publicar servicio»'),
     ('V8', 'ServExpLista', 'SX8 · Mis servicios: Editar y menú ⋯ (Duplicar, Pausar, Archivar)')]
c = json.load(open(CANVAS)); B = c['boards']
y0 = max(b['y'] + b['h'] for k, b in B.items() if b.get('page') == 'experto' and not k.startswith('ServExp')) + 700
for i, (cap, key, t) in enumerate(F):
    html, h = dc(cap, 'Alta de servicios · ' + t.split(' · ', 1)[1])
    html = html.replace('background: #F4F6F9;', 'background: #F6F8F6;')
    open(DEST + key + '.dc.html', 'w').write(html); open(W + '/project/' + key + '.dc.html', 'w').write(html)
    B[key + '.dc.html'] = {'w': 1280, 'h': h, 'page': 'experto', 'x': i * 1360, 'y': y0, 'title': t}
    if key + '.dc.html' not in c['order']: c['order'].append(key + '.dc.html')
c['notes']['servExpT'] = {'kind': 'title1', 'maxW': 8000, 'page': 'experto', 'w': 240, 'x': 0, 'y': y0 - 640, 'text': 'Alta de servicios del experto · asistente por pasos, en lila, con los mismos campos que el editor de servicios de empresa · prototipo: design/prototipos/crear-servicio.html'}
c['notes']['servExpDev'] = {'fill': 'orange', 'maxH': 260, 'page': 'experto', 'size': 24, 'w': 1280, 'x': 0, 'y': y0 - 340, 'text':
  'PARA DESARROLLO · Alta de servicios del experto\n\nSigue el HTML del prototipo navegable: tipos de la familia Servicios, especies y producciones, ramas y cargos del CRM, zonas (presencial y a distancia con idiomas) y los datos propios de cada tipo salen del mismo modelo que el alta de producto. Ningún dato es obligatorio salvo el nombre, el tipo y dónde se presta.\n\nPrototipo: design/prototipos/crear-servicio.html\nVersión publicada: ' + URL}
json.dump(c, open(CANVAS, 'w'), ensure_ascii=False, indent=1)
print('ok', y0)
