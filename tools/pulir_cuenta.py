"""Pulido visual de Mi cuenta (C1, C2, C2a–C2e) a partir de la referencia de C2a. Se aplica sobre los archivos generados."""
import os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
FILES = ['CuentaPerfil', 'CuentaCompras', 'CuentaPlanes', 'CuentaPedidos', 'CuentaFacturas', 'CuentaPagos', 'CuentaDirecciones']
ARROW = ' <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="vertical-align: -2px;"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CSS = ('.card{box-shadow:0 1px 3px rgba(16,40,28,.05)}.h2{font-size:16.5px !important}'
       '.tabs{gap:28px !important;font-size:14px !important}.tabs .on{border-bottom-width:2.5px !important}'
       '.btns{height:42px;border-radius:10px;background:#EEF6EE;color:#17231D;font-size:13.5px;font-weight:500;display:flex;align-items:center;justify-content:center;gap:8px}'
       '.ico{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex:none}'
       '.kebab{color:#56615B;font-size:18px;line-height:1;text-align:center;width:24px}'
       '.tb th{color:#4A5650 !important}')
SUB = {'CuentaPerfil': 'Tus datos de la cuenta global y lo que configuras en Agroolink.'}
SUB_C = 'Gestiona aquí tus planes, suscripciones, pedidos, facturas, métodos de pago y direcciones.'
SVG = lambda d, c='currentColor', s=20: '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="%s"/></svg>' % (s, s, c, d)
BLDG = 'M5 3h14v18H5zM9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2'
USER = 'M12 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM4 21a8 8 0 0 1 16 0'
CLOCK = 'M12 3a9 9 0 1 1-8.5 6M3 4v5h5M12 7v5l3 2'
GEAR = 'M12 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6zM12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1'

def rep(s, a, b, n=1):
    assert a in s, a[:70]
    return s.replace(a, b) if n == 0 else s.replace(a, b, n)

for f in FILES:
    p = P + f + '.dc.html'; s = open(p).read()
    if '.btns{' in s:
        continue
    s = s.replace('</style>', CSS + '\n</style>', 1)
    # subtítulo bajo el título
    h1 = re.search(r'<h1 style="margin: 0; font-size: 28px; font-weight: 600;">([^<]+)</h1>', s)
    s = s.replace(h1.group(0), h1.group(0) + '<p style="margin: 2px 0 0; font-size: 13.5px; color: #4A5650;">%s</p>' % SUB.get(f, SUB_C), 1)
    # banner cuenta global
    s = rep(s, 'background: #F1F3F6; border: 1px solid #E1E5EA;', 'background: #F4F7FB; border: 1px solid #E2E8F0;')
    s = rep(s, '<a href="#" style="white-space: nowrap; font-size: 13px;">Ir a mi cuenta global ↗</a>', '<a href="#" style="white-space: nowrap; font-size: 13px; font-weight: 600;">Ir a mi cuenta global ↗</a>')
    # enlaces «Ver…» con flecha
    s = re.sub(r'(<a href="#"[^>]*>)(Ver todo|Ver planes de empresa|Ver planes de experto)(</a>)', lambda m: m.group(1).replace('style="', 'style="font-weight: 600; ', 1) + m.group(2) + ARROW + m.group(3), s)
    if f == 'CuentaPlanes':
        s = rep(s, '<span class="k">Sin coste, sin tarjeta.</span>', '<span class="k">Sin coste, sin tarjeta.</span>\n          <a href="#" class="btns" style="margin-top: auto;">' + SVG(GEAR, s=17) + 'Gestionar plan</a>')
        s = rep(s, '<a href="#" class="btn" style="margin-top: auto;">Avísame cuando esté</a>', '<a href="#" class="btnp" style="margin-top: auto; height: 42px;">Avísame cuando esté disponible</a>')
        s = rep(s, '<section class="card" style="flex: 1; padding: 13px 16px; gap: 5px;">\n            <div class="hd"><h2 class="h2" style="font-size: 14.5px;">¿Vendes o distribuyes?</h2>',
                '<section class="card" style="flex: 1; padding: 13px 16px; gap: 5px; flex-direction: row; align-items: flex-start;"><span class="ico" style="background: #EEF6EE; color: #0E5A3A;">' + SVG(BLDG) + '</span><div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px; align-self: stretch;">\n            <div class="hd"><h2 class="h2" style="font-size: 14.5px;">¿Vendes o distribuyes?</h2>')
        s = rep(s, '<section class="card" style="flex: 1; padding: 13px 16px; gap: 5px;">\n            <div class="hd"><h2 class="h2" style="font-size: 14.5px;">¿Ofreces servicios?</h2>',
                '<section class="card" style="flex: 1; padding: 13px 16px; gap: 5px; flex-direction: row; align-items: flex-start; background: #FAF8FE; border-color: #E9E4F8;"><span class="ico" style="background: #F1EEFB; color: #4B3BA6;">' + SVG(USER) + '</span><div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px; align-self: stretch;">\n            <div class="hd"><h2 class="h2" style="font-size: 14.5px;">¿Ofreces servicios?</h2>')
        s = re.sub(r'(Ver planes de (?:empresa|experto)' + re.escape(ARROW) + r'</a>)\n          </section>', r'\1</div>\n          </section>', s)
        s = s.replace('font-size: 14.5px;">¿Vendes', 'font-size: 14.5px !important;">¿Vendes').replace('font-size: 14.5px;">¿Ofreces', 'font-size: 14.5px !important;">¿Ofreces')
        # suscripciones: cabecera Acciones + menú ⋮
        s = rep(s, '<th>Estado</th><th></th></tr>', '<th>Estado</th><th>Acciones</th><th></th></tr>')
        s = re.sub(r'(<td><a href="#"[^<]*</a>(?: · <a href="#"[^>]*>[^<]*</a>)?</td>)</tr>', r'\1<td class="kebab">⋮</td></tr>', s)
        s = rep(s, '<div class="hd"><h2 class="h2">Historial de cambios</h2></div>',
                '<div class="hd" style="align-items: center;"><span style="display: flex; align-items: center; gap: 12px;"><span class="ico" style="width: 36px; height: 36px; border-radius: 50%; background: #EEF6EE; color: #0E5A3A;">' + SVG(CLOCK, s=18) + '</span><h2 class="h2">Historial de cambios</h2></span><a href="#" class="btn" style="height: 34px; font-size: 12.5px;">Ver todo' + ARROW + '</a></div>')
    if f == 'CuentaPedidos':
        s = rep(s, '<th>Estado</th><th></th></tr>', '<th>Estado</th><th>Acciones</th></tr>')
    if f == 'CuentaFacturas':
        s = rep(s, '<th class="r">Total</th><th></th></tr>', '<th class="r">Total</th><th>PDF</th></tr>')
    open(p, 'w').write(s)
print('ok')
