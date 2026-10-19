"""Alta de empresa en móvil según la configuración (005a Fab-Com, 005b Fab-Sucursales, 005c Sucursal, 005d Distribuidor y lo que faltaba de 005 Fab-Dist).
Cada configuración es una tira: las pantallas del prototipo alta-empresa capturadas a 390 px (tools/captura_empresa_config.js → capture/CD*, CS*, CX*)
y, a continuación, las pantallas propias del escritorio que el prototipo no tiene (equipo comercial, países, permisos, marcas, Mensajes…).
Política de contactos: el comprador nunca ve teléfonos, emails ni webs; las solicitudes y avisos van por Mensajes.
Movil_canvas.py coloca las tiras como filas de «005_MB_Alta empresa» (y la de Fab-Dist en «005_MB_Alta empresa_Fab-Dist»).
Uso: python3 tools/empresa_config_movil.py <canvas.json>"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, svg, I, hdr, backbar, tabbar, av, W, DEST, AZ, EMP_TABS, CSS as CSS_MV

I.update({'chev': 'M9 6l6 6-6 6', 'clip': 'M21 11.5 12.5 20a5 5 0 0 1-7-7L14 4.5a3.5 3.5 0 0 1 5 5L10.5 18a2 2 0 0 1-3-3L15 7.5', 'ok': 'M5 12l5 5 9-10', 'x': 'M6 6l12 12M18 6 6 18',
          'globe': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18', 'up': 'M12 16V4M6 10l6-6 6 6M4 20h16', 'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4'})
SOFT = '#E9F0F9'

# ---------- piezas ----------
def card(t, cuerpo, extra=''):
    hd = ('<div style="display:flex;align-items:baseline;gap:8px"><strong style="flex:1;font-size:15px">' + t + '</strong>' + extra + '</div>') if t else ''
    return '<div class="card">' + hd + cuerpo + '</div>'
def st(t, est='background:#EEF6EE;color:#0E5A3A'):
    return '<span class="st" style="' + est + '">' + t + '</span>'
AZST, WN, GR = 'background:' + SOFT + ';color:' + AZ, 'background:#FFF4E0;color:#7A4B00', 'background:#F2F5F3;color:#4A5650'
def btn(t, prim=False, flex=False):
    return '<span class="' + ('btnp' if prim else 'btn') + '" style="' + ('background:' + AZ + ';' if prim else 'border-color:' + AZ + ';color:' + AZ + ';') + ('flex:1;' if flex else '') + '">' + t + '</span>'
def fila(izq, t, d, der='', borde=True):
    return ('<div style="display:flex;gap:10px;align-items:center;padding:9px 0;' + ('border-top:1px solid #EEF1EE' if borde else '') + '">' + izq +
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:1px"><strong style="font-size:13.5px;font-weight:600">' + t + '</strong><span class="hint">' + d + '</span></span>' + der + '</div>')
def nota(t, bg='#F4F7FB', bd='#E2E8F0'):
    return '<div style="padding:10px 12px;border-radius:12px;background:' + bg + ';border:1px solid ' + bd + ';font-size:12.5px;color:#33424C;display:flex;gap:8px"><span style="flex:none">' + svg(I['info'], 16) + '</span><span>' + t + '</span></div>'
def contactos():
    return nota('<strong>El comprador nunca ve teléfonos, emails ni webs.</strong> Cada solicitud abre un hilo en Mensajes.', '#FFF8EC', '#F3DFB8')
def campo(k, v, hint=''):
    return ('<div style="display:flex;flex-direction:column;gap:5px"><span style="font-size:12.5px;font-weight:600">' + k + (' <span class="hint" style="font-weight:400">· ' + hint + '</span>' if hint else '') + '</span>'
            '<span style="min-height:44px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;padding:0 12px;font-size:14px">' + v + '</span></div>')
def chips(lista, on=(0,)):
    return '<div style="display:flex;gap:6px;flex-wrap:wrap">' + ''.join('<span class="chip" style="%s">%s</span>' % ('background:%s;border-color:%s;color:#FFFFFF' % (AZ, AZ) if i in on else '', t) for i, t in enumerate(lista)) + '</div>'
def paso(n, t, sub):
    return ('<div style="display:flex;flex-direction:column;gap:6px"><span class="hint" style="font-weight:600">' + n + '</span><h1 style="margin:0;font-size:21px;font-weight:700;line-height:1.2">' + t + '</h1><span style="font-size:13px;color:#56615B">' + sub + '</span></div>')
def pie(prim, sec='Anterior'):
    return '<div class="foot"><span class="btn" style="height:48px;flex:1">' + sec + '</span><span class="btnp" style="height:48px;flex:2;background:' + AZ + '">' + prim + '</span></div>'
def emp(ini, color, s=34):
    return av(ini, color, s, '9px')

def pantalla(cuerpo, back=None, tab='Solicitudes', foot='', avatar='ZU', pad=110):
    top = backbar(*back) if back else hdr('Empresa', AZ)
    return SB + top + '<div style="padding:14px 16px ' + str(pad) + 'px;display:flex;flex-direction:column;gap:12px">' + cuerpo + '</div>' + foot + (tabbar(tab, AZ, EMP_TABS, avatar) if tab else '')
def asistente(cuerpo, foot):
    top = ('<div class="top" style="padding:0 6px 0 16px"><span style="flex:1;display:flex;align-items:center;gap:8px"><img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height:24px;width:auto;display:block">'
           '<span style="font-size:11px;font-weight:600;color:' + AZ + ';background:' + SOFT + ';border-radius:999px;padding:2px 9px">Empresas</span></span><span class="hint" style="margin-right:6px">Guardar y salir</span></div>')
    return SB + top + '<div style="padding:18px 16px 150px;display:flex;flex-direction:column;gap:14px;background:#FFFFFF">' + cuerpo + '</div>' + foot

# Mensajes: un hilo con registros (nada se borra)
def registro(t, cuando):
    return '<div style="align-self:center;max-width:92%;padding:7px 11px;border-radius:10px;background:#F1F3F6;font-size:11.5px;color:#4A5560;text-align:center">Registro · ' + t + ' · ' + cuando + '</div>'
def burbuja(quien, t, cuando, mio):
    return ('<div style="display:flex;justify-content:' + ('flex-end' if mio else 'flex-start') + '"><div style="max-width:84%;padding:9px 12px;border-radius:14px;font-size:13px;line-height:1.38;' +
            ('background:' + AZ + ';color:#FFFFFF;border-bottom-right-radius:4px' if mio else 'background:#FFFFFF;border:1px solid #E3E8E4;border-bottom-left-radius:4px') + '"><div class="hint" style="margin-bottom:3px;' + ('color:#D6E2F2' if mio else '') + '">' + quien + ' · ' + cuando + '</div>' + t + '</div></div>')
def hilo(ini, color, t, sub, cuerpo, aviso):
    top = ('<div class="top" style="padding-left:6px"><span class="ib">' + svg(I['back'], 22, 2) + '</span>' + emp(ini, color) +
           '<span style="flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2;margin-left:6px"><strong style="font-size:15px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + t + '</strong><span class="hint" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + sub + '</span></span><span class="ib">' + svg(I['info']) + '</span></div>')
    foot = ('<div style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 12px 30px;display:flex;gap:8px;align-items:center"><span class="ib" style="width:36px;color:#56615B">' + svg(I['clip'], 20) + '</span>'
            '<span style="flex:1;height:42px;border:1px solid #D5DED8;border-radius:21px;display:flex;align-items:center;padding:0 14px;color:#8A948F;font-size:13.5px">Escribe un mensaje…</span>'
            '<span style="width:42px;height:42px;border-radius:50%;background:' + AZ + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg(I['send'], 18) + '</span></div>')
    return SB + top + '<div style="padding:12px 12px 110px;display:flex;flex-direction:column;gap:10px">' + cuerpo + nota(aviso) + '</div>' + foot

# ---------- 005a · Fabricante con comerciales (Zucami) ----------
def k_crear():
    b = (paso('Paso 4 de 8 · Equipo comercial', 'Crear perfil de comercial', 'Para quien aún no tiene cuenta. Sale en tu ficha y recibe las solicitudes de su zona.') +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + campo('Nombre', 'Pedro') + campo('Apellidos', 'Lima') + '</div>' + campo('Cargo', 'Comercial') +
         campo('Email para avisarle', 'pedro.lima@zucami.com', 'no se muestra') + campo('Idiomas', 'Portugués · Español') + campo('Zona que cubre', 'Portugal · todo el país') +
         nota('Le enviamos un email con la solicitud; se da de alta con ese email, sin contraseña. <strong>El comprador ve su foto, nombre, cargo, zona e idiomas; nunca su email ni su teléfono.</strong>'))
    return asistente(b, pie('Crear perfil', 'Cancelar'))
def k_email():
    b = ('<div class="card" style="gap:10px"><span class="hint">De: Agroolink · en nombre de Zucami<br>Para: Pedro Lima</span><strong style="font-size:16px">Tienes una solicitud de un comprador de Leiria</strong>'
         '<span style="font-size:13.5px">Hola, Pedro: Zucami te ha añadido como comercial para Portugal en Agroolink. Un comprador de tu zona ha pedido información:</span>' +
         ''.join('<div style="display:flex;justify-content:space-between;padding:7px 0;border-top:1px solid #EEF1EE;font-size:13px"><span class="hint" style="font-size:12.5px">%s</span><strong style="font-weight:500">%s</strong></div>' % kv for kv in
                 [('Producto', 'Aviarios'), ('Proyecto', 'Nave nueva'), ('Nº de aves', '60.000 ponedoras'), ('Ubicación', 'Leiria, Portugal'), ('Plazo', 'Antes de 6 meses')]) +
         nota('Por privacidad, el nombre y el contacto del comprador solo se ven en Agroolink. Responde desde allí para que la conversación quede guardada.') +
         '<span class="btnp" style="height:48px;background:' + AZ + '">Darme de alta y ver la solicitud</span><span class="hint" style="text-align:center">Gratis, en un minuto, con este email. El comprador espera respuesta en 24 h.</span></div>')
    return SB + '<div class="top"><strong style="flex:1;font-size:15px">Correo</strong></div><div style="padding:14px 12px;display:flex;flex-direction:column;gap:12px">' + b + '</div>'
def k_alta():
    b = ('<div class="card" style="flex-direction:row;align-items:center;gap:10px;background:' + SOFT + ';border-color:#D4E1F1">' + emp('ZU', '#1E8A3C') + '<span style="flex:1"><strong>1 solicitud te espera</strong><br><span class="hint">Aviarios · 60.000 ponedoras · Leiria</span></span></div>' +
         paso('', 'Activa tu cuenta, Pedro', 'Zucami ya ha creado tu perfil de comercial. Solo falta confirmar tu email.') + campo('Email', 'pedro.lima@zucami.com') +
         '<div style="display:flex;flex-direction:column;gap:5px"><span style="font-size:12.5px;font-weight:600">Código que te hemos enviado</span><div style="display:flex;gap:8px">' +
         ''.join('<span style="flex:1;height:52px;border:1.5px solid %s;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:600">%s</span>' % ((AZ, d) if d else ('#D5DED8', '')) for d in ['2', '7', '', '', '', '']) + '</div></div>'
         '<span style="font-size:12.5px;display:flex;gap:8px"><span style="width:20px;height:20px;border-radius:5px;background:' + AZ + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center;flex:none">' + svg(I['ok'], 13, 3) + '</span>Acepto las condiciones de uso. Mi cuenta es la misma para Agroolink y Agrinews.</span>' +
         '<span class="hint">Tu nombre, cargo, idiomas y zona ya los ha puesto Zucami; podrás cambiarlos en tu perfil.</span>')
    return asistente(b, '<div class="foot"><span class="btnp" style="height:48px;flex:1;background:' + AZ + '">Activar y ver la solicitud</span></div>')
def k_zona():
    b = ('<div style="display:flex;gap:12px;align-items:center">' + av('LG', AZ, 52, '50%') + '<span style="flex:1"><strong style="font-size:17px">Laura García</strong><br><span class="hint">Responsable comercial · cuenta activa</span></span></div>' +
         card('Datos', fila('', 'Cargo', 'Responsable comercial', '', False) + fila('', 'Idiomas', 'Español, inglés, catalán') + fila('', 'Suplente si está fuera', 'Javier Ruiz', svg(I['chev'], 16)) +
              fila('', 'Avisos de solicitudes', 'En la app y por email · no se muestran al comprador')) +
         card('Zona que cubre', chips(['Cataluña', 'Aragón', 'Navarra', 'País Vasco', '+ Zona'], (0, 1, 2, 3)) + '<span class="hint">Las solicitudes de compradores de estas zonas le llegan a ella.</span>') +
         card('Si nadie cubre la zona del comprador', '<span style="font-size:13px">Galicia, Asturias, Cantabria, Extremadura, Baleares y Canarias</span><span class="hint">Sus solicitudes van a la Oficina comercial de Zucami, en Mensajes.</span>') +
         card('Qué ve el comprador', '<div style="display:flex;gap:10px;align-items:center">' + av('LG', AZ, 40, '50%') + '<span><strong>Laura García</strong><br><span class="hint">Responsable comercial · Zona Nordeste · ES EN CA</span></span></div>' + btn('Contactar con Laura') + '<span class="hint">El mensaje llega a su bandeja en Agroolink.</span>'))
    return pantalla(b, ('Laura García', 'Equipo comercial · detalle'), tab='Empresa')
def k_bandeja():
    sol = lambda est, estilo, emp_, d, prod, txt, acc: ('<div class="card" style="gap:6px"><div style="display:flex;justify-content:space-between;align-items:center">' + st(est, estilo) + '<span class="hint">' + d + '</span></div>'
                                                    '<strong style="font-size:14px">' + emp_ + '</strong><span class="hint">' + prod + '</span><span style="font-size:13px;color:#33424C">«' + txt + '»</span>'
                                                    '<div style="display:flex;gap:8px">' + btn(acc, True, True) + btn('Reasignar') + '</div></div>')
    b = ('<div><span class="hint">Zucami · comercial</span><h1 style="margin:0;font-size:22px;font-weight:700">Mis solicitudes</h1><span class="hint">Te llegan las de tu zona; las demás las ve la Dirección comercial.</span></div>' +
         chips(['Abiertas 3', 'Respondidas 18', 'Cerradas 41']) +
         nota('<strong>Responder hoy:</strong> Granja Los Olmos lleva 20 h esperando. A las 48 h se avisa a la Dirección comercial.', '#FFF4E0', '#F3DFB8') +
         sol('Nueva', AZST, 'Avícola Montsià', 'Tarragona · hace 2 h', 'Aviarios · nave nueva · 60.000 aves', 'Queremos pasar de jaula a aviario en 2027. ¿Podéis visitarnos?', 'Responder') +
         sol('Responder hoy', WN, 'Granja Los Olmos', 'Lleida · hace 20 h', 'Climatización · ampliación', 'Busco cooling para la nave 2. ¿Tenéis instaladores en Lleida?', 'Responder') +
         sol('En conversación', GR, 'Huevos del Ebro SL', 'Zaragoza · ayer', 'Recogida de huevos · reposición', 'Gracias por la oferta, la revisamos esta semana.', 'Abrir') +
         card('', '<div style="display:flex;justify-content:space-between"><span><strong style="font-size:20px">9 h</strong><br><span class="hint">tu tiempo medio de respuesta · compromiso 24 h</span></span>' + btn('Ausente') + '</div>'))
    return pantalla(b, avatar='LG')
def k_hilo():
    c = (registro('Solicitud por la ficha de Zucami Aviary Pro · zona Cataluña → Laura García', 'ayer 16:02') +
         burbuja('Avícola Montsià · comprador', 'Queremos pasar de jaula a aviario en 2027. ¿Podéis visitarnos?', 'ayer', False) +
         burbuja('Laura · Zucami', 'Hola, encantada. Puedo ir la semana que viene. ¿Os viene bien el jueves a las 10?', '11:20', True) +
         registro('Javier Ortega (Dirección comercial) ha leído la conversación', '11:31'))
    return hilo('AM', '#7A8B6F', 'Avícola Montsià', 'Solicitud · Aviary Pro · atiende Laura García', c, 'El comprador ve «Zucami» y el nombre de pila de quien responde; nunca teléfonos ni emails. «Traducir» traduce al leer; queda el original.')
def k_interno():
    c = (registro('Zona cambiada por Javier Ortega: + La Rioja', '2 oct') + registro('Granja del Segre lleva 48 h sin respuesta · aviso a Dirección comercial', 'ayer 18:00') +
         burbuja('Javier Ortega · Dirección comercial', 'Laura, ¿la puedes atender hoy o se la paso a Pedro?', 'ayer 18:05', False) +
         burbuja('Laura García', 'Pásasela a Pedro, esta semana estoy en ferias.', '08:50', True) +
         registro('Solicitud de Granja del Segre reasignada de Laura García a Pedro Lima', '09:05'))
    return hilo('LG', AZ, 'Laura García', 'Equipo comercial · hilo interno', c, 'Fecha, autor y cambio quedan guardados. No se puede borrar; el superadmin puede consultarlo si hay un desacuerdo.')

# ---------- 005b · Fabricante con sucursales (Big Dutchman) ----------
def s_aviso():
    b = ('<div class="card" style="gap:10px"><span class="hint">De: Agroolink · avisos<br>Para: Anna Becker (Sede) y administradores de Big Dutchman Ibérica · copia al superadmin</span>'
         '<strong style="font-size:16px">Lucía Pérez se ha unido a Big Dutchman Ibérica</strong><span style="font-size:13.5px">Hola, Anna: una persona nueva se ha unido a la sucursal Big Dutchman Ibérica.</span>' +
         ''.join('<div style="display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-top:1px solid #EEF1EE;font-size:13px"><span class="hint" style="font-size:12.5px">%s</span><strong style="font-weight:500;text-align:right">%s</strong></div>' % kv for kv in
                 [('Persona', 'Lucía Pérez'), ('Cargo', 'Directora de Big Dutchman Ibérica'), ('Dominio', '@bigdutchman.es · verificado'), ('Rol', 'Administradora de la sucursal'), ('Fecha', '18 oct 2026, 16:02')]) +
         '<div style="display:flex;gap:8px">' + btn('Ver el equipo', True, True) + btn('No le conozco') + '</div><span class="hint">Si nadie lo revisa en 7 días, el acceso se mantiene.</span></div>')
    return SB + '<div class="top"><strong style="flex:1;font-size:15px">Correo</strong></div><div style="padding:14px 12px;display:flex;flex-direction:column;gap:12px">' + b + '</div>'
def s_paises():
    reg = lambda t, ps: card(t, '<div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join('<span class="chip" style="height:30px;font-size:12px">%s <span style="color:%s;font-weight:600;margin-left:4px">%s</span></span>' % (p, AZ if s != '—' else '#B42318', s) for p, s in ps) + '</div>')
    b = (paso('Paso 4 de 8 · Países', 'Qué países atiende cada sucursal', 'Con esto, cada solicitud llega a la sucursal correcta.') +
         '<div style="display:flex;justify-content:space-between;align-items:center"><span class="hint">23 países asignados</span>' + btn('Importar Excel') + '</div>' +
         reg('Europa', [('España', 'SG'), ('Portugal', 'SG'), ('Francia', 'SG'), ('Alemania', 'EU'), ('Italia', '2')]) +
         reg('América', [('EE. UU.', 'US'), ('México', 'MX'), ('Brasil', 'LA'), ('Chile', 'LA'), ('Perú', 'LA')]) +
         reg('Asia', [('China', 'Sede'), ('Vietnam', 'Sede'), ('India', '—')]) +
         nota('<strong>Italia la cubren dos sucursales:</strong> va a la principal y la otra recibe copia. <strong>Países sin sucursal</strong> (India): los atiende la Sede global.') +
         card('Así elige el comprador su país', campo('País o región', 'México') + '<span style="font-size:13px">Tu solicitud irá a <strong>Big Dutchman México</strong></span>' + btn('Enviar a mi sucursal', True)))
    return asistente(b, pie('Continuar'))
def s_permisos():
    filas = [('Marca, logo y frase', 'Sede'), ('Ficha global y «Sobre la empresa»', 'Sede'), ('Ficha base de los productos', 'Sede'), ('Países de cada sucursal', 'Sede'),
             ('Página de la sucursal: texto y fotos', 'Sucursal'), ('Productos destacados en su región', 'Sucursal'), ('Versión local de las fichas', 'Sucursal'),
             ('Contenidos locales', 'Propone la sucursal, aprueba la Sede'), ('Solicitudes de sus países', 'Sucursal · la Sede las ve'), ('Su equipo comercial o distribuidores', 'Sucursal')]
    b = (paso('Paso 4 de 8 · Permisos', 'Qué decide la Sede y qué cada sucursal', 'La marca y la ficha base son comunes. Lo local lo gestiona cada sucursal.') +
         card('', ''.join(fila('', t, '', st(q, AZST if q == 'Sede' else 'background:#EEF6EE;color:#0E5A3A' if q == 'Sucursal' else WN), i > 0) for i, (t, q) in enumerate(filas))) +
         '<span style="display:flex;gap:10px;align-items:center;font-size:13px"><span style="width:40px;height:24px;border-radius:12px;background:' + AZ + ';position:relative;flex:none"><span style="position:absolute;top:3px;right:3px;width:18px;height:18px;border-radius:50%;background:#FFFFFF"></span></span>Avisarme cuando una sucursal cambie su página o sus destacados</span>')
    return asistente(b, pie('Continuar'))
def s_pagina():
    b = ('<div><span class="hint">Big Dutchman LATAM · sucursal · borrador</span><h1 style="margin:0;font-size:21px;font-weight:700">Página de la sucursal</h1><span class="hint">Es lo que ve un comprador de tu región. La marca y el logo vienen de la Sede.</span></div>' +
         campo('Nombre', 'Big Dutchman LATAM') + campo('Ciudad', 'São Paulo, Brasil') + campo('Frase', 'Soluciones avícolas para un futuro más sostenible', 'máx. 70') +
         card('Zonas de venta', chips(['Brasil', 'Colombia', 'Perú', 'Chile', 'Argentina', 'Ecuador'], ()) + '<span class="hint">' + svg(I['lock'], 13) + ' Las asigna la Sede</span>') +
         card('Productos destacados en tu región', '<span class="hint">6 de 6 · del catálogo de Big Dutchman</span>' + chips(['BD Aviary Pro', 'BD Nest Pro', 'BD EggFlow', 'BD FeedLine', 'BD DrinkTech', 'BD Aviary Compact'], ())) +
         card('Contacto de la sucursal', fila('', 'Las solicitudes llegan a', 'Equipo LATAM · 3 personas · en Mensajes', '', False) + fila('', 'Idiomas', 'PT · ES · EN')) +
         nota('Al publicar, la Sede recibe un aviso.'))
    foot = '<div class="foot" style="bottom:84px;padding-bottom:10px">' + btn('Guardar borrador') + '<span class="btnp" style="flex:1;height:44px;background:' + AZ + '">Publicar página</span></div>'
    return pantalla(b, tab='Empresa', foot=foot, avatar='RS', pad=180)
def s_hilo():
    c = (registro('Nueva versión de la ficha base ChickBox (capacidad y consumo). La versión local de México queda en «Revisar cambios de la Sede»', 'lun') +
         burbuja('Carlos Méndez · LATAM', 'Revisado. En México lo vendemos con ventilación reforzada, lo añado en nuestra versión.', '11:58', False) +
         registro('Big Dutchman LATAM activó ChickBox en México con versión local', '12:10') +
         burbuja('Anna Becker · Sede', 'Perfecto. Si algún cliente pregunta por Perú, nos lo pasáis por aquí.', '12:14', True))
    return hilo('BL', '#B5121B', 'Big Dutchman LATAM', 'Sucursal · México, Colombia, Perú · 18 productos', c, 'Activaciones, versiones locales y cambios de la ficha base quedan por escrito. Nada se borra: solo se archiva.')

# ---------- 005c · Sucursal de un grupo (Aviagen Ibérica) ----------
def u_tipo():
    sede = lambda t, v: fila(svg(I['lock'], 16), t, v, '', True)
    b = (paso('Paso 1 de 8', 'Tipo de empresa', 'Eres una sucursal: la marca y el catálogo vienen de la Sede; tú completas lo de tu país.') +
         '<div class="card" style="gap:6px;border:2px solid ' + AZ + '"><span style="display:flex;justify-content:space-between;align-items:center"><strong>Sucursal o filial</strong>' + st('Del CRM', AZST) + '</span><span class="hint">de Aviagen · Sede del grupo · ya está en Agroolink</span><span style="font-size:12.5px;color:' + AZ + ';font-weight:600">¿No es correcto? Pedir cambio</span></div>' +
         card('Viene de la Sede · no lo editas', sede('Marca y logo', 'Aviagen').replace('border-top:1px solid #EEF1EE', '', 1) + sede('Actividad', 'Fabricante · Servicios') + sede('Especies', 'Avicultura · reproductoras, pollos de engorde') +
              sede('Rama', 'Genética · animales y líneas genéticas') + sede('Catálogo base', 'Ross® · Arbor Acres® · Indian River®')) +
         card('Es tuyo · lo editas tú', fila('', 'Países', 'España · Portugal', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Editar</span>', False) +
              fila('', 'Contacto', 'Equipo de Aviagen Ibérica · 4 personas', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Editar</span>') +
              fila('', 'Destacados', 'Qué productos se ven primero', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Elegir</span>') + fila('', 'Contenidos', 'Noticias y documentos en español y portugués')) +
         nota('Un comprador de España o Portugal llega a tu equipo; si es de otro país, va a la Sede o a la sucursal que lo atiende.'))
    return asistente(b, pie('Continuar'))
def u_hilo():
    c = (registro('Pablo Ruiz se unió a Aviagen Ibérica (sucursal) y entró directamente · aviso a la Sede y al superadmin', '15 oct') +
         burbuja('Emma Clark · Sede', 'Bienvenido, Pablo. Activa Ross 308 y Ross 708 para España y Portugal cuando tengas la versión local.', '15 oct', False) +
         registro('La Sede publicó una nueva versión de Ross 308 (índices 2026). Tu versión local queda en «Revisar cambios de la Sede»', '10:30') +
         burbuja('Pablo Ruiz · Aviagen Ibérica', 'Recibido. Lo reviso hoy y actualizo la versión de España.', '10:41', True))
    return hilo('AV', '#C8102E', 'Aviagen · Sede', 'Sede del grupo · marca, catálogo y especies', c, 'Lo que hables con la Sede queda aquí: altas, avisos y cambios de la ficha base.')

# ---------- 005d · Distribuidor multimarca (NewFarms) ----------
def x_elegir():
    prod = lambda n, m, ficha, est, on: ('<div style="display:flex;gap:10px;align-items:center;padding:10px 0;border-top:1px solid #EEF1EE"><span style="width:22px;height:22px;border-radius:6px;flex:none;' +
                                         ('background:' + AZ + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center' if on else 'border:1.5px solid #B9C6BE') + '">' + (svg(I['ok'], 13, 3) if on else '') + '</span>'
                                         '<span style="flex:1;min-width:0"><strong style="font-size:13.5px">' + n + '</strong><br><span class="hint">' + m + ' · ' + ficha + '</span></span>' + st(est, WN if 'Valid' in est else 'background:#EEF6EE;color:#0E5A3A') + '</div>')
    b = ('<div><span class="hint">Productos · añadir</span><h1 style="margin:0;font-size:21px;font-weight:700">Añadir productos a tu catálogo</h1><span class="hint">Si el producto ya existe, usas su ficha y solo adaptas tu versión local.</span></div>'
         '<div style="height:44px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;gap:8px;padding:0 12px;font-size:14px">' + svg(I['lupa'], 18) + 'aviario ponedoras</div>' +
         chips(['Marca ▾', 'Tipo ▾'], ()) +
         card('', prod('Zucami Aviary Pro', 'Zucami', 'ficha oficial', 'Validación de Zucami', True).replace('border-top:1px solid #EEF1EE', '', 1) + prod('Zucami Aviary Edge', 'Zucami', 'ficha oficial', 'Validación de Zucami', True) +
              prod('Zucami Nest Pro', 'Zucami', 'ficha oficial', 'Validación de Zucami', True) + prod('Comedero Roxell Feedmax', 'Roxell', 'propuesta por un distribuidor', 'Al momento', False)) +
         card('¿Dónde los vendes?', chips(['España', 'Portugal', '+ País'], (0, 1))) +
         nota('Entran ya en tu catálogo como «Distribuido». Zucami recibe un aviso para validarte; cuando lo haga, apareces en su «Dónde comprar» como «Distribuidor validado».') +
         '<span style="font-size:13px;color:' + AZ + ';font-weight:600">¿No lo encuentras? Subir un producto nuevo →</span>')
    foot = '<div class="foot" style="bottom:84px;padding-bottom:10px"><span class="btnp" style="flex:1;height:44px;background:' + AZ + '">Añadir 3 productos</span></div>'
    return pantalla(b, tab='Productos', foot=foot, avatar='NF', pad=180)
def x_subir():
    b = (paso('Productos · subir', 'Subir un producto nuevo', 'Con lo básico basta para publicarlo. Podrás completarlo después.') + campo('Marca', 'Roxell') + campo('Nombre del producto', 'Comedero Roxell Minimax') +
         campo('Referencia o EAN', 'RX-MNX', 'evita duplicados') + campo('Tipo de producto', 'Comederos') +
         '<div class="card" style="border-color:#F3DFB8;background:#FFF8EC;gap:6px"><strong style="font-size:14px">¿Es este?</strong><span class="hint">Ya existe en Agroolink con un nombre parecido</span>'
         '<span style="font-size:13px"><strong>Roxell Minimax</strong> · comedero de pollitos · propuesto por Agrovet Ibérica</span><div style="display:flex;gap:8px">' + btn('Es este, usarlo', True, True) + btn('No, es otro') + '</div></div>' +
         card('Fotos y ficha técnica', '<div style="display:flex;gap:8px">' + btn(svg(I['up'], 16) + '&nbsp;Foto') + btn(svg(I['up'], 16) + '&nbsp;PDF del fabricante') + '</div><span class="hint">Revisamos los archivos al subirlos: sin teléfonos, emails ni webs.</span>') +
         card('Invitar a Roxell', '<span class="hint">Opcional · le avisamos de que su producto está en Agroolink.</span>'))
    return asistente(b, pie('Publicar', 'Cancelar'))
def x_validacion():
    b = (paso('Marcas · validación', 'Validación de Zucami', 'Al añadir productos de Zucami, la marca recibe un aviso. Puedes añadir un mensaje.') +
         '<div class="card" style="flex-direction:row;align-items:center;gap:10px">' + emp('ZU', '#1E8A3C', 40) + '<span style="flex:1"><strong>Zucami Poultry Equipment</strong><br><span class="hint">Fabricante · equipamiento avícola · en Agroolink</span></span></div>' +
         card('Productos que has añadido', chips(['Aviary Pro', 'Aviary Edge', 'Nest Pro', 'EggFlow', 'FeedLine'], ())) + card('¿Dónde?', chips(['España ×', 'Portugal ×', '+ País o región'], (0, 1))) +
         campo('Mensaje para Zucami', 'Distribuimos equipamiento avícola en España y Portugal desde hace 12 años…') +
         card('Lo que recibe Zucami', '<span style="font-size:13px"><strong>NewFarms</strong> · distribuidor · pide Aviary Pro, Aviary Edge, Nest Pro · España, Portugal</span><div style="display:flex;gap:6px">' + btn('Rechazar') + btn('Ajustar') + btn('Aprobar', True) + '</div>'
              '<span class="hint">Al aprobar, Zucami crea un acuerdo de distribución y NewFarms recibe las fichas sincronizadas para su versión local.</span>'))
    return asistente(b, pie('Enviar a Zucami', 'Anterior'))
def x_delegaciones():
    dele = lambda t, lugar, atiende, borde: fila(emp('NF', '#2E7D4F', 32), t, lugar + ' · atiende ' + atiende, '<span class="hint">Mensajes</span>', borde)
    b = (paso('Paso 7 de 8 · Contacto', 'Delegaciones', 'A quién llega cada consulta. Todo entra en Solicitudes y Mensajes.') +
         card('Delegaciones', dele('Sede central', 'Madrid', 'España', False) + dele('Delegación Portugal', 'Lisboa', 'Portugal', True) + dele('Delegación LATAM', 'Santiago de Chile', 'Chile, Perú, Colombia', True), '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">+ Delegación</span>') +
         card('Motivos de contacto', ''.join(fila('', m, d, '', i > 0) for i, (m, d) in enumerate([('Información de un producto', 'Delegación del país del comprador'), ('Pedido o presupuesto', 'Delegación del país del comprador'),
                                                                                                   ('Servicios (asesoría, logística)', 'Equipo técnico · 4'), ('Soy fabricante y busco distribuidor', 'Dirección comercial')]))) +
         card('Así contacta el comprador', campo('Motivo de contacto', 'Información de un producto') + campo('Mensaje', 'Escribe tu consulta…') + btn('Enviar mensaje', True) +
              '<span class="hint">Sin pedir teléfono ni email: la respuesta llega por Mensajes.</span>') + contactos())
    return asistente(b, pie('Continuar'))
def x_hilo_fab():
    c = (registro('NewFarms añadió 3 productos de Zucami a su catálogo · pendientes de validación', '16 oct') + registro('Zucami validó Aviary Pro y Nest Pro · rechazó ClimaLine', '13:05') +
         burbuja('Javier Ortega · Zucami', 'ClimaLine solo lo vende nuestro equipo comercial en Aragón. Los otros dos, adelante.', '13:05', False) +
         burbuja('Laura García · NewFarms', 'Entendido, lo quitamos de Aragón. ¿Podemos ofrecerlo en Navarra?', '13:20', True))
    return hilo('ZU', '#1E8A3C', 'Zucami', 'Marca que vendes · 2 validados · 1 rechazado', c, 'La validación de la marca y sus motivos quedan por escrito. No se puede borrar; el superadmin puede consultarlo.')
def x_hilo_sol():
    c = (registro('Solicitud por la ficha de Zucami EggFlow · comprador en Zaragoza → delegación de Zaragoza', 'ayer 09:12') +
         burbuja('Huevos del Ebro · comprador', 'Necesitamos reponer la recogida de huevos de dos naves. ¿Plazo de entrega?', 'ayer', False) +
         burbuja('Sergio · NewFarms Zaragoza', 'Hola, tenemos stock para una nave; la segunda en 3 semanas. Os mando oferta hoy.', '12:40', True))
    return hilo('HE', '#7A8B6F', 'Huevos del Ebro SL', 'Solicitud · Zucami EggFlow · delegación de Zaragoza', c, 'El comprador ve «NewFarms» y el nombre de pila de quien responde; nunca teléfonos ni emails.')

# ---------- 005 · Fab-Dist: lo que faltaba ----------
def d_cabecera_admin():
    b = (paso('Paso 2 de 8', 'Cabecera de la ficha', 'La marca y las sociedades vienen del CRM; el resto lo escribes tú.') +
         nota('<strong>Modo superadmin:</strong> marca y sociedades se guardan en el CRM.', '#FFF4E0', '#F3DFB8') +
         campo('Nombre de marca', 'DSM-Firmenich', 'se guarda en el CRM') + campo('Actividad principal', 'Fabricante global de nutrición animal') +
         campo('Frase de presentación', 'Ciencia, innovación y soluciones en nutrición animal', 'máx. 70') +
         card('Sociedades', fila('', 'Sede central', 'DSM-Firmenich AG · Kaiseraugst, Suiza', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Editar</span>', False) +
              fila('', 'ES · DSM Nutritional Products Ibérica', 'Tarragona · versión local activa', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Editar</span>') +
              fila('', 'BR · DSM Produtos Nutricionais Brasil', 'São Paulo · versión local activa', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Editar</span>') +
              '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Ver las 12 filiales · + Añadir filial</span>', st('Editable', WN)) +
         card('Botones de la cabecera', chips(['Encontrar distribuidor', 'Quiero ser distribuidor', 'Solicitar información'], (0,)) + '<span class="hint">El principal lo fija el tipo de empresa. Sin botón de web: el comprador contacta por Mensajes.</span>'))
    return asistente(b, pie('Continuar'))
def d_hilo():
    c = (registro('Acuerdo creado por Marta López: Vitaminas y Enzimas · Zona Centro · 58 productos', '12 mar') +
         registro('Cambio en la ficha base de Hy-D® 1,25 %: «Saco 25 kg» → «Saco 20 kg». La versión local de NutriGan queda en «Revisar cambios del fabricante»', '09:15') +
         burbuja('Laura García · NutriGan', 'Visto. Actualizo nuestra versión local. ¿Cambia el precio de tarifa con el saco de 20 kg?', '10:02', False) +
         burbuja('Marta López · DSM-Firmenich', 'Sí, os mando la tarifa nueva por aquí antes del viernes.', '10:42', True))
    return hilo('NG', '#5B6B2F', 'NutriGan Distribuciones', 'Acuerdo · Vitaminas y Enzimas · Zona Centro', c, 'Los avisos de cambios del acuerdo quedan escritos en el hilo. Nada se borra: solo se archiva.')

PROPIAS = {'k_crear': ('K2b · Crear perfil de comercial sin cuenta', k_crear), 'k_email': ('K2c · Email al comercial: tiene una solicitud', k_email), 'k_alta': ('K2d · El comercial se da de alta', k_alta),
           'k_zona': ('K3 · Detalle del comercial y su zona', k_zona), 'k_bandeja': ('K6 · Bandeja de la comercial', k_bandeja), 'k_hilo': ('KM1 · Mensajes: solicitud de un comprador', k_hilo), 'k_interno': ('KM2 · Hilo interno con la Dirección comercial', k_interno),
           's_aviso': ('S2b · Aviso a la Sede y a la sucursal', s_aviso), 's_paises': ('S3 · Países de cada sucursal', s_paises), 's_permisos': ('S4 · Qué decide la Sede y qué cada sucursal', s_permisos),
           's_pagina': ('S5 · Página de la sucursal', s_pagina), 's_hilo': ('SM1 · Hilo Sede ↔ sucursal', s_hilo), 'u_tipo': ('U1 · Tipo de empresa cuando eres sucursal', u_tipo), 'u_hilo': ('U2 · Mensajes con la Sede', u_hilo),
           'x_elegir': ('X3 · Añadir productos que ya existen', x_elegir), 'x_subir': ('X4 · Subir un producto nuevo', x_subir), 'x_validacion': ('X5 · Validación de la marca', x_validacion),
           'x_delegaciones': ('X6 · Contacto: delegaciones', x_delegaciones), 'x_hilo_fab': ('XM1 · Hilo con el fabricante', x_hilo_fab), 'x_hilo_sol': ('XM2 · Solicitud atendida por una delegación', x_hilo_sol),
           'd_admin': ('D2s · Cabecera vista por el superadmin', d_cabecera_admin), 'd_hilo': ('DM1 · Hilo fabricante ↔ distribuidor', d_hilo)}
CAPT = {'CD1': 'D1 · Tipo de empresa · con distribuidores', 'CD2': 'D4 · Red: distribuidores', 'CD3': 'D7 · Contacto: al distribuidor de la zona', 'CD4': 'D1b-2 · Especies · modo «Excluir»',
        'CS1': 'S1 · Tipo de empresa · Sede con sucursales', 'CS2': 'S2 · Red de sucursales', 'CS3': 'S · Contacto: a la sucursal del país',
        'CX1': 'X1 · Tipo de empresa · distribuidor multimarca', 'CX2': 'X2 · Marcas que vendes', 'CX3': 'X · Contacto: a la delegación más cercana'}
TIRAS = [('MB_EmpTiraFabDist', 'Fab-Dist · lo que faltaba', ['CD1', 'CD4', 'CD2', 'CD3', 'd_admin', 'd_hilo']),
         ('MB_EmpTiraFabCom', '005a · Fabricante con comerciales', ['k_crear', 'k_email', 'k_alta', 'k_zona', 'k_bandeja', 'k_hilo', 'k_interno']),
         ('MB_EmpTiraFabSuc', '005b · Fabricante con sucursales', ['CS1', 'CS2', 's_aviso', 's_paises', 's_permisos', 'CS3', 's_pagina', 's_hilo']),
         ('MB_EmpTiraSucursal', '005c · Sucursal de un grupo', ['u_tipo', 'u_hilo']),
         ('MB_EmpTiraDistribuidor', '005d · Distribuidor multimarca', ['CX1', 'CX2', 'x_elegir', 'x_subir', 'x_validacion', 'CX3', 'x_delegaciones', 'x_hilo_fab', 'x_hilo_sol'])]

# ---------- CSS: cada pantalla aislada con anidamiento (las capturas usan el CSS del prototipo; las propias, el de proyectos_movil) ----------
def medias(css):
    out, i = '', 0
    while True:
        m = re.search(r'@media\s*\(([^)]*)\)\s*\{', css[i:])
        if not m: return out + css[i:]
        j = i + m.start(); k, n = i + m.end(), 1
        while n:
            n += {'{': 1, '}': -1}.get(css[k], 0); k += 1
        mw = re.match(r'\s*max-width:\s*(\d+)px\s*$', m.group(1))
        out += css[i:j] + (css[i + m.end():k - 1] + '\n' if (mw and int(mw.group(1)) >= 390) else ''); i = k
def css_captura(css):
    css = re.sub(r'@media \(prefers-color-scheme: dark\)\{:root:not\(\[data-theme="light"\]\)\{.*?\}\}', '', css, flags=re.S)
    css = re.sub(r':root\[data-theme="dark"\]\{.*?\}', '', css, flags=re.S)
    css = medias(css).replace('position:sticky', 'position:relative').replace('.modal{position:fixed', '.modal{position:absolute').replace('.ov{position:fixed', '.ov{position:absolute').replace('.toast{position:fixed', '.toast{position:absolute')
    css = re.sub(r':root\s*\{', '&{', css)   # las variables del prototipo pasan al contenedor de cada pantalla
    return re.sub(r'(^|\})\s*(?:html,\s*body|body)\s*\{', r'\1&{', css)
def tira(t, claves, alto):
    css, telefonos, H = {}, [], 0
    for k in claves:
        if k in CAPT:
            d = json.load(open(W + '/capture/' + k + '.json')); css['cap'] = css_captura(d['css']); h, cuerpo, cls, tt = d['h'], d['body'].replace('{{', '{ {'), 'cap', CAPT[k]
        else:
            tt, f = PROPIAS[k]; h, cuerpo, cls = int(alto.get(k, 844)), f(), 'mv'
        H = max(H, h); telefonos.append((tt, h, cuerpo, cls))
    css['mv'] = re.sub(r'(^|\})\s*body\s*\{', r'\1&{', CSS_MV).replace('.m{', '&.m{')
    Wt = len(telefonos) * 390 + (len(telefonos) - 1) * 40; H += 44
    cuerpo = '<div style="display:flex;gap:40px;align-items:flex-start;background:#FFFFFF">' + ''.join(
        '<div style="width:390px;display:flex;flex-direction:column;gap:14px"><span style="font:600 15px Poppins,sans-serif;color:#17231D;height:30px;display:flex;align-items:center">' + tt + '</span>'
        '<div class="' + cls + (' m' if cls == 'mv' else '') + '" style="width:390px;height:' + str(h) + 'px;position:relative;overflow:hidden;background:#F6F8F6;border-radius:18px;box-shadow:0 0 0 1px #E3E8E4">' + c + '</div></div>' for tt, h, c, cls in telefonos) + '</div>'
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>Móvil · ' + t + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\nbody{margin:0}\n' + ''.join('.' + k + '{\n' + v + '\n}\n' for k, v in css.items()) + '</style>\n</helmet>\n<div style="width: ' + str(Wt) + 'px; height: ' + str(H) + 'px; background: #FFFFFF;">' + cuerpo + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":' + str(Wt) + ',"height":' + str(H) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

ALTOS = {'x_elegir': 950, 'x_subir': 1010, 'x_validacion': 920, 'x_delegaciones': 1190, 'x_hilo_fab': 844, 'x_hilo_sol': 844, 'k_crear': 844, 'k_email': 844, 'k_alta': 844, 'k_zona': 990, 'k_bandeja': 1000, 'k_hilo': 844, 'k_interno': 844, 'd_admin': 1060, 'd_hilo': 844, 's_aviso': 844, 's_paises': 1030, 's_permisos': 880, 's_pagina': 1180, 's_hilo': 844, 'u_tipo': 1140, 'u_hilo': 844}   # medidas en el navegador (out/prevusr)
if __name__ == '__main__':
    alto = dict(ALTOS, **dict(a.split('=') for a in sys.argv[2:] if '=' in a))
    for k, t, claves in TIRAS:
        html = tira(t, claves, alto)
        open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
    print('ok', len(TIRAS))
