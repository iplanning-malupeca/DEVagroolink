"""Pantallas del asistente de proyectos (prototipo) como tableros del canvas + modelo de datos de Proyecto."""
import json, os, re, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
snaps = json.load(open(sys.argv[1]))
css = snaps['css']
css = re.sub(r'@media \(prefers-color-scheme: dark\)\{.*?\}\}', '', css, flags=re.S)
css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css, flags=re.S)
css += '\n[hidden]{display:none!important}\nbody{margin:0}\n.q.enter{animation:none}'
B = [('W','ProyAsistBienvenida','J1 · Asistente · bienvenida',900),
     ('T','ProyAsistTipo','J1a · Asistente · tipo de proyecto (10 tipos)',1000),
     ('L','ProyAsistLugar','J1b · Asistente · dónde (país con buscador)',900),
     ('E','ProyAsistEscenario','J1c · Asistente · pregunta del escenario (nueva explotación)',900),
     ('P','ProyAsistProductos','J1d · Asistente · productos y «Tu selección»',1420),
     ('R','ProyAsistResumen','J1e · Asistente · resumen con Editar',1300),
     ('F','ProyFicha','J4 · Ficha del proyecto · Resumen (estado editable)',900),
     ('F2','ProyFichaEmpresas','J4b · Ficha del proyecto · Empresas y expertos (contactar uno a uno)',900)]
for k, fn, title, h in B:
    t = ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
         '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n<style>%s</style>\n</helmet>\n'
         '<div style="width: 1280px; height: %dpx; overflow: hidden; background: #FFFFFF; font-family: \'Poppins\', sans-serif;">%s</div>\n</x-dc>\n'
         '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":%d}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n') % (title, css, h, snaps[k].replace('{{', '{ {'), h)
    open(P + fn + '.dc.html', 'w').write(t)
# índice
c = json.load(open(P + 'canvas.json')); BO = c['boards']; N = c['notes']
y0 = 0
for n, (k, fn, title, h) in enumerate(B[:6]):
    BO[fn + '.dc.html'] = {'h': h, 'page': 'proyectos', 'title': title, 'w': 1280, 'x': n * 1360, 'y': y0}
# fila 2: después de crear
y1 = 1420 + 500
for fn in ['ProyFicha.dc.html', 'ProyFichaEmpresas.dc.html']:
    BO.setdefault(fn, {'h': 900, 'page': 'proyectos', 'title': '', 'w': 1280, 'x': 0, 'y': 0})
for n, fn in enumerate(['ProyFicha.dc.html', 'ProyFichaEmpresas.dc.html', 'ProyMis.dc.html', 'ProyDetalle.dc.html']):
    BO[fn].update(x=n * 1360, y=y1)
BO['ProyFicha.dc.html'].update(h=900, page='proyectos', title=B[6][2], w=1280)
BO['ProyFichaEmpresas.dc.html'].update(h=900, page='proyectos', title=B[7][2], w=1280)
BO['ProyMis.dc.html']['title'] = 'J3 · Mis proyectos'
BO['ProyDetalle.dc.html']['title'] = 'J4c · Detalle del proyecto con propuestas recibidas'
# fila 3: empresas y expertos
y2 = y1 + 1000 + 500
for n, fn in enumerate(['ProyOportunidades.dc.html', 'ProyPropuesta.dc.html', 'ProyExperto.dc.html']):
    BO[fn]['y'] = y2; BO[fn]['x'] = n * 1360
# fila 4: versión anterior
y3 = y2 + 1000 + 500
BO['ProyCrear.dc.html'].update(x=0, y=y3, title='Anterior · J1 formulario en una página (sustituido por el asistente)')
BO['ProyDestinatarios.dc.html'].update(x=1360, y=y3, title='Anterior · J2 a quién se lo enviamos (pasa a «Contactar» en la ficha)')
N['proyT1'].update(text='Proyectos · el ganadero crea su proyecto con el asistente (una pregunta por pantalla) · prototipo navegable: design/prototipos/crear-proyecto.html', y=-300)
N['proyT2'].update(text='Empresas y expertos reciben oportunidades cuando el proyecto se comparte', y=y2 - 300)
N['proyT3'] = {'kind': 'title1', 'maxW': 6000, 'page': 'proyectos', 'text': 'Después de crear · ficha del proyecto, Mis proyectos y propuestas', 'w': 240, 'x': 0, 'y': y1 - 300}
N['proyT4'] = {'kind': 'title1', 'maxW': 6000, 'page': 'proyectos', 'text': 'Versión anterior (no se usa)', 'w': 240, 'x': 0, 'y': y3 - 300}
o = c['order']
for k, fn, *_ in B:
    if fn + '.dc.html' not in o: o.insert(o.index('ProyCrear.dc.html'), fn + '.dc.html')
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
json.dump(snaps['model'], open(W + '/tools/proyecto_modelo.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
