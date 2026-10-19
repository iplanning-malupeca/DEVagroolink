"""Front por piezas (3): ventanas (modales) del front, rehechas desde Figma (F11, F12, F17, F20–F27, F29–F35, F47, F48, F51, F56, F57, F61, F63)
con las reglas de Agroolink: nadie escribe ni ve teléfonos, emails ni webs. «Pedir información», «Pedir asesoramiento» y «Escribir» son
mensajes de Agroolink; ya no hay campos de teléfono ni email (la cuenta ya sabe quién eres). «Visitar la web» (F52) no se hace.
El acceso sigue los textos del alta (Login1Email, Login1bCodigo, Login2SinCuenta, Login5Creada); el registro es el de Agrinews.
Uso: python3 tools/front_modales.py <carpeta>/project   → escribe FrMod*.dc.html y modales.json"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from front_piezas import DEST, B, IMG, svg, I, doc, cabecera
import front_paginas  # añade sus imágenes e iconos
IMG.update({k: B(v) for k, v in {'aviario': 'b8d696a2d6be6376c254991f79f9fb67'}.items()})

I.update({'x': 'M6 6l12 12M18 6 6 18', 'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01', 'mapa': 'M9 4 3 6v14l6-2 6 2 6-2V4l-6 2zM9 4v14M15 6v14', 'persona': 'M12 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM4 21a8 8 0 0 1 16 0',
          'campana': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4', 'mail': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6',
          'candado': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4', 'play': 'M8 5v14l11-7z', 'mas': 'M12 5v14M5 12h14', 'tablero': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z'})
LOGO = IMG['logo']

def fondo(modal, w=560, alto=900):
    pagina = ('<div aria-hidden="true" style="position: absolute; top: 68px; left: 0; right: 0; bottom: 0; padding: 32px 60px; display: flex; gap: 24px;">'
              '<div style="width: 520px; height: 420px; border-radius: 18px; background: #E9EEEA;"></div><div style="flex: 1; display: flex; flex-direction: column; gap: 14px;">'
              '<div style="width: 60%; height: 34px; border-radius: 8px; background: #E9EEEA;"></div><div style="width: 80%; height: 16px; border-radius: 6px; background: #EEF2EF;"></div>'
              '<div style="width: 70%; height: 16px; border-radius: 6px; background: #EEF2EF;"></div><div style="width: 40%; height: 44px; border-radius: 10px; background: #E9EEEA; margin-top: 20px;"></div></div></div>')
    return (cabecera() + pagina + '<div style="position: absolute; inset: 0; background: rgba(7, 43, 30, .45);"></div>'
            '<div role="dialog" aria-modal="true" style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: ' + str(w) + 'px; background: #FFFFFF; border-radius: 20px; box-shadow: 0 24px 60px rgba(7, 43, 30, .3); padding: 26px 28px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px;">' + modal + '</div>')

def tit(t, sub='', icono=None):
    return ('<div style="display: flex; gap: 12px; align-items: flex-start;">' + ('<span style="width: 40px; height: 40px; border-radius: 12px; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I[icono], 20) + '</span>' if icono else '') +
            '<div style="flex: 1;"><h2 style="margin: 0; font-size: 20px; font-weight: 700;">' + t + '</h2>' + ('<p style="margin: 3px 0 0; font-size: 14px; color: #4A5650;">' + sub + '</p>' if sub else '') + '</div>'
            '<button type="button" aria-label="Cerrar" style="width: 34px; height: 34px; border-radius: 50%; border: 0; background: #F1F4F2; color: #33424C; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I['x'], 16, 2) + '</button></div>')
def campo(l, v, alto=40, ph=True):
    return ('<label style="display: flex; flex-direction: column; gap: 5px;"><span style="font-size: 13.5px; font-weight: 600;">' + l + '</span><span style="min-height: ' + str(alto) + 'px; box-sizing: border-box; border: 1px solid #D5DED8; border-radius: 10px; padding: 9px 12px; font-size: 14px; color: ' + ('#8A948F' if ph else '#17231D') + ';">' + v + '</span></label>')
def pie_btn(sec, pri):
    return '<div style="display: flex; gap: 10px; justify-content: flex-end; padding-top: 4px;">' + ('<a href="#" class="btn2" style="border-color: #D5DED8; color: #17231D;">' + sec + '</a>' if sec else '') + '<a href="#" class="btn">' + pri + '</a></div>'
def aviso(t, color='#F2F7F3', borde='#E1ECE4'):
    return '<div style="display: flex; gap: 10px; align-items: flex-start; padding: 10px 12px; border-radius: 12px; background: ' + color + '; border: 1px solid ' + borde + '; font-size: 12.5px; color: #33424C;"><span style="color: #0E5A3A; flex: none;">' + svg(I['candado'], 16) + '</span><span>' + t + '</span></div>'
def chips(ls, on=0):
    return '<div style="display: flex; flex-wrap: wrap; gap: 6px;">' + ''.join('<span class="chip' + (' on' if i == on else '') + '">' + t + '</span>' for i, t in enumerate(ls)) + '</div>'
def producto_mini(k, n, d):
    return '<div style="display: flex; gap: 12px; align-items: center; padding: 10px; border-radius: 12px; background: #F6F8F6;"><img src="' + IMG[k] + '" alt="" style="width: 52px; height: 52px; border-radius: 10px; object-fit: cover;"><span style="display: flex; flex-direction: column;"><strong style="font-size: 14.5px;">' + n + '</strong><span style="font-size: 12.5px; color: #56615B;">' + d + '</span></span></div>'
def radio(t, d, on=False):
    return ('<label style="display: flex; gap: 12px; align-items: center; padding: 11px 12px; border-radius: 12px; border: ' + ('1.5px solid #0E5A3A; background: #F2F7F3' if on else '1px solid #E3E8E4') + ';"><span style="width: 18px; height: 18px; border-radius: 50%; border: 2px solid ' + ('#0E5A3A' if on else '#B9C6BE') + '; display: flex; align-items: center; justify-content: center; flex: none;">' +
            ('<span style="width: 8px; height: 8px; border-radius: 50%; background: #0E5A3A;"></span>' if on else '') + '</span><span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 14px; font-weight: 600;">' + t + '</strong>' + ('<span style="font-size: 12.5px; color: #56615B;">' + d + '</span>' if d else '') + '</span></label>')
REGLA = 'Se envía como mensaje de Agroolink desde tu cuenta. No escribas teléfonos, emails ni webs: el mensaje no se enviaría. Te responden en Mensajes.'

def m_info():
    return fondo(tit('Pedir información', 'A Cargill, sobre este producto. La recibe su equipo o el distribuidor de tu zona.', 'msg') + producto_mini('of_bolsa', 'OptiFeed®', 'Cargill · Aditivos') +
                 '<span style="font-size: 13.5px; font-weight: 600;">¿Qué necesitas?</span>' + chips(['Precio y plazo', 'Disponibilidad en mi zona', 'Ficha técnica', 'Una muestra', 'Otra cosa']) +
                 campo('Tu mensaje', 'Tengo dos naves de broilers en Lleida (40.000 aves). ¿Qué dosis recomendáis y con qué plazo de entrega?', 96, False) +
                 '<span style="font-size: 12.5px; color: #4A5650;">Enviada por <strong>Samuel E.</strong> · Granja Los Olmos · Lleida</span>' + aviso(REGLA) + pie_btn('Cancelar', 'Enviar ' + svg(I['flecha'], 16, 2)))

def m_asesoramiento():
    return fondo(tit('Pedir asesoramiento', 'Cuéntale tu caso al Dr. Carlos Martínez. Te responde en Mensajes.', 'persona') +
                 '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">' + campo('Tipo de consulta', 'Nutrición avícola ▾', 40, False) + campo('Cómo prefieres', 'A distancia ▾', 40, False) + '</div>' +
                 campo('Tu consulta', 'Describe brevemente tu consulta, tus objetivos y el tipo de apoyo que necesitas…', 110) + aviso(REGLA) + pie_btn('Cancelar', 'Enviar consulta ' + svg(I['flecha'], 16, 2)))

def m_guardar():
    return fondo(tit('Guardar en un tablero', 'Elige dónde guardar OptiFeed®.', 'guardar') + producto_mini('of_bolsa', 'OptiFeed®', 'Cargill · Aditivos') +
                 radio('Nutrición avícola', '8 productos', True) + radio('Proveedores posibles', '5 productos') + radio('Proyecto · Nueva granja 2027', '12 productos') + radio('Comparativa de aditivos', '4 productos') +
                 '<a href="#" class="ver" style="font-size: 14px;">' + svg(I['mas'], 16, 2) + 'Crear un tablero</a>' + campo('Nota (opcional)', 'Ej.: comparar con otros aditivos, pedir precio…', 40) +
                 '<span class="hint">Plan Gratis: 4 de 5 tableros.</span>' + pie_btn('Cancelar', 'Guardar'), 520)

def m_guardado():
    return fondo('<div style="display: flex; flex-direction: column; align-items: center; gap: 12px; text-align: center; padding: 10px 0;"><span style="width: 56px; height: 56px; border-radius: 50%; background: #0E5A3A; color: #FFFFFF; display: flex; align-items: center; justify-content: center;">' + svg(I['ok'], 28, 2.6) + '</span>'
                 '<h2 style="margin: 0; font-size: 20px;">Guardado</h2><p style="margin: 0; color: #4A5650;">OptiFeed® está en tu tablero <strong>«Nutrición avícola»</strong>.</p>'
                 '<a href="#" class="btn" style="width: 100%; justify-content: center;">Ver el tablero ' + svg(I['flecha'], 16, 2) + '</a><a href="#" style="font-size: 14px;">Seguir navegando</a></div>', 400)

def m_ficha():
    doc_ = ('<div style="display: flex; gap: 16px; align-items: center; padding: 14px; border-radius: 14px; background: #F6F8F6;"><span style="width: 72px; height: 92px; border-radius: 8px; background: #FFFFFF; border: 1px solid #E3E8E4; display: flex; align-items: center; justify-content: center; color: #C0392B; font-weight: 700; font-size: 13px;">PDF</span>'
            '<span style="display: flex; flex-direction: column; gap: 3px; font-size: 13px; color: #4A5650;"><strong style="font-size: 15px; color: #17231D;">OptiFeed® · Ficha técnica</strong><span>PDF · 2,4 MB · actualizada en septiembre de 2026</span><span>Revisada por Agroolink: sin datos de contacto</span></span></div>')
    return fondo(tit('Descargar la ficha técnica', 'Hay una ficha por idioma: elige el tuyo.', 'descarga') + doc_ + '<span style="font-size: 13.5px; font-weight: 600;">Idioma</span>' + chips(['Español', 'English', 'Português', 'Français']) +
                 '<span class="hint">Las fichas se descargan con tu cuenta: la empresa ve que la has descargado, no tus datos de contacto.</span>' + pie_btn('Cancelar', svg(I['descarga'], 16, 2) + 'Descargar'), 520)

def m_disponible():
    item = lambda ic, t: '<span style="display: flex; gap: 8px; align-items: center; font-size: 13.5px;"><span style="color: #0E5A3A;">' + svg(I[ic], 16) + '</span>' + t + '</span>'
    return fondo('<div style="display: flex; align-items: center; gap: 8px;"><span style="color: #0E5A3A;">' + svg(I['pais'], 18) + '</span><strong style="flex: 1;">Disponible en Lleida, España</strong><a href="#" style="font-size: 13px;">Cambiar zona</a>'
                 '<button type="button" aria-label="Cerrar" style="width: 30px; height: 30px; border-radius: 50%; border: 0; background: #F1F4F2; display: flex; align-items: center; justify-content: center;">' + svg(I['x'], 14, 2) + '</button></div>'
                 '<span class="kick" style="color: #56615B;">Distribuidor oficial en tu zona</span>'
                 '<div class="card" style="padding: 14px; display: flex; flex-direction: column; gap: 8px;"><div style="display: flex; gap: 12px; align-items: center;"><span style="width: 44px; height: 44px; border-radius: 10px; background: #2E8B57; color: #FFFFFF; font-weight: 700; display: flex; align-items: center; justify-content: center;">AS</span>'
                 '<span style="display: flex; flex-direction: column;"><strong>Agropecuària del Segre</strong><span style="font-size: 12px; font-weight: 600; color: #0E5A3A;">Distribuidor autorizado de Cargill</span></span></div>' +
                 item('mapa', 'Cubre Lleida, Huesca y Zaragoza') + item('ok', 'Disponible: entrega en 48–72 h') + item('persona', 'Asesoramiento técnico y comercial') + '</div>'
                 '<a href="#" class="btn" style="justify-content: center;">' + svg(I['msg'], 17) + 'Escribir a Agropecuària del Segre</a><a href="#" class="ver" style="justify-content: center; font-size: 14px;">Ver su ficha ' + svg(I['flecha'], 16, 2) + '</a>', 440)

def m_nodisponible():
    op = lambda ic, t, d: ('<a href="#" class="card" style="display: flex; gap: 12px; align-items: center; padding: 12px 14px; color: #17231D;"><span style="width: 36px; height: 36px; border-radius: 10px; background: #F1F4F2; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I[ic], 18) + '</span>'
                           '<span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 14px; font-weight: 600;">' + t + '</strong><span style="font-size: 12.5px; font-weight: 400; color: #56615B;">' + d + '</span></span>' + svg(I['der'], 15, 2) + '</a>')
    return fondo('<div style="display: flex; align-items: center; gap: 8px;"><span style="color: #A3271B;">' + svg(I['pais'], 18) + '</span><strong style="flex: 1;">No disponible en Lleida, España</strong><a href="#" style="font-size: 13px;">Cambiar zona</a></div>'
                 '<div style="display: flex; gap: 12px; align-items: flex-start; padding: 12px; border-radius: 12px; background: #FFF8EC; border: 1px solid #F3DFB8;"><span style="color: #7A4B00;">' + svg(I['info'], 20) + '</span><span style="font-size: 14px;"><strong>Aún no hay distribuidor de OptiFeed® en tu zona.</strong><br><span style="color: #4A5650;">Puedes ver otros países o escribir directamente al fabricante.</span></span></div>' +
                 op('mapa', 'Ver en otro país', 'Dónde se vende ahora') + op('msg', 'Escribir a Cargill', 'Por Mensajes de Agroolink') + op('manos', 'Quiero distribuirlo', 'Si eres distribuidor en esta zona') + op('campana', 'Avisarme cuando llegue', 'Te avisamos en Avisos y por email'), 440)

def m_zona():
    provs = ''.join('<span style="padding: 9px 12px; border-radius: 8px; font-size: 14px; ' + ('background: #EEF6EE; color: #0E5A3A; font-weight: 600;' if p == 'Lleida' else '') + '">' + p + '</span>' for p in ['Huesca', 'Lleida', 'Madrid', 'Murcia', 'Navarra', 'Segovia'])
    return fondo(tit('Cambiar zona', 'Para ver la disponibilidad de OptiFeed® y quién lo vende cerca de ti.', 'pais') +
                 '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;"><div style="display: flex; flex-direction: column; gap: 8px;">' + campo('País', 'España ▾', 40, False) +
                 '<span style="border: 1px solid #D5DED8; border-radius: 10px; padding: 8px 12px; font-size: 14px; color: #8A948F;">Buscar provincia…</span><div style="display: flex; flex-direction: column; border: 1px solid #E3E8E4; border-radius: 12px; padding: 4px;">' + provs + '</div></div>'
                 '<div style="border-radius: 14px; background: #F2F7F3; padding: 18px; display: flex; flex-direction: column; gap: 8px; align-items: center; text-align: center; justify-content: center;"><span style="color: #0E5A3A;">' + svg(I['mapa'], 40, 1.4) + '</span>'
                 '<strong>Lleida, España</strong><span style="font-size: 13px; color: #4A5650;">Disponible a través de <strong>Agropecuària del Segre</strong>.</span></div></div>' + pie_btn('Cancelar', 'Usar esta zona'), 640)

def m_distribuidor():
    return fondo(tit('Quiero distribuir este producto', 'Tu solicitud llega a Cargill, que decide si te da de alta como distribuidor.', 'manos') + producto_mini('of_bolsa', 'OptiFeed®', 'Cargill · Aditivos') +
                 '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">' + campo('Tu empresa', 'AgroExport SRL (tu cuenta)', 40, False) + campo('Tipo de actividad', 'Distribuidor ▾', 40, False) +
                 campo('Dónde vendes', 'España ▾', 40, False) + campo('Provincias', 'Lleida, Huesca, Zaragoza', 40, False) + '</div>' +
                 campo('Cuéntanos', 'A qué clientes vendes, con qué equipo y qué marcas distribuyes ya…', 84) + aviso(REGLA) + pie_btn('Cancelar', 'Enviar solicitud ' + svg(I['flecha'], 16, 2)), 600)

def m_comercial():
    pasos = ''.join('<span style="display: flex; align-items: center; gap: 6px; font-size: 13px; ' + ('color: #0E5A3A; font-weight: 600;' if i < 2 else 'color: #8A948F;') + '"><span style="width: 24px; height: 24px; border-radius: 50%; ' + ('background: #0E5A3A; color: #FFFFFF;' if i < 2 else 'border: 1.5px solid #C9D2CC;') + ' display: flex; align-items: center; justify-content: center; font-size: 12px;">' + str(i + 1) + '</span>' + t + '</span>' for i, t in enumerate(['Tu zona', 'Tu comercial', 'Mensaje']))
    sucursal = lambda ini, n, d: ('<div style="display: flex; gap: 12px; align-items: center; padding: 12px 0; border-top: 1px solid #EEF1EE;"><span style="width: 40px; height: 40px; border-radius: 50%; background: #E9F0F9; color: #1D4E89; font-weight: 600; font-size: 13px; display: flex; align-items: center; justify-content: center;">' + ini + '</span>'
                                  '<span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 14.5px;">' + n + '</strong><span style="font-size: 12.5px; color: #56615B;">' + d + '</span></span><a href="#" class="btn" style="height: 34px; font-size: 13.5px;">' + svg(I['msg'], 15) + 'Escribir</a></div>')
    return fondo(tit('Encuentra tu comercial', 'Zucami tiene un comercial por zona. Le escribes por Mensajes.', 'persona') + '<div style="display: flex; gap: 22px;">' + pasos + '</div>' +
                 '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">' + campo('País', 'España ▾', 40, False) + campo('Provincia', 'Segovia ▾', 40, False) + '</div>' +
                 '<span class="kick" style="color: #56615B; padding-top: 4px;">Tu comercial</span>' + sucursal('JP', 'Jorge Pérez', 'Comercial · Castilla y León · Zucami España') +
                 '<span class="kick" style="color: #56615B; padding-top: 4px;">Otras sedes de Zucami</span>' + sucursal('ZM', 'Zucami México', 'Querétaro · México y Centroamérica') + sucursal('ZI', 'Zucami Italia', 'Bérgamo · Italia') +
                 '<span class="hint">No mostramos teléfonos ni emails de las sedes: todo va por Mensajes.</span>', 580)

def m_video():
    caps = ''.join('<span style="display: flex; gap: 12px; font-size: 13.5px; padding: 6px 0; border-top: 1px solid #EEF1EE;"><span style="color: #56615B; width: 40px;">' + t + '</span>' + n + '</span>' for t, n in [('00:00', 'Introducción'), ('00:28', 'Bienestar animal'), ('00:56', 'Diseño modular'), ('01:40', 'Manejo y recogida de huevos'), ('02:10', 'Sostenibilidad y rentabilidad')])
    return fondo(tit('Vídeo del producto', 'Zucami Aviary Pro · 2:36') + '<div style="position: relative; border-radius: 14px; overflow: hidden;"><img src="' + IMG['aviario'] + '" alt="" style="width: 100%; height: 330px; object-fit: cover; display: block; filter: brightness(.8);">'
                 '<span style="position: absolute; left: 50%; top: 50%; transform: translate(-50%, -50%); width: 64px; height: 64px; border-radius: 50%; background: #FFFFFF; color: #0E5A3A; display: flex; align-items: center; justify-content: center;">' + svg(I['play'], 26, 2) + '</span>'
                 '<span style="position: absolute; left: 14px; right: 14px; bottom: 12px; height: 4px; border-radius: 2px; background: rgba(255,255,255,.4);"><span style="display: block; width: 18%; height: 100%; background: #FFFFFF; border-radius: 2px;"></span></span></div>'
                 '<strong style="font-size: 15px;">Capítulos</strong><div>' + caps + '</div>', 680)

def acceso(cuerpo, w=420):
    return fondo('<div style="display: flex; justify-content: space-between; align-items: center;"><img src="' + LOGO + '" alt="Agroolink" style="height: 26px;"><button type="button" aria-label="Cerrar" style="width: 30px; height: 30px; border-radius: 50%; border: 0; background: #F1F4F2; display: flex; align-items: center; justify-content: center;">' + svg(I['x'], 14, 2) + '</button></div>' + cuerpo, w)
def icono_grande(ic, fondo_='#EEF6EE', tinta='#0E5A3A'):
    return '<span style="align-self: center; width: 60px; height: 60px; border-radius: 50%; background: ' + fondo_ + '; color: ' + tinta + '; display: flex; align-items: center; justify-content: center;">' + svg(I[ic], 28, 2) + '</span>'
def m_acceso():
    return acceso(icono_grande('mail') + '<div style="text-align: center;"><h2 style="margin: 0; font-size: 21px;">Accede para continuar</h2><p style="margin: 4px 0 0; font-size: 14px; color: #4A5650;">Introduce tu email y te enviaremos un código de verificación si ya tienes una cuenta.</p></div>' +
                  campo('Email', 'nombre@empresa.com', 42) + '<a href="#" class="btn" style="justify-content: center; height: 42px;">Continuar</a>' + aviso('Tus datos están seguros. Solo los usamos para identificar tu cuenta.'))
def m_codigo():
    cajas = ''.join('<span style="width: 46px; height: 54px; border-radius: 10px; border: ' + ('2px solid #0E5A3A' if i == 4 else '1px solid #D5DED8') + '; display: flex; align-items: center; justify-content: center; font-size: 22px; font-weight: 600;">' + d + '</span>' for i, d in enumerate(['4', '8', '2', '9', '', '']))
    return acceso(icono_grande('mail') + '<div style="text-align: center;"><h2 style="margin: 0; font-size: 21px;">Introduce tu código</h2><p style="margin: 4px 0 0; font-size: 14px; color: #4A5650;">Te hemos enviado un código de 6 cifras a <strong>s•••@granjalosolmos.es</strong> · <a href="#">Cambiar</a></p></div>'
                  '<div style="display: flex; gap: 8px; justify-content: center;">' + cajas + '</div><a href="#" class="btn" style="justify-content: center; height: 42px;">Entrar</a>'
                  '<span style="text-align: center; font-size: 13px; color: #56615B;">¿No te ha llegado? Revisa el spam o reenvía el código en 0:42</span>' + aviso('Es tu cuenta de Agrinews. Si es la primera vez que entras en Agroolink, te preguntaremos cómo quieres empezar.'))
def m_sincuenta():
    ok = lambda t: '<span style="display: flex; gap: 8px; align-items: center; font-size: 14px;"><span style="color: #0E5A3A;">' + svg(I['ok'], 16, 2.4) + '</span>' + t + '</span>'
    return acceso(icono_grande('persona') + '<div style="text-align: center;"><h2 style="margin: 0; font-size: 21px;">Parece que todavía no tienes una cuenta</h2><p style="margin: 4px 0 0; font-size: 14px; color: #4A5650;">Para continuar necesitas una cuenta gratuita. Solo te llevará un minuto.</p></div>'
                  '<div style="display: flex; flex-direction: column; gap: 8px; padding: 12px 14px; border-radius: 12px; background: #F2F7F3;">' + ok('Accede a fichas técnicas y contenido exclusivo') + ok('Guarda productos en tus tableros') + ok('Recibe recomendaciones para tu producción') + '</div>'
                  '<a href="#" class="btn" style="justify-content: center; height: 42px;">Crear cuenta</a><a href="#" class="btn2" style="justify-content: center;">Ya tengo una cuenta</a>'
                  '<span class="hint" style="text-align: center;">La cuenta se crea con el registro de Agrinews y vuelves aquí al terminar.</span>', 440)
def m_creada():
    return acceso(icono_grande('ok', '#0E5A3A', '#FFFFFF') + '<div style="text-align: center;"><h2 style="margin: 0; font-size: 21px;">¡Cuenta creada!</h2><p style="margin: 4px 0 0; font-size: 14px; color: #4A5650;">Ya puedes usar Agroolink con tu cuenta de Agrinews.</p></div>' +
                  aviso('Vuelves a la página donde estabas: hemos guardado lo que ibas a hacer (guardar OptiFeed® en un tablero).') + '<a href="#" class="btn" style="justify-content: center; height: 42px;">Continuar ' + svg(I['flecha'], 16, 2) + '</a>', 440)

PIEZAS = [('FrModInfo', 'M01 · Pedir información a la empresa (mensaje, sin teléfono ni email)', m_info), ('FrModAsesoramiento', 'M02 · Pedir asesoramiento a un experto', m_asesoramiento),
          ('FrModGuardar', 'M03 · Guardar en un tablero', m_guardar), ('FrModGuardado', 'M04 · Guardado en el tablero', m_guardado), ('FrModFicha', 'M05 · Descargar la ficha técnica (una por idioma)', m_ficha),
          ('FrModDisponible', 'M06 · Disponible en tu zona: distribuidor oficial (Escribir, Ver ficha)', m_disponible), ('FrModNoDisponible', 'M07 · No disponible en tu zona: qué puedes hacer', m_nodisponible),
          ('FrModZona', 'M08 · Cambiar zona', m_zona), ('FrModDistribuidor', 'M09 · Quiero distribuir este producto', m_distribuidor), ('FrModComercial', 'M10 · Encuentra tu comercial / sede (Escribir)', m_comercial),
          ('FrModVideo', 'M11 · Vídeo del producto con capítulos', m_video), ('FrModAcceso', 'M12 · Acceso · email', m_acceso), ('FrModCodigo', 'M13 · Acceso · código', m_codigo),
          ('FrModSinCuenta', 'M14 · Acceso · todavía no tienes cuenta', m_sincuenta), ('FrModCreada', 'M15 · Acceso · cuenta creada', m_creada)]
if __name__ == '__main__':
    for k, t, f in PIEZAS:
        open(DEST + k + '.dc.html', 'w').write(doc('Front · ' + t, 1440, 900, f()))
    json.dump({'piezas': [(k, t) for k, t, f in PIEZAS]}, open(DEST + '../modales.json', 'w'), ensure_ascii=False)
    print('ok', len(PIEZAS))
