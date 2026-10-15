"""Compras y facturación: una pantalla por pestaña, con la misma cabecera que CuentaCompras (C2)."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
base = open(P + 'CuentaCompras.dc.html').read()
i = base.index('      <div class="tabs">'); j = base.index('\n', i) + 1
head, tail = base[:i], base[base.index('    </main>'):]
TABS = ['Resumen', 'Planes y suscripciones', 'Pedidos', 'Facturas', 'Métodos de pago', 'Direcciones']
EXTRA = ('.tb{width:100%;border-collapse:collapse;font-size:13px}.tb th{font-size:11.5px;font-weight:500;color:#56615B;text-align:left;padding:8px 10px;border-bottom:1px solid #E3E8E4;white-space:nowrap}'
         '.tb td{padding:10px;border-bottom:1px solid #EEF1EE;vertical-align:middle}.tb tr:last-child td{border-bottom:0}.r{text-align:right !important;white-space:nowrap}'
         '.sel td{background:#F2F7F3}.chip{display:inline-flex;align-items:center;height:30px;padding:0 12px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12.5px;white-space:nowrap}'
         '.chip.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}.btn{height:38px;padding:0 16px;border-radius:10px;border:1.5px solid #0E5A3A;color:#0E5A3A;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;box-sizing:border-box}'
         '.btnp{height:38px;padding:0 16px;border-radius:10px;background:#0E5A3A;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;white-space:nowrap}'
         '.bar{height:6px;border-radius:3px;background:#E3E8E4;overflow:hidden}.bar span{display:block;height:100%;background:#0E5A3A}.er{background:#FDECEA;color:#A3271B}.gr{background:#F1F3F6;color:#4A5560}'
         '.li{display:flex;gap:8px;font-size:12.5px;line-height:1.45}.li::before{content:"✓";color:#0E5A3A;font-weight:700}')
head = head.replace('</style>', EXTRA + '\n</style>', 1)

def tabs(on):
    return '      <div class="tabs">' + ''.join('<span%s>%s</span>' % (' class="on"' if t == on else '', t) for t in TABS) + '</div>\n'
def src(t): return '<span class="src">%s</span>' % t
def st(t, c='ok'): return '<span class="st %s">%s</span>' % (c, t)
def table(cols, rows, right=(), sel=None):
    h = '<table class="tb"><thead><tr>' + ''.join('<th%s>%s</th>' % (' class="r"' if k in right else '', c) for k, c in enumerate(cols)) + '</tr></thead><tbody>'
    for n, r in enumerate(rows):
        h += '<tr%s>' % (' class="sel"' if n == sel else '') + ''.join('<td%s%s>%s</td>' % (' class="r"' if k in right else '', ' style="white-space: nowrap;"' if k < 2 else '', c) for k, c in enumerate(r)) + '</tr>'
    return h + '</tbody></table>'
VISA = '<span style="width: 46px; height: 32px; border-radius: 6px; background: #1F3A5F; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">VISA</span>'
SEPA = '<span style="width: 46px; height: 32px; border-radius: 6px; background: #F1F3F6; color: #1F3A5F; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none; border: 1px solid #DCE3DE;">SEPA</span>'

def board(fn, title, on, body, h=980):
    t = head.replace('<title>Mi cuenta · Compras y facturación</title>', '<title>Mi cuenta · %s</title>' % title)
    t = t.replace('height: 980px;', 'height: %dpx;' % h)
    t += tabs(on) + body + '\n' + tail.replace('"height":980', '"height":%d' % h)
    open(P + fn, 'w').write(t)

# ---- Planes y suscripciones ----
body = """      <div style="display: grid; grid-template-columns: 1.1fr 1fr 1fr; gap: 16px; align-items: stretch;">
        <section class="card" style="border: 1.5px solid #0E5A3A;">
          <div class="hd"><h2 class="h2">Tu plan en Agroolink</h2>""" + st('Actual') + """</div>
          <span style="font-size: 20px; font-weight: 600;">Comprador Gratis</span>
          <div class="kv"><span class="k" style="display: flex; justify-content: space-between;">Proyectos activos <span>1 de 2</span></span><div class="bar"><span style="width: 50%;"></span></div></div>
          <div class="kv"><span class="k" style="display: flex; justify-content: space-between;">Productos por comparación <span>hasta 3</span></span></div>
          <div class="kv"><span class="k" style="display: flex; justify-content: space-between;">Tableros <span>ilimitados</span></span></div>
          <span class="k">Sin coste, sin tarjeta.</span>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Comprador Pro</h2>""" + st('Próximamente', 'pe') + """</div>
          <span style="font-size: 18px; font-weight: 600;">9,90 €/mes <span class="k" style="font-size: 12.5px;">o 99 €/año</span></span>
          <span class="li">Proyectos activos ilimitados</span><span class="li">Comparar hasta 6 productos</span><span class="li">Tableros compartidos con tu equipo</span>
          <a href="#" class="btn" style="margin-top: auto;">Avísame cuando esté</a>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">¿Ofreces servicios?</h2></div>
          <span style="font-size: 18px; font-weight: 600;">Experto Pro <span class="k" style="font-size: 12.5px;">19,90 €/mes</span></span>
          <span style="font-size: 12.5px; color: #4A5650; line-height: 1.45;">Perfil de experto, servicios y consultas sin límite. Incluye Comprador Pro.</span>
          <a href="#" style="margin-top: auto; font-size: 13px;">Ver planes de experto y de empresa</a>
        </section>
      </div>
      <section class="card">
        <div class="hd"><h2 class="h2">Suscripciones</h2><span class="k">Sin permanencia: si cancelas, sigues teniendo acceso hasta el final del periodo pagado.</span></div>
        """ + table(['Suscripción', 'Origen', 'Precio', 'Próximo cobro', 'Método', 'Estado', ''], [
            ['<strong style="font-weight: 600;">Revista digital Pro</strong>', src('Agrinews'), '9,90 €/mes', '1 nov 2026', 'Visa •••• 4242', st('Activa'), '<a href="#">Gestionar</a> · <a href="#" style="color: #A3271B;">Cancelar</a>'],
            ['<strong style="font-weight: 600;">Alertas de mercado</strong>', src('Agrinews'), 'Gratis', 'Semanal', '—', st('Activa'), '<a href="#">Darse de baja</a>'],
            ['<strong style="font-weight: 600;">Novedades según tus intereses</strong>', src('Agroolink'), 'Gratis', 'Semanal', '—', st('Activa'), '<a href="#">Darse de baja</a>'],
            ['<strong style="font-weight: 600;">Anuario Avicultura 2026</strong>', src('Agrinews'), '29,00 €/año', '—', '—', st('Cancelada', 'gr'), '<a href="#">Reactivar</a>']], right=(2,)) + """
      </section>
      <section class="card">
        <div class="hd"><h2 class="h2">Historial de cambios</h2></div>
        <div class="row"><span style="width: 110px;" class="k">15 oct 2026</span><span style="flex: 1;">Alta en Agroolink con tu cuenta global · plan Comprador Gratis</span>""" + src('Agroolink') + """</div>
        <div class="row"><span style="width: 110px;" class="k">1 mar 2025</span><span style="flex: 1;">Alta en Revista digital Pro</span>""" + src('Agrinews') + """</div>
      </section>"""
board('CuentaPlanes.dc.html', 'Planes y suscripciones', 'Planes y suscripciones', body)

# ---- Pedidos ----
rows = [
 ['AGL-26-0142', '12 oct 2026', 'Entrada AviForum 2026 × 2', src('Agroolink'), '90,00 €', st('Pagado'), '<a href="#">Ver</a>'],
 ['AGN-26-8831', '1 oct 2026', 'Revista digital Pro · octubre', src('Agrinews'), '9,90 €', st('Pagado'), '<a href="#">Ver</a>'],
 ['AGN-26-8102', '18 sep 2026', 'Informe «Ventilación en broilers»', src('Agrinews'), '19,00 €', st('Pagado'), '<a href="#">Descargar</a>'],
 ['AGL-26-0098', '2 sep 2026', 'Webinar «Bienestar en ponedoras»', src('Agroolink'), '0,00 €', st('Inscrito', 'pe'), '<a href="#">Grabación</a>'],
 ['AGN-26-7710', '1 sep 2026', 'Revista digital Pro · septiembre', src('Agrinews'), '9,90 €', st('Pagado'), '<a href="#">Ver</a>'],
 ['AGN-26-7012', '14 ago 2026', 'Libro «Manual de bioseguridad»', src('Agrinews'), '32,00 €', st('Enviado', 'pe'), '<a href="#">Seguimiento</a>'],
 ['AGN-26-6390', '20 jul 2026', 'Curso online «Gestión de la nave»', src('Agrinews'), '45,00 €', st('Reembolsado', 'gr'), '<a href="#">Ver</a>']]
body = """      <div style="display: flex; align-items: center; gap: 8px;"><span class="chip on">Todos</span><span class="chip">Agroolink</span><span class="chip">Agrinews</span><span class="chip">2026 ▾</span>
        <div style="margin-left: auto; height: 36px; width: 260px; border: 1px solid #DCE3DE; border-radius: 10px; background: #FFFFFF; display: flex; align-items: center; padding: 0 12px; font-size: 13px; color: #8A948F;">Buscar pedido o concepto…</div></div>
      <div style="display: grid; grid-template-columns: 1fr 270px; gap: 16px; align-items: start;">
        <section class="card" style="padding: 8px 10px;">""" + table(['Nº', 'Fecha', 'Concepto', 'Origen', 'Importe', 'Estado', ''], rows, right=(4,), sel=0) + """</section>
        <section class="card">
          <div class="hd"><h2 class="h2">AGL-26-0142</h2>""" + st('Pagado') + """</div>
          <span style="font-size: 15px; font-weight: 600;">Entrada AviForum 2026</span>
          <span class="k">12–13 nov · Madrid · comprado el 12 oct 2026</span>
          <div class="row"><span style="flex: 1;">Entrada general × 2</span><span>90,00 €</span></div>
          <div class="row"><span style="flex: 1;" class="k">Incluye IVA (21 %)</span><span class="k">15,62 €</span></div>
          <div class="row" style="font-weight: 600;"><span style="flex: 1;">Total</span><span>90,00 €</span></div>
          <div class="kv"><span class="k">Asistentes</span><span style="font-size: 13px;">Samuel Esteban · Marta Esteban</span></div>
          <div class="kv"><span class="k">Pagado con</span><span style="font-size: 13px;">Visa •••• 4242</span></div>
          <div style="display: flex; gap: 8px; flex-wrap: wrap;"><a href="#" class="btnp">Ver entradas</a><a href="#" class="btn">Factura PDF</a></div>
          <a href="#" style="font-size: 12.5px;">¿Algún problema con este pedido?</a>
        </section>
      </div>"""
board('CuentaPedidos.dc.html', 'Pedidos', 'Pedidos', body)

# ---- Facturas ----
fr = [
 ['F-AGL-26-0142', '12 oct 2026', 'Entrada AviForum 2026 × 2', src('Agroolink'), '74,38 €', '15,62 €', '<strong style="font-weight: 600;">90,00 €</strong>', '<a href="#">PDF</a>'],
 ['F-AGN-26-8831', '1 oct 2026', 'Revista digital Pro · octubre', src('Agrinews'), '8,18 €', '1,72 €', '<strong style="font-weight: 600;">9,90 €</strong>', '<a href="#">PDF</a>'],
 ['F-AGN-26-8102', '18 sep 2026', 'Informe «Ventilación en broilers»', src('Agrinews'), '15,70 €', '3,30 €', '<strong style="font-weight: 600;">19,00 €</strong>', '<a href="#">PDF</a>'],
 ['F-AGN-26-7710', '1 sep 2026', 'Revista digital Pro · septiembre', src('Agrinews'), '8,18 €', '1,72 €', '<strong style="font-weight: 600;">9,90 €</strong>', '<a href="#">PDF</a>'],
 ['F-AGN-26-7012', '14 ago 2026', 'Libro «Manual de bioseguridad»', src('Agrinews'), '30,77 €', '1,23 € (4 %)', '<strong style="font-weight: 600;">32,00 €</strong>', '<a href="#">PDF</a>'],
 ['R-AGN-26-6390', '24 jul 2026', 'Rectificativa · curso «Gestión de la nave»', src('Agrinews'), '−37,19 €', '−7,81 €', '<strong style="font-weight: 600;">−45,00 €</strong>', '<a href="#">PDF</a>']]
body = """      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px;">
        <section class="card"><span class="k">Facturado en 2026</span><span style="font-size: 22px; font-weight: 600;">115,70 €</span><span class="k">6 facturas · 1 rectificativa</span></section>
        <section class="card"><span class="k">Se facturan a</span><span class="v">Granja Los Olmos SL · B25••••87</span><a href="#" style="font-size: 12.5px;">Cambiar en Direcciones</a></section>
        <section class="card"><div class="hd"><span class="k">Enviar copia de cada factura a</span><span class="tg"></span></div><span class="v">contabilidad@granjalosolmos.es</span><a href="#" style="font-size: 12.5px;">Cambiar email</a></section>
      </div>
      <div style="display: flex; align-items: center; gap: 8px;"><span class="chip on">Todas</span><span class="chip">Agroolink</span><span class="chip">Agrinews</span><span class="chip">2026 ▾</span><a href="#" class="btn" style="margin-left: auto;">Descargar 2026 (ZIP)</a></div>
      <section class="card" style="padding: 8px 10px;">""" + table(['Nº factura', 'Fecha', 'Concepto', 'Emite', 'Base', 'IVA', 'Total', ''], fr, right=(4, 5, 6)) + """</section>
      <p style="margin: 0; font-size: 12px; color: #56615B;">Cada plataforma emite sus propias facturas; aquí las tienes todas juntas. Para corregir datos fiscales de una factura ya emitida, pide una rectificativa desde la factura.</p>"""
board('CuentaFacturas.dc.html', 'Facturas', 'Facturas', body)

# ---- Métodos de pago ----
body = """      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: stretch;">
        <section class="card" style="border: 1.5px solid #0E5A3A;">
          <div style="display: flex; align-items: center; gap: 12px;">""" + VISA + """<span style="display: flex; flex-direction: column; flex: 1;"><span class="v">Visa •••• 4242</span><span class="k">Samuel Esteban · caduca 08/28</span></span>""" + st('Predeterminada') + """</div>
          <span class="k">Se usa en Agroolink y Agrinews.</span>
          <div style="display: flex; gap: 14px; font-size: 12.5px; margin-top: auto;"><a href="#">Editar</a><a href="#" style="color: #A3271B;">Eliminar</a></div>
        </section>
        <section class="card">
          <div style="display: flex; align-items: center; gap: 12px;">""" + SEPA + """<span style="display: flex; flex-direction: column; flex: 1;"><span class="v">Domiciliación SEPA</span><span class="k">ES•• •••• •••• •••• 1234 · Granja Los Olmos SL</span></span></div>
          <span class="k">Útil para suscripciones anuales y facturas de empresa.</span>
          <div style="display: flex; gap: 14px; font-size: 12.5px; margin-top: auto;"><a href="#">Hacer predeterminada</a><a href="#">Editar</a><a href="#" style="color: #A3271B;">Eliminar</a></div>
        </section>
        <section class="card" style="border: 1.5px dashed #CFD8D2; background: #FBFCFB;">
          <h2 class="h2">Añadir método de pago</h2>
          <a href="#" class="btn" style="justify-content: flex-start;">+ Tarjeta</a><a href="#" class="btn" style="justify-content: flex-start;">+ Domiciliación SEPA</a>
          <span class="k">La transferencia se elige al pagar.</span>
        </section>
      </div>
      <section class="card">
        <div class="hd"><h2 class="h2">Qué método usa cada cobro</h2><span class="k">Si no eliges, se usa el predeterminado.</span></div>
        """ + table(['Cobro', 'Origen', 'Importe', 'Método'], [
            ['Revista digital Pro', src('Agrinews'), '9,90 €/mes', 'Visa •••• 4242 <a href="#" style="margin-left: 8px; font-size: 12.5px;">Cambiar</a>'],
            ['Próximas compras', src('Agroolink'), '—', 'Predeterminado (Visa •••• 4242)']], right=(2,)) + """
      </section>
      <div style="display: flex; align-items: center; gap: 10px; font-size: 12.5px; color: #56615B;"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg>El pago lo gestiona una pasarela segura; ni Agroolink ni Agrinews guardan los datos completos de tu tarjeta.</div>"""
board('CuentaPagos.dc.html', 'Métodos de pago', 'Métodos de pago', body)

# ---- Direcciones ----
body = """      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start;">
        <section class="card">
          <div class="hd"><h2 class="h2">Datos de facturación</h2><a href="#">+ Añadir</a></div>
          <div style="border: 1.5px solid #0E5A3A; border-radius: 12px; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px;">
            <div class="hd"><span class="v">Granja Los Olmos SL</span>""" + st('Predeterminada') + """</div>
            <span style="font-size: 13px; line-height: 1.5;">CIF B25••••87<br>Partida Els Plans s/n · 25001 Lleida · España</span>
            <span class="k">Facturas a contabilidad@granjalosolmos.es</span>
            <div style="display: flex; gap: 14px; font-size: 12.5px; margin-top: 4px;"><a href="#">Editar</a></div>
          </div>
          <div style="border: 1px solid #E3E8E4; border-radius: 12px; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px;">
            <div class="hd"><span class="v">Samuel Esteban · a título personal</span></div>
            <span style="font-size: 13px; line-height: 1.5;">NIF ••••5678Z<br>C/ Major 12, 2.º · 25001 Lleida · España</span>
            <div style="display: flex; gap: 14px; font-size: 12.5px; margin-top: 4px;"><a href="#">Hacer predeterminada</a><a href="#">Editar</a><a href="#" style="color: #A3271B;">Eliminar</a></div>
          </div>
          <span class="k">Al pagar puedes elegir a nombre de quién va la factura.</span>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Direcciones de envío</h2><a href="#">+ Añadir</a></div>
          <div style="border: 1.5px solid #0E5A3A; border-radius: 12px; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px;">
            <div class="hd"><span class="v">Granja</span>""" + st('Predeterminada') + """</div>
            <span style="font-size: 13px; line-height: 1.5;">Samuel Esteban · +34 6•• ••• 214<br>Partida Els Plans s/n · 25001 Lleida · España</span>
            <span class="k">Entrega de 8:00 a 14:00</span>
            <div style="display: flex; gap: 14px; font-size: 12.5px; margin-top: 4px;"><a href="#">Editar</a></div>
          </div>
          <div style="border: 1px solid #E3E8E4; border-radius: 12px; padding: 12px 14px; display: flex; flex-direction: column; gap: 4px;">
            <div class="hd"><span class="v">Oficina</span></div>
            <span style="font-size: 13px; line-height: 1.5;">C/ Major 12, 2.º · 25001 Lleida · España</span>
            <div style="display: flex; gap: 14px; font-size: 12.5px; margin-top: 4px;"><a href="#">Hacer predeterminada</a><a href="#">Editar</a><a href="#" style="color: #A3271B;">Eliminar</a></div>
          </div>
          <span class="k">Para libros, revistas en papel y material de eventos.</span>
        </section>
      </div>
      <p style="margin: 0; font-size: 12px; color: #56615B;">Estas direcciones se comparten entre Agroolink y Agrinews. La ubicación de tus explotaciones para recibir propuestas se indica en cada <a href="#">proyecto</a>.</p>"""
board('CuentaDirecciones.dc.html', 'Direcciones', 'Direcciones', body)

# ---- índice ----
c = json.load(open(P + 'canvas.json')); B = c['boards']; N = c['notes']
L = [('CuentaPlanes.dc.html', 'C2a · Compras · Planes y suscripciones'), ('CuentaPedidos.dc.html', 'C2b · Compras · Pedidos (detalle a la derecha)'),
     ('CuentaFacturas.dc.html', 'C2c · Compras · Facturas'), ('CuentaPagos.dc.html', 'C2d · Compras · Métodos de pago'), ('CuentaDirecciones.dc.html', 'C2e · Compras · Direcciones')]
for n, (fn, ti) in enumerate(L):
    B[fn] = {'h': 980, 'page': 'intranet', 'title': ti, 'w': 1280, 'x': n * 1360, 'y': 5200}
    if fn not in c['order']: c['order'].append(fn)
N['intTitulo5'] = {'kind': 'title1', 'maxW': 6720, 'page': 'intranet', 'text': 'Compras y facturación · una pantalla por pestaña', 'w': 240, 'x': 0, 'y': 4900}
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
