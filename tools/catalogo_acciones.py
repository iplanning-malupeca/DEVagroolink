"""011a y 011b (18/10/2026): menú ⋯ en cada producto del catálogo (Editar, Duplicar, Ocultar, Archivar),
el menú abierto (PA1b, PC1b) y el catálogo tras duplicar (PA1c, PC1c). La edición es la de 011 (K3–K6)."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); PR = W + '/project/'
def cierre(s, i):   # índice tras el </div> que cierra el <div que empieza en i
    n = 0; k = i
    while True:
        a, b = s.find('<div', k), s.find('</div>', k)
        if a != -1 and a < b: n += 1; k = a + 4
        else:
            n -= 1; k = b + 6
            if n == 0: return k
def filas(s, cols):
    out = []; k = 0
    while True:
        i = s.find('<div style="display: grid; grid-template-columns: ' + cols, k)
        if i < 0: return out
        j = cierre(s, i); out.append((i, j)); k = j
BTN = '<button type="button" aria-label="Más acciones" style="width: 28px; height: 28px; border: 0; border-radius: 8px; background: {bg}; color: #56615B; font-size: 16px; line-height: 1; cursor: pointer;">⋯</button>'
def menu(quien):
    it = lambda t, d: '<span style="display: flex; flex-direction: column; gap: 1px; padding: 8px 10px; border-radius: 8px;"><strong style="font-size: 13px; font-weight: 600;">' + t + '</strong><span style="font-size: 11.5px; color: #56615B;">' + d + '</span></span>'
    return ('<div role="menu" style="position: absolute; right: 10px; top: 42px; z-index: 5; width: 320px; background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 12px; box-shadow: 0 14px 34px rgba(10,20,30,.16); padding: 6px; display: flex; flex-direction: column; text-align: left; white-space: normal;">' +
            it('Editar', 'Cambia cualquier apartado; si afecta a ' + quien + ', eliges si avisar') +
            it('Duplicar', 'Crea un borrador igual con «(copia)», por ejemplo para otra presentación') +
            it('Ocultar', 'Deja de salir en búsquedas; las solicitudes abiertas siguen') +
            it('Archivar', 'Lo quita del catálogo; se puede recuperar') + '</div>')
def hacer(base, cols, quien, fila_menu, fila_copia):
    s0 = open(PR + base + '.dc.html').read()
    if '⋯' not in s0:   # columna ⋯ en el catálogo
        cols2 = cols + ' 28px'
        out = s0
        for i, j in reversed(filas(s0, cols)):
            row = out[i:j]
            cell = '<span></span>' if 'PRODUCTO' in row else '<span style="position: relative;">' + BTN.format(bg='none') + '</span>'
            row = row[:-6] + cell + '</div>'
            out = out[:i] + row + out[j:]
        out = out.replace('grid-template-columns: ' + cols + ';', 'grid-template-columns: ' + cols2 + ';')
        open(PR + base + '.dc.html', 'w').write(out); s0 = out
    cols2 = cols + ' 28px'
    F = filas(s0, cols2)
    caja = s0.rfind('overflow: hidden; box-shadow', 0, F[0][0])
    caja = caja if caja > -1 else s0.rfind('overflow: hidden', 0, F[0][0])
    abre = lambda s: s[:caja] + s[caja:].replace('overflow: hidden', 'overflow: visible', 1)
    # b · menú abierto
    i, j = F[fila_menu]; row = s0[i:j]
    row = row.replace(BTN.format(bg='none'), BTN.format(bg='#E9F0F9') + menu(quien), 1)
    sb = abre(s0[:i] + row + s0[j:])
    sb = sb.replace('<title>', '<title>Menú de acciones · ', 1)
    # c · tras duplicar
    i, j = F[fila_copia]; row = s0[i:j]
    nombre = re.search(r'<strong style="font-weight: 600;">([^<]+)</strong>', row).group(1)
    copia = re.sub(r'<strong style="font-weight: 600;">[^<]+</strong>', '<strong style="font-weight: 600;">' + nombre + ' (copia)</strong>', row, count=1)
    copia = re.sub(r'<span class="st (ok|wn|er)">[^<]+</span>', '<span class="st dr">Borrador</span>', copia, count=1)
    copia = copia.replace('defaultChecked="{{ yes }}" ', '').replace('style="display: grid;', 'style="background: #FFF8EA !important; display: grid;', 1)
    copia = re.sub(r'background: #F3F7FC;', '', copia)
    ins = F[1][0]
    sc = s0[:ins] + copia + s0[ins:]
    toast = ('<div role="status" style="position: absolute; left: 50%; transform: translateX(-50%); bottom: 24px; z-index: 6; display: flex; align-items: center; gap: 14px; background: #17231D; color: #FFFFFF; border-radius: 12px; padding: 11px 16px; font-size: 13px; box-shadow: 0 10px 30px rgba(0,0,0,.2); white-space: nowrap;">'
             'Borrador creado: «' + nombre + ' (copia)». Cambia lo que necesites.<a href="#" style="color: #B5D334; font-weight: 600;">Editar la copia</a></div>')
    k = sc.rfind('</x-dc>'); k = sc.rfind('</div>', 0, k)
    sc = sc[:k] + toast + sc[k:]
    sc = sc.replace('<title>', '<title>Tras duplicar · ', 1)
    open(PR + base + 'Menu.dc.html', 'w').write(sb); open(PR + base + 'Copia.dc.html', 'w').write(sc)
hacer('PrdFabCatalogo', '18px 38px minmax(0,1.7fr) 1fr 1fr 70px 80px 104px 92px', 'distribuidores o solicitudes', 3, 2)
hacer('PrdComCatalogo', '18px 38px minmax(0,1.5fr) 1fr 74px minmax(0,1.2fr) 52px 100px 84px', 'comerciales o solicitudes', 3, 2)
c = json.load(open(PR + 'canvas.json')); B = c['boards']
for pg, base, cod, quien in (('prodfab', 'PrdFabCatalogo', 'PA1', 'distribuidores'), ('prodcom', 'PrdComCatalogo', 'PC1', 'comerciales')):
    B[base + 'Menu.dc.html'] = {'w': 1280, 'h': 940, 'page': pg, 'x': 0, 'y': 1340, 'title': cod + 'b · Menú ⋯ de un producto: Editar, Duplicar, Ocultar y Archivar'}
    B[base + 'Copia.dc.html'] = {'w': 1280, 'h': 940, 'page': pg, 'x': 1360, 'y': 1340, 'title': cod + 'c · Tras «Duplicar»: borrador «(copia)» arriba del catálogo y «Editar la copia»'}
    for k in (base + 'Menu.dc.html', base + 'Copia.dc.html'):
        if k not in c['order']: c['order'].append(k)
    c['notes'][pg + 'T2'] = {'kind': 'title1', 'maxW': 6800, 'page': pg, 'w': 240, 'x': 0, 'y': 1040,
        'text': 'Editar y duplicar desde el catálogo · «Editar» abre la edición por bloques de «011_Alta de producto» (K3–K6): si el cambio afecta a ' + quien + ' o solicitudes, eliges si avisar'}
json.dump(c, open(PR + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
