"""Divide las tiras (varias pantallas en un tablero) en tableros de una pantalla, en el canvas «Agroolink · Móvil».
Cada pantalla ocupa el sitio de la tira, en fila (390 px + 80), con su título; las imágenes usan los ids del canvas móvil (tools/blobs_movil.json).
Uso: python3 tools/dividir_tiras.py <carpeta>/project/canvas.json   → escribe los tableros nuevos en esa carpeta y actualiza el índice."""
import os, re, sys, json
CANVAS = sys.argv[1]; DEST = os.path.dirname(CANVAS) + '/'
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import usuario_movil as U, experto_movil as X, empresa_config_movil as E
from proyectos_movil import wrap, W
BLOBS = json.load(open(W + '/tools/blobs_movil.json'))

def board_captura(k, titulo):
    d = json.load(open(W + '/capture/' + k + '.json'))
    css = re.sub(r'@media \(prefers-color-scheme: dark\)\{:root:not\(\[data-theme="light"\]\)\{.*?\}\}', '', d['css'], flags=re.S)
    css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css, flags=re.S)
    css = E.medias(css).replace('position:sticky', 'position:relative').replace('.modal{position:fixed', '.modal{position:absolute').replace('.ov{position:fixed', '.ov{position:absolute').replace('.toast{position:fixed', '.toast{position:absolute')
    h = d['h']
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>Móvil · ' + titulo + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + css + '\nhtml,body{min-height:0}\n</style>\n</helmet>\n<div style="width: 390px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">' + d['body'].replace('{{', '{ {') + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":390,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n'), h

def pantallas():
    """{tira: [(clave_nueva, título, html, alto)]}"""
    out = {}
    for mod in (U, X):
        P = {k: (t, h, f) for k, t, h, f in mod.PANT}
        for tira, _, claves in mod.TIRAS:
            out[tira] = [(k, P[k][0].replace('Móvil · ', ''), wrap(P[k][0], P[k][1], P[k][2]()), P[k][1]) for k in claves]
    alto = E.ALTOS
    for tira, _, claves in E.TIRAS:
        pref = 'MB_' + tira.replace('MB_EmpTira', '') + '_'
        lista = []
        for k in claves:
            if k in E.CAPT:
                t = E.CAPT[k]; html, h = board_captura(k, t)
            else:
                t, f = E.PROPIAS[k]; h = int(alto.get(k, 844)); html = wrap('Móvil · ' + t, h, f())
            lista.append((pref + re.sub(r'[^A-Za-z0-9-]', '', t.split(' · ')[0]), t, html, h))
        out[tira] = lista
    return out

if __name__ == '__main__':
    c = json.load(open(CANVAS)); B = c['boards']; nuevos = []
    for tira, lista in pantallas().items():
        k0 = tira + '.dc.html'
        if k0 not in B: continue
        b = B.pop(k0); pos = c['order'].index(k0); c['order'].remove(k0)
        for i, (k, t, html, h) in enumerate(lista):
            html = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '/_blob/' + BLOBS.get(m.group(1), m.group(1)), html)
            open(DEST + k + '.dc.html', 'w').write(html)
            B[k + '.dc.html'] = {'w': 390, 'h': h, 'page': b['page'], 'x': b['x'] + i * 470, 'y': b['y'], 'title': t}
            c['order'].insert(pos + i, k + '.dc.html'); nuevos.append(k + '.dc.html')
        print(tira, '→', len(lista))
    json.dump(c, open(CANVAS, 'w'), ensure_ascii=False, indent=1)
    json.dump(nuevos, open(DEST + '../nuevos.json', 'w'))
    print('ok', len(nuevos))
