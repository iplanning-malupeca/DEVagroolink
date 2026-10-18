"""Pasa las capturas del prototipo (capture/*.json) a tableros DC y reorganiza la página «011_Alta de producto»."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
URL = 'https://claude.ai/artifact/FhRs7ySjp5wCRVgvHbhuwS'
def dc(cap, title):
    d = json.load(open(W + '/capture/' + cap + '.json'))
    css = d['css']
    css = re.sub(r'@media \(prefers-color-scheme: dark\)\{:root:not\(\[data-theme="light"\]\)\{.*?\}\}', '', css, flags=re.S)
    css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css, flags=re.S)
    css = css.replace('position:sticky;top:env(safe-area-inset-top,0px);', '')
    h = d['h']; body = d['body'].replace('{{', '{ {')
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + css + '\n</style>\n</helmet>\n<div style="width: 1280px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F4F6F9;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n'), h
F1 = [('E1', 'ProdAltaEspecies', 'G1 · Especies de destino: Porcino › Lechones y Avicultura › Pollos de engorde (o «no depende de especie»)'),
      ('G1', 'ProdAltaCategoria', 'G2 · Tipo de producto: familia › subfamilia › tipo, con nombres cortos'),
      ('G2', 'ProdAltaMercados', 'G3 · Mercados: buscar y atajos + inclusiones y exclusiones'),
      ('G3', 'ProdAltaIdentidad', 'G4 · Identidad: nombre, marca, web o contacto, descripciones'),
      ('G4', 'ProdAltaTecnicos', 'G5 · Datos técnicos del tipo (aquí: probióticos)'),
      ('GA', 'ProdAltaAplicaciones', 'G6 · Aplicación por especie: una tarjeta por segmento con fases y dosis propias'),
      ('G5', 'ProdAltaEnfermedad', 'G7 · Enfermedad diana: filtro aparte, solo de las especies elegidas'),
      ('G6', 'ProdAltaVariantes', 'G8 · Variantes según el tipo (aquí: embalaje)'),
      ('G7', 'ProdAltaDocumentos', 'G9 · Fotos (subir, arrastrar, principal, ordenar), vídeos con capítulos y documentos'),
      ('GC', 'ProdAltaCertificaciones', 'G10 · Certificaciones y sellos: alcance, entidad, fechas y documento; sin documento no hay sello'),
      ('G8', 'ProdAltaRevision', 'G11 · Revisión: qué falta, estado, ficha pública y comparador')]
F2 = [('H1', 'ProdAltaOrdeno', 'H1 · Ordeño + vacuno de leche: capacidad, rendimiento y conectividad; ningún campo de vacunas'),
      ('H2', 'ProdAltaVacunaEnf', 'H2 · Vacuna + gallinas ponedoras: solo enfermedades aviares'),
      ('H3', 'ProdAltaVacunaApl', 'H3 · Vacuna: edad, dosis, primovacunación y revacunación por especie'),
      ('H4', 'ProdAltaPienso', 'H4 · Pienso completo + ponedoras: composición con calcio y fósforo'),
      ('H5', 'ProdAltaSinEspecie', 'H5 · «No depende de especie» para equipos y servicios transversales'),
      ('H6', 'ProdAltaMolino', 'H6 · Molino sin especie: rendimiento, granulometría y potencia'),
      ('H7', 'ProdAltaNoAplica', 'H7 · Con vacuno de leche no se ofrecen aviarios, nidales, parideras ni incubación'),
      ('H8', 'ProdAltaMercadosExcluir', 'H8 · Mercados: todo el mundo salvo regiones o países'),
      ('H9', 'ProdAltaOtro', 'H9 · «Otro…» en cada grupo y familia: se escribe y lo revisa Agroolink'),
      ('H10', 'ProdAltaOcultos', 'H10 · Al cambiar de tipo, los datos que ya no aplican se guardan pero no se publican'),
      ('H11', 'ProdAltaPublica', 'H11 · Vista previa de la ficha pública: solo lo rellenado que aplica'),
      ('H12', 'ProdAltaComparador', 'H12 · Así entra en el comparador: misma plantilla y especie, «No informado» si falta')]
F3 = [('K1', 'ProdEdCatalogo', 'K1 · Mis productos: cada ficha con su estado, «Editar» y el menú ⋯'),
      ('K2', 'ProdEdMenu', 'K2 · Menú de acciones: Editar, Duplicar, Ocultar y Archivar'),
      ('K3', 'ProdEdBloques', 'K3 · Editar por bloques: cada «Editar» abre su paso aquí mismo; uno abierto a la vez'),
      ('K4', 'ProdEdGuardar', 'K4 · Guardar cambios: qué cambia y si avisar a distribuidores, sucursales y compradores'),
      ('K5', 'ProdEdGuardado', 'K5 · Tras guardar: el catálogo indica a quién se avisó'),
      ('K6', 'ProdEdRegulado', 'K6 · Vacuna (regulado): los cambios vuelven a revisión; se sigue viendo la versión publicada'),
      ('K7', 'ProdEdArchivar', 'K7 · Tras archivar: «Deshacer» y «Ver archivados»'),
      ('K8', 'ProdEdArchivados', 'K8 · Productos archivados: «Recuperar» con su estado'),
      ('K9', 'ProdEdDesdeRevision', 'K9 · En el alta: editar un apartado desde la revisión y volver a ella')]
F4 = [('L1', 'ProdTradEdicion', 'L1 · Traducciones en la edición: original y traducción lado a lado; automática, revisada o editada a mano'),
      ('L2', 'ProdTradDesact', 'L2 · Cambió el original: lo editado a mano no se pisa, pasa a «Desactualizada» (mantener la mía o volver a traducir)'),
      ('L3', 'ProdTradFicha', 'L3 · Lo que ve el comprador en inglés: «Traducido automáticamente · Ver original»'),
      ('L4', 'ProdTradRegulado', 'L4 · Vacuna: los campos sensibles no se publican traducidos hasta que se revisan'),
      ('L5', 'ProdTradReguladoFicha', 'L5 · Vacuna en francés sin revisar: se muestra el original con el aviso de la ficha técnica oficial')]
VIEJOS = ['ProdAltaAplicacion', 'ProdAltaEspeciesSolo', 'ProdAltaBuscar', 'ProdAltaCambio', 'ProdAltaTecEnzima', 'ProdAltaTecClima', 'ProdAltaTecVacuna', 'ProdAltaRevServicio']
c = json.load(open(W + '/project/canvas.json'))
for k in [v + '.dc.html' for v in VIEJOS]:
    c['boards'].pop(k, None); c['order'] = [o for o in c['order'] if o != k]
alturas = {}
for fila in (F1, F2, F3, F4):
    for cap, key, t in fila:
        html, h = dc(cap, 'Alta de producto · ' + t.split(' · ', 1)[1])
        open(W + '/project/' + key + '.dc.html', 'w').write(html); alturas[key] = h
y1 = 0; y2 = y1 + max(alturas[k] for _, k, _ in F1) + 420; y3 = y2 + max(alturas[k] for _, k, _ in F2) + 420
y4 = y3 + max(alturas[k] for _, k, _ in F3) + 420
for y, fila in ((y1, F1), (y2, F2), (y3, F3), (y4, F4)):
    for i, (cap, key, t) in enumerate(fila):
        k = key + '.dc.html'
        c['boards'][k] = {'w': 1280, 'h': alturas[key], 'page': 'productos', 'x': i * 1360, 'y': y, 'title': t}
        if k not in c['order']: c['order'].append(k)
P = ['ProdFichaGeneral', 'ProdFichaVariantes', 'ProdFichaBeneficios', 'ProdFichaEspecificaciones', 'ProdEspecEquipamiento', 'ProdFichaDocumentos', 'ProdFichaMercados']
for k in P:   # las pestañas antiguas de la ficha (P4–P9) se quitaron el 18/10/2026: queda solo el asistente
    c['boards'].pop(k + '.dc.html', None); c['order'] = [o for o in c['order'] if o != k + '.dc.html']
c['notes'].pop('prodT5', None)
c['notes']['prodT2'].update({'x': 0, 'y': -640, 'maxW': 8000, 'text': 'Alta de un producto · asistente por pasos, como Proyectos: primero las especies de destino; los datos técnicos cambian según el tipo y hay una tarjeta de aplicación por especie · prototipo navegable: design/prototipos/crear-producto.html'})
c['notes']['prodDev1'] = {'fill': 'orange', 'maxH': 300, 'page': 'productos', 'size': 24, 'w': 1280, 'x': 0, 'y': -340, 'text':
  'PARA DESARROLLO · Asistente de alta de producto\n\nEstas pantallas (G1–G11, H1–H12, K1–K9 y L1–L6) son muestras de algunos estados. Para programar el asistente, sigue el HTML del prototipo navegable: monta los campos técnicos a partir del modelo declarativo (una plantilla por grupo de categorías, reglas condicionales, especies, enfermedades y arquetipos), no con formularios fijos por producto.\n\n'
  'Prototipo: design/prototipos/crear-producto.html (repo DEVagroolink)\nVersión publicada: ' + URL + '\nModelo de datos: docs/modelo-producto/producto.json (v2, taxonomía C01–C12)\n\nSi una pantalla del canvas y el HTML no coinciden, manda el HTML, salvo en estilos visuales (colores, tipografía), que se toman del canvas.'}
c['notes']['prodT4'] = {'kind': 'title1', 'maxW': 8000, 'page': 'productos', 'w': 240, 'x': 0, 'y': y2 - 300, 'text': 'Casos de prueba del documento del árbol condicional y reglas · ordeño, vacuna, pienso de ponedoras, molino sin especie, categorías que no aplican, mercados, «Otro…», datos que no se publican, ficha pública y comparador'}
c['boards']['ProdTradGlosario.dc.html'] = {'w': 1280, 'h': 1180, 'page': 'productos', 'x': len(F4) * 1360, 'y': y4, 'title': 'L6 · Superadmin: glosario del sector, términos que no se traducen y fichas sin revisar'}
if 'ProdTradGlosario.dc.html' not in c['order']: c['order'].append('ProdTradGlosario.dc.html')
c['notes']['prodT7'] = {'kind': 'title1', 'maxW': 8000, 'page': 'productos', 'w': 240, 'x': 0, 'y': y4 - 300, 'text': 'Traducciones · la IA traduce el texto libre a ES, EN, PT y FR; la empresa revisa o edita y lo editado no se pisa; en regulados, lo sensible no se publica sin revisar; los mensajes se traducen solo al leer'}
c['notes']['prodT6'] = {'kind': 'title1', 'maxW': 8000, 'page': 'productos', 'w': 240, 'x': 0, 'y': y3 - 300, 'text': 'Edición del producto, como en Proyectos · catálogo con acciones, edición por bloques con aviso a quien lo vende o lo ha pedido, revisión de nuevo en productos regulados, archivar y recuperar'}
for p in c['pages']:
    if p['id'] == 'productos': p['name'] = '011_Alta de producto'
json.dump(c, open(W + '/project/canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok', y2, y3, alturas)
