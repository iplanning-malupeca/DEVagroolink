"""Qué se bloquea por login gratuito, por límite de plan o por plan de pago (19/10/2026).
Fuente única para desarrollo: data/planes.json (+ docs/modelo-producto/planes.json en el repo).
Genera la página «Planes · qué se bloquea» (matriz + 3 ventanas en escritorio) y los boards MB_Plan* (móvil).
Uso: python3 tools/planes.py <canvas.json> [alturas.json]"""
import json, os, sys, html
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = '/Volumes/DEV/GIT/DEVagroolink/'
CANVAS = sys.argv[1]; DEST = os.path.dirname(CANVAS) + '/'
ALT = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
e = html.escape

REGLAS = [
    'Preguntar nunca se bloquea para el comprador. Los expertos reciben y responden sin límite; la empresa Gratis ve las consultas de 3 compradores y las siguientes se guardan hasta que pasa a Pro (nunca se pierden).',
    'Contactos fuera de Agroolink: prohibidos para todos y en todos los planes. Nunca se muestran teléfonos, emails, webs, WhatsApp, Telegram, redes sociales, direcciones exactas ni códigos QR; todo se habla en Mensajes y queda registrado.',
    'Filtro restrictivo: si un mensaje, propuesta, solicitud, ficha, descripción, servicio, proyecto, nombre de archivo o imagen contiene un contacto (también disimulado: «arroba», «punto com», números en letras), NO se envía ni se publica: se marcan los datos y el autor tiene que quitarlos. Cada intento queda registrado; al tercero en 30 días se pausan sus envíos y el superadmin revisa la cuenta.',
    'Archivos (PDF, imágenes, documentos): se revisan al subirlos (texto, texto de imágenes por OCR, códigos QR, enlaces y metadatos). Si contienen un contacto no se adjuntan ni se publican: se indica la página y el dato para corregirlo; los metadatos (autor, empresa, email) se eliminan siempre.',
    'Sin cuenta solo se mira (buscar, ver fichas y cambiar de idioma); todo lo demás pide la cuenta gratis, que se pide al pulsar la acción, nunca al entrar ni al navegar.',
    'Las funciones de pago se ven; el aviso salta al pulsarlas, no al verlas.',
    'Al bajar de plan nada se borra: lo que sobra pasa a solo lectura o se despublica (el usuario elige qué mantiene).',
    'Traducción automática (ES · EN · PT · FR) en todos los planes.',
    'Verificado no se compra.']
# bloqueo: login = pide cuenta gratuita · limite = funciona hasta un número · plan = solo en un plan de pago · nunca = no existe en ningún plan · libre
# Sin cuenta solo se puede mirar: se define por lo que SÍ permite; cualquier acción nueva pide la cuenta gratis por defecto
VISITANTE = {'permite': [('buscar', 'Buscar y filtrar productos, empresas y expertos'), ('ver_fichas', 'Ver las fichas completas'), ('traduccion', 'Verlas en su idioma (traducción automática)')],
             'resto': 'Todo lo demás pide la cuenta gratis: guardar, comparar, solicitar, Mensajes, proyectos, tableros, documentos, alertas y seguir.',
             'regla': 'Por defecto, toda acción nueva pide la cuenta gratis; solo las de esta lista se permiten sin cuenta.',
             'franja_planes': 'Sin cuenta puedes buscar y ver todas las fichas. Para guardar, comparar, preguntar y crear proyectos, crea tu cuenta gratis: 30 segundos, sin contraseña ni tarjeta.'}
CUENTAS = {
 'todos': {'label': 'Todas las cuentas · con la cuenta gratis', 'color': '#17231D', 'soft': '#EEF1EF', 'cols': ['Cuenta gratis'], 'acciones': [
   ('solicitud', 'Enviar solicitudes y consultas', ['Ilimitadas · la 1.ª pide email verificado'], 'login'),
   ('mensajes', 'Mensajes', ['Sí'], 'login'),
   ('guardar', 'Guardar en tableros', ['Sí'], 'login'),
   ('comparar', 'Comparar productos', ['Sí'], 'login'),
   ('documentos', 'Descargar documentos técnicos', ['Sí'], 'login'),
   ('seguir', 'Seguir empresas y crear alertas', ['Sí'], 'login'),
   ('contacto', 'Ver teléfono, email, web, WhatsApp o redes de otro usuario', ['Nunca'], 'nunca'),
   ('escribir_contacto', 'Escribir contactos en mensajes, fichas o documentos', ['Se bloquea el envío'], 'nunca')]},
 'comprador': {'label': 'Comprador', 'color': '#0E5A3A', 'soft': '#EEF6EE', 'cols': ['Gratis', 'Pro · 9,90 € (próximamente)'], 'acciones': [
   ('proyectos', 'Publicar proyectos / RFQ', ['1', 'Ilimitados'], 'limite'),
   ('tableros', 'Tableros', ['5', 'Ilimitados'], 'limite'),
   ('comparar_max', 'Productos por comparación', ['Hasta 4', 'Hasta 10 y guardar'], 'limite'),
   ('compartir', 'Compartir tableros', ['1 colaborador', 'Con todo el equipo'], 'limite'),
   ('alertas', 'Alertas de productos y proveedores', ['5', 'Ilimitadas'], 'limite'),
   ('alertas_cambios', 'Alertas de precio, stock y ficha', ['—', 'Sí'], 'plan'),
   ('pdf', 'Exportar a PDF', ['—', 'Sí'], 'plan')]},
 'experto': {'label': 'Experto', 'color': '#4B3BA6', 'soft': '#F1EEFB', 'cols': ['Gratis', 'Pro · 19,90 €'], 'acciones': [
   ('consultas', 'Recibir y responder consultas', ['Ilimitadas', 'Ilimitadas'], 'libre'),
   ('servicios', 'Servicios publicados', ['1', 'Ilimitados'], 'limite'),
   ('candidaturas', 'Candidaturas a proyectos', ['Solo ver proyectos abiertos', 'Ilimitadas'], 'plan'),
   ('portfolio', 'Portfolio / casos', ['1', 'Ilimitado'], 'limite'),
   ('organizar', 'Consultas organizadas (estados y notas)', ['—', 'Sí'], 'plan'),
   ('contenido', 'Publicar contenido', ['—', 'Sí'], 'plan'),
   ('recomendado', 'Recomendado en búsquedas', ['—', 'Sí'], 'plan'),
   ('estadisticas', 'Estadísticas', ['Básicas', 'Avanzadas'], 'plan'),
   ('comprador_pro', 'Ventajas de Comprador Pro', ['—', 'Incluidas'], 'plan')]},
 'empresa': {'label': 'Empresa', 'color': '#1D4E89', 'soft': '#E9F0F9', 'cols': ['Gratis', 'Pro · 79 €', 'Premium · 199 €'], 'acciones': [
   ('consultas', 'Recibir y responder consultas y solicitudes', ['De 3 compradores · el resto con Pro', 'Ilimitadas', 'Ilimitadas'], 'limite'),
   ('distribucion', 'Solicitudes de distribución', ['Sí', 'Sí', 'Sí'], 'libre'),
   ('productos', 'Productos publicados', ['15', '100', 'Ilimitados'], 'limite'),
   ('miembros', 'Miembros del equipo', ['Ilimitados', 'Ilimitados', 'Ilimitados'], 'libre'),
   ('sucursales', 'Sucursales y filiales', ['Alta gratis', 'Alta gratis', 'Plan de grupo a medida'], 'medida'),
   ('leads', 'Leads organizados (estados, asignación, notas)', ['—', 'Sí', 'Sí'], 'plan'),
   ('contenido', 'Contenido vinculado', ['—', '5 al mes', 'Ilimitado'], 'plan'),
   ('destacar', 'Destacar productos', ['—', 'Extra de pago', '4 al mes'], 'plan'),
   ('oportunidades', 'Oportunidades (proyectos / RFQ del mercado)', ['Solo el número', '2 al mes', 'Ilimitadas + matching'], 'plan'),
   ('estadisticas', 'Estadísticas', ['Básicas', 'Avanzadas', 'Avanzadas + benchmark'], 'plan'),
   ('adjuntos', 'Adjuntar archivos a propuestas y mensajes (revisados: sin contactos)', ['—', '—', 'Sí'], 'plan'),
   ('exportar', 'Exportar informes de solicitudes (sin contactos)', ['—', '—', 'Sí'], 'plan'),
   ('gestor', 'Gestor de cuenta', ['—', '—', 'Sí'], 'plan')]}}
VENTANAS = {
 'login': {'cuando': 'Sin cuenta, al pulsar cualquier cosa que no sea buscar, ver una ficha o cambiar de idioma.',
           'titulo': 'Entra para {accion}', 'texto': 'Es gratis y sin contraseña: te enviamos un código a tu email.', 'botones': ['Continuar', 'Ahora no'],
           'despues': 'Al entrar, la acción se completa sola (se guarda, se envía…).'},
 'limite': {'cuando': 'Al intentar superar un número del plan (16.º producto, 2.º proyecto del comprador, 3.er servicio del experto…).',
            'titulo': 'Has llegado a {n} {cosa}', 'texto': 'Con {plan} tienes {mas}. Nada se borra: lo que ya tienes sigue publicado.',
            'botones': ['Probar {plan} 14 días', 'Ver planes', 'Ahora no'], 'despues': 'Siempre con una alternativa gratuita (archivar, despublicar…). Máximo 1 aviso por sesión; 7 días de pausa tras «Ahora no».'},
 'plan': {'cuando': 'Al pulsar una función que el plan no incluye (exportar, publicar contenido, leads organizados…). El botón se ve siempre.',
          'titulo': '{funcion} es de {plan}', 'texto': 'Qué hace y un ejemplo con sus datos.', 'botones': ['Pasar a {plan}', 'Ahora no'], 'despues': 'Comprador Pro aún no existe: el botón es «Avísame cuando esté».'},
 'filtro': {'cuando': 'Al enviar o publicar un texto, archivo o imagen con un teléfono, email, web, @usuario, enlace de WhatsApp/Telegram o QR, aunque esté disimulado.',
            'titulo': 'No se puede enviar: hay datos de contacto', 'texto': 'En Agroolink todo se habla en Mensajes. Quita los datos marcados para poder enviar.', 'botones': ['Quitar los datos marcados'],
            'despues': 'No se envía nada hasta quitarlos. Intento registrado; al tercero en 30 días se pausan los envíos y el superadmin revisa la cuenta.'},
 'medida': {'cuando': 'Sede que quiere varias sucursales con plan completo.', 'titulo': 'Plan de grupo', 'texto': 'Cada sucursal se da de alta gratis; para tenerlas con plan completo, precio a medida.', 'botones': ['Hablar con nosotros'], 'despues': 'Lo atiende el equipo comercial de Agroolink.'}}

def fuente():
    return {'version': 1, 'fecha': '2026-10-19', 'reglas': REGLAS, 'visitante': {'permite': [{'id': i, 'accion': t} for i, t in VISITANTE['permite']], 'resto': VISITANTE['resto'], 'regla': VISITANTE['regla'], 'franja_planes': VISITANTE['franja_planes']},
            'bloqueos': {'libre': 'Sin bloqueo', 'login': 'Pide login gratuito', 'limite': 'Funciona hasta un número del plan', 'plan': 'Solo en un plan de pago', 'medida': 'Precio a medida', 'nunca': 'No existe en ningún plan'},
            'cuentas': {k: {'label': c['label'], 'niveles': c['cols'], 'acciones': [{'id': a[0], 'accion': a[1], 'valores': dict(zip(c['cols'], a[2])), 'bloqueo': a[3]} for a in c['acciones']]} for k, c in CUENTAS.items()},
            'ventanas': VENTANAS}

LOGO = '<img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height: {h}px; width: auto; display: block;">'
CSS = """*{box-sizing:border-box}body{margin:0}.pl{font-family:'Poppins',system-ui,sans-serif;color:#17231D;font-size:15px;line-height:1.4}
.ic{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:6px;font-size:11px;flex:none}
.b-login{background:#FFF4E0;color:#7A4B00}.b-limite{background:#E9F0F9;color:#1D4E89}.b-plan{background:#F1EEFB;color:#4B3BA6}.b-nunca{background:#FDECEA;color:#A3271B}.b-medida{background:#EEF6EE;color:#0E5A3A}.b-libre{background:#EEF1EF;color:#56615B}
.tag{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px;border-radius:999px;font-size:12px;font-weight:600}
.btnp{height:44px;border:0;border-radius:10px;font:inherit;font-weight:600;color:#FFFFFF;display:flex;align-items:center;justify-content:center;width:100%}
.btn{height:42px;border:1px solid #D2DAE3;border-radius:10px;background:#FFFFFF;font:inherit;font-weight:500;display:flex;align-items:center;justify-content:center;width:100%;color:#17231D}
.lnk{font-size:14px;color:#56615B;text-align:center}
"""
ICO = {'login': '🔑', 'limite': '📏', 'plan': '🔒', 'nunca': '✕', 'medida': '✉', 'libre': '✓'}
LEY = [('login', 'Login gratuito'), ('limite', 'Límite del plan'), ('plan', 'Solo en plan de pago'), ('medida', 'Precio a medida'), ('nunca', 'Nunca, en ningún plan'), ('libre', 'Libre')]

def wrap(title, w, h, body):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n<div class="pl" style="width: ' + str(w) + 'px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F4F6F9;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":' + str(w) + ',"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

def celda(v, b):
    if v in ('—',): return '<span style="color:#A3ACA7">—</span>'
    if v == 'Login': return '<span class="tag b-login">🔑 Login gratis</span>'
    if v == 'Nunca' or v == 'Nunca visibles': return '<span class="tag b-nunca">✕ Nunca</span>'
    return e(v)

def matriz():
    h = ('<div style="padding:40px 48px;display:flex;flex-direction:column;gap:22px">'
         '<div style="display:flex;align-items:center;gap:14px">' + LOGO.format(h=28) + '<span style="font-size:13px;color:#56615B">Para desarrollo · fuente: planes.json</span></div>'
         '<div><div style="font-size:12px;font-weight:600;letter-spacing:.09em;color:#56615B;text-transform:uppercase">Planes</div><h1 style="margin:4px 0 0;font-size:28px;font-weight:700">Qué se bloquea y cómo</h1>'
         '<p style="margin:6px 0 0;color:#56615B;max-width:80ch">Sin cuenta solo se mira; todo lo demás pide la cuenta gratis, que se pide al pulsar. Preguntar nunca se bloquea, y ningún contacto (teléfono, email, web, WhatsApp, redes…) se ve ni se puede escribir.</p></div>'
         '<div style="display:flex;gap:8px;flex-wrap:wrap">' + ''.join('<span class="tag b-' + k + '">' + ICO[k] + ' ' + t + '</span>' for k, t in LEY) + '</div>'
         '<section style="display:grid;grid-template-columns:1fr 1.3fr;gap:0;background:#FFFFFF;border:1px solid #E1E6EC;border-radius:16px;overflow:hidden">'
         '<div style="padding:18px 22px;display:flex;flex-direction:column;gap:8px"><span class="tag b-libre" style="align-self:flex-start">Sin cuenta · solo mirar</span>' +
         ''.join('<span style="display:flex;gap:8px;font-size:14.5px"><span style="color:#0E5A3A;font-weight:700">✓</span>' + e(t) + '</span>' for _, t in VISITANTE['permite']) + '</div>'
         '<div style="padding:18px 22px;display:flex;flex-direction:column;gap:8px;background:#FFF8EC"><span class="tag b-login" style="align-self:flex-start">🔑 Todo lo demás · cuenta gratis</span><span style="font-size:14.5px">' + e(VISITANTE['resto'].split(': ', 1)[1][:1].upper() + VISITANTE['resto'].split(': ', 1)[1][1:]) + '</span>'
         '<span style="font-size:13px;color:#56615B">' + e(VISITANTE['regla']) + ' Abajo, «Gratis» es siempre con la cuenta gratis creada.</span></div></section>'
         '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px;align-items:start">')
    for k, c in CUENTAS.items():
        n = len(c['cols']); cols = '2.2fr ' + ' '.join(['1.25fr'] * n) + ' 40px'
        h += ('<section style="background:#FFFFFF;border:1px solid #E1E6EC;border-radius:16px;overflow:hidden">'
              '<div style="display:flex;align-items:center;gap:10px;padding:14px 18px;background:' + c['soft'] + '"><span style="width:12px;height:12px;border-radius:50%;background:' + c['color'] + '"></span><strong style="font-size:17px;color:' + c['color'] + '">' + e(c['label']) + '</strong></div>'
              '<div style="display:grid;grid-template-columns:' + cols + ';gap:10px;padding:10px 18px;border-bottom:1px solid #E1E6EC;font-size:12px;font-weight:600;color:#56615B"><span>Acción</span>' + ''.join('<span>' + e(x) + '</span>' for x in c['cols']) + '<span></span></div>')
        for a in c['acciones']:
            h += ('<div style="display:grid;grid-template-columns:' + cols + ';gap:10px;padding:9px 18px;border-bottom:1px solid #EEF1F4;font-size:13.5px;align-items:center">'
                  '<span style="font-weight:500">' + e(a[1]) + '</span>' + ''.join('<span>' + celda(v, a[3]) + '</span>' for v in a[2]) + '<span class="ic b-' + a[3] + '" title="' + a[3] + '">' + ICO[a[3]] + '</span></div>')
        h += '</section>'
    h += ('</div><section style="background:#FFFFFF;border:1px solid #E1E6EC;border-radius:16px;padding:18px 22px"><strong style="font-size:16px">Reglas en todos los planes</strong><ul style="margin:10px 0 0;padding-left:20px;display:flex;flex-direction:column;gap:6px;font-size:14px">' +
          ''.join('<li>' + e(r) + '</li>' for r in REGLAS) + '</ul></section>'
          '<section style="display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:14px">' +
          ''.join('<div style="background:#FFFFFF;border:1px solid #E1E6EC;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:6px"><span class="tag b-' + ('nunca' if k == 'filtro' else k) + '" style="align-self:flex-start">' + ICO.get(k, '✕') + ' Ventana «' + {'login': 'Login', 'limite': 'Límite', 'plan': 'Plan de pago', 'medida': 'A medida', 'filtro': 'Contacto bloqueado'}[k] + '»</span><span style="font-size:13px"><strong>Cuándo:</strong> ' + e(v['cuando']) + '</span><span style="font-size:13px;color:#56615B">' + e(v['despues']) + '</span></div>' for k, v in VENTANAS.items()) +
          '</section></div>')
    return h

# ---------- ventanas (escritorio 1280×800, móvil 390×844) ----------
def fondo_esc():
    return ('<div style="position:absolute;inset:0;filter:none">'
            '<div style="height:56px;background:#FFFFFF;border-bottom:1px solid #E1E6EC;display:flex;align-items:center;gap:18px;padding:0 60px">' + LOGO.format(h=26) +
            '<div style="flex:1;max-width:560px;height:40px;border:1px solid #D2DAE3;border-radius:999px;display:flex;align-items:center;padding:0 16px;color:#8A948F;font-size:14px">Buscar productos, empresas, expertos…</div><span style="flex:1"></span><span style="font-weight:600;color:#0E5A3A">Entrar</span></div>'
            '<div style="padding:28px 60px;display:grid;grid-template-columns:1fr 1fr;gap:32px"><div style="height:420px;border-radius:18px;background:linear-gradient(135deg,#DDE6DF,#C9D6CD)"></div>'
            '<div style="display:flex;flex-direction:column;gap:12px"><span style="font-size:13px;color:#56615B">DSM-Firmenich · Aditivos</span><span style="font-size:28px;font-weight:700">Probiótico para lechones y broilers</span><span style="color:#56615B">Mejora la salud intestinal en posdestete y en las primeras semanas de engorde.</span>'
            '<div style="display:flex;gap:8px"><span class="tag b-libre">Porcino</span><span class="tag b-libre">Avicultura</span></div><div style="display:flex;gap:10px;margin-top:10px"><span class="btnp" style="background:#0E5A3A;width:220px">Solicitar información</span><span class="btn" style="width:150px">Guardar</span><span class="btn" style="width:150px">Comparar</span></div></div></div>'
            '<div style="position:absolute;inset:0;background:rgba(14,19,25,.48)"></div></div>')
def fondo_mov():
    return ('<div style="position:absolute;inset:0">'
            '<div style="height:56px;background:#FFFFFF;border-bottom:1px solid #E1E6EC;display:flex;align-items:center;justify-content:space-between;padding:0 16px">' + LOGO.format(h=22) + '<span style="width:34px;height:34px;border-radius:50%;border:1px solid #D2DAE3"></span></div>'
            '<div style="padding:16px;display:flex;flex-direction:column;gap:10px"><div style="height:220px;border-radius:16px;background:linear-gradient(135deg,#DDE6DF,#C9D6CD)"></div><span style="font-size:12px;color:#56615B">DSM-Firmenich · Aditivos</span><span style="font-size:21px;font-weight:700">Probiótico para lechones y broilers</span><span style="color:#56615B;font-size:14px">Mejora la salud intestinal en posdestete.</span></div>'
            '<div style="position:absolute;left:0;right:0;bottom:0;height:64px;background:#FFFFFF;border-top:1px solid #E1E6EC;display:grid;grid-template-columns:repeat(4,1fr);font-size:11px;color:#56615B;text-align:center;align-items:center"><span style="color:#0E5A3A;font-weight:600">Explorar</span><span>Proyectos</span><span>Tableros</span><span>Tú</span></div>'
            '<div style="position:absolute;inset:0;background:rgba(14,19,25,.48)"></div></div>')
def caja(movil, color, soft, tag, titulo, texto, extra, botones):
    inner = ('<span class="tag" style="align-self:flex-start;background:' + soft + ';color:' + color + '">' + tag + '</span>'
             '<strong style="font-size:' + ('20' if movil else '22') + 'px;line-height:1.25">' + titulo + '</strong><span style="color:#56615B;font-size:14.5px">' + texto + '</span>' + extra +
             '<div style="display:flex;flex-direction:column;gap:8px;margin-top:4px">' + ''.join(
                 ('<span class="btnp" style="background:' + color + '">' + b + '</span>') if i == 0 else ('<span class="lnk">' + b + '</span>' if i == len(botones) - 1 else '<span class="btn">' + b + '</span>') for i, b in enumerate(botones)) + '</div>')
    if movil:
        return '<div style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-radius:20px 20px 0 0;padding:10px 20px 26px;display:flex;flex-direction:column;gap:12px"><span style="width:40px;height:4px;border-radius:2px;background:#D2DAE3;align-self:center;margin-bottom:6px"></span>' + inner + '</div>'
    return '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:460px;background:#FFFFFF;border-radius:20px;padding:26px 28px;display:flex;flex-direction:column;gap:12px;box-shadow:0 20px 60px rgba(0,0,0,.25)">' + inner + '</div>'
EMAIL = '<div style="height:46px;border:1.5px solid #0E5A3A;border-radius:10px;display:flex;align-items:center;padding:0 14px;color:#8A948F">tu@email.com</div><span style="font-size:12.5px;color:#56615B">Con tu cuenta de Agroolink o Agrinews. Al entrar se guarda en «Nutrición lechones».</span>'
def barra(n, de, color):
    return '<div style="display:flex;flex-direction:column;gap:6px"><div style="display:flex;justify-content:space-between;font-size:13px"><span>' + n + '</span><span style="font-weight:600">' + de + '</span></div><div style="height:6px;border-radius:3px;background:#E1E6EC"><div style="height:6px;border-radius:3px;width:100%;background:' + color + '"></div></div></div>'
def lista(items, color):
    return '<div style="display:flex;flex-direction:column;gap:6px;font-size:14px">' + ''.join('<span style="display:flex;gap:8px"><span style="color:' + color + ';font-weight:700">✓</span>' + i + '</span>' for i in items) + '</div>'
TARJ = {
 'PlanLogin': ('Ventana «Login» · sin cuenta, al pulsar Guardar', False, ('#0E5A3A', '#EEF6EE', '🔑 Gratis', 'Entra para guardar este producto', 'Es gratis y sin contraseña: te enviamos un código a tu email.', EMAIL, ['Continuar', 'Ahora no'])),
 'PlanLimite': ('Ventana «Límite» · empresa Gratis, producto 16', False, ('#1D4E89', '#E9F0F9', '📏 Plan Gratis', 'Has llegado a 15 productos', 'Con Empresa Pro publicas hasta 100. Nada se borra: tus 15 productos siguen publicados.', barra('Productos publicados', '15 de 15', '#1D4E89'), ['Probar Pro 14 días', 'Ver planes', 'Ahora no'])),
 'PlanPago': ('Ventana «Plan de pago» · experto Gratis, al pulsar Publicar contenido', False, ('#4B3BA6', '#F1EEFB', '🔒 Experto Pro', 'Publicar contenido es de Experto Pro', 'Comparte artículos y casos de éxito en tu perfil y en las fichas de tus especies.', lista(['Servicios y candidaturas ilimitados', 'Recomendado en búsquedas', 'Incluye Comprador Pro'], '#4B3BA6') + '<span style="font-size:13px;color:#56615B">19,90 €/mes · sin permanencia</span>', ['Pasar a Pro', 'Ahora no'])),
 'PlanFiltro': ('Ventana «Contacto bloqueado» · al enviar un mensaje con teléfono y email', False, ('#A3271B', '#FDECEA', '✕ Nunca en Agroolink', 'No se puede enviar: hay datos de contacto', 'En Agroolink todo se habla en Mensajes. Quita los datos marcados para poder enviar; este intento queda registrado.', '''<div style="display:flex;flex-direction:column;gap:8px"><div style="align-self:flex-end;max-width:85%;background:#E9F0F9;border-radius:14px 14px 4px 14px;padding:10px 12px;font-size:14px">Le paso precio por volumen. Llámeme al <span style="background:#FDECEA;color:#A3271B;border-radius:4px;padding:0 4px;text-decoration:underline wavy #A3271B">seis uno dos 34 56 78</span> o escríbame a <span style="background:#FDECEA;color:#A3271B;border-radius:4px;padding:0 4px;text-decoration:underline wavy #A3271B">pedro arroba granja.es</span></div><span style="font-size:12px;color:#A3271B;align-self:flex-end;font-weight:600">No enviado · 2 datos de contacto marcados</span></div>''', ['Quitar los datos marcados'])),
 'MB_PlanLogin': ('Móvil · Login al pulsar Guardar', True, ('#0E5A3A', '#EEF6EE', '🔑 Gratis', 'Entra para guardar este producto', 'Es gratis y sin contraseña: te enviamos un código a tu email.', EMAIL, ['Continuar', 'Ahora no'])),
 'MB_PlanLimite': ('Móvil · Límite: 2.º proyecto del comprador', True, ('#0E5A3A', '#EEF6EE', '📏 Plan Gratis', 'Ya tienes 1 proyecto publicado', 'Con la cuenta gratis puedes tener 1 proyecto publicado. Archiva o cierra el actual para publicar otro; nada se borra.', barra('Proyectos publicados', '1 de 1', '#0E5A3A') + '<span style="font-size:13px;color:#56615B">Comprador Pro (proyectos ilimitados) llega pronto.</span>', ['Archivar «Nueva nave 2027»', 'Avísame cuando esté Pro', 'Ahora no'])),
 'MB_PlanPago': ('Móvil · Plan de pago: exportar informes (empresa Pro)', True, ('#1D4E89', '#E9F0F9', '🔒 Empresa Premium', 'Exportar informes es de Premium', 'Descarga tus solicitudes por producto, zona y estado. Nunca incluye teléfonos ni emails.', lista(['Productos y oportunidades ilimitados', '4 productos destacados al mes', 'Gestor de cuenta'], '#1D4E89'), ['Pasar a Premium', 'Ahora no'])),
 'MB_PlanFiltro': ('Móvil · Mensaje bloqueado por datos de contacto', True, ('#A3271B', '#FDECEA', '✕ Nunca en Agroolink', 'No se puede enviar: hay datos de contacto', 'Todo se habla en Mensajes. Quita los datos marcados; el intento queda registrado.', '''<div style="display:flex;flex-direction:column;gap:8px"><div style="align-self:flex-end;max-width:85%;background:#E9F0F9;border-radius:14px 14px 4px 14px;padding:10px 12px;font-size:14px">Le paso precio por volumen. Llámeme al <span style="background:#FDECEA;color:#A3271B;border-radius:4px;padding:0 4px;text-decoration:underline wavy #A3271B">seis uno dos 34 56 78</span> o escríbame a <span style="background:#FDECEA;color:#A3271B;border-radius:4px;padding:0 4px;text-decoration:underline wavy #A3271B">pedro arroba granja.es</span></div><span style="font-size:12px;color:#A3271B;align-self:flex-end;font-weight:600">No enviado · 2 datos de contacto marcados</span></div>''', ['Quitar los datos marcados']))}

def main():
    src = fuente(); txt = json.dumps(src, ensure_ascii=False, indent=1)
    open(W + '/data/planes.json', 'w').write(txt)
    if os.path.isdir(R + 'docs/modelo-producto'): open(R + 'docs/modelo-producto/planes.json', 'w').write(txt)
    c = json.load(open(CANVAS)); B = c['boards']
    # desde el 19/10/2026 los bloqueos van en la misma página que los planes, debajo (OFF px)
    OFF = 4600
    files = {}
    hm = ALT.get('PlanBloqueos', 2200)
    files['PlanBloqueos'] = (wrap('Planes · qué se bloquea', 1280, hm, matriz()), 1280, hm, 'planes', 0, OFF, 'BL1 · Matriz: qué se bloquea por cuenta y nivel')
    for i, (k, (t, mov, a)) in enumerate(TARJ.items()):
        w, h = (390, 844) if mov else (1280, 800)
        body = (fondo_mov() if mov else fondo_esc()) + caja(mov, *a)
        if mov: files[k] = (wrap(t, w, h, body), w, h, None, None, None, t)
        else: files[k] = (wrap(t, w, h, body), w, h, 'planes', 1400, OFF + i * 900, 'BL%d · %s' % (i + 2, t))
    for k, (htm, w, h, pg, x, y, t) in files.items():
        open(DEST + k + '.dc.html', 'w').write(htm); open(W + '/project/' + k + '.dc.html', 'w').write(htm)
        if pg:
            B[k + '.dc.html'] = {'w': w, 'h': h, 'page': pg, 'x': x, 'y': y, 'title': t}
            if k + '.dc.html' not in c['order']: c['order'].append(k + '.dc.html')
    c['notes']['blt'] = {'kind': 'title1', 'maxW': 4000, 'page': 'planes', 'w': 240, 'x': 0, 'y': OFF - 300, 'text': 'Planes · qué se bloquea por login, límite o plan de pago'}
    c['notes']['bldev'] = {'fill': 'orange', 'maxH': 360, 'page': 'planes', 'size': 24, 'w': 1280, 'x': 2800, 'y': OFF, 'text':
        'PARA DESARROLLO · Bloqueos\n\nFuente única: docs/modelo-producto/planes.json (cuentas → acciones → valor por nivel + tipo de bloqueo; ventanas con cuándo salen y textos).\n\nTipos: login · límite · plan de pago · a medida · nunca.\n\nDecisiones 19/10/2026: contactos fuera de Agroolink prohibidos y filtrados (teléfono, email, web, WhatsApp, redes, QR); Empresa Gratis ve consultas de 3 compradores; Experto con consultas ilimitadas; comprador Gratis publica 1 proyecto; sucursales con alta gratis y plan de grupo a medida; traducción en todos los planes. Las versiones móviles están en MB_08 Planes.'}
    json.dump(c, open(CANVAS, 'w'), ensure_ascii=False, indent=1)
    print('ok', list(files))
main()
