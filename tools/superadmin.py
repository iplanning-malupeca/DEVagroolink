"""Superadmin (escritorio): SA1 Panel, SA2 Moderación de contactos, SA3 Cuenta en pausa, SA4 Archivos revisados, SA5 Altas y CRM.
Reglas de data/planes.json: un texto, archivo o imagen con un contacto (también disimulado) no se envía ni se publica; cada intento
queda registrado; al tercero en 30 días se pausan los envíos y lo revisa el superadmin. Archivos: texto, OCR, QR, enlaces y metadatos;
los metadatos se eliminan siempre. Los contactos detectados se ven enmascarados, nunca completos.
Uso: python3 tools/superadmin.py <carpeta>/project   → escribe SA*.dc.html"""
import os, sys
DEST = sys.argv[1].rstrip('/') + '/'
SA, AZ = '#2B2257', '#1D4E89'
LOGO = '<img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height: 26px; width: auto; display: block;">'
CSS = """body{margin:0;line-height:1.3;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#2B2257;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-sizing:border-box;min-width:0}
.h2{margin:0;font-size:16px;font-weight:600}
.hint{font-size:12px;color:#56615B}
.st{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap}
.ok{background:#EEF6EE;color:#0E5A3A}.wn{background:#FFF4E0;color:#7A4B00}.gr{background:#F1F3F6;color:#4A5560}.er{background:#FDECEA;color:#A3271B}.sa{background:#ECE9F7;color:#2B2257}.az{background:#E9F0F9;color:#1D4E89}
.chip{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 13px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12.5px;white-space:nowrap}
.chip.on{background:#2B2257;border-color:#2B2257;color:#FFFFFF}
.btn{height:36px;padding:0 14px;border-radius:10px;border:1.5px solid #2B2257;color:#2B2257;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;box-sizing:border-box}
.btnp{height:36px;padding:0 14px;border-radius:10px;background:#2B2257;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.btnr{height:36px;padding:0 14px;border-radius:10px;border:1.5px solid #A3271B;color:#A3271B;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;white-space:nowrap;box-sizing:border-box}
.th{display:grid;gap:12px;padding:0 0 8px;font-size:11px;font-weight:600;letter-spacing:.04em;color:#56615B}
.tr{display:grid;gap:12px;align-items:center;padding:11px 0;border-top:1px solid #EEF1EE;font-size:13px}
.mask{background:#FDECEA;color:#A3271B;border-radius:5px;padding:1px 5px;font-weight:600;white-space:nowrap}
.nota{display:flex;gap:10px;align-items:flex-start;padding:10px 14px;border-radius:12px;background:#F4F3FA;border:1px solid #E1DDF1;font-size:12.5px;color:#33424C}
.ni{display:flex;align-items:center;gap:12px;height:40px;padding:0 12px;border-radius:10px;font-size:14px;color:#D9D6EC}"""

def svg(d, s=16, w=1.9):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="%s"/></svg>' % (s, s, w, d)
I = {'panel': 'M3 3h8v10H3zM13 3h8v6h-8zM13 11h8v10h-8zM3 15h8v6H3z', 'escudo': 'M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z', 'pausa': 'M8 5v14M16 5v14',
     'doc': 'M6 3h9l4 4v14H6zM14 3v5h5', 'crm': 'M5 3h14v18H5zM9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2', 'org': 'M9 4.5a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zM2 20a7 7 0 0 1 14 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a7 7 0 0 1 4 6',
     'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01', 'ok': 'M5 12l5 5 9-10', 'x': 'M6 6l12 12M18 6 6 18', 'hist': 'M3 12a9 9 0 1 0 3-6.7L3 8M3 3v5h5M12 7v5l3 2'}
MENU = [('Panel', 'panel', ''), ('Moderación', 'escudo', '7'), ('En pausa', 'pausa', '1'), ('Archivos', 'doc', '3'), ('Altas y CRM', 'crm', '5'), ('Organizaciones', 'org', '')]

def pagina(titulo, activo, cab, cuerpo, h=900):
    menu = ''.join('<span class="ni" style="' + ('background: rgba(255,255,255,.12); color: #FFFFFF; font-weight: 600;' if t == activo else '') + '">' + svg(I[ic], 19) + '<span style="flex: 1;">' + t + '</span>' +
                   ('<span style="min-width: 22px; height: 22px; border-radius: 999px; background: #F2B530; color: #17231D; font-size: 11.5px; font-weight: 700; display: flex; align-items: center; justify-content: center; padding: 0 6px; box-sizing: border-box;">' + b + '</span>' if b else '') + '</span>' for t, ic, b in MENU)
    lateral = ('<nav aria-label="Menú del superadmin" style="width: 240px; flex: none; background: ' + SA + '; padding: 20px 14px; box-sizing: border-box; display: flex; flex-direction: column; gap: 2px;">'
               '<span style="font-size: 11.5px; font-weight: 600; letter-spacing: .08em; color: #B9B3DD; padding: 0 12px 10px;">SUPERADMIN</span>' + menu +
               '<span style="flex: 1;"></span><span style="font-size: 11.5px; color: #B9B3DD; padding: 0 12px; line-height: 1.4;">Cada decisión queda registrada con fecha y autor.</span></nav>')
    top = ('<header style="height: 60px; background: #FFFFFF; border-bottom: 1px solid #E3E8E4; display: flex; align-items: center; gap: 12px; padding: 0 24px;">' + LOGO +
           '<span class="st sa" style="font-size: 11.5px;">Superadmin</span><span style="flex: 1;"></span><span class="hint">Lucía Pérez · equipo de Agroolink</span>'
           '<span style="width: 34px; height: 34px; border-radius: 50%; background: ' + SA + '; color: #FFFFFF; font-size: 12px; font-weight: 600; display: flex; align-items: center; justify-content: center;">LP</span></header>')
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + titulo + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n'
            '<div style="width: 1280px; height: ' + str(h) + 'px; background: #F6F6F9; display: flex; flex-direction: column; overflow: hidden;">' + top +
            '<div style="flex: 1; display: flex; min-height: 0;">' + lateral + '<main style="flex: 1; min-width: 0; padding: 22px 28px; display: flex; flex-direction: column; gap: 16px;">' + cab + cuerpo + '</main></div></div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

def cabecera(h1, sub, acciones=''):
    return ('<div style="display: flex; align-items: flex-end; gap: 16px;"><div style="flex: 1; min-width: 0;"><h1 style="margin: 0; font-size: 27px; font-weight: 600;">' + h1 + '</h1>'
            '<p style="margin: 2px 0 0; font-size: 13.5px; color: #4A5650;">' + sub + '</p></div>' + acciones + '</div>')

# ---------- SA1 · Panel ----------
def panel():
    kpi = lambda n, t, link, estilo='sa': ('<div class="card" style="gap: 2px; padding: 14px 16px;"><span style="font-size: 26px; font-weight: 600;">' + n + '</span><span style="font-size: 12.5px; color: #4A5650;">' + t + '</span>'
                                          '<a href="#" style="font-size: 12.5px; margin-top: 4px;">' + link + ' →</a></div>')
    item = lambda st_, cls, t, d, cuando, borde=True: ('<div class="tr" style="grid-template-columns: 120px minmax(0,1fr) 90px;' + ('' if borde else ' border-top: 0;') + '"><span><span class="st ' + cls + '">' + st_ + '</span></span>'
                                                       '<span><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + d + '</span></span><span class="hint">' + cuando + '</span></div>')
    cuerpo = ('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px;">' + kpi('7', 'Contenidos bloqueados por revisar', 'Moderación') + kpi('1', 'Cuenta con envíos en pausa', 'Cuentas en pausa') +
              kpi('3', 'Archivos rechazados hoy', 'Archivos') + kpi('5', 'Altas y cambios del CRM', 'Altas y CRM') + '</div>'
              '<div style="display: flex; gap: 16px;"><section class="card" style="flex: 1;"><h2 class="h2">Lo urgente</h2>' +
              item('En pausa', 'er', 'Nutrivet Catalunya · 3.er intento en 30 días', 'Envíos pausados hasta tu revisión', 'hace 1 h', False) +
              item('Por revisar', 'wn', 'Propuesta de Piensos del Sur', 'Teléfono escrito en letras', 'hace 2 h') +
              item('Alta', 'az', 'Lucía Pérez se unió a Big Dutchman Ibérica', 'Dominio @bigdutchman.es · verificado', 'hace 3 h') +
              item('CRM', 'sa', 'Zucami pide cambiar su sociedad en Portugal', 'Datos fiscales · solo superadmin', 'ayer') + '</section>'
              '<section class="card" style="width: 340px; flex: none;"><h2 class="h2">El filtro, últimos 30 días</h2>'
              '<div class="tr" style="grid-template-columns: 1fr auto; border-top: 0;"><span>Envíos bloqueados</span><strong>48</strong></div>'
              '<div class="tr" style="grid-template-columns: 1fr auto;"><span>Corregidos por el autor</span><strong>41</strong></div>'
              '<div class="tr" style="grid-template-columns: 1fr auto;"><span>Falsos positivos liberados</span><strong>3</strong></div>'
              '<div class="tr" style="grid-template-columns: 1fr auto;"><span>Cuentas pausadas</span><strong>2</strong></div>'
              '<span class="hint">Lo más frecuente: teléfonos en letras y «arroba» en lugar de @.</span></section></div>'
              '<div class="nota">' + svg(I['info'], 16) + '<span>Los contactos detectados se ven enmascarados también aquí. El superadmin decide sobre el envío, no lee datos de contacto.</span></div>')
    return pagina('Superadmin · Panel', 'Panel', cabecera('Panel', 'Lo que espera una decisión del equipo de Agroolink.'), cuerpo, 760)

# ---------- SA2 · Moderación ----------
def moderacion():
    cols = 'grid-template-columns: minmax(0,1.2fr) minmax(0,1.1fr) minmax(0,1.5fr) 90px 92px;'
    fila = lambda quien, rol, donde, detectado, intentos, est, cls, on=False: (
        '<div class="tr" style="' + cols + (' background: #F4F3FA; margin: 0 -12px; padding: 11px 12px; border-radius: 10px; border-top-color: transparent;' if on else '') + '"><span><strong style="font-weight: 600;">' + quien + '</strong><br><span class="hint">' + rol + '</span></span>'
        '<span>' + donde + '</span><span>' + detectado + '</span><span>' + intentos + '</span><span><span class="st ' + cls + '">' + est + '</span></span></div>')
    tabla = ('<section class="card" style="flex: 1; min-width: 0; padding-top: 14px;"><div class="th" style="' + cols + '"><span>AUTOR</span><span>DÓNDE</span><span>QUÉ SE DETECTÓ</span><span>INTENTOS</span><span>ESTADO</span></div>' +
             fila('Piensos del Sur', 'Distribuidor · Sevilla', 'Propuesta a un proyecto', 'Teléfono en letras <span class="mask">seis •••</span>', '2 de 3', 'Por revisar', 'wn', True) +
             fila('Nutrivet Catalunya', 'Distribuidor · Lleida', 'Mensaje a un comprador', 'Email con «arroba» <span class="mask">••• arroba •••</span>', '3 de 3', 'En pausa', 'er') +
             fila('Granja El Pinar', 'Comprador · Huesca', 'Descripción de un proyecto', 'Web <span class="mask">www.•••</span>', '1 de 3', 'Corregido', 'ok') +
             fila('Laura Gil', 'Experta · Huesca', 'Descripción de un servicio', '@usuario de red social <span class="mask">@•••</span>', '1 de 3', 'Corregido', 'ok') +
             fila('AgroVet Ibérica', 'Distribuidor · Zaragoza', 'Imagen de una ficha', 'Código QR', '1 de 3', 'Por revisar', 'wn') +
             '<span class="hint" style="padding-top: 8px;">Cuando el autor quita el dato, el contenido se envía solo y el caso pasa a «Corregido».</span></section>')
    detalle = ('<aside class="card" style="width: 340px; flex: none; gap: 12px;"><span style="display: flex; justify-content: space-between; align-items: center;"><span class="st wn">Por revisar</span><span class="hint">hace 2 h</span></span>'
               '<strong style="font-size: 15px;">Propuesta de Piensos del Sur</strong><span class="hint">Para el proyecto «Sistema de alimentación · Nave 2» (Lleida)</span>'
               '<div style="padding: 10px 12px; border-radius: 12px; background: #F6F6F9; font-size: 13px; line-height: 1.45;">«…podemos instalarlo en 3 semanas. Para cerrar detalles llamadme al <span class="mask">seis ••• ••• •••</span> y lo vemos.»</div>'
               '<div class="tr" style="grid-template-columns: 1fr auto; border-top: 0; padding: 0;"><span class="hint">Detectado</span><strong style="font-weight: 500;">Teléfono escrito en letras</strong></div>'
               '<div class="tr" style="grid-template-columns: 1fr auto; padding: 6px 0 0;"><span class="hint">Intentos en 30 días</span><strong style="font-weight: 500;">2 de 3</strong></div>'
               '<span class="hint">El autor ya ve el aviso y los datos marcados. Si es un error del filtro, libéralo; si no, el envío sigue bloqueado hasta que lo corrija.</span>'
               '<div style="display: flex; gap: 8px;"><a href="#" class="btnp" style="flex: 1;">Mantener bloqueo</a><a href="#" class="btn">Falso positivo</a></div>'
               '<a href="#" style="font-size: 12.5px;">Ver historial de la cuenta →</a></aside>')
    cab = cabecera('Moderación de contactos', 'Textos, mensajes e imágenes que no se enviaron porque llevaban un teléfono, email, web, @usuario, WhatsApp, Telegram o QR.')
    cuerpo = ('<div style="display: flex; gap: 8px; flex-wrap: wrap;"><span class="chip on">Por revisar 2</span><span class="chip">En pausa 1</span><span class="chip">Corregidos 41</span><span class="chip">Falsos positivos 3</span>'
              '<span style="flex: 1;"></span><span class="chip">Tipo de dato ▾</span><span class="chip">Dónde ▾</span></div>'
              '<div style="display: flex; gap: 16px; align-items: flex-start;">' + tabla + detalle + '</div>')
    return pagina('Superadmin · Moderación de contactos', 'Moderación', cab, cuerpo, 820)

# ---------- SA3 · Cuenta en pausa ----------
def pausa():
    hito = lambda cuando, t, d, cls, est: ('<div style="display: flex; gap: 12px; padding: 10px 0; border-top: 1px solid #EEF1EE;"><span class="hint" style="width: 80px; flex: none;">' + cuando + '</span>'
                                           '<span style="flex: 1;"><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + d + '</span></span><span><span class="st ' + cls + '">' + est + '</span></span></div>')
    historial = ('<section class="card" style="flex: 1; min-width: 0; gap: 0;"><h2 class="h2" style="padding-bottom: 8px;">Intentos en los últimos 30 días</h2>' +
                 hito('2 oct', 'Mensaje a un comprador de Lleida', 'Teléfono en letras <span class="mask">seis •••</span> · lo corrigió en 4 min', 'ok', 'Corregido') +
                 hito('11 oct', 'Ficha de un producto', 'Web en la descripción <span class="mask">www.•••</span> · lo corrigió al día siguiente', 'ok', 'Corregido') +
                 hito('Hoy 09:40', 'Mensaje a un comprador de Tarragona', 'Email con «arroba» <span class="mask">••• arroba •••</span> · 3.er intento', 'er', 'Pausa') +
                 '<span class="hint" style="padding-top: 10px;">Desde la pausa, la empresa ve sus conversaciones pero no puede enviar mensajes, propuestas ni publicar hasta tu decisión.</span></section>')
    decide = ('<aside class="card" style="width: 360px; flex: none; gap: 12px;"><span class="st er" style="align-self: flex-start;">Envíos en pausa · desde hoy 09:40</span>'
              '<span style="display: flex; gap: 10px; align-items: center;"><span style="width: 42px; height: 42px; border-radius: 10px; background: #2E8B57; color: #FFFFFF; font-weight: 700; display: flex; align-items: center; justify-content: center;">NC</span>'
              '<span><strong style="font-size: 15px;">Nutrivet Catalunya</strong><br><span class="hint">Distribuidor · Lleida · Plan Gratis · 3 personas</span></span></span>'
              '<span style="font-size: 12.5px; font-weight: 600;">¿Qué haces?</span>' +
              ''.join('<label style="display: flex; gap: 10px; align-items: flex-start; padding: 10px 12px; border-radius: 12px; border: ' + ('1.5px solid ' + SA + '; background: #F4F3FA' if on else '1px solid #E3E8E4') + '; font-size: 13px;">'
                      '<span style="width: 16px; height: 16px; border-radius: 50%; border: 1.5px solid ' + (SA if on else '#B9C6BE') + '; flex: none; margin-top: 2px; display: flex; align-items: center; justify-content: center;">' + ('<span style="width: 8px; height: 8px; border-radius: 50%; background: ' + SA + ';"></span>' if on else '') + '</span>'
                      '<span><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + d + '</span></span></label>' for t, d, on in
                      [('Reactivar con aviso', 'Vuelve a enviar; recibe un aviso con la norma. El contador sigue.', True), ('Mantener la pausa 7 días', 'Puede leer, no enviar. Se reactiva sola después.', False), ('Suspender la cuenta', 'Solo con reincidencia grave. Avisa a sus administradores.', False)]) +
              '<span style="height: 70px; border: 1px solid #D5DED8; border-radius: 10px; padding: 8px 12px; font-size: 13px; color: #8A948F;">Nota interna (no la ve la empresa)…</span>'
              '<a href="#" class="btnp" style="height: 42px;">Guardar decisión</a><span class="hint">La decisión, la fecha y quién la toma quedan en el historial de la cuenta.</span></aside>')
    cab = cabecera('Cuenta en pausa', 'Tercer intento en 30 días: los envíos se pausan y el equipo de Agroolink revisa la cuenta.', '<a href="#" class="btn">← Moderación</a>')
    return pagina('Superadmin · Cuenta en pausa', 'En pausa', cab, '<div style="display: flex; gap: 16px; align-items: flex-start;">' + historial + decide + '</div>', 840)

# ---------- SA4 · Archivos ----------
def archivos():
    cols = 'grid-template-columns: minmax(0,1.4fr) minmax(0,1fr) repeat(3, 56px) 92px minmax(0,1.2fr) 96px;'
    ck = lambda v: '<span style="color: ' + ('#0E5A3A' if v == 'ok' else '#A3271B') + ';">' + svg(I['ok'] if v == 'ok' else I['x'], 16, 2.4) + '</span>'
    fila = lambda n, quien, t, o, q, m, res, est, cls: ('<div class="tr" style="' + cols + '"><span><strong style="font-weight: 600;">' + n + '</strong></span><span class="hint" style="font-size: 12.5px;">' + quien + '</span>' +
                                                       ck(t) + ck(o) + ck(q) + '<span class="st gr" style="justify-self: start;">' + m + '</span><span style="font-size: 12.5px;">' + res + '</span><span><span class="st ' + cls + '">' + est + '</span></span></div>')
    tabla = ('<section class="card" style="padding-top: 14px;"><div class="th" style="' + cols + '"><span>ARCHIVO</span><span>QUIÉN · DÓNDE</span><span>TEXTO</span><span>OCR</span><span>QR</span><span>METADATOS</span><span>RESULTADO</span><span>ESTADO</span></div>' +
             fila('Oferta_CV-20_Lleida.pdf', 'AgroExport · Mensajes', 'ok', 'ok', 'ok', 'Eliminados', 'Sin contactos', 'Adjuntado', 'ok') +
             fila('Catalogo_2026.pdf', 'Piensos del Sur · ficha', 'x', 'ok', 'ok', 'Eliminados', 'Pág. 14: teléfono <span class="mask">9•• ••• •••</span>', 'Rechazado', 'er') +
             fila('Foto_nave.jpg', 'AgroVet Ibérica · ficha', 'ok', 'ok', 'x', 'Eliminados', 'Código QR en la esquina inferior', 'Rechazado', 'er') +
             fila('Ficha_tecnica_Hy-D.pdf', 'NewFarms · producto', 'ok', 'x', 'ok', 'Eliminados', 'Pág. 2 (imagen): web <span class="mask">www.•••</span>', 'Rechazado', 'er') +
             fila('Propuesta_nave2.pdf', 'Zucami · propuesta (Premium)', 'ok', 'ok', 'ok', 'Eliminados', 'Sin contactos', 'Adjuntado', 'ok') + '</section>')
    cab = cabecera('Archivos revisados', 'Cada PDF, imagen o documento se revisa al subirlo. Si lleva un contacto no se adjunta: se indica la página y el dato para corregirlo.')
    cuerpo = ('<div style="display: flex; gap: 8px;"><span class="chip on">Hoy</span><span class="chip">Rechazados 3</span><span class="chip">Adjuntados 2</span><span style="flex: 1;"></span><span class="chip">Dónde ▾</span></div>' + tabla +
              '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px;">'
              '<div class="nota">' + svg(I['info'], 16) + '<span><strong>Qué se revisa:</strong> el texto, el texto de las imágenes (OCR), los códigos QR, los enlaces y los metadatos.</span></div>'
              '<div class="nota">' + svg(I['info'], 16) + '<span><strong>Metadatos:</strong> autor, empresa y email del archivo se eliminan siempre, aunque el archivo pase.</span></div>'
              '<div class="nota">' + svg(I['info'], 16) + '<span>Un archivo rechazado cuenta como intento: suma al contador de 30 días de esa cuenta.</span></div></div>')
    return pagina('Superadmin · Archivos revisados', 'Archivos', cab, cuerpo, 760)

# ---------- SA5 · Altas y CRM ----------
def altas():
    item = lambda tipo, cls, t, d, acciones, borde=True: ('<div class="tr" style="grid-template-columns: 150px minmax(0,1fr) auto;' + ('' if borde else ' border-top: 0;') + '"><span><span class="st ' + cls + '">' + tipo + '</span></span>'
                                                         '<span><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + d + '</span></span><span style="display: flex; gap: 8px;">' + acciones + '</span></div>')
    b = lambda t, p=False: '<a href="#" class="' + ('btnp' if p else 'btn') + '">' + t + '</a>'
    lista = ('<section class="card" style="flex: 1; min-width: 0;">' +
             item('Alta en organización', 'az', 'Lucía Pérez se unió a Big Dutchman Ibérica', 'Dominio @bigdutchman.es · verificado · sus administradores ya tienen el aviso', b('Ver') + b('Quitar acceso'), False) +
             item('Poder de representación', 'wn', 'Pablo Ruiz quiere gestionar Aviagen Ibérica', 'Su email no es del dominio de la empresa · ha subido un poder (revisado: sin contactos)', b('Validar', True) + b('Rechazar')) +
             item('Organización nueva', 'sa', 'Granjas Pirineo', 'Creada por Marta Soler · no estaba en el CRM · ¿es la misma que «Granjas del Pirineo, S.L.»?', b('Fusionar', True) + b('Añadir al CRM')) +
             item('Cambio en el CRM', 'sa', 'Zucami: sociedad de Portugal', 'Pide cambiar «Zucami Portugal, Lda.» y su NIF · datos fiscales', b('Revisar cambio', True)) +
             item('Rama «Otro»', 'gr', 'NewFarms propone la rama «Bioseguridad y desinfección»', 'No existe en la lista del CRM · 2 empresas la han pedido', b('Crear rama', True) + b('Asignar existente')) + '</section>')
    lado = ('<aside style="width: 300px; flex: none; display: flex; flex-direction: column; gap: 14px;"><section class="card" style="gap: 6px;"><h2 class="h2">Solo el superadmin</h2>'
            '<span style="font-size: 13px; color: #33424C; line-height: 1.4;">Marca, sociedades, datos fiscales, estatuto en el grupo y ramas del CRM. Las empresas lo piden con «Pedir un cambio» y llega aquí.</span></section>'
            '<div class="nota">' + svg(I['info'], 16) + '<span>Si nadie revisa un alta en 7 días, el acceso se mantiene. Las empresas pueden quitar el acceso a quien no conozcan.</span></div></aside>')
    cab = cabecera('Altas y CRM', 'Quién entra en cada organización y los cambios en los datos del CRM, en una sola bandeja.')
    cuerpo = ('<div style="display: flex; gap: 8px;"><span class="chip on">Pendientes 5</span><span class="chip">Altas</span><span class="chip">Organizaciones nuevas</span><span class="chip">Cambios del CRM</span><span class="chip">Ramas</span></div>'
              '<div style="display: flex; gap: 16px; align-items: flex-start;">' + lista + lado + '</div>')
    return pagina('Superadmin · Altas y CRM', 'Altas y CRM', cab, cuerpo, 820)

PANT = [('SAPanel', 'SA1 · Panel del superadmin: lo que espera una decisión', panel), ('SAModeracion', 'SA2 · Moderación de contactos: lo bloqueado, enmascarado, con intentos y decisión', moderacion),
        ('SAPausa', 'SA3 · Cuenta en pausa: 3.er intento en 30 días y qué decidir', pausa), ('SAArchivos', 'SA4 · Archivos revisados: texto, OCR, QR, enlaces y metadatos', archivos),
        ('SAAltas', 'SA5 · Altas y CRM: altas, poderes, organizaciones nuevas, cambios del CRM y ramas', altas)]
if __name__ == '__main__':
    for k, t, f in PANT:
        open(DEST + k + '.dc.html', 'w').write(f())
    print('ok', len(PANT))
