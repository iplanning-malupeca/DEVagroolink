"""Intranet de usuario en móvil (versión de los Usr* de 004_LP_Intranet · Usuario). Escribe MB_Usr*; movil_canvas.py los pone en «004_MB_Intranet · Usuario».
No repite lo que ya hay en móvil: el menú «Tú» es M4 (MobHeaderTu) y Mis proyectos es MB_ProyU1.
Límites de Comprador Gratis según data/planes.json: 1 proyecto, 5 tableros, hasta 4 productos por comparación.
Uso: python3 tools/usuario_movil.py <canvas.json>"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, svg, I, wrap, tabbar, hdr, backbar, av, W, DEST, VE, LI, IMG

I.update({'chev': 'M9 6l6 6-6 6', 'clip': 'M21 11.5 12.5 20a5 5 0 0 1-7-7L14 4.5a3.5 3.5 0 0 1 5 5L10.5 18a2 2 0 0 1-3-3L15 7.5', 'ext': 'M14 4h6v6M20 4l-9 9M18 14v6H4V6h6',
          'down': 'M12 4v12M6 10l6 6 6-6M4 20h16', 'card': 'M3 6h18v12H3zM3 10h18', 'pin': 'M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z'})
CH = svg(I['chev'], 18, 2)

def pagina(titulo, sub, cuerpo, activo='Tú', back=None):
    top = backbar(back[0], back[1]) if back else hdr()
    cab = '' if back else '<div><span class="hint">' + sub + '</span><h1 style="margin:0;font-size:22px;font-weight:700">' + titulo + '</h1></div>'
    return SB + top + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + cab + cuerpo + '</div>' + tabbar(activo)

def card(t, cuerpo, link=None):
    hd = '<div style="display:flex;align-items:baseline"><strong style="flex:1;font-size:15px">' + t + '</strong>' + ('<span style="font-size:12.5px;color:' + VE + ';font-weight:600">' + link + '</span>' if link else '') + '</div>' if t else ''
    return '<div class="card">' + hd + cuerpo + '</div>'

def fila(izq, t, d, der='', borde=True):
    return ('<div style="display:flex;gap:10px;align-items:center;padding:9px 0;' + ('border-top:1px solid #EEF1EE' if borde else '') + '">' + izq +
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:1px"><strong style="font-size:13.5px;font-weight:600">' + t + '</strong><span class="hint">' + d + '</span></span>' + der + '</div>')

def ico(k, col=VE, bg='#EEF6EE'):
    return '<span style="width:36px;height:36px;border-radius:10px;background:' + bg + ';color:' + col + ';display:flex;align-items:center;justify-content:center;flex:none">' + svg(I[k], 18) + '</span>'

def th(bg, s=44):
    return '<span style="width:%dpx;height:%dpx;border-radius:10px;background:%s;flex:none"></span>' % (s, s, bg)

def chips(lista, on=0):
    return '<div style="display:flex;gap:6px;overflow:hidden">' + ''.join('<span class="chip" style="%s">%s</span>' % ('background:%s;border-color:%s;color:#FFFFFF' % (VE, VE) if i == on else '', t) for i, t in enumerate(lista)) + '</div>'

def sw(on=True):
    return '<span style="width:40px;height:24px;border-radius:12px;background:%s;position:relative;flex:none"><span style="position:absolute;top:3px;%s:3px;width:18px;height:18px;border-radius:50%%;background:#FFFFFF"></span></span>' % (VE if on else '#CBD3CE', 'right' if on else 'left')

def kv(k, v):
    return '<div style="display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-top:1px solid #EEF1EE;font-size:13px"><span class="hint" style="font-size:12.5px">' + k + '</span><span style="text-align:right;font-weight:500">' + v + '</span></div>'

def nota(t, bg='#F4F7FB', bd='#E2E8F0'):
    return '<div style="padding:10px 12px;border-radius:12px;background:' + bg + ';border:1px solid ' + bd + ';font-size:12.5px;color:#33424C;display:flex;gap:8px">' + svg(I['info'], 16) + '<span>' + t + '</span></div>'

def btn(t, prim=False, full=False):
    return '<span class="' + ('btnp' if prim else 'btn') + '" style="' + ('background:' + VE + ';' if prim else 'border-color:' + VE + ';color:' + VE + ';') + ('width:100%;' if full else '') + '">' + t + '</span>'

ST = lambda t, c='ok': '<span class="st ' + c + '">' + t + '</span>'

# ---------- Mi espacio ----------
def espacio():
    b = ('<div class="card" style="flex-direction:row;align-items:center;gap:12px"><span style="display:flex;gap:4px">' + th('#FFF4DE', 34) + th('#E5F1F7', 34) + '</span>'
         '<span style="flex:1;min-width:0;display:flex;flex-direction:column"><span class="hint" style="font-weight:600;letter-spacing:.04em">CONTINÚA DONDE LO DEJASTE</span><strong style="font-size:14px">Tablero «Nave 2 · broilers»</strong><span class="hint">8 productos · 1 comparación</span></span>' + CH + '</div>' +
         card('Tu proyecto', fila(ico('proy'), 'Sistema de alimentación · Nave 2', '4 propuestas · cierra en 12 días', '<span class="st" style="background:#E5484D;color:#FFFFFF">2 nuevas</span>', False) +
              fila(ico('proy', '#4A5650', '#F2F5F3'), 'Ventilación y cooling · Nave 1', 'Borrador · falta «Detalles»', ST('Borrador', 'dr')), 'Ver todos') +
         card('Mensajes', fila(av('AE', '#1F3A5F'), 'AgroExport SRL', '«Te enviamos precio y plazo…»', '<span class="hint">2 h</span>', False) +
              fila(av('Z', '#C8102E'), 'Zucami', 'Propuesta para tu proyecto', '<span class="hint">ayer</span>') +
              fila(av('AR', LI, 34, '50%'), 'Dra. Ana Ruiz', 'Experta · te ha respondido', '<span class="hint">3 d</span>'), 'Ir a Mensajes') +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' +
         card('', '<strong style="font-size:14px">Tus intereses</strong><span class="hint">Avicultura · Porcino · Nutrición y aditivos · +5</span><span style="font-size:12.5px;color:' + VE + ';font-weight:600">Editar</span>') +
         card('', '<span style="display:flex;justify-content:space-between"><strong style="font-size:14px">Tu plan</strong>' + ST('Gratis') + '</span><span class="hint">Proyectos activos 1 de 1</span><span style="height:6px;border-radius:3px;background:' + VE + '"></span><span style="font-size:12.5px;color:' + VE + ';font-weight:600">Ver planes</span>') + '</div>' +
         card('Para ti', '<div style="display:flex;gap:10px;overflow:hidden">' + ''.join('<span style="width:128px;flex:none;display:flex;flex-direction:column;gap:4px"><span style="height:78px;border-radius:12px;background:%s"></span><strong style="font-size:12.5px">%s</strong><span class="hint">%s</span></span>' % x for x in
              [('#FFF4DE', 'Ronozyme® ProAct', 'DSM-Firmenich · Enzimas'), ('#EEF2E6', 'Aviary Pro', 'Zucami · Aviarios'), ('#E5F1F7', 'Sensor NH₃ / CO₂', 'AgroNova')]) + '</div>', 'Ver más'))
    return pagina('Hola de nuevo, Samuel', 'Mi espacio', b)

# ---------- Mensajes ----------
def hilo(ini, col, t, sobre, txt, cuando, n=0, r='9px', on=False):
    return ('<div style="display:flex;gap:10px;padding:12px;border-radius:12px;' + ('background:#EEF6EE' if on else 'background:#FFFFFF;border:1px solid #E6EBE7') + '">' + av(ini, col, 40, r) +
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:1px"><span style="display:flex;justify-content:space-between"><strong style="font-size:13.5px">' + t + '</strong><span class="hint">' + cuando + '</span></span>'
            '<span class="hint" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + sobre + '</span><span style="font-size:12.5px;color:#33424C;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + txt + '</span></span>' +
            ('<span class="st" style="align-self:center;background:#E5484D;color:#FFFFFF">%d</span>' % n if n else '') + '</div>')

def mensajes():
    b = ('<div style="height:42px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;gap:8px;padding:0 12px;color:#8A948F;font-size:13.5px">' + svg(I['lupa'], 16) + 'Buscar conversación</div>' +
         chips(['Todas', 'Sin leer 2', 'Proyectos']) +
         hilo('AE', '#1F3A5F', 'AgroExport SRL', 'Corrector vitamínico CV-20 · solicitud', 'Te enviamos precio y plazo de entrega…', '2 h', 1, on=True) +
         hilo('Z', '#C8102E', 'Zucami', 'Proyecto · Sistema de alimentación Nave 2', 'Adjuntamos la propuesta en PDF', 'Ayer', 1) +
         hilo('AR', LI, 'Dra. Ana Ruiz', 'Consulta · bienestar en broilers', 'Podemos hacer una visita la semana…', '3 d', r='50%') +
         hilo('NC', '#2E8B57', 'Nutrivet Catalunya', 'Ronozyme® HiPhos · distribuidor de tu zona', 'Gracias, te respondemos mañana por aquí.', '12 oct') +
         nota('Empresas y expertos te responden siempre por Mensajes; tus datos de contacto no se muestran.'))
    return pagina('Mensajes', 'Mi espacio', b)

def burbuja(t, cuando, mio):
    return ('<div style="display:flex;justify-content:' + ('flex-end' if mio else 'flex-start') + '"><div style="max-width:82%;padding:10px 13px;border-radius:14px;font-size:13px;line-height:1.38;' +
            ('background:' + VE + ';color:#FFFFFF;border-bottom-right-radius:4px' if mio else 'background:#FFFFFF;border:1px solid #E3E8E4;border-bottom-left-radius:4px') + '">' + t +
            '<div class="hint" style="margin-top:4px;' + ('color:#D6E8DC' if mio else '') + '">' + cuando + '</div></div></div>')

def conversacion():
    top = ('<div class="top" style="padding-left:6px"><span class="ib">' + svg(I['back'], 22, 2) + '</span>' + av('AE', '#1F3A5F', 34) +
           '<span style="flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2;margin-left:6px"><strong style="font-size:15px">AgroExport SRL</strong><span class="hint">Carla Martín · responde en 2 h de media</span></span><span class="ib">' + svg(I['dots']) + '</span></div>')
    b = ('<div style="margin:10px 12px 0;padding:9px 11px;border-radius:12px;background:#F4F7FB;border:1px solid #E2E8F0;display:flex;align-items:center;gap:10px;font-size:12.5px">' + th('#FFF4DE', 34) +
         '<span style="flex:1;min-width:0"><strong>Sobre: Corrector vitamínico CV-20</strong><br><span class="hint">Solicitud del 13 oct · Ver producto · Guardar en tablero</span></span></div>'
         '<div style="padding:14px 12px;display:flex;flex-direction:column;gap:10px">' +
         burbuja('Hola, querría precio y plazo para 2 t de CV-20 para broilers. Estoy en Lleida.', '13 oct · 09:12', True) +
         burbuja('Hola Samuel, gracias por tu interés. Para Lleida te sirve nuestro distribuidor Agropecuària del Segre. Te enviamos precio y plazo en el PDF adjunto.', 'Hoy · 08:40', False) +
         '<span style="align-self:flex-start;display:inline-flex;align-items:center;gap:8px;padding:8px 12px;border-radius:10px;background:#FFFFFF;border:1px solid #E3E8E4;font-size:12.5px">' + svg(I['clip'], 15) + 'Oferta_CV-20_Lleida.pdf · 240 KB</span></div>')
    foot = ('<div style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 12px 30px;display:flex;gap:8px;align-items:center"><span class="ib" style="width:36px;color:#56615B">' + svg(I['clip'], 20) + '</span>'
            '<span style="flex:1;height:42px;border:1px solid #D5DED8;border-radius:21px;display:flex;align-items:center;padding:0 14px;color:#8A948F;font-size:13.5px">Escribe un mensaje…</span>'
            '<span style="width:42px;height:42px;border-radius:50%;background:' + VE + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg(I['send'], 18) + '</span></div>')
    return SB + top + b + foot

# ---------- Tableros, comparaciones, historial ----------
def tablero(t, tipo, d, n, est, upd):
    return ('<div class="card" style="gap:6px"><div style="display:flex;gap:4px">' + th('#FFF4DE', 52) + th('#E5F1F7', 52) + th('#EEF2E6', 52) + '</div>'
            '<span style="display:flex;align-items:center;gap:8px"><strong style="font-size:14.5px;flex:1">' + t + '</strong>' + ST(tipo, 'dr') + '</span><span class="hint">' + d + '</span>'
            '<span style="font-size:12.5px;color:#33424C">' + n + '</span><span class="hint">' + est + ' · ' + upd + '</span></div>')

def tableros():
    b = (chips(['Míos', 'Compartidos conmigo']) +
         '<div class="card" style="flex-direction:row;align-items:center;gap:12px;background:#F4F7FB;border-color:#E2E8F0">' + ico('rec') + '<span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px">Historial · automático</strong><span class="hint">48 elementos · últimos 90 días</span></span>' + CH + '</div>' +
         tablero('Nave 2 · broilers', 'Proyecto', 'Equipamiento y nutrición para la nave nueva', '14 elementos · 2 comparativas', '5 por revisar · 4 interesantes · 3 contactados', 'Hoy') +
         tablero('Bioseguridad 2027', 'Investigación', 'Desinfección, control de plagas y vacunación', '8 elementos · 1 comparativa', '6 por revisar · 2 interesantes', 'Ayer') +
         tablero('Proveedores de pienso', 'Compras', 'Comparar fábricas y premezclas para 2027', '6 elementos · 1 comparativa', '1 por revisar · 3 contactados', '12 oct') +
         '<span class="hint" style="text-align:center">Plan Gratis · 4 de 5 tableros</span>')
    top = SB + hdr()
    cab = '<div style="display:flex;align-items:flex-end"><span style="flex:1"><span class="hint">Mi espacio</span><h1 style="margin:0;font-size:22px;font-weight:700">Mis tableros</h1></span>' + btn(svg(I['mas'], 16, 2.2) + 'Nuevo', True) + '</div>'
    return top + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + cab + b + '</div>' + tabbar('Tableros')

def comp(t, tipo, cuando, prods, acc):
    return ('<div class="card"><span style="display:flex;justify-content:space-between"><strong style="font-size:14.5px">' + t + '</strong><span class="hint">' + cuando + '</span></span><span class="hint">' + tipo + '</span>'
            '<div style="display:grid;grid-template-columns:repeat(%d,1fr);gap:6px">' % len(prods) + ''.join('<span style="display:flex;flex-direction:column;gap:3px"><span style="height:56px;border-radius:10px;background:%s"></span><strong style="font-size:11.5px;line-height:1.25">%s</strong><span class="hint" style="font-size:10.5px">%s</span></span>' % p for p in prods) + '</div>'
            '<div style="display:flex;gap:8px">' + btn('Abrir', True) + btn(acc) + '</div></div>')

def comparaciones():
    b = (comp('Enzimas · fitasas', 'Enzimas · 3 productos', 'Hoy', [('#FFF4DE', 'Ronozyme® HiPhos', 'DSM-Firmenich'), ('#E5F1F7', 'Axtra® PHY', 'IFF'), ('#EEF2E6', 'Quantum® Blue', 'AB Vista')], 'Solicitar información a los 3') +
         comp('Bebederos para broilers', 'Bebederos · 2 productos', 'Hace 3 días', [('#F1EEFB', 'Nipple Pro', 'Fabricante A'), ('#F3EEE6', 'AquaLine', 'Fabricante B')], 'Guardar en tablero') +
         comp('Ventiladores de túnel', 'Sistemas de ventilación · 3 productos', '12 oct', [('#E5F1F7', 'Turbo 50"', 'Fabricante C'), ('#EEF2E6', 'Cone Fan 54"', 'Fabricante D'), ('#FFF4DE', 'EcoFlow', 'Fabricante E')], 'Ver en tablero') +
         nota('Plan Gratis: hasta 4 productos por comparación. Sin precios: para precio, «Solicitar información».'))
    return pagina('Mis comparaciones', '', b, 'Tableros', ('Mis comparaciones', 'Sueltas o dentro de un tablero'))

def hist(k, t, tipo, d, h, acc):
    return fila(ico(k), t + ' <span class="st dr" style="margin-left:4px">' + tipo + '</span>', d + ' · ' + h, '<span style="font-size:12px;color:' + VE + ';font-weight:600;white-space:nowrap">' + acc + '</span>')

def historial():
    b = (chips(['Todo', 'Productos', 'Empresas', 'Expertos']) +
         card('', '<span class="hint" style="font-weight:600;letter-spacing:.04em">HOY</span>' + hist('prod', 'Ronozyme® ProAct', 'Producto', 'DSM-Firmenich', '10:42', 'Guardar') +
              hist('panel', 'Zucami Poultry Equipment', 'Empresa', 'Fabricante', '10:30', 'En «Nave 2»') + hist('info', 'Estrés térmico en broilers', 'Contenido', 'Agrinews', '09:15', 'Guardar')) +
         card('', '<span class="hint" style="font-weight:600;letter-spacing:.04em">AYER</span>' + hist('info', 'Dra. Ana Ruiz', 'Experto', 'Bienestar animal · Lleida', '18:02', 'Guardar') +
              hist('prod', 'Sensor NH₃ / CO₂', 'Producto', 'AgroNova', '17:40', 'Guardar')) +
         '<div style="display:flex;gap:8px">' + btn('Guardar historial en un tablero') + '<span class="btn" style="color:#B42318">Borrar todo</span></div>' +
         nota('Se guarda lo que consultas durante 90 días. Solo lo ves tú.'))
    return pagina('Historial', '', b, 'Tableros', ('Historial', 'Todo lo que has consultado'))

# ---------- Mi cuenta ----------
def perfil():
    b = (nota('Tus datos vienen de tu cuenta global (la misma de Agrinews). Si los cambias aquí, cambian en todas las plataformas. <b style="color:' + VE + '">Ir a mi cuenta global ↗</b>') +
         card('Datos personales', '<div style="display:flex;gap:12px;align-items:center">' + av('SE', VE, 52, '50%') + '<span style="flex:1"><strong style="font-size:15px">Samuel Esteban</strong><br><span class="hint">Miembro desde marzo 2024 (Agrinews)</span></span></div>' +
              kv('Email', 'samuel@granjalosolmos.es · verificado') + kv('Acceso', 'Código por email') + kv('Teléfono', '+34 6•• ••• 214') + kv('Cargo', 'Granjero') + kv('Empresa', 'Granja Los Olmos') + kv('País y provincia', 'España · Lleida'), 'Editar') +
         card('Tus intereses', kv('Especies', 'Avicultura · Porcino') + kv('Categorías', 'Nutrición y aditivos · Equipamiento avícola') + kv('Objetivos', 'Bienestar animal · +4'), 'Editar') +
         card('Tus espacios', fila(av('SE', VE, 34, '50%'), 'Personal', 'Buscar, comparar y proyectos', ST('Activo'), False) +
              fila(ico('mas', '#1D4E89', '#E9F0F9'), 'Crear o vincular empresa', 'Ficha, productos y solicitudes', CH) + fila(ico('mas', LI, '#F1EEFB'), 'Crear perfil de experto', 'Ofrece tus servicios', CH)) +
         card('Notificaciones', ''.join(fila('', t, d, sw(o), i > 0) for i, (t, d, o) in enumerate([('Propuestas a mis proyectos', 'Aviso en la app', True), ('Respuestas a mis consultas', 'Aviso en la app', True), ('Novedades según mis intereses', 'Semanal', True), ('Resumen semanal por email', 'Lunes', False)]))) +
         card('Privacidad', fila('', 'Tus datos de contacto nunca se muestran', 'Empresas y expertos te responden por Mensajes', ST('Siempre'), False) + fila('', 'Aparecer en «Quién vio tu ficha»', 'Las empresas ven tu perfil, nunca tu contacto', sw(False))) +
         card('Seguridad y cuenta', fila('', 'Cerrar sesión en todos los dispositivos', '', '<span style="font-size:12.5px;color:' + VE + ';font-weight:600">Cerrar</span>', False) +
              fila('', 'Descargar mis datos', '', '<span style="font-size:12.5px;color:' + VE + ';font-weight:600">Solicitar</span>') + fila('', 'Eliminar cuenta', 'En tu cuenta global', svg(I['ext'], 16))))
    return pagina('Mi perfil', '', b, back=('Mi perfil', 'Mi cuenta'))

def sel(k, v, extra=''):
    return '<div style="display:flex;flex-direction:column;gap:5px"><span style="font-size:12.5px;font-weight:600">' + k + extra + '</span><span style="height:44px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;justify-content:space-between;padding:0 12px;font-size:14px">' + v + svg('M6 9l6 6 6-6', 16, 2) + '</span></div>'

def idioma():
    gl = ' <span class="hint" style="font-weight:400">· cuenta global</span>'
    b = (card('Idioma', sel('Idioma de la plataforma', 'Español', gl) + '<span class="hint">Menús, emails y avisos.</span><span style="font-size:12.5px;font-weight:600">Idiomas de los contenidos</span>' +
              '<div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join('<span class="chip" style="%s">%s</span>' % ('background:#EEF6EE;border-color:' + VE + ';color:' + VE if on else '', t) for t, on in [('✓ Español', True), ('✓ Inglés', True), ('Portugués', False), ('Francés', False)]) + '</div><span class="hint">Fichas técnicas y documentos en estos idiomas primero.</span>') +
         card('Zona', sel('País', 'España', gl) + sel('Provincia', 'Lleida') + '<span class="hint">Verás «Disponible en España» y los distribuidores de Cataluña primero.</span>') +
         card('Formato', sel('Unidades', 'Sistema métrico (kg, t, °C)') + sel('Moneda de referencia', 'Euro (€)') + '<span class="hint">Solo para precios orientativos de servicios y planes.</span>') +
         card('Zona horaria', sel('Zona horaria', 'Europa/Madrid (GMT+2)') + '<span class="hint">Para eventos, webinars y plazos de proyectos.</span>'))
    foot = '<div class="foot" style="bottom:84px;padding-bottom:10px">' + btn('Cancelar') + '<span class="btnp" style="flex:1;background:' + VE + '">Guardar cambios</span></div>'
    return pagina('Idioma y zona', '', b, back=('Idioma y zona', 'Mi cuenta')) + foot

def ayuda():
    temas = [('Primeros pasos', 'Cuenta, intereses y cómo moverte'), ('Proyectos y propuestas', 'Publicar, recibir y elegir'), ('Tableros y comparador', 'Guardar, comparar y compartir'),
             ('Cuenta y facturación', 'Planes, pagos y facturas'), ('Privacidad y datos', 'Quién ve qué y cuándo'), ('Para empresas y expertos', 'Ficha, productos y servicios')]
    faq = ['¿Las empresas ven mis datos cuando creo un proyecto?', '¿Por qué no veo precios en las fichas?', '¿Cómo cambio el país o la provincia?', '¿Mi cuenta es la misma que en Agrinews?', '¿Qué pasa si quito un interés?']
    b = ('<div style="height:46px;border:1px solid #D5DED8;border-radius:12px;background:#FFFFFF;display:flex;align-items:center;gap:8px;padding:0 12px;color:#8A948F;font-size:13.5px">' + svg(I['lupa'], 18) + '¿En qué podemos ayudarte?</div>' +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">' + ''.join('<div class="card" style="gap:2px;padding:11px 12px"><strong style="font-size:13px">%s</strong><span class="hint">%s</span></div>' % t for t in temas) + '</div>' +
         card('Preguntas frecuentes', ''.join('<div style="display:flex;justify-content:space-between;gap:8px;padding:10px 0;%sfont-size:13px">%s%s</div>' % ('border-top:1px solid #EEF1EE;' if i else '', q, svg('M6 9l6 6 6-6', 16, 2)) for i, q in enumerate(faq))) +
         card('¿Hablamos?', fila(ico('mail'), 'Chat', 'Lunes a viernes, 9:00–18:00', btn('Abrir chat'), False) + fila(ico('edit'), 'Formulario', 'Respondemos en 24 h laborables', btn('Escribir')) +
              fila(ico('cal'), 'Demo guiada', 'Para empresas: 20 min por videollamada', btn('Reservar'))))
    return pagina('Ayuda y contacto', '', b, back=('Ayuda y contacto', 'Mi cuenta'))

# ---------- Facturación ----------
FT = ['Resumen', 'Planes', 'Pedidos', 'Facturas', 'Pagos', 'Direcciones']
def fact(on, cuerpo, h1=False):
    b = (chips(FT, on) + (nota('Se gestiona en tu cuenta global: planes, pedidos, facturas, pagos y direcciones de Agroolink y Agrinews en un solo sitio. <b style="color:' + VE + '">Ir a mi cuenta global ↗</b>') if on == 0 else '') + cuerpo)
    return pagina('Facturación', '', b, back=('Facturación', 'Mi cuenta' if on == 0 else 'Mi cuenta · ' + FT[on]))

def pedido(n, f, c, o, imp, est, cls='ok'):
    return fila('', c, f + ' · ' + o + ' · ' + n, '<span style="display:flex;flex-direction:column;align-items:flex-end;gap:3px"><strong style="font-size:13px">' + imp + '</strong>' + ST(est, cls) + '</span>')

def facturacion():
    b = (card('Tu plan en Agroolink', '<strong style="font-size:17px">Comprador Gratis</strong><span class="hint">1 proyecto activo · comparador hasta 4 productos · 5 tableros</span>' + btn('Ver planes')) +
         card('Suscripciones', fila('', 'Revista digital Pro', '9,90 €/mes · renueva el 1 nov · Agrinews', '', False) + fila('', 'Alertas de mercado', 'Gratis · semanal · Agrinews'), 'Gestionar') +
         card('Método de pago', fila(ico('card'), 'VISA •••• 4242', 'Caduca 08/28 · predeterminada', '', False) + '<span class="hint">Se usa en Agroolink y Agrinews.</span>', 'Cambiar') +
         card('Últimos pedidos', pedido('', '12 oct', 'Entrada AviForum 2026 · 2 personas', 'Agroolink', '90,00 €', 'Pagado').replace('border-top:1px solid #EEF1EE', '', 1) +
              pedido('', '1 oct', 'Revista digital Pro · octubre', 'Agrinews', '9,90 €', 'Pagado') + pedido('', '18 sep', 'Informe «Ventilación en broilers»', 'Agrinews', '19,00 €', 'Pagado'), 'Ver todo') +
         card('Direcciones', kv('Facturación', 'Granja Los Olmos SL · Lleida') + kv('Envío', 'La misma que facturación'), 'Editar') +
         nota('Lo que compras a una empresa a través de Agroolink se ve en Mis proyectos y en Mensajes; aquí solo lo que pagas a Agroolink o Agrinews.'))
    return fact(0, b)

def planes():
    li = lambda t: '<span style="display:flex;gap:6px;font-size:13px">' + svg('M5 12l5 5 9-10', 16, 2.2, VE) + t + '</span>'
    b = ('<div class="card" style="border:2px solid ' + VE + '"><span style="display:flex;justify-content:space-between"><strong style="font-size:16px">Comprador Gratis</strong>' + ST('Actual') + '</span>' +
         kv('Proyectos activos', '1 de 1') + kv('Productos por comparación', 'hasta 4') + kv('Tableros', 'hasta 5') + '<span class="hint">Sin coste, sin tarjeta.</span></div>' +
         card('', '<span style="display:flex;justify-content:space-between"><strong style="font-size:16px">Comprador Pro</strong>' + ST('Próximamente', 'wn') + '</span><span style="font-size:13px">9,90 €/mes o 99 €/año</span>' +
              li('Proyectos ilimitados') + li('Comparar hasta 10 productos') + li('Tableros compartidos con tu equipo') + btn('Avísame cuando esté disponible', full=True)) +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">' +
         '<div class="card" style="gap:3px;border-top:3px solid #1D4E89"><strong style="font-size:13px">¿Vendes o distribuyes?</strong><span class="hint">Empresa · Gratis · Pro 79 € · Premium 199 €/mes</span><span style="font-size:12.5px;color:#1D4E89;font-weight:600">Planes de empresa</span></div>'
         '<div class="card" style="gap:3px;border-top:3px solid ' + LI + '"><strong style="font-size:13px">¿Ofreces servicios?</strong><span class="hint">Experto · Gratis · Pro 19,90 €/mes</span><span style="font-size:12.5px;color:' + LI + ';font-weight:600">Planes de experto</span></div></div>' +
         card('Suscripciones', fila('', 'Revista digital Pro', 'Agrinews · 9,90 €/mes · 1 nov · Visa •••• 4242', ST('Activa'), False) + fila('', 'Alertas de mercado', 'Agrinews · Gratis · semanal', ST('Activa')) +
              fila('', 'Novedades según tus intereses', 'Agroolink · Gratis · semanal', ST('Activa')) + fila('', 'Anuario Avicultura 2026', 'Agrinews · 29,00 €/año', ST('Cancelada', 'dr')) + '<span class="hint">Sin permanencia: si cancelas, sigues con acceso hasta el final del periodo pagado.</span>'))
    return fact(1, b)

def pedidos():
    b = ('<div style="display:flex;gap:8px"><span style="flex:1;height:42px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;gap:8px;padding:0 12px;color:#8A948F;font-size:13px">' + svg(I['lupa'], 16) + 'Buscar pedido…</span><span class="btn">' + svg(I['filt'], 16) + '&nbsp;2026</span></div>' +
         card('', pedido('AGL-26-0142', '12 oct', 'Entrada AviForum 2026 × 2', 'Agroolink', '90,00 €', 'Pagado').replace('border-top:1px solid #EEF1EE', '', 1) +
              pedido('AGN-26-8831', '1 oct', 'Revista digital Pro · octubre', 'Agrinews', '9,90 €', 'Pagado') + pedido('AGN-26-8102', '18 sep', 'Informe «Ventilación en broilers»', 'Agrinews', '19,00 €', 'Pagado') +
              pedido('AGL-26-0098', '2 sep', 'Webinar «Bienestar en ponedoras»', 'Agroolink', '0,00 €', 'Inscrito', 'nw') + pedido('AGN-26-7012', '14 ago', 'Libro «Manual de bioseguridad»', 'Agrinews', '32,00 €', 'Enviado', 'wn') +
              pedido('AGN-26-6390', '20 jul', 'Curso online «Gestión de la nave»', 'Agrinews', '45,00 €', 'Reembolsado', 'dr')) +
         '<span class="hint" style="text-align:center">Toca un pedido para ver el detalle →</span>')
    return fact(2, b)

def pedido_det():
    b = ('<div class="card"><span style="display:flex;justify-content:space-between"><span class="hint">AGL-26-0142</span>' + ST('Pagado') + '</span><strong style="font-size:17px">Entrada AviForum 2026</strong><span class="hint">12–13 nov · Madrid · comprado el 12 oct 2026</span>' +
         kv('Entrada general × 2', '90,00 €') + kv('Incluye IVA (21 %)', '15,62 €') + '<div style="display:flex;justify-content:space-between;padding-top:8px;border-top:1px solid #EEF1EE;font-size:15px;font-weight:700"><span>Total</span><span>90,00 €</span></div></div>' +
         card('', kv('Asistentes', 'Samuel Esteban · Marta Esteban').replace('border-top:1px solid #EEF1EE;', '', 1) + kv('Pagado con', 'Visa •••• 4242')) +
         '<div style="display:flex;gap:8px">' + '<span class="btnp" style="flex:1;background:' + VE + '">Ver entradas</span>' + btn(svg(I['down'], 16) + '&nbsp;Factura PDF') + '</div>' +
         '<span style="text-align:center;font-size:13px;color:' + VE + ';font-weight:600">¿Algún problema con este pedido?</span>')
    return pagina('', '', b, back=('Pedido AGL-26-0142', 'Facturación · Pedidos'))

def facturas():
    fac = lambda n, f, c, o, base, iva, tot: fila(ico('down'), c, f + ' · ' + o + ' · ' + n, '<span style="display:flex;flex-direction:column;align-items:flex-end"><strong style="font-size:13px">' + tot + '</strong><span class="hint" style="font-size:10.5px">base ' + base + ' · IVA ' + iva + '</span></span>')
    b = ('<div class="card" style="flex-direction:row;align-items:center"><span style="flex:1;display:flex;flex-direction:column"><span class="hint">Facturado en 2026</span><strong style="font-size:22px">115,70 €</strong><span class="hint">6 facturas · 1 rectificativa</span></span>' + btn(svg(I['down'], 16) + '&nbsp;ZIP 2026') + '</div>' +
         card('', kv('Se facturan a', 'Granja Los Olmos SL · B25••••87').replace('border-top:1px solid #EEF1EE;', '', 1) + kv('Copia a contabilidad', 'contabilidad@granjalosolmos.es')) +
         chips(['Todas', 'Agroolink', 'Agrinews']) +
         card('', fac('F-AGL-26-0142', '12 oct', 'Entrada AviForum 2026 × 2', 'Agroolink', '74,38 €', '15,62 €', '90,00 €').replace('border-top:1px solid #EEF1EE', '', 1) +
              fac('F-AGN-26-8831', '1 oct', 'Revista digital Pro · octubre', 'Agrinews', '8,18 €', '1,72 €', '9,90 €') + fac('F-AGN-26-8102', '18 sep', 'Informe «Ventilación en broilers»', 'Agrinews', '15,70 €', '3,30 €', '19,00 €') +
              fac('F-AGN-26-7012', '14 ago', 'Libro «Manual de bioseguridad»', 'Agrinews', '30,77 €', '1,23 € (4 %)', '32,00 €') + fac('R-AGN-26-6390', '24 jul', 'Rectificativa · curso «Gestión de la nave»', 'Agrinews', '−37,19 €', '−7,81 €', '−45,00 €')) +
         nota('Cada plataforma emite sus propias facturas; aquí las tienes juntas. Para corregir datos fiscales, pide una rectificativa desde la factura.'))
    return fact(3, b)

def pagos():
    b = ('<div class="card"><div style="display:flex;gap:10px;align-items:center">' + ico('card') + '<span style="flex:1"><strong style="font-size:14px">Visa •••• 4242</strong><br><span class="hint">Samuel Esteban · caduca 08/28</span></span>' + ST('Predeterminada') + '</div><span class="hint">Se usa en Agroolink y Agrinews.</span><div style="display:flex;gap:8px">' + btn('Editar') + '<span class="btn" style="color:#B42318">Eliminar</span></div></div>' +
         '<div class="card"><div style="display:flex;gap:10px;align-items:center">' + ico('card', '#4A5650', '#F2F5F3') + '<span style="flex:1"><strong style="font-size:14px">Domiciliación SEPA</strong><br><span class="hint">ES•• •••• •••• •••• 1234 · Granja Los Olmos SL</span></span></div><span class="hint">Útil para suscripciones anuales y facturas de empresa.</span><div style="display:flex;gap:8px">' + btn('Hacer predeterminada') + btn('Editar') + '</div></div>' +
         card('Añadir método de pago', '<div style="display:flex;gap:8px">' + btn('+ Tarjeta') + btn('+ Domiciliación SEPA') + '</div><span class="hint">La transferencia se elige al pagar.</span>') +
         card('Qué método usa cada cobro', fila('', 'Revista digital Pro', 'Agrinews · 9,90 €/mes · Visa •••• 4242', '<span style="font-size:12.5px;color:' + VE + ';font-weight:600">Cambiar</span>', False) + fila('', 'Próximas compras', 'Agroolink · predeterminado (Visa •••• 4242)')) +
         nota('El pago lo gestiona una pasarela segura; ni Agroolink ni Agrinews guardan los datos completos de tu tarjeta.'))
    return fact(4, b)

def direcciones():
    dire = lambda t, pred, lineas, acc: ('<div class="card" style="gap:4px"><span style="display:flex;justify-content:space-between"><strong style="font-size:14px">' + t + '</strong>' + (ST('Predeterminada') if pred else '') + '</span>' +
                                       ''.join('<span class="hint" style="font-size:12.5px">' + l + '</span>' for l in lineas) + '<div style="display:flex;gap:8px;margin-top:6px">' + ''.join(btn(a) for a in acc) + '</div></div>')
    sec = lambda t: '<div style="display:flex;align-items:baseline;margin-top:4px"><strong style="flex:1;font-size:15px">' + t + '</strong><span style="font-size:12.5px;color:' + VE + ';font-weight:600">+ Añadir</span></div>'
    b = (sec('Datos de facturación') + dire('Granja Los Olmos SL', True, ['CIF B25••••87', 'Partida Els Plans s/n · 25001 Lleida · España', 'Facturas a contabilidad@granjalosolmos.es'], ['Editar']) +
         dire('Samuel Esteban · a título personal', False, ['NIF ••••5678Z', 'C/ Major 12, 2.º · 25001 Lleida · España'], ['Hacer predeterminada', 'Editar']) +
         '<span class="hint">Al pagar eliges a nombre de quién va la factura.</span>' +
         sec('Direcciones de envío') + dire('Granja', True, ['Samuel Esteban · +34 6•• ••• 214', 'Partida Els Plans s/n · 25001 Lleida', 'Entrega de 8:00 a 14:00'], ['Editar']) +
         dire('Oficina', False, ['C/ Major 12, 2.º · 25001 Lleida'], ['Hacer predeterminada', 'Editar']) +
         nota('Se comparten entre Agroolink y Agrinews. La ubicación de tus explotaciones para recibir propuestas se indica en cada proyecto.'))
    return fact(5, b)

PANT = [('MB_UsrEspacio', 'Móvil · Mi espacio', 1140, espacio), ('MB_UsrMensajes', 'Móvil · Mensajes', 844, mensajes), ('MB_UsrConversacion', 'Móvil · Conversación', 844, conversacion),
        ('MB_UsrTableros', 'Móvil · Mis tableros', 970, tableros), ('MB_UsrComparaciones', 'Móvil · Mis comparaciones', 990, comparaciones), ('MB_UsrHistorial', 'Móvil · Historial', 850, historial),
        ('MB_UsrPerfil', 'Móvil · Mi perfil', 1850, perfil), ('MB_UsrIdioma', 'Móvil · Idioma y zona', 1210, idioma), ('MB_UsrAyuda', 'Móvil · Ayuda y contacto', 1150, ayuda),
        ('MB_UsrFacturacion', 'Móvil · Facturación', 1340, facturacion), ('MB_UsrFactPlanes', 'Móvil · Planes y suscripciones', 1160, planes), ('MB_UsrFactPedidos', 'Móvil · Pedidos', 844, pedidos),
        ('MB_UsrFactPedido', 'Móvil · Detalle de pedido', 844, pedido_det), ('MB_UsrFactFacturas', 'Móvil · Facturas', 1150, facturas), ('MB_UsrFactPagos', 'Móvil · Métodos de pago', 980, pagos),
        ('MB_UsrFactDirecciones', 'Móvil · Direcciones', 1070, direcciones)]
TIRAS = [('MB_UsrTiraEspacio', 'Mi espacio y Mensajes', ['MB_UsrEspacio', 'MB_UsrMensajes', 'MB_UsrConversacion']),
         ('MB_UsrTiraTableros', 'Tableros, comparaciones e historial', ['MB_UsrTableros', 'MB_UsrComparaciones', 'MB_UsrHistorial']),
         ('MB_UsrTiraCuenta', 'Mi cuenta: perfil, idioma y ayuda', ['MB_UsrPerfil', 'MB_UsrIdioma', 'MB_UsrAyuda']),
         ('MB_UsrTiraFacturacion', 'Facturación', ['MB_UsrFacturacion', 'MB_UsrFactPlanes', 'MB_UsrFactPedidos', 'MB_UsrFactPedido', 'MB_UsrFactFacturas', 'MB_UsrFactPagos', 'MB_UsrFactDirecciones'])]

def tira(t, keys, pant=None):
    """Varias pantallas de 390 px en un solo tablero (el lienzo admite 511 archivos)."""
    P = {k: (tt, h, f) for k, tt, h, f in (pant or PANT)}
    H = max(P[k][1] for k in keys) + 44; Wt = len(keys) * 390 + (len(keys) - 1) * 40
    body = '<div style="display:flex;gap:40px;align-items:flex-start;background:#FFFFFF">' + ''.join(
        '<div style="width:390px;display:flex;flex-direction:column;gap:14px"><span style="font:600 15px Poppins,sans-serif;color:#17231D;height:30px;display:flex;align-items:center">' + P[k][0].replace('Móvil · ', '') + '</span>'
        '<div class="m" style="width:390px;height:' + str(P[k][1]) + 'px;position:relative;overflow:hidden;background:#F6F8F6;border-radius:18px;box-shadow:0 0 0 1px #E3E8E4">' + P[k][2]() + '</div></div>' for k in keys) + '</div>'
    html = wrap('Móvil · ' + t, H, body)
    html = html.replace('<div class="m" style="width: 390px; height: ' + str(H) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">', '<div style="width: ' + str(Wt) + 'px; height: ' + str(H) + 'px; background: #FFFFFF;">', 1)
    return html.replace('"width":390,"height":' + str(H), '"width":' + str(Wt) + ',"height":' + str(H))

if __name__ == '__main__':
    for k, t, keys in TIRAS:
        html = tira(t, keys)
        open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
    print('ok', len(TIRAS))
