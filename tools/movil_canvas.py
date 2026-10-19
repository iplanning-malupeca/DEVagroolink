"""Páginas MB_01…MB_07 (móvil, antes «013_Móvil») (19/10/2026): capturas a 390 px de los prototipos y, sin duplicar,
las pantallas móviles que ya existían (cabecera, home y búsqueda) importadas tal cual."""
import json, os, re, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CANVAS = sys.argv[1]; DEST = os.path.dirname(CANVAS) + '/'
def medias(css):
    out, i = '', 0
    while True:
        m = re.search(r'@media\s*\(([^)]*)\)\s*\{', css[i:])
        if not m: return out + css[i:]
        j = i + m.start(); k, n = i + m.end(), 1
        while n:
            n += {'{': 1, '}': -1}.get(css[k], 0); k += 1
        cond, body = m.group(1), css[i + m.end():k - 1]
        mw = re.match(r'\s*max-width:\s*(\d+)px\s*$', cond)
        keep = body + '\n' if (mw and int(mw.group(1)) >= 390) else ''
        out += css[i:j] + keep; i = k
def board(cap, title):
    d = json.load(open(W + '/capture/' + cap + '.json'))
    css = d['css']
    css = re.sub(r'@media \(prefers-color-scheme: dark\)\{:root:not\(\[data-theme="light"\]\)\{.*?\}\}', '', css, flags=re.S)
    css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css, flags=re.S)
    css = medias(css).replace('position:sticky', 'position:relative').replace('.modal{position:fixed', '.modal{position:absolute').replace('.ov{position:fixed', '.ov{position:absolute').replace('.toast{position:fixed', '.toast{position:absolute')
    h = d['h']; body = d['body'].replace('{{', '{ {')
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + css + '\nhtml,body{min-height:0}\n</style>\n</helmet>\n<div style="width: 390px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":390,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n'), h
def importa(name, w, h, title):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n<style>body{margin:0}</style>\n</helmet>\n'
            '<div style="width: ' + str(w) + 'px; height: ' + str(h) + 'px; overflow: hidden;"><dc-import name="' + name + '" hint-size="' + str(w) + 'px,' + str(h) + 'px"></dc-import></div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":' + str(w) + ',"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')
c = json.load(open(CANVAS)); B = c['boards']
FILAS = [
 ('MB_01 Navegación', 'Navegación · Home y filtros (la cabecera, el menú inferior y la búsqueda abierta están en MB_000_Header)', 'imp', [('MobHome', 'Home'), ('BuscaMovFiltros', 'Al tocar el botón de filtros: «Filtros» a pantalla completa', 'MB_Nav_Filtros')]),
 ('MB_02 Búsqueda', 'Búsqueda y filtros (de 005)', 'imp', [('BuscaMovResultados', 'Resultados'), ('BuscaMovEspecie', 'Buscar por pasos'), ('BuscaMovCategoria', 'Categoría'), ('BuscaMovFiltros', 'Filtros')]),
 ('MB_03 Alta de producto', 'Alta de producto (prototipo crear-producto)', 'cap', [('MP1', 'Especies'), ('MP2', 'Categoría'), ('MP3', 'Mercados'), ('MP4', 'Identidad (idioma detectado)'), ('MP5', 'Datos técnicos'), ('MP6', 'Aplicación por especie'), ('MP7', 'Fotos, vídeos y documentos'), ('MP8', 'Certificaciones'), ('MP9', 'Revisión')]),
 ('MB_04 Mis productos', 'Mis productos, edición y traducciones', 'cap', [('ME1', 'Mis productos'), ('ME2', 'Menú ⋯'), ('ME3', 'Editar por bloques'), ('ME4', 'Guardar y avisar'), ('ME5', 'Traducciones'), ('ME6', 'Ficha en inglés')]),
 ('MB_05 Alta de servicios', 'Alta de servicios del experto (prototipo crear-servicio)', 'cap', [('MS1', 'Tipo de servicio'), ('MS2', 'Especies'), ('MS3', 'Dirigido a'), ('MS4', 'Dónde lo prestas'), ('MS5', 'Detalles'), ('MS6', 'Revisión'), ('MS7', 'Mis servicios')]),
 ('MB_06 Alta de empresa', 'Alta de empresa 006–010 en un solo asistente (prototipo alta-empresa) · fabricante con comerciales; al final, organización nueva y sucursal', 'cap', [('MA1', 'Tu organización (CRM)'), ('MA2', 'Confirmar email'), ('MA3', 'Tipo de empresa'), ('MA4', 'Especies'), ('MA5', 'Rama de negocio'), ('MA6', 'Mercados'), ('MA7', 'Cabecera'), ('MA8', 'Sobre la empresa'), ('MA9', 'Equipo comercial'), ('MA10', 'Contacto'), ('MA11', 'Revisar y publicar'), ('MA12', 'Publicada'), ('MA13', 'Crear organización nueva'), ('MA14', 'Sucursal: entra directa'), ('MA15', 'Sucursal: tu Sede')]),
 ('MB_07 Proyectos', 'Proyectos (prototipo crear-proyecto)', 'cap', [('MJ1', 'Bienvenida'), ('MJ2', 'Una pregunta por pantalla'), ('MJ3', 'Resumen'), ('MJ4', 'Editar desde el resumen')]),
 ('MB_08 Planes', 'Planes · ventanas de bloqueo en móvil (login, límite, plan de pago) · generadas por tools/planes.py', 'own', [('MB_PlanLogin', 'Login al pulsar Guardar'), ('MB_PlanLimite', 'Límite: 2.º proyecto del comprador'), ('MB_PlanPago', 'Plan de pago: exportar informes'), ('MB_PlanFiltro', 'Contacto ocultado')])]
MBP = lambda pg: pg == 'movil2' or str(pg).startswith('mb')
for k in [k for k, b in B.items() if MBP(b.get('page'))]: del B[k]
c['order'] = [k for k in c['order'] if k in B]
for k in [k for k, n in c['notes'].items() if MBP(n.get('page'))]: del c['notes'][k]
pos = next((k for k, p in enumerate(c['pages']) if p['id'] == 'movil2' or p['id'].startswith('mb')), None)
if pos is None: pos = next(k for k, p in enumerate(c['pages']) if p['id'] == 'altaserv') + 1
c['pages'] = [p for p in c['pages'] if not MBP(p['id'])]
for r, (pag, tit, modo, items) in enumerate(FILAS):
    pid = 'mb%d' % (r + 1); c['pages'].insert(pos + r, {'id': pid, 'name': pag})
    c['notes']['mbt%d' % r] = {'kind': 'title1', 'maxW': 8000, 'page': pid, 'w': 240, 'x': 0, 'y': -300, 'text': tit}
    for i, it in enumerate(items):
        src, t = it[0], it[1]
        key = it[2] if len(it) > 2 else (src if modo == 'own' else 'MB_' + src)
        if modo == 'own':
            w, h = 390, 844
            B[key + '.dc.html'] = {'w': w, 'h': h, 'page': pid, 'x': i * 470, 'y': 0, 'title': t}; c['order'].append(key + '.dc.html'); continue
        if modo == 'imp':
            ob = B[src + '.dc.html']; w, h = ob['w'], ob['h']; html = importa(src, w, h, 'Móvil · ' + t)
        else:
            html, h = board(src, 'Móvil · ' + t); w = 390
        open(DEST + key + '.dc.html', 'w').write(html); open(W + '/project/' + key + '.dc.html', 'w').write(html)
        B[key + '.dc.html'] = {'w': w, 'h': h, 'page': pid, 'x': i * 470, 'y': 0, 'title': t}
        c['order'].append(key + '.dc.html')
c['notes']['mbdev'] = {'fill': 'orange', 'maxH': 320, 'page': 'mb1', 'size': 24, 'w': 1280, 'x': 1100, 'y': -300, 'text':
  'PARA DESARROLLO · Versión móvil\n\nLos prototipos son responsive: por debajo de 900 px pasan a una columna (y la búsqueda a pastilla + menú inferior). Estas pantallas son esos mismos prototipos capturados a 390 px; lo de navegación y búsqueda se importa de 000_Header y 005 para no duplicarlo.\n\nEl alta de empresa (006–010) ya es un prototipo único (alta-empresa) que se adapta a cómo vende la empresa.\n\nPendiente de pasar a móvil: catálogos por tipo de empresa (011a–011e), mensajes e intranets; hoy son pantallas fijas de escritorio y conviene convertirlas antes en prototipo.'}
json.dump(c, open(CANVAS, 'w'), ensure_ascii=False, indent=1)
print('ok', len([1 for b in B.values() if MBP(b.get('page'))]), [p['name'] for p in c['pages'] if MBP(p['id'])])
