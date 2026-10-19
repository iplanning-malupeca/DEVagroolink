"""Intranet de usuario (escritorio, Samuel · comprador Gratis): U11 Siguiendo, U12 Alertas, U13 Avisos.
Mismo armazón que U1–U10 (IntSidebar modo personal + IntHeader). Límites según data/planes.json (todos y comprador): seguir es gratis;
alertas 5 en Gratis; alertas de precio, stock y ficha con Comprador Pro (próximamente). Nunca contactos: todo va por Mensajes.
Uso: python3 tools/usuario_intranet.py <carpeta>/project   → escribe UsrSiguiendo, UsrAlertas, UsrAvisos"""
import os, sys
DEST = sys.argv[1].rstrip('/') + '/'
AZ = '#0E5A3A'
CSS = """body{margin:0;line-height:1.3;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#0E5A3A;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-sizing:border-box;min-width:0}
.h2{margin:0;font-size:16px;font-weight:600}
.hint{font-size:12px;color:#56615B}
.row{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13px}
.av{width:36px;height:36px;border-radius:50%;background:#EEF6EE;color:#0E5A3A;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none}
.st{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap}
.ok{background:#EEF6EE;color:#0E5A3A}.wn{background:#FFF4E0;color:#7A4B00}.gr{background:#F1F3F6;color:#4A5560}.az{background:#EEF6EE;color:#0E5A3A}.er{background:#FDECEA;color:#A3271B}
.chip{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 13px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12.5px;white-space:nowrap;color:#17231D}
.chip.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}
.btn{height:38px;padding:0 16px;border-radius:10px;border:1.5px solid #0E5A3A;color:#0E5A3A;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;box-sizing:border-box}
.btnp{height:38px;padding:0 16px;border-radius:10px;background:#0E5A3A;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.nota{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;background:#F2F7F3;border:1px solid #E1ECE4;font-size:12.5px;color:#33424C}
.pro{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:12.5px;color:#33424C}
.th{display:grid;gap:12px;padding:0 0 8px;font-size:11px;font-weight:600;letter-spacing:.04em;color:#56615B}
.tr{display:grid;gap:12px;align-items:center;padding:11px 0;border-top:1px solid #EEF1EE;font-size:13px}"""

def svg(d, s=16, w=1.9):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="%s"/></svg>' % (s, s, w, d)
I = {'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01', 'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4', 'mas': 'M12 5v14M5 12h14',
     'msg': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6', 'ok': 'M5 12l5 5 9-10', 'flecha': 'M5 12h14M13 6l6 6-6 6', 'x': 'M6 6l12 12M18 6 6 18'}

def pagina(titulo, activo, cab, cuerpo, h=1000, sub=''):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + titulo + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n'
            '<div style="width: 1280px; height: ' + str(h) + 'px; background: #F6F8F6; position: relative; overflow: hidden;">\n'
            '  <div style="display: flex; padding-top: 68px; height: ' + str(h) + 'px; box-sizing: border-box;">\n'
            '    <dc-import name="IntSidebar" modo="personal" activo="' + activo + '"' + (' sub="' + sub + '"' if sub else '') + ' alto="' + str(h - 68) + '" hint-size="256px,' + str(h - 68) + 'px"></dc-import>\n'
            '    <main style="flex: 1; min-width: 0; padding: 22px 28px; display: flex; flex-direction: column; gap: 16px;">' + cab + cuerpo + '</main>\n'
            '  </div>\n  <div style="position: absolute; top: 0; left: 0; width: 1280px;">\n'
            '    <dc-import name="IntHeader" persona="Samuel E." iniciales="SE" color="#0E5A3A" variante="personal" hint-size="1280px,68px"></dc-import>\n  </div>\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

def cabecera(miga, h1, sub, acciones=''):
    return ('<div style="display: flex; align-items: flex-end; gap: 16px;"><div style="flex: 1; min-width: 0;"><div style="font-size: 13px; color: #56615B;">Mi espacio › ' + miga + '</div>'
            '<h1 style="margin: 2px 0 0; font-size: 28px; font-weight: 600;">' + h1 + '</h1><p style="margin: 2px 0 0; font-size: 13.5px; color: #4A5650;">' + sub + '</p></div>' + acciones + '</div>')

I.update({'star': 'M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z', 'bell': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4',
          'pkg': 'M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8', 'doc': 'M6 3h9l4 4v14H6zM14 3v5h5', 'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z', 'file': 'M3 21V10l9-6 9 6v11M2 21h20M9 21v-6h6v6M9 11h6'})
def sw(on=True):
    return ('<span style="width: 36px; height: 20px; border-radius: 999px; background: ' + (AZ if on else '#C9D2CC') + '; position: relative; display: inline-block; flex: none;"><span style="position: absolute; top: 2px; ' + ('right' if on else 'left') + ': 2px; width: 16px; height: 16px; border-radius: 50%; background: #FFFFFF;"></span></span>')
def logo(ini, color):
    return '<span style="width: 40px; height: 40px; border-radius: 10px; background: ' + color + '; color: #FFFFFF; font-size: 12.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">' + ini + '</span>'

# ---------- U11 · Siguiendo ----------
def siguiendo():
    q = lambda ini, color, n, d, tipo, aviso=True, borde=True: ('<div class="row"' + ('' if borde else ' style="border-top: 0;"') + '>' + logo(ini, color) +
                                                              '<span style="flex: 1; min-width: 0;"><strong style="font-weight: 600;">' + n + '</strong> <span class="st gr" style="margin-left: 4px;">' + tipo + '</span><br><span class="hint">' + d + '</span></span>'
                                                              '<span class="hint" style="display: flex; align-items: center; gap: 8px;">Avisarme ' + sw(aviso) + '</span><a href="#" style="font-size: 12.5px; margin-left: 10px; white-space: nowrap;">Dejar de seguir</a></div>')
    lista = ('<section class="card" style="flex: 1; min-width: 0; gap: 0;"><h2 class="h2" style="padding-bottom: 6px;">Sigues a 6</h2>' +
             q('DSM', '#1D4E89', 'DSM-Firmenich', 'Nutrición · Enzimas, vitaminas · 48 productos', 'Fabricante', True, False) +
             q('ZU', '#2E6FB7', 'Zucami', 'Equipos de alimentación y bebederos · 31 productos', 'Fabricante') +
             q('BD', '#B23A2E', 'Big Dutchman Ibérica', 'Naves y equipamiento avícola · 64 productos', 'Fabricante') +
             q('AS', '#2E8B57', 'Agropecuària del Segre', 'Distribuidor en tu zona · Lleida', 'Distribuidor', False) +
             q('NF', '#6B7A2E', 'NewFarms', 'Bioseguridad y desinfección · 12 productos', 'Fabricante', False) +
             q('LG', '#4B3BA6', 'Laura Gil', 'Nutrición avícola · Huesca', 'Experta') + '</section>')
    nov = lambda ic, t, d, cuando: ('<div class="row" style="align-items: flex-start;"><span style="width: 32px; height: 32px; border-radius: 9px; background: #EEF6EE; color: ' + AZ + '; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I[ic], 16) + '</span>'
                                    '<span style="flex: 1; min-width: 0;"><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + d + '</span></span><span class="hint">' + cuando + '</span></div>')
    feed = ('<section class="card" style="width: 340px; flex: none; gap: 0;"><h2 class="h2" style="padding-bottom: 6px;">Novedades de quien sigues</h2>' +
            nov('pkg', 'DSM-Firmenich publicó Ronozyme® HiPhos GT', 'Producto nuevo · Enzimas · Avicultura', '2 h').replace('class="row"', 'class="row" style="border-top: 0;"', 1).replace('style="border-top: 0;" style="align-items: flex-start;"', 'style="border-top: 0; align-items: flex-start;"') +
            nov('doc', 'Laura Gil publicó «Cómo bajar el índice de conversión»', 'Contenido · 6 min de lectura', 'ayer') +
            nov('pkg', 'Zucami actualizó la ficha del bebedero Optima', 'Nueva ficha técnica para descargar', '2 d') +
            nov('file', 'Big Dutchman Ibérica: nuevo distribuidor en Aragón', 'Ya puedes pedirle información desde la ficha', '4 d') +
            '<a href="#" style="font-size: 12.5px; padding-top: 10px;">Ver todas en Avisos →</a></section>')
    cab = cabecera('Siguiendo', 'Siguiendo', 'Empresas y expertos que sigues. Te avisamos de sus productos, fichas y contenidos nuevos.',
                   '<span style="display: flex; gap: 6px;"><span class="chip on">Todos 6</span><span class="chip">Empresas 5</span><span class="chip">Expertos 1</span></span>')
    cuerpo = ('<div style="display: flex; gap: 16px; align-items: flex-start;">' + lista + feed + '</div>'
              '<div class="nota">' + svg(I['info'], 16) + '<span>Seguir es gratis y sin límite. Para hablar con una empresa o una experta, escríbele por Mensajes desde su ficha: Agroolink no muestra teléfonos, emails ni webs.</span></div>')
    return pagina('Intranet usuario · Siguiendo', 'Siguiendo y alertas', cab, cuerpo, sub='Siguiendo')

# ---------- U12 · Alertas ----------
def alertas():
    cols = 'grid-template-columns: minmax(0,1.2fr) minmax(0,1.4fr) 84px 104px 40px;'
    f = lambda t, que, freq, ult, on=True: ('<div class="tr" style="' + cols + '"><span><strong style="font-weight: 600;">' + t + '</strong></span><span style="font-size: 12.5px;">' + que + '</span>'
                                          '<span class="hint" style="font-size: 12.5px;">' + freq + '</span><span class="hint" style="font-size: 12.5px;">' + ult + '</span>' + sw(on) + '</div>')
    tabla = ('<section class="card" style="flex: 1; min-width: 0; padding-top: 14px;"><div class="th" style="' + cols + '"><span>QUÉ BUSCAS</span><span>TE AVISAMOS DE</span><span>CADA CUÁNTO</span><span>ÚLTIMO AVISO</span><span>ACTIVA</span></div>' +
             f('Enzimas · Avicultura › Broilers', 'Productos nuevos', 'Al momento', 'Hoy · 3 nuevos') +
             f('Bebederos · Avicultura', 'Productos nuevos y proveedores en tu zona', 'Semanal', 'Lunes · 1 nuevo') +
             f('Coccidiosis · Broilers', 'Productos y contenidos nuevos', 'Diario', 'Ayer · 2 nuevos') +
             f('Expertos en nutrición · Aragón', 'Expertos nuevos', 'Semanal', 'Sin novedades', False) +
             '<div class="tr" style="' + cols + ' color: #8A948F;"><span>Te queda 1 alerta</span><span></span><span></span><span></span><span></span></div></section>')
    campo = lambda l, v: '<span style="display: flex; flex-direction: column; gap: 4px;"><span style="font-size: 12px; font-weight: 600;">' + l + '</span><span style="height: 38px; border: 1px solid #D5DED8; border-radius: 10px; padding: 0 12px; font-size: 13px; display: flex; align-items: center;">' + v + '</span></span>'
    nueva = ('<aside class="card" style="width: 290px; flex: none; gap: 10px;"><h2 class="h2">Nueva alerta</h2>'
             '<span class="hint">Parte de tu búsqueda: especie, categoría o enfermedad.</span>'
             '<span style="display: flex; gap: 6px; flex-wrap: wrap;"><span class="chip on">Porcino › Cebo</span><span class="chip on">Acidificantes</span></span>' +
             campo('Te avisamos de', 'Productos nuevos ▾') + campo('Cada cuánto', 'Semanal ▾') +
             '<span style="display: flex; justify-content: space-between; align-items: center; font-size: 13px;">En Avisos ' + sw(True) + '</span>'
             '<span style="display: flex; justify-content: space-between; align-items: center; font-size: 13px;">También por email ' + sw(True) + '</span>'
             '<a href="#" class="btnp">Crear alerta</a><span class="hint">4 de 5 alertas usadas en Gratis.</span></aside>')
    pro = ('<div class="pro">' + svg(I['lock'], 16) + '<span style="flex: 1;"><strong>Alertas de precio, stock y cambios de ficha</strong> de un producto concreto, y alertas sin límite: con Comprador Pro · 9,90 €/mes, próximamente.</span><a href="#" class="btn" style="height: 34px;">Avisarme cuando salga</a></div>')
    cab = cabecera('Siguiendo y alertas › Alertas', 'Alertas', 'Te avisamos cuando aparece algo nuevo que encaja con lo que buscas.', '<span class="st ok" style="font-size: 12px;">4 de 5 · Gratis</span>')
    cuerpo = '<div style="display: flex; gap: 16px; align-items: flex-start;">' + tabla + nueva + '</div>' + pro
    return pagina('Intranet usuario · Alertas', 'Siguiendo y alertas', cab, cuerpo, sub='Alertas')

# ---------- U13 · Avisos ----------
def avisos():
    av = lambda ic, t, d, cuando, nuevo=False, borde=True: ('<div class="row" style="align-items: flex-start;' + ('' if borde else ' border-top: 0;') + (' background: #F2F7F3; margin: 0 -12px; padding: 10px 12px; border-radius: 10px;' if nuevo else '') + '">'
                                                          '<span style="width: 34px; height: 34px; border-radius: 9px; background: ' + ('#FFFFFF' if nuevo else '#EEF6EE') + '; color: ' + AZ + '; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I[ic], 17) + '</span>'
                                                          '<span style="flex: 1; min-width: 0;"><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + d + '</span></span><span class="hint">' + cuando + '</span>' +
                                                          ('<span style="width: 8px; height: 8px; border-radius: 50%; background: #D93A3A; margin-top: 6px;"></span>' if nuevo else '') + '</div>')
    k = '<span class="hint" style="font-weight: 600; letter-spacing: .05em; padding: 12px 0 4px;">%s</span>'
    lista = ('<section class="card" style="flex: 1; min-width: 0; gap: 0;"><span class="hint" style="font-weight: 600; letter-spacing: .05em; padding-bottom: 4px;">HOY</span>' +
             av('msg', 'Agropecuària del Segre te ha respondido', 'Mensajes · «Corrector vitamínico CV-20: precio y plazo»', '10:42', True, False) +
             av('file', 'Nueva propuesta para «Sistema de alimentación · Nave 2»', 'Mis proyectos · Zucami · 3 propuestas en total', '09:15', True) +
             av('bell', '3 productos nuevos en «Enzimas · Avicultura › Broilers»', 'Alertas · DSM-Firmenich, Adisseo, Novus', '08:00', True) +
             k % 'AYER' +
             av('star', 'Laura Gil publicó «Cómo bajar el índice de conversión»', 'Siguiendo · contenido', '18:30', False, False) +
             av('grid', 'Marta te ha invitado al tablero «Nave 2 · bebederos»', 'Mis tableros · puedes ver y comentar', '12:04') +
             k % 'ESTA SEMANA' +
             av('pkg', 'Zucami actualizó la ficha del bebedero Optima', 'Siguiendo · nueva ficha técnica', 'lun', False, False) +
             av('info', 'Tu email está verificado', 'Cuenta · ya puedes enviar solicitudes', 'lun') + '</section>')
    pref = lambda t, a, e: '<div class="row"><span style="flex: 1;">' + t + '</span><span style="width: 66px; display: flex; justify-content: center;">' + sw(a) + '</span><span style="width: 56px; display: flex; justify-content: center;">' + sw(e) + '</span></div>'
    prefs = ('<aside class="card" style="width: 360px; flex: none; gap: 0;"><h2 class="h2" style="padding-bottom: 8px;">Qué te avisamos y dónde</h2>'
             '<div class="row" style="border-top: 0; font-size: 11px; font-weight: 600; letter-spacing: .04em; color: #56615B;"><span style="flex: 1;">AVISO</span><span style="width: 66px; text-align: center;">AQUÍ</span><span style="width: 56px; text-align: center;">EMAIL</span></div>' +
             pref('Mensajes nuevos', True, True) + pref('Propuestas a tus proyectos', True, True) + pref('Alertas', True, True) + pref('Novedades de quien sigues', True, False) + pref('Tableros compartidos', True, False) +
             '<div class="row"><span style="flex: 1;">Resumen por email</span><span class="chip" style="height: 30px;">Diario ▾</span></div>'
             '<span class="hint" style="padding-top: 10px;">Los emails de la cuenta (verificación, seguridad, facturas) se envían siempre.</span></aside>')
    cab = cabecera('Avisos', 'Avisos', 'Todo lo que ha pasado en tu cuenta, en un solo sitio.',
                   '<a href="#" style="font-size: 13px;">Marcar todo como leído</a>')
    cuerpo = ('<div style="display: flex; gap: 8px;"><span class="chip on">Todo</span><span class="chip">Sin leer 3</span><span class="chip">Mensajes</span><span class="chip">Proyectos</span><span class="chip">Alertas</span><span class="chip">Siguiendo</span><span class="chip">Tableros</span><span class="chip">Cuenta</span></div>'
              '<div style="display: flex; gap: 16px; align-items: flex-start;">' + lista + prefs + '</div>')
    return pagina('Intranet usuario · Avisos', '', cab, cuerpo)

PANT = [('UsrSiguiendo', 'U11 · Siguiendo: empresas y expertos que sigues y sus novedades', siguiendo),
        ('UsrAlertas', 'U12 · Alertas: 5 en Gratis; precio, stock y ficha con Comprador Pro (próximamente)', alertas),
        ('UsrAvisos', 'U13 · Avisos: la campana, todo lo que ha pasado y qué te avisamos por email', avisos)]
if __name__ == '__main__':
    for k, t, f in PANT:
        open(DEST + k + '.dc.html', 'w').write(f())
    print('ok', len(PANT))
