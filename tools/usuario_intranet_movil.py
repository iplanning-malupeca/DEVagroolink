"""Intranet de usuario en móvil (versión de U11–U13): siguiendo, alertas y avisos, una pantalla por tablero, para «Agroolink · Móvil».
Va en la fila de usuario de «004_MB_Intranet» detrás de MB_UsrFactDirecciones. Las imágenes se reescriben con tools/blobs_movil.json.
Uso: python3 tools/usuario_intranet_movil.py <carpeta-movil>/project/canvas.json [clave=alto …]"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import svg, I, wrap, W, DEST, VE
from usuario_movil import pagina, card, fila, ico, chips, sw, nota, btn, ST

I.update({'star': 'M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z', 'bell': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4', 'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4',
          'pkg': 'M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8', 'doc': 'M6 3h9l4 4v14H6zM14 3v5h5', 'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z',
          'file': 'M3 21V10l9-6 9 6v11M2 21h20M9 21v-6h6v6M9 11h6', 'msg': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6'})
def logo(ini, color):
    return '<span style="width:36px;height:36px;border-radius:10px;background:' + color + ';color:#FFFFFF;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:none">' + ini + '</span>'
def pro(t):
    return '<div style="padding:10px 12px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:12.5px;color:#33424C;display:flex;gap:8px"><span style="flex:none">' + svg(I['lock'], 16) + '</span><span>' + t + '</span></div>'

def siguiendo():
    q = lambda ini, color, n, d, on=True, borde=True: fila(logo(ini, color), n, d, sw(on), borde)
    b = (chips(['Todos 6', 'Empresas 5', 'Expertos 1']) +
         card('Novedades', fila(ico('pkg'), 'DSM-Firmenich publicó Ronozyme® HiPhos GT', 'Producto nuevo · hace 2 h', '', False) +
              fila(ico('doc'), 'Laura Gil publicó «Cómo bajar el índice de conversión»', 'Contenido · ayer') +
              fila(ico('pkg'), 'Zucami actualizó la ficha del bebedero Optima', 'Nueva ficha técnica · 2 d'), 'Ver en Avisos') +
         card('Sigues a 6 · avisarme', q('DSM', '#1D4E89', 'DSM-Firmenich', 'Fabricante · 48 productos', True, False) + q('ZU', '#2E6FB7', 'Zucami', 'Fabricante · 31 productos') +
              q('BD', '#B23A2E', 'Big Dutchman Ibérica', 'Fabricante · 64 productos') + q('AS', '#2E8B57', 'Agropecuària del Segre', 'Distribuidor en tu zona', False) +
              q('NF', '#6B7A2E', 'NewFarms', 'Fabricante · 12 productos', False) + q('LG', '#4B3BA6', 'Laura Gil', 'Experta · Nutrición avícola')) +
         nota('Seguir es gratis y sin límite. Para hablar con una empresa o una experta, escríbele por Mensajes: Agroolink no muestra teléfonos, emails ni webs.'))
    return pagina('Siguiendo', '', b, 'Tú', ('Siguiendo', 'Empresas y expertos'))

def alertas():
    a = lambda t, d, on=True, borde=True: fila(ico('bell'), t, d, sw(on), borde)
    b = ('<div style="display:flex;align-items:center;justify-content:space-between">' + ST('4 de 5 · Gratis') + btn('+ Nueva alerta', True) + '</div>' +
         card('', a('Enzimas · Avicultura › Broilers', 'Productos nuevos · al momento · hoy 3 nuevos', True, False) +
              a('Bebederos · Avicultura', 'Productos y proveedores en tu zona · semanal') +
              a('Coccidiosis · Broilers', 'Productos y contenidos · diario · ayer 2 nuevos') +
              a('Expertos en nutrición · Aragón', 'Expertos nuevos · semanal', False)) +
         card('Nueva alerta', '<div style="display:flex;gap:6px;flex-wrap:wrap"><span class="chip" style="background:' + VE + ';border-color:' + VE + ';color:#FFFFFF">Porcino › Cebo</span><span class="chip" style="background:' + VE + ';border-color:' + VE + ';color:#FFFFFF">Acidificantes</span></div>' +
              fila('', 'Te avisamos de', 'Productos nuevos', '', False) + fila('', 'Cada cuánto', 'Semanal') + fila('', 'También por email', 'Además de en Avisos', sw(True)) + btn('Crear alerta', True, True)) +
         pro('<strong>Precio, stock y cambios de ficha</strong> de un producto, y alertas sin límite: Comprador Pro · 9,90 €/mes, próximamente.'))
    return pagina('Alertas', '', b, 'Tú', ('Alertas', 'Te avisamos de lo nuevo'))

def avisos():
    n = lambda ic, t, d, nuevo=False, borde=True: fila(ico(ic), t, d, '<span style="width:8px;height:8px;border-radius:50%;background:#D93A3A;flex:none"></span>' if nuevo else '', borde)
    k = lambda t: '<span class="hint" style="font-weight:600;letter-spacing:.04em">' + t + '</span>'
    b = ('<div style="display:flex;align-items:center;justify-content:space-between">' + chips(['Todo', 'Sin leer 3']) + '<span style="font-size:12.5px;color:' + VE + ';font-weight:600;white-space:nowrap">Marcar leído</span></div>' +
         card('', k('HOY') + n('msg', 'Agropecuària del Segre te ha respondido', 'Mensajes · 10:42', True) + n('file', 'Nueva propuesta para «Nave 2»', 'Mis proyectos · Zucami · 09:15', True) +
              n('bell', '3 productos nuevos en «Enzimas · Broilers»', 'Alertas · 08:00', True)) +
         card('', k('AYER') + n('star', 'Laura Gil publicó un contenido', 'Siguiendo · 18:30') + n('grid', 'Marta te invitó al tablero «Nave 2 · bebederos»', 'Mis tableros · 12:04')) +
         card('Qué te avisamos por email', fila('', 'Mensajes y propuestas', 'Al momento', sw(True), False) + fila('', 'Alertas', 'Según cada alerta', sw(True)) +
              fila('', 'Novedades de quien sigues', 'Solo aquí', sw(False)) + fila('', 'Resumen por email', 'Diario', '')) +
         nota('Los emails de la cuenta (verificación, seguridad, facturas) se envían siempre.'))
    return pagina('Avisos', '', b, 'Tú', ('Avisos', '3 sin leer'))

PANT = [('MB_UsrSiguiendo', 'U11 · Siguiendo', siguiendo), ('MB_UsrAlertas', 'U12 · Alertas', alertas), ('MB_UsrAvisos', 'U13 · Avisos', avisos)]
ALTOS = {'MB_UsrSiguiendo': 1080, 'MB_UsrAlertas': 1010, 'MB_UsrAvisos': 1110}   # medidas en el navegador
if __name__ == '__main__':
    alto = dict(ALTOS, **{k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    BLOBS = json.load(open(W + '/tools/blobs_movil.json'))
    c = json.load(open(sys.argv[1])); B = c['boards']
    ref = B['MB_UsrFactDirecciones.dc.html']; x0 = ref['x'] + 470
    for i, (k, t, f) in enumerate(PANT):
        h = int(alto.get(k, 1100))
        html = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '/_blob/' + BLOBS.get(m.group(1), m.group(1)), wrap('Móvil · ' + t, h, f()))
        open(DEST + k + '.dc.html', 'w').write(html)
        B[k + '.dc.html'] = {'w': 390, 'h': h, 'page': ref['page'], 'x': x0 + i * 470, 'y': ref['y'], 'title': t}
        if k + '.dc.html' not in c['order']: c['order'].append(k + '.dc.html')
    json.dump(c, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    print('ok', len(PANT), ref['page'], ref['y'])
