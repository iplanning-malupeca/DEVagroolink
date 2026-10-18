"""011a–011c (18/10/2026): vuelve la pestaña «Importaciones» (carga masiva de catálogos por Excel), solo para el superadmin."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); PR = W + '/project/'
SA = '<span style="font-size: 10px; font-weight: 700; letter-spacing: .04em; background: #17231D; color: #FFFFFF; border-radius: 999px; padding: 1px 7px; margin-left: 6px; vertical-align: 1px;">SUPERADMIN</span>'
def edit(f, fn):
    p = PR + f + '.dc.html'; s = open(p).read(); s2 = fn(s); assert s2 != s, f; open(p, 'w').write(s2)
def tab(s):   # pestaña después de «Catálogo»
    if 'Importaciones' in s: return s
    m = re.search(r'(<div class="tabs"><span[^>]*>Catálogo\s*<span[^>]*>\d+</span></span>)', s); assert m
    return s[:m.end()] + '<span>Importaciones' + SA + '</span>' + s[m.end():]
for f in ['PrdFabCatalogo', 'PrdFabAcuerdos', 'PrdComCatalogo', 'PrdSucCatalogo', 'PrdSucActivacion']: edit(f, tab)
edit('ProdImportar', lambda s: s.replace('Importaciones</span>', 'Importaciones' + SA + '</span>', 1) if SA not in s else s)
for f in ['PrdFabCatalogo', 'PrdComCatalogo', 'PrdSucCatalogo']:
    edit(f, lambda s: s if s.count(SA) > 1 else re.sub(r'(</svg>\s*Importar)(\s*</)', lambda m: m.group(1) + SA + m.group(2), s, count=1))
for f in ['PrdFabNuevo', 'PrdComNuevo', 'PrdSucNuevo']:
    edit(f, lambda s: s if SA in s else s.replace('Importar desde Excel</strong>', 'Importar desde Excel' + SA + '</strong>', 1))
c = json.load(open(PR + 'canvas.json')); B = c['boards']
B['ProdImportar.dc.html']['title'] = 'PA3 · Importaciones (solo superadmin): carga masiva del catálogo por Excel; actualiza por referencia interna'
B['PrdFabNuevo.dc.html']['title'] = 'PA2 · «Nuevo producto»: crear la ficha, importar (solo superadmin) o duplicar'
B['PrdComNuevo.dc.html']['title'] = 'PC2 · «Nuevo producto»: crear la ficha, importar (solo superadmin) o duplicar'
c['notes']['prodfabT1']['text'] = 'Productos de un fabricante con distribuidores — DSM-Firmenich. 1 Catálogo → 2 Nuevo producto → 3 Importaciones (solo superadmin: carga masiva por Excel) o crear la ficha en «011_Alta de producto» → 4 Mercados → 5 Acuerdos de distribución'
json.dump(c, open(PR + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
