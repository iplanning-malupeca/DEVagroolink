"""Mi cuenta: Mi perfil (datos de la cuenta global) y Compras y facturación (centralizado, reflejado aquí)."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#0E5A3A;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;min-width:0;box-sizing:border-box}
.h2{margin:0;font-size:15.5px;font-weight:600}
.hd{display:flex;align-items:baseline;justify-content:space-between;gap:10px}
.hd a{font-size:12.5px}
.k{font-size:11.5px;color:#56615B}
.v{font-size:13.5px;font-weight:500}
.kv{display:flex;flex-direction:column;gap:1px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px 24px}
.glob{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 9px;border-radius:999px;background:#EEF0F3;color:#4A5560;font-size:11px;font-weight:600;white-space:nowrap}
.own{display:inline-flex;align-items:center;gap:5px;height:22px;padding:0 9px;border-radius:999px;background:#EEF6EE;color:#0E5A3A;font-size:11px;font-weight:600;white-space:nowrap}
.row{display:flex;align-items:center;gap:12px;padding:9px 0;border-top:1px solid #EEF1EE;font-size:13px}
.row:first-of-type{border-top:0}
.tg{width:36px;height:20px;border-radius:999px;background:#0E5A3A;position:relative;flex:none}
.tg::after{content:'';position:absolute;top:2px;right:2px;width:16px;height:16px;border-radius:50%%;background:#FFFFFF}
.tg.off{background:#CFD8D2}.tg.off::after{right:auto;left:2px}
.st{font-size:11px;font-weight:600;padding:2px 9px;border-radius:999px;white-space:nowrap}
.ok{background:#EEF6EE;color:#0E5A3A}.pe{background:#FFF4E0;color:#7A4B00}
.src{font-size:10.5px;font-weight:600;color:#56615B;border:1px solid #DCE3DE;border-radius:6px;padding:1px 6px;white-space:nowrap}
.tabs{display:flex;gap:22px;border-bottom:1px solid #E3E8E4;font-size:13px;color:#56615B;white-space:nowrap}
.tabs span{padding-bottom:10px}.tabs .on{color:#0E5A3A;font-weight:600;border-bottom:2px solid #0E5A3A;margin-bottom:-1px}
</style>
</helmet>
<div style="width: 1280px; height: %dpx; background: #F6F8F6; position: relative; overflow: hidden;">
  <div style="display: flex; padding-top: 68px; height: %dpx; box-sizing: border-box;">
    <dc-import name="IntSidebar" modo="personal" activo="%s" hint-size="256px,832px"></dc-import>
    <main style="flex: 1; min-width: 0; padding: 20px 28px; display: flex; flex-direction: column; gap: 16px;">
"""
TAIL = """    </main>
  </div>
  <div style="position: absolute; top: 0; left: 0; width: 1280px;">
    <dc-import name="IntHeader" persona="Samuel E." iniciales="SE" color="#0E5A3A" variante="personal" hint-size="1280px,68px"></dc-import>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1280,"height":%d}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
"""
GLOBE = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'
def glob(t='Cuenta global'): return '<span class="glob">' + GLOBE + t + '</span>'
def kv(k, v): return '<div class="kv"><span class="k">%s</span><span class="v">%s</span></div>' % (k, v)
def banner(txt):
    return ('<div style="display: flex; align-items: center; gap: 12px; padding: 12px 16px; border-radius: 14px; background: #F1F3F6; border: 1px solid #E1E5EA; font-size: 13px; color: #33424C;">'
            '<span style="width: 34px; height: 34px; border-radius: 10px; background: #FFFFFF; color: #4A5560; display: flex; align-items: center; justify-content: center; flex: none;">'
            + GLOBE.replace('12', '18', 2) + '</span><span style="flex: 1; line-height: 1.45;">' + txt + '</span><a href="#" style="white-space: nowrap; font-size: 13px;">Ir a mi cuenta global ↗</a></div>')

# ---------- Mi perfil ----------
H = 1080
t = HEAD % ('Mi cuenta · Mi perfil', H, H, 'Mi perfil')
t += """      <div><div style="font-size: 13px; color: #56615B;">Mi cuenta</div><h1 style="margin: 0; font-size: 28px; font-weight: 600;">Mi perfil</h1></div>
"""
t += '      ' + banner('<strong style="font-weight: 600;">Tus datos vienen de tu cuenta global</strong> (la misma de Agrinews). Si los cambias aquí, cambian en todas las plataformas.') + '\n'
t += """      <div style="display: grid; grid-template-columns: 1.35fr 1fr; gap: 16px; align-items: start;">
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <section class="card">
            <div class="hd"><span style="display: flex; align-items: center; gap: 10px;"><h2 class="h2">Datos personales</h2>""" + glob() + """</span><a href="#">Editar</a></div>
            <div style="display: flex; align-items: center; gap: 14px; padding: 4px 0 6px;"><span style="width: 56px; height: 56px; border-radius: 50%; background: #0E5A3A; color: #FFFFFF; font-size: 18px; font-weight: 600; display: flex; align-items: center; justify-content: center;">SE</span><span style="display: flex; flex-direction: column;"><span style="font-size: 16px; font-weight: 600;">Samuel Esteban</span><span class="k">Miembro desde marzo 2024 (Agrinews)</span></span><a href="#" style="margin-left: auto; font-size: 12.5px;">Cambiar foto</a></div>
            <div class="g2">""" + kv('Email', 'samuel@granjalosolmos.es <span class="st ok">Verificado</span>') + kv('Acceso', 'Código por email (sin contraseña)') + kv('Teléfono', '+34 6•• ••• 214') + kv('Cargo', 'Granjero') + kv('Empresa', 'Granja Los Olmos') + kv('País y provincia', 'España · Lleida') + """</div>
          </section>
          <section class="card">
            <div class="hd"><span style="display: flex; align-items: center; gap: 10px;"><h2 class="h2">Tus intereses</h2><span class="own">Agroolink</span></span><a href="#">Editar</a></div>
            <div class="g2" style="grid-template-columns: 1fr;">""" + kv('Especies', 'Avicultura · Porcino') + kv('Categorías', 'Nutrición y aditivos · Equipamiento avícola') + kv('Objetivos', 'Bienestar animal · Conversión alimenticia · Huevo campero · Reducción de costes · Sostenibilidad') + """</div>
          </section>
          <section class="card">
            <div class="hd"><span style="display: flex; align-items: center; gap: 10px;"><h2 class="h2">Tus espacios</h2><span class="own">Agroolink</span></span></div>
            <div class="row"><span style="width: 32px; height: 32px; border-radius: 50%; background: #0E5A3A; color: #FFF; font-size: 11px; font-weight: 600; display: flex; align-items: center; justify-content: center;">SE</span><span style="flex: 1;"><strong style="font-weight: 600;">Personal</strong> · buscar, comparar y proyectos</span><span class="st ok">Activo</span></div>
            <div class="row"><span style="width: 32px; height: 32px; border-radius: 9px; background: #EEF6EE; color: #0E5A3A; font-size: 16px; display: flex; align-items: center; justify-content: center;">+</span><span style="flex: 1;">Crear o vincular empresa</span><a href="#">Empezar</a></div>
            <div class="row"><span style="width: 32px; height: 32px; border-radius: 9px; background: #F1EEFB; color: #4B3BA6; font-size: 16px; display: flex; align-items: center; justify-content: center;">+</span><span style="flex: 1;">Crear perfil de experto</span><a href="#">Empezar</a></div>
          </section>
        </div>
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <section class="card">
            <div class="hd"><h2 class="h2">Notificaciones</h2><span class="own">Agroolink</span></div>
            <div class="row"><span style="flex: 1;">Propuestas a mis proyectos</span><span class="tg"></span></div>
            <div class="row"><span style="flex: 1;">Respuestas a mis consultas</span><span class="tg"></span></div>
            <div class="row"><span style="flex: 1;">Novedades según mis intereses</span><span class="tg"></span></div>
            <div class="row"><span style="flex: 1;">Resumen semanal por email</span><span class="tg off"></span></div>
          </section>
          <section class="card">
            <div class="hd"><h2 class="h2">Privacidad</h2><span class="own">Agroolink</span></div>
            <div class="row"><span style="flex: 1; line-height: 1.4;">Las empresas ven tus datos de contacto<br><span class="k">Solo cuando tú les escribes o respondes</span></span></div>
            <div class="row"><span style="flex: 1;">Aparecer en «Quién vio tu ficha»</span><span class="tg off"></span></div>
          </section>
          <section class="card">
            <div class="hd"><span style="display: flex; align-items: center; gap: 10px;"><h2 class="h2">Seguridad y cuenta</h2>""" + glob() + """</span></div>
            <div class="row"><span style="flex: 1;">Cerrar sesión en todos los dispositivos</span><a href="#">Cerrar</a></div>
            <div class="row"><span style="flex: 1;">Descargar mis datos</span><a href="#">Solicitar</a></div>
            <div class="row"><span style="flex: 1; color: #A3271B;">Eliminar cuenta</span><a href="#" style="color: #A3271B;">En mi cuenta global ↗</a></div>
          </section>
        </div>
      </div>
"""
t += TAIL % H
open(P + 'CuentaPerfil.dc.html', 'w').write(t)

# ---------- Compras y facturación ----------
H2 = 980
t = HEAD % ('Mi cuenta · Compras y facturación', H2, H2, 'Compras y facturación')
t += """      <div style="display: flex; align-items: flex-end; gap: 16px;"><div style="flex: 1;"><div style="font-size: 13px; color: #56615B;">Mi cuenta</div><h1 style="margin: 0; font-size: 28px; font-weight: 600;">Compras y facturación</h1></div></div>
"""
t += '      ' + banner('<strong style="font-weight: 600;">Se gestiona en tu cuenta global</strong> y se ve reflejado aquí: planes, suscripciones, pedidos, facturas, pagos y direcciones de Agroolink y Agrinews en un solo sitio.') + '\n'
t += """      <div class="tabs"><span class="on">Resumen</span><span>Planes y suscripciones</span><span>Pedidos</span><span>Facturas</span><span>Métodos de pago</span><span>Direcciones</span></div>
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: start;">
        <section class="card">
          <div class="hd"><h2 class="h2">Tu plan en Agroolink</h2></div>
          <span style="font-size: 20px; font-weight: 600;">Comprador Gratis</span>
          <span class="k" style="line-height: 1.45;">2 proyectos activos · comparador hasta 3 productos</span>
          <a href="#" style="height: 38px; border-radius: 10px; border: 1.5px solid #0E5A3A; display: flex; align-items: center; justify-content: center; font-size: 13.5px;">Ver planes</a>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Suscripciones</h2><a href="#">Gestionar</a></div>
          <div class="row"><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Revista digital Pro</strong><br><span class="k">9,90 €/mes · renueva el 1 nov</span></span><span class="src">Agrinews</span></div>
          <div class="row"><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Alertas de mercado</strong><br><span class="k">Gratis · semanal</span></span><span class="src">Agrinews</span></div>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Método de pago</h2><a href="#">Cambiar</a></div>
          <div style="display: flex; align-items: center; gap: 12px;"><span style="width: 46px; height: 32px; border-radius: 6px; background: #1F3A5F; color: #FFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center;">VISA</span><span style="display: flex; flex-direction: column;"><span class="v">•••• 4242</span><span class="k">Caduca 08/28 · predeterminada</span></span></div>
          <span class="k">Se usa en Agroolink y Agrinews.</span>
        </section>
      </div>
      <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 16px; align-items: start;">
        <section class="card">
          <div class="hd"><h2 class="h2">Últimos pedidos y facturas</h2><a href="#">Ver todo</a></div>
          <div class="row" style="color: #56615B; font-size: 11.5px;"><span style="width: 90px;">Fecha</span><span style="flex: 1;">Concepto</span><span style="width: 80px;">Origen</span><span style="width: 70px; text-align: right;">Importe</span><span style="width: 74px;">Estado</span><span style="width: 60px;"></span></div>
          <div class="row"><span style="width: 90px;">12 oct 2026</span><span style="flex: 1;">Entrada AviForum 2026 · 2 personas</span><span style="width: 80px;"><span class="src">Agroolink</span></span><span style="width: 70px; text-align: right;">90,00 €</span><span style="width: 74px;"><span class="st ok">Pagado</span></span><a href="#" style="width: 60px; font-size: 12.5px;">Factura</a></div>
          <div class="row"><span style="width: 90px;">1 oct 2026</span><span style="flex: 1;">Revista digital Pro · octubre</span><span style="width: 80px;"><span class="src">Agrinews</span></span><span style="width: 70px; text-align: right;">9,90 €</span><span style="width: 74px;"><span class="st ok">Pagado</span></span><a href="#" style="width: 60px; font-size: 12.5px;">Factura</a></div>
          <div class="row"><span style="width: 90px;">18 sep 2026</span><span style="flex: 1;">Informe técnico «Ventilación en broilers»</span><span style="width: 80px;"><span class="src">Agrinews</span></span><span style="width: 70px; text-align: right;">19,00 €</span><span style="width: 74px;"><span class="st ok">Pagado</span></span><a href="#" style="width: 60px; font-size: 12.5px;">Factura</a></div>
          <div class="row"><span style="width: 90px;">2 sep 2026</span><span style="flex: 1;">Webinar «Bienestar en ponedoras»</span><span style="width: 80px;"><span class="src">Agroolink</span></span><span style="width: 70px; text-align: right;">0,00 €</span><span style="width: 74px;"><span class="st pe">Inscrito</span></span><span style="width: 60px;"></span></div>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Direcciones</h2><a href="#">Editar</a></div>
          <div class="kv"><span class="k">Facturación</span><span class="v" style="line-height: 1.45;">Granja Los Olmos SL · B25••••87<br><span style="font-weight: 400; font-size: 12.5px;">Partida Els Plans s/n, 25001 Lleida</span></span></div>
          <div class="kv"><span class="k">Envío</span><span class="v" style="font-weight: 400; font-size: 12.5px;">La misma que facturación</span></div>
        </section>
      </div>
      <p style="margin: 0; font-size: 12px; color: #56615B;">Lo que compras en una empresa a través de Agroolink (presupuestos, pedidos) se ve en <a href="#">Mis proyectos</a> y en <a href="#">Mensajes</a>; aquí solo lo que pagas a Agroolink o Agrinews.</p>
"""
t += TAIL % H2
open(P + 'CuentaCompras.dc.html', 'w').write(t)

# ---------- menú lateral: MI CUENTA ----------
p = P + 'IntSidebar.dc.html'; s = open(p).read()
a = """    const cuenta = { titulo: 'MI CUENTA', chip: '', items: [
      it('Mi perfil', I.user), it('Configuración', I.gear), it('Idioma y zona', I.globe), it('Ayuda y contacto', I.help)
    ]};"""
if a in s:
    s = s.replace(a, """    const cuenta = { titulo: 'MI CUENTA', chip: 'Global', chipFondo: '#EEF0F3', chipTinta: '#4A5560', items: [
      it('Mi perfil', I.user), it('Compras y facturación', I.card), it('Idioma y zona', I.globe), it('Ayuda y contacto', I.help)
    ]};""")
    s = s.replace("      help: 'M12 3a9", "      card: 'M3 6h18v12H3zM3 10h18M7 15h4',\n      help: 'M12 3a9", 1)
    open(p, 'w').write(s)

# ---------- índice ----------
c = json.load(open(P + 'canvas.json')); B = c['boards']; N = c['notes']
B['CuentaPerfil.dc.html'] = {'h': H, 'page': 'intranet', 'title': 'C1 · Mi cuenta · Mi perfil (datos de la cuenta global + lo propio de Agroolink)', 'w': 1280, 'x': 0, 'y': 3720}
B['CuentaCompras.dc.html'] = {'h': H2, 'page': 'intranet', 'title': 'C2 · Mi cuenta · Compras y facturación (centralizado, reflejado aquí)', 'w': 1280, 'x': 1360, 'y': 3720}
N['intTitulo4'] = {'kind': 'title1', 'maxW': 2640, 'page': 'intranet', 'text': 'Mi cuenta · lo global (cuenta Agrinews) y lo propio de Agroolink', 'w': 240, 'x': 0, 'y': 3420}
o = c['order']
for k in ['CuentaPerfil.dc.html', 'CuentaCompras.dc.html']:
    if k not in o: o.append(k)
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
