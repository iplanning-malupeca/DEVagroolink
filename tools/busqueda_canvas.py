"""005_Búsqueda y filtros (19/10/2026): la página se rehace desde el prototipo navegable (out/buscar.html).
Se quitan las variantes y duplicados; quedan solo las pantallas que se van a programar, en escritorio y móvil."""
import json, os, re, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); PR = W + '/project/'
URL = sys.argv[1] if len(sys.argv) > 1 else ''
def medias(css, movil):
    out, i, tag = '', 0, '@media (max-width:899px){'
    while True:
        j = css.find(tag, i)
        if j < 0: return out + css[i:]
        k, n = j + len(tag), 1
        while n:
            n += {'{': 1, '}': -1}.get(css[k], 0); k += 1
        out += css[i:j] + (css[j + len(tag):k - 1] + '\n' if movil else ''); i = k
def dc(cap, title):
    d = json.load(open(W + '/capture/' + cap + '.json'))
    css = d['css']
    css = re.sub(r'@media \(prefers-color-scheme: dark\)\{:root:not\(\[data-theme="light"\]\)\{.*?\}\}', '', css, flags=re.S)
    css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css, flags=re.S)
    css = css.replace('position:sticky;top:0;', '').replace('.ov{position:fixed;', '.ov{position:absolute;')
    w, h = d.get('w', 1280), d['h']; body = d['body'].replace('{{', '{ {')
    css = medias(css, w < 900)   # en el canvas el ancho es fijo: móvil aplica sus reglas sin media query; escritorio las quita
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + css + '\n</style>\n</helmet>\n<div style="width: ' + str(w) + 'px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":' + str(w) + ',"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n'), w, h
ESC = [('S1', 'BuscaResultados', 'B1 · Resultados: botón «Filtros» con contador, un botón por filtro (mismo icono siempre), filtros activos y cómo se combinan'),
       ('S2', 'BuscaAutocompletar', 'B2 · Al escribir en «Qué buscas»: buscar el texto, o ir directo a una categoría, especie, producto o empresa'),
       ('S3', 'BuscaEspecie', 'B3 · Barra · Especie: especies con recuento y, si quieres, su producción (sin marcar = todas)'),
       ('S4', 'BuscaCategoria', 'B4 · Barra · Categoría: familia › grupo › tipo con nombres cortos y recuentos; en gris lo que no aplica a la especie'),
       ('S5', 'BuscaEnfermedad', 'B5 · Barra · Enfermedad: solo las de las especies elegidas, por tipo clínico; las compartidas salen una vez'),
       ('S6', 'BuscaVarios', 'B6 · Varios filtros a la vez: «Coincide con» en cada tarjeta'),
       ('S7', 'BuscaTecnicos', 'B7 · Con un tipo de producto elegido aparece «Filtros técnicos» (los de su plantilla)'),
       ('S8', 'BuscaFiltros', 'B8 · «Filtros»: todo en una ventana (especie, categoría, enfermedad, técnicos, país y marca) y «Ver N resultados»'),
       ('S9', 'BuscaSinResultados', 'B9 · Sin resultados: qué filtro quitar, con cuántos resultados quedarían, y crear un proyecto')]
MOV = [('T1', 'BuscaMovResultados', 'M1 · Móvil · Resultados: pastilla de búsqueda arriba; «Filtros» y los botones de filtro se deslizan'),
       ('T2', 'BuscaMovEspecie', 'M2 · Móvil · Al tocar la pastilla: pasos apilados (Qué · Especie · Categoría · Enfermedad)'),
       ('T3', 'BuscaMovCategoria', 'M3 · Móvil · Categoría: un nivel cada vez, con «‹ atrás»'),
       ('T4', 'BuscaMovFiltros', 'M4 · Móvil · «Filtros» a pantalla completa, con técnicos y «Ver N resultados»')]
c = json.load(open(PR + 'canvas.json')); B = c['boards']
viejos = [k for k, b in B.items() if b.get('page') == 'busqueda' and (k.startswith('Bus') or k.startswith('HeaderHd')) and k != 'BusIntranetBuscar.dc.html' and not k.startswith('Busca')]
for k in viejos: del B[k]
c['order'] = [k for k in c['order'] if k not in viejos]
for k in [k for k, n in c['notes'].items() if n.get('page') == 'busqueda' and k != 'busT7']: del c['notes'][k]
x = 0; hmax = 0
for cap, key, t in ESC:
    html, w, h = dc(cap, 'Búsqueda · ' + t.split(' · ', 1)[1]); open(PR + key + '.dc.html', 'w').write(html)
    B[key + '.dc.html'] = {'w': w, 'h': h, 'page': 'busqueda', 'x': x, 'y': 0, 'title': t}; x += w + 80; hmax = max(hmax, h)
    if key + '.dc.html' not in c['order']: c['order'].append(key + '.dc.html')
y2 = hmax + 420; x = 0; h2 = 0
for cap, key, t in MOV:
    html, w, h = dc(cap, 'Búsqueda · ' + t.split(' · ', 1)[1]); open(PR + key + '.dc.html', 'w').write(html)
    B[key + '.dc.html'] = {'w': w, 'h': h, 'page': 'busqueda', 'x': x, 'y': y2, 'title': t}; x += w + 80; h2 = max(h2, h)
    if key + '.dc.html' not in c['order']: c['order'].append(key + '.dc.html')
y3 = y2 + h2 + 420
B['BusIntranetBuscar.dc.html'].update(x=0, y=y3)
c['notes']['busT7'].update(x=0, y=y3 - 300)
c['notes']['busT1'] = {'kind': 'title1', 'maxW': 12000, 'page': 'busqueda', 'w': 240, 'x': 0, 'y': -640, 'text': 'Búsqueda y filtros · escritorio (1280 px). Barra combinada Qué · Especie · Categoría · Enfermedad y un único botón «Filtros»'}
c['notes']['busDev'] = {'fill': 'orange', 'maxH': 300, 'page': 'busqueda', 'size': 24, 'w': 1280, 'x': 0, 'y': -340, 'text':
  'PARA DESARROLLO · Búsqueda\n\nSolo están las pantallas que se programan; se quitaron las variantes (ventana o panel izquierdo, Airbnb, Figma) y los duplicados. Para programar, sigue el HTML del prototipo navegable: usa el mismo modelo que el alta de producto (categorías con nombres cortos, especies y producciones, enfermedades por especie, pertinencia y plantillas para los filtros técnicos).\n\n'
  'Prototipo: design/prototipos/buscar.html (repo DEVagroolink)' + ('\nVersión publicada: ' + URL if URL else '') + '\nModelo: docs/modelo-producto/producto.json\n\nReglas: entre filtros, Y; dentro de un filtro, O. Lo que no depende de especie sale con cualquier especie. Mismo icono por filtro en botón y chip.'}
c['notes']['busT2'] = {'kind': 'title1', 'maxW': 4000, 'page': 'busqueda', 'w': 240, 'x': 0, 'y': y2 - 300, 'text': 'Búsqueda y filtros · móvil (390 px). Mismos componentes; la barra se resume en una pastilla'}
json.dump(c, open(PR + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print(len(viejos), 'quitados:', ' '.join(sorted(viejos)))
