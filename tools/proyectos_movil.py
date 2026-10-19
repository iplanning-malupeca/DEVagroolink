"""Gestión de proyectos en móvil (390 px): usuario (Mis proyectos, acciones, detalle con propuestas, propuesta y conversación,
editar, avisar a las empresas, archivados) y empresa/experto (oportunidades, proyectos para la experta).
Escribe MB_ProyU* y MB_ProyE*; movil_canvas.py los coloca en «MB_07 Proyectos · Usuario» y «MB_07b Proyectos · Empresas y expertos».
Uso: python3 tools/proyectos_movil.py <canvas.json>"""
import os, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.dirname(sys.argv[1]) + '/'
VE, AZ, LI = '#0E5A3A', '#1D4E89', '#4B3BA6'
IMG = {'nave2': '/_blob/482aa9551e386fdb30306651ef167e6c', 'bio': '/_blob/613352c1a286bd888bf87722c7309779', 'vent': '/_blob/272663d3e08ffd129f99c54a39782a89', 'alm': '/_blob/850aac941f71c3c0f800184a213aa749'}
LOGO = '<img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height:24px;width:auto;display:block">'
CSS = """*{box-sizing:border-box}body{margin:0}.m{font-family:'Poppins',system-ui,sans-serif;color:#17231D;font-size:14px;line-height:1.38}
.sb{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 26px 0 30px;font-size:15px;font-weight:600;background:#FFFFFF}
.top{height:56px;display:flex;align-items:center;gap:6px;padding:0 8px 0 16px;background:#FFFFFF;border-bottom:1px solid #E3E8E4}
.ib{width:44px;height:44px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;color:#17231D;position:relative;flex:none}
.bdg{position:absolute;top:5px;right:3px;min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:#D93A3A;color:#FFFFFF;font-size:10.5px;font-weight:600;display:flex;align-items:center;justify-content:center;border:2px solid #FFFFFF}
.card{background:#FFFFFF;border:1px solid #E6EBE7;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.hint{font-size:11.5px;color:#56615B}
.st{font-size:10.5px;font-weight:600;padding:3px 8px;border-radius:999px;white-space:nowrap;display:inline-flex;align-items:center}
.ok{background:#EEF6EE;color:#0E5A3A}.dr{background:#F2F5F3;color:#4A5650}.wn{background:#FFF4E0;color:#7A4B00}.nw{background:#E7EEFB;color:#2A4A8C}
.btn{height:40px;border-radius:10px;border:1px solid #D2DAE3;background:#FFFFFF;font-weight:500;font-size:13px;display:inline-flex;align-items:center;justify-content:center;padding:0 14px;white-space:nowrap}
.btnp{height:40px;border-radius:10px;color:#FFFFFF;font-weight:600;font-size:13px;display:inline-flex;align-items:center;justify-content:center;gap:6px;padding:0 14px;white-space:nowrap}
.chip{display:inline-flex;align-items:center;height:32px;padding:0 12px;border-radius:999px;border:1px solid #DCE4DE;background:#FFFFFF;font-size:12.5px;white-space:nowrap}
.tbi{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:10.5px;font-weight:500;color:#56615B;min-height:56px;position:relative}
.tbp{width:54px;height:30px;border-radius:15px;display:flex;align-items:center;justify-content:center}
.foot{position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 16px 30px;display:flex;gap:8px}
.ov{position:absolute;inset:0;background:rgba(16,30,22,.45)}
.sheet{position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-radius:20px 20px 0 0;padding:8px 16px 30px;display:flex;flex-direction:column;gap:10px}
.li{display:flex;gap:12px;align-items:flex-start;padding:12px 2px;border-bottom:1px solid #EEF1EE}
"""
def svg(d, s=22, w=1.8, c='currentColor'):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, c, w, ''.join('<path d="%s"/>' % p for p in d.split('|')))
I = {'lupa': 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5', 'proy': 'M3 21V10l9-6 9 6v11M2 21h20M9 21v-6h6v6M9 11h6', 'tab': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z',
     'mail': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6', 'back': 'M15 6l-6 6 6 6', 'mas': 'M12 5v14M5 12h14', 'dots': 'M5 12h.01M12 12h.01M19 12h.01',
     'edit': 'M4 20h4L18.5 9.5a2.8 2.8 0 0 0-4-4L4 16z', 'dup': 'M8 8h12v12H8zM4 16V4h12', 'pause': 'M8 5v14M16 5v14', 'arch': 'M3 7h18v13H3zM3 7l2-4h14l2 4M10 12h4', 'rec': 'M3 12a9 9 0 1 0 3-6.7L3 8|M3 3v5h5',
     'send': 'M22 2 11 13M22 2l-7 20-4-9-9-4z', 'cal': 'M3 5h18v16H3zM3 10h18M8 3v4M16 3v4', 'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01',
     'panel': 'M3 3h8v10H3zM13 3h8v6h-8zM13 11h8v10h-8zM3 15h8v6H3z', 'sol': 'M4 13h4l2 3h4l2-3h4M5 5h14l2 8v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5z', 'prod': 'M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8', 'filt': 'M4 6h16M7 12h10M10 18h4'}
SB = ('<div class="sb"><span>9:41</span><span style="display:flex;gap:6px;align-items:center"><svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="1" fill="#17231D"/><rect x="5" y="5" width="3" height="7" rx="1" fill="#17231D"/><rect x="10" y="2.5" width="3" height="9.5" rx="1" fill="#17231D"/><rect x="15" y="0" width="3" height="12" rx="1" fill="#17231D"/></svg>'
      '<svg width="26" height="12" viewBox="0 0 26 12" aria-hidden="true"><rect x=".5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="#17231D" opacity=".4"/><rect x="2" y="2" width="17" height="8" rx="2" fill="#17231D"/></svg></span></div>')
MSG = '<span class="ib" aria-label="Mensajes, 3 sin leer">' + svg(I['mail']) + '<span class="bdg">3</span></span>'
def hdr(rol=None, color=VE):
    tag = '' if not rol else '<span style="font-size:11px;font-weight:600;color:%s;background:%s;border-radius:999px;padding:2px 9px;margin-left:8px">%s</span>' % (color, {AZ: '#E9F0F9', LI: '#F1EEFB'}[color], rol)
    return '<div class="top" style="%s"><span style="flex:1;display:flex;align-items:center">%s%s</span><span class="ib">%s</span>%s</div>' % ('border-top:3px solid %s;' % color if rol else '', LOGO, tag, svg(I['lupa']), MSG)
def backbar(t, sub):
    return '<div class="top" style="padding-left:6px"><span class="ib">' + svg(I['back'], 22, 2) + '</span><span style="flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2"><strong style="font-size:15.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + t + '</strong><span class="hint" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + sub + '</span></span>' + MSG + '</div>'
def tabbar(activo, color=VE, items=None, avatar='SE'):
    items = items or [('lupa', 'Explorar'), ('proy', 'Proyectos'), ('tab', 'Tableros'), (None, 'Tú')]
    soft = {VE: '#E4F0D0', AZ: '#E9F0F9', LI: '#F1EEFB'}[color]
    h = '<nav style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;z-index:6"><div style="display:flex;padding:2px 6px 0">'
    for ic, t in items:
        on = t == activo
        icon = svg(I[ic], 22, 2.1 if on else 1.8) if ic else '<span style="width:26px;height:26px;border-radius:%s;background:%s;color:#FFFFFF;font-size:10.5px;font-weight:600;display:flex;align-items:center;justify-content:center">%s</span>' % ('8px' if color == AZ else '50%', color, avatar)
        h += '<span class="tbi" style="%s"><span class="tbp" style="background:%s">%s</span>%s</span>' % ('color:%s;font-weight:600' % color if on else '', soft if on else 'transparent', icon, t)
    return h + '</div><div style="height:26px;display:flex;align-items:center;justify-content:center"><span style="width:134px;height:5px;border-radius:3px;background:#17231D"></span></div></nav>'
def wrap(title, h, body):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n<div class="m" style="width: 390px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":390,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')
def av(ini, col, s=34, r='9px'):
    return '<span style="width:%dpx;height:%dpx;border-radius:%s;background:%s;color:#FFFFFF;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:none">%s</span>' % (s, s, r, col, ini)
def thumb(k, gris=False):
    return '<span style="width:64px;height:56px;border-radius:12px;flex:none;background:#E6EBE7 url(\'%s\') center / cover no-repeat;%s"></span>' % (IMG[k], 'filter:grayscale(1);opacity:.7;' if gris else '')
# ---------- usuario ----------
PROY = [('nave2', 'Sistema de alimentación · Nave 2', 'ok', 'Evaluando propuestas', 'Broilers · Lleida', '<strong>4</strong> propuestas · cierra en 12 días', '<span class="st nw">2 nuevas</span>', 'Ver propuestas', True),
        ('bio', 'Asesoría en bioseguridad', 'wn', 'Contactando proveedores', 'Consultoría veterinaria · Lleida', '<strong>1</strong> propuesta · cierra en 20 días', '', 'Ver propuesta', False),
        ('vent', 'Ventilación y cooling · Nave 1', 'dr', 'Borrador', 'Ventilación · falta «Detalles»', 'Sin publicar', '', 'Continuar', False)]
def tarjeta(p, sin_arch=False):
    k, t, cl, est, sub, num, extra, cta, prim = p
    return ('<article class="card"><div style="display:flex;gap:12px;align-items:flex-start">' + thumb(k) + '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:3px"><strong style="font-size:14.5px;line-height:1.25">' + t + '</strong>'
            '<span style="display:flex;gap:6px;flex-wrap:wrap"><span class="st ' + cl + '">' + est + '</span>' + extra + '</span><span class="hint">' + sub + '</span></span><span class="ib" style="width:36px;height:36px;margin:-6px -6px 0 0">' + svg(I['dots'], 20, 3) + '</span></div>'
            '<div style="display:flex;align-items:center;gap:8px"><span class="hint" style="flex:1;color:#2F3D36">' + num + '</span><span class="' + ('btnp' if prim else 'btn') + '" style="height:36px;' + ('background:%s' % VE if prim else '') + '">' + cta + '</span></div></article>')
def mis(menu=False, archivado=False):
    lst = PROY[:2] if archivado else PROY
    body = (SB + hdr() + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:10px"><div style="display:flex;align-items:flex-end;gap:10px"><span style="flex:1"><span class="hint" style="font-weight:600;letter-spacing:.08em">MI ESPACIO</span><h1 style="margin:2px 0 0;font-size:22px;font-weight:700">Mis proyectos</h1></span>'
            '<span class="btnp" style="background:' + VE + ';height:38px">' + svg(I['mas'], 16, 2.2) + 'Crear</span></div>' + ''.join(tarjeta(p) for p in lst) +
            '<span style="display:flex;gap:8px;align-items:center;font-size:12.5px;color:' + VE + ';font-weight:500;padding:4px 2px">' + svg(I['arch'], 16) + 'Ver archivados (' + ('2' if archivado else '1') + ')</span>'
            '<div class="card" style="flex-direction:row;gap:10px;background:#F2F7F3;border-color:#DCE9DF;font-size:12.5px"><span style="color:' + VE + '">' + svg(I['tab'], 18) + '</span><span>Ligado a tu tablero «Nave 2 · broilers»: las propuestas que te interesen se guardan allí.</span></div></div>')
    if archivado:
        body += '<div style="position:absolute;left:16px;right:16px;bottom:100px;background:#17231D;color:#FFFFFF;border-radius:12px;padding:12px 14px;display:flex;align-items:center;gap:10px;font-size:13px;z-index:7"><span style="flex:1">«Ventilación y cooling · Nave 1» archivado</span><strong style="color:#B5D334">Deshacer</strong></div>'
    if menu:
        acc = [('edit', 'Editar', 'Cambia datos; si afecta a las propuestas, eliges si avisar'), ('dup', 'Duplicar', 'Crea un borrador igual, por ejemplo para la Nave 3'),
               ('pause', 'Pausar', 'No entran propuestas nuevas; las conversaciones siguen'), ('arch', 'Archivar', 'Lo quita de tu lista; se puede recuperar')]
        body += ('<div class="ov" style="z-index:8"></div><div class="sheet" style="z-index:9"><span style="align-self:center;width:40px;height:5px;border-radius:3px;background:#D5DED8"></span><strong style="font-size:15.5px">Sistema de alimentación · Nave 2</strong>' +
                 ''.join('<div class="li"><span style="color:' + VE + '">' + svg(I[i], 20) + '</span><span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px;font-weight:600">' + t + '</strong><span class="hint">' + d + '</span></span></div>' for i, t, d in acc) +
                 '<span class="btn" style="height:44px">Cancelar</span></div>')
    return body + tabbar('Proyectos')
PROPS = [('AN', '#1E8A3C', 'AgroNova', 'Distribuidor validado de Roxell', 'Roxell Feedmax + silos y transporte, montaje incluido', '48.000 – 55.000 €', '8 semanas', '2 años', '<span class="st nw">Nueva</span>', '96%', True),
         ('ZU', '#1E8A3C', 'Zucami', 'Fabricante · Zona Nordeste', 'FeedLine con transporte en espiral', '52.000 – 60.000 €', '10 semanas', '3 años', '<span class="st nw">Nueva</span>', '91%', False),
         ('BD', '#C8102E', 'Big Dutchman', 'Fabricante · Cataluña', 'FlexVey con comederos de plato', 'A consultar', '12 semanas', '2 años', '<span class="st wn">Te ha escrito</span>', '88%', False),
         ('MT', '#5B4B9E', 'Montajes Segre', 'Montador · Lleida', 'Solo montaje y puesta en marcha', '9.000 €', '3 semanas', '1 año', '<span class="st dr">Vista</span>', '74%', False)]
def detalle():
    cards = ''.join(('<article class="card" style="%s"><div style="display:flex;gap:10px;align-items:center">' % ('border:1.5px solid %s;background:#F5FAF6' % VE if sel else '') + av(a, c) + '<span style="flex:1;min-width:0;display:flex;flex-direction:column"><strong style="font-size:14px">' + n + '</strong><span class="hint">' + d + '</span></span>' + tag + '</div>'
                     '<span style="font-size:12.5px;color:#2F3D36">' + sol + '</span><div style="display:flex;gap:10px;align-items:center;font-size:12.5px"><strong>' + pr + '</strong><span class="hint">· ' + pl + ' · garantía ' + ga + '</span><span style="margin-left:auto;font-size:11.5px;font-weight:600;color:' + VE + '">' + enc + ' encaje</span></div></article>')
                    for a, c, n, d, sol, pr, pl, ga, tag, enc, sel in PROPS)
    return (SB + backbar('Sistema de alimentación · Nave 2', 'Broilers · 40.000 aves · Lleida · cierra en 12 días') +
            '<div style="padding:12px 16px 110px;display:flex;flex-direction:column;gap:10px"><div style="display:flex;gap:8px;align-items:center"><span class="st ok">Evaluando propuestas</span><span style="flex:1"></span><span class="btn" style="height:34px">Editar</span><span class="btn" style="height:34px">Invitar</span></div>'
            '<div style="display:flex;gap:6px;overflow:hidden"><span class="chip" style="background:' + VE + ';border-color:' + VE + ';color:#FFFFFF">Todas · 4</span><span class="chip">Nuevas · 2</span><span class="chip">Mejor encaje</span><span class="chip">Precio</span></div>' + cards +
            '<div class="card" style="background:#F1EEFB;border-color:#E3DDF6;gap:4px"><strong style="font-size:13px;color:' + LI + '">¿Dudas al comparar?</strong><span class="hint" style="color:#4A5650">Laura Gil, veterinaria, se ha ofrecido a revisar las propuestas contigo.</span></div>'
            '<span class="hint">Todo se habla dentro de Agroolink: tu teléfono y tu email no se comparten nunca. Adjudicar cierra el proyecto y avisa a todas.</span></div>' + tabbar('Proyectos'))
def bub(ini, col, txt, meta, yo=False):
    return ('<div style="display:flex;gap:8px;align-items:flex-end;%s">' % ('flex-direction:row-reverse' if yo else '') + av(ini, col, 28, '8px') +
            '<span style="display:flex;flex-direction:column;gap:3px;max-width:82%%;%s"><span style="background:%s;color:%s;border:1px solid %s;border-radius:14px;padding:9px 12px;font-size:13px">%s</span><span class="hint">%s</span></span></div>' % ('align-items:flex-end' if yo else '', VE if yo else '#FFFFFF', '#FFFFFF' if yo else '#2F3D36', VE if yo else '#E6EBE7', txt, meta))
def evt(t, verde=False):
    return '<span style="align-self:center;font-size:11px;color:%s;background:%s;border-radius:999px;padding:4px 12px;text-align:center">%s</span>' % (VE if verde else '#56615B', '#EEF6EE' if verde else '#F2F5F3', t)
def propuesta():
    return (SB + backbar('Propuesta de AgroNova', 'Distribuidor validado de Roxell · Lleida') +
            '<div style="padding:12px 16px 170px;display:flex;flex-direction:column;gap:10px">'
            '<div class="card"><div style="display:flex;align-items:center;gap:8px"><strong style="flex:1">La propuesta</strong><span class="st wn">En conversación</span></div>'
            '<span style="font-size:13px"><strong>46.000 – 52.000 €</strong> <span style="color:#7A857F;text-decoration:line-through;font-size:11.5px">48.000 – 55.000 €</span></span><span class="hint">8 semanas · garantía 2 años · montaje incluido</span>'
            '<span style="font-size:12.5px;color:#2F3D36">Roxell Feedmax · silo 20 t · montaje · 2 visitas de seguimiento</span><span style="font-size:12.5px;color:' + VE + ';font-weight:500">Comparar con las otras 3 →</span></div>'
            '<strong style="font-size:13.5px;margin-top:4px">Conversación con AgroNova</strong>' + evt('Propuesta recibida · 14 oct') +
            bub('AN', '#1E8A3C', 'Te dejamos la oferta con Feedmax y silo de 20 t. Si nos dices el ancho de la nave, afinamos las líneas.', 'Jordi · AgroNova · 14 oct') +
            evt('Has respondido: AgroNova ve tu nombre, nunca tu teléfono ni tu email') +
            bub('SE', VE, 'La nave mide 16 × 120 m. ¿El montaje incluye la conexión eléctrica?', 'Tú · 15 oct · leído', True) +
            bub('AN', '#1E8A3C', 'Sí, incluida. Con 16 m bastan 4 líneas: hemos ajustado el precio. ¿Pasamos el martes 21?', 'Jordi · AgroNova · 16 oct') +
            evt('AgroNova ha actualizado la propuesta · 46.000 – 52.000 €', True) +
            '<div class="card" style="flex-direction:row;align-items:center;gap:10px;font-size:12.5px"><span style="color:' + VE + '">' + svg(I['cal'], 18) + '</span><span style="flex:1"><strong>Visita propuesta</strong><br>martes 21 oct, 10:00 · en la granja</span><span class="btnp" style="background:' + VE + ';height:34px">Aceptar</span></div></div>'
            '<div style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 16px 30px;display:flex;flex-direction:column;gap:8px">'
            '<div style="display:flex;gap:8px"><span style="flex:1;height:42px;border:1px solid #D5DED8;border-radius:10px;display:flex;align-items:center;padding:0 12px;font-size:13px;color:#8A948F">Escribe a AgroNova…</span><span class="btnp" style="background:' + VE + ';width:46px;height:42px;padding:0">' + svg(I['send'], 16, 2) + '</span></div>'
            '<div style="display:flex;gap:8px"><span class="btn" style="flex:1">Descartar</span><span class="btnp" style="flex:2;background:' + VE + '">Adjudicar a AgroNova</span></div></div>')
BLO = [('QUÉ NECESITAS', 'Sistema de alimentación completo para una nave nueva', False), ('DÓNDE', 'España · Lleida · Nave 2 <span class="hint">· las empresas solo ven la provincia</span>', False),
       ('ESCENARIO Y PLAZOS', 'Nave nueva · <s style="color:#8A948F">40.000</s> <strong>45.000 aves</strong> · antes de <s style="color:#8A948F">marzo</s> <strong>abril de 2027</strong>', True),
       ('PRODUCTOS Y SERVICIOS', 'Comederos · Silos · Transporte de pienso · Montaje · Puesta en marcha', False), ('PRESUPUESTO', '45.000 – 60.000 € <span class="hint">· orientativo, no lo ven las empresas</span>', False),
       ('DOCUMENTOS Y FOTOS', 'Plano_nave2.pdf · 3 fotos', False), ('DESCRIPCIÓN', 'Nave nueva de broilers. Buscamos línea de comederos, silo con transporte y montaje llave en mano.', False)]
def editar(avisar=False):
    b = (SB + backbar('Editar proyecto', 'Sistema de alimentación · Nave 2') + '<div style="padding:12px 16px 150px;display:flex;flex-direction:column;gap:8px"><span class="hint">Cambia solo lo que necesites: cada bloque abre su pregunta del asistente.</span>' +
         ''.join('<div class="card" style="gap:4px;%s"><div style="display:flex;align-items:center;gap:8px"><span class="hint" style="font-weight:600;letter-spacing:.06em;flex:1">%s</span>%s<span style="font-size:12.5px;color:%s;font-weight:500">Cambiar</span></div><span style="font-size:13px">%s</span></div>' % ('border:1.5px solid #E0A33B' if mod else '', t, '<span class="st wn">Modificado</span>' if mod else '', VE, v) for t, v, mod in BLO) +
         '</div><div class="foot" style="flex-direction:column"><span class="hint">2 cambios sin guardar · 4 empresas tienen propuesta</span><div style="display:flex;gap:8px"><span class="btn" style="flex:1;height:46px">Descartar</span><span class="btnp" style="flex:1;height:46px;background:' + VE + '">Guardar cambios</span></div></div>')
    if avisar:
        opt = lambda on, t, d: '<div style="display:flex;gap:10px;padding:12px;border:%s;border-radius:12px;background:%s"><span style="width:20px;height:20px;border-radius:50%%;border:1.5px solid %s;flex:none;display:flex;align-items:center;justify-content:center">%s</span><span style="display:flex;flex-direction:column;gap:2px"><strong style="font-size:13.5px">%s</strong><span class="hint">%s</span></span></div>' % ('1.5px solid ' + VE if on else '1px solid #DCE3DE', '#F5FAF6' if on else '#FFFFFF', VE if on else '#C9D2CC', '<span style="width:10px;height:10px;border-radius:50%;background:' + VE + '"></span>' if on else '', t, d)
        b += ('<div class="ov" style="z-index:8"></div><div class="sheet" style="z-index:9"><span style="align-self:center;width:40px;height:5px;border-radius:3px;background:#D5DED8"></span><strong style="font-size:16px">¿Avisar a las empresas con propuesta?</strong>'
              '<span class="hint" style="font-size:12.5px">Has cambiado datos que pueden afectar a sus precios y plazos: aves 40.000 → 45.000 · plazo marzo → abril de 2027.</span>' +
              opt(True, 'Sí, avisar a las 4 empresas', 'Les llega un aviso en vuestra conversación y su propuesta se marca «Puede estar desactualizada».') + opt(False, 'No, guardar sin avisar', 'Las propuestas actuales se mantienen tal cual.') +
              '<div style="border:1px solid #D5DED8;border-radius:12px;padding:10px 12px;font-size:13px;color:#2F3D36">Finalmente serán 45.000 aves y podemos esperar hasta abril. ¿Podéis revisar la propuesta?</div>'
              '<div style="display:flex;gap:8px"><span class="btn" style="flex:1;height:46px">Volver</span><span class="btnp" style="flex:1;height:46px;background:' + VE + '">Guardar y avisar</span></div></div>')
    return b
def archivados():
    it = [('vent', 'Ventilación y cooling · Nave 1', 'Borrador', 'Archivado hoy, 16 oct', 'Falta el paso «Detalles»'), ('alm', 'Reforma del almacén de pienso', 'Finalizado', 'Archivado el 2 sep', '3 propuestas · adjudicado a Silos Córdoba')]
    return (SB + backbar('Proyectos archivados', 'No reciben propuestas nuevas') + '<div style="padding:12px 16px 110px;display:flex;flex-direction:column;gap:10px">' +
            ''.join('<article class="card" style="background:#FAFBFA"><div style="display:flex;gap:12px;align-items:flex-start">' + thumb(k, True) + '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:3px"><strong style="font-size:14px;color:#4A5650">' + t + '</strong><span class="st dr" style="align-self:flex-start">' + e + '</span><span class="hint">' + f + ' · ' + d + '</span></span></div><span class="btnp" style="background:' + VE + '">' + svg(I['rec'], 16, 2) + 'Recuperar</span></article>' for k, t, e, f, d in it) +
            '<div class="card" style="flex-direction:row;gap:10px;background:#F2F7F3;border-color:#DCE9DF;font-size:12.5px"><span style="color:' + VE + '">' + svg(I['info'], 18) + '</span><span><strong>Archivar no borra nada.</strong> Se conservan propuestas, mensajes y documentos. Al recuperar, vuelve con el estado que tenía.</span></div></div>' + tabbar('Proyectos'))
# ---------- empresa / experto ----------
def oportunidad(enc, t, quien, checks, precio, plazo, cupo, color, cta):
    return ('<article class="card"><div style="display:flex;gap:10px;align-items:flex-start"><span style="width:46px;height:46px;border-radius:12px;background:%s;color:%s;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:none">%s</span><span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:2px"><strong style="font-size:14px;line-height:1.25">%s</strong><span class="hint">%s</span></span></div>' % ({AZ: '#E9F0F9', LI: '#F1EEFB'}[color], color, enc, t, quien) +
            '<div style="display:flex;flex-direction:column;gap:2px">' + ''.join('<span style="font-size:12px;color:#0E5A3A">✓ ' + c + '</span>' for c in checks) + '</div>'
            '<div style="display:flex;gap:8px;align-items:center"><span class="hint" style="flex:1;color:#2F3D36">' + precio + ' · ' + plazo + ' · ' + cupo + '</span><span class="btnp" style="height:36px;background:' + color + '">' + cta + '</span></div></article>')
EMP_TABS = [('panel', 'Panel'), ('sol', 'Solicitudes'), ('prod', 'Productos'), (None, 'Empresa')]
def oportunidades():
    return (SB + hdr('Empresa', AZ) + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:10px"><span><span class="hint" style="font-weight:600;letter-spacing:.08em">AGRONOVA</span><h1 style="margin:2px 0 0;font-size:22px;font-weight:700">Oportunidades</h1><span class="hint">Proyectos que encajan con tu catálogo, tus especies y tu zona.</span></span>'
            '<div style="display:flex;gap:6px;overflow:hidden"><span class="chip" style="background:' + AZ + ';border-color:' + AZ + ';color:#FFFFFF">Recomendadas · 6</span><span class="chip">Mis propuestas · 2</span><span class="chip">Adjudicadas · 1</span></div>'
            '<div style="display:flex;gap:6px"><span class="chip">' + svg(I['filt'], 15) + '&nbsp;Filtros</span><span class="chip">Especie</span><span class="chip">Zona</span></div>' +
            oportunidad('96%', 'Sistema de alimentación · nave de 40.000 broilers', 'Granja de broilers en Lleida', ['Tienes Roxell Feedmax en tu catálogo', 'Avicultura › Broilers', 'Lleida está en tu zona'], 'Precio no indicado', 'antes de mar 2027', '4 de 10 propuestas', AZ, 'Preparar propuesta') +
            oportunidad('85%', 'Cambio de bebederos en 4 naves', 'Integradora en Huesca', ['Bebederos en tu catálogo', 'Huesca está en tu zona'], '15.000 – 25.000 €', '3 meses', '1 de 10', AZ, 'Preparar propuesta') +
            '<div class="card" style="background:#F3F7FC;border-color:#C8D8EE;font-size:12.5px"><span><strong>Recibe más oportunidades:</strong> completa los mercados de 12 productos y añade zonas a 2 servicios.</span><span style="color:' + AZ + ';font-weight:500">Completar →</span></div></div>' +
            tabbar('Solicitudes', AZ, EMP_TABS, 'AN'))
def experto():
    return (SB + hdr('Experta', LI) + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:10px"><span><span class="hint" style="font-weight:600;letter-spacing:.08em">COMO EXPERTA</span><h1 style="margin:2px 0 0;font-size:22px;font-weight:700">Proyectos para ti</h1><span class="hint">Donde piden tu especialidad, tus especies y tu zona.</span></span>'
            '<div style="display:flex;gap:6px;overflow:hidden"><span class="chip" style="background:' + LI + ';border-color:' + LI + ';color:#FFFFFF">Para ti · 3</span><span class="chip">Mis candidaturas · 1</span><span class="chip">Adjudicados</span></div>' +
            oportunidad('94%', 'Plan de bioseguridad para 3 naves', 'Granja de broilers en Lleida · Consultoría veterinaria', ['Veterinaria · avicultura', 'Lleida a 40 km de ti', 'Bioseguridad en tu perfil'], 'A consultar', '2 meses', '1 de 5 candidaturas', LI, 'Enviar candidatura') +
            oportunidad('87%', 'Revisar 4 propuestas de alimentación', 'Granja de broilers en Lleida · Consultoría', ['Avicultura › Broilers', 'Revisión de propuestas activada'], '300 – 500 €', '2 semanas', '0 candidaturas', LI, 'Enviar candidatura') +
            '<div class="card" style="background:#F1EEFB;border-color:#E3DDF6;font-size:12.5px"><span><strong>Ayuda a comparar:</strong> los ganaderos pueden pedirte que revises las propuestas que reciben.</span><span style="color:' + LI + ';font-weight:500">Activar en «Mis servicios» →</span></div></div>' +
            tabbar('Proyectos', LI, avatar='LG'))
B = {'MB_ProyU1_Mis': ('Móvil · Mis proyectos', 1000, mis()),
     'MB_ProyU2_Acciones': ('Móvil · Mis proyectos · menú ⋯', 1000, mis(menu=True)),
     'MB_ProyU3_Detalle': ('Móvil · Proyecto y propuestas recibidas', 1240, detalle()),
     'MB_ProyU4_Propuesta': ('Móvil · Propuesta y conversación', 1080, propuesta()),
     'MB_ProyU5_Editar': ('Móvil · Editar proyecto', 1000, editar()),
     'MB_ProyU6_Avisar': ('Móvil · Editar · ¿avisar a las empresas?', 1000, editar(avisar=True)),
     'MB_ProyU7_Archivar': ('Móvil · Archivado con «Deshacer»', 1000, mis(archivado=True)),
     'MB_ProyU8_Archivados': ('Móvil · Proyectos archivados', 844, archivados()),
     'MB_ProyE1_Oportunidades': ('Móvil · Oportunidades para la empresa', 1000, oportunidades()),
     'MB_ProyE2_Experto': ('Móvil · Proyectos para la experta', 1000, experto())}
if __name__ == '__main__':
    import json
    alt = {}
    if len(sys.argv) > 2: alt = json.load(open(sys.argv[2]))
    for k, (t, h, body) in B.items():
        html = wrap(t, alt.get(k, h), body)
        open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
    print('ok', len(B))
