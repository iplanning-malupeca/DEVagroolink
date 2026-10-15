"""Intranet consolidada · Usuario (Samuel) y Experto (Laura).
Una pantalla por entrada del menú lateral. Las que ya existían con IntSidebar se reutilizan con dc-import (una sola fuente)."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'

CSS = """
body{margin:0;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#0E5A3A;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;min-width:0;box-sizing:border-box;box-shadow:0 1px 3px rgba(16,40,28,.05)}
.h2{margin:0;font-size:16px;font-weight:600}
.hd{display:flex;align-items:center;justify-content:space-between;gap:10px}
.hd a{font-size:12.5px}
.k{font-size:11.5px;color:#56615B}
.v{font-size:13.5px;font-weight:500}
.row{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13px}
.row:first-of-type{border-top:0}
.st{font-size:11px;font-weight:600;padding:2px 9px;border-radius:999px;white-space:nowrap}
.ok{background:#EEF6EE;color:#0E5A3A}.pe{background:#FFF4E0;color:#7A4B00}.gr{background:#F1F3F6;color:#4A5560}.li{background:#F1EEFB;color:#4B3BA6}.nw{background:#E5484D;color:#FFFFFF}
.tabs{display:flex;gap:26px;border-bottom:1px solid #E3E8E4;font-size:14px;color:#56615B;white-space:nowrap}
.tabs span{padding-bottom:10px}.tabs .on{color:#0E5A3A;font-weight:600;border-bottom:2.5px solid #0E5A3A;margin-bottom:-1px}
.tabs.lila .on{color:#4B3BA6;border-color:#4B3BA6}
.chip{display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 12px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12.5px;white-space:nowrap;color:#17231D}
.chip.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}
.chip.lon{background:#4B3BA6;border-color:#4B3BA6;color:#FFFFFF}
.btn{height:38px;padding:0 16px;border-radius:10px;border:1.5px solid #0E5A3A;color:#0E5A3A;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;box-sizing:border-box}
.btnp{height:38px;padding:0 16px;border-radius:10px;background:#0E5A3A;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.btnl{height:38px;padding:0 16px;border-radius:10px;background:#4B3BA6;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.btns{height:38px;padding:0 14px;border-radius:10px;background:#EEF6EE;color:#17231D;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.ico{width:40px;height:40px;border-radius:12px;display:flex;align-items:center;justify-content:center;flex:none;background:#EEF6EE;color:#0E5A3A}
.ico.l{background:#F1EEFB;color:#4B3BA6}
.av{width:38px;height:38px;border-radius:10px;color:#FFFFFF;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none}
.th{border-radius:12px;background:#EAF0EB;height:88px}
.bar{height:6px;border-radius:3px;background:#E3E8E4;overflow:hidden}.bar span{display:block;height:100%;background:#0E5A3A}
.kpi{display:flex;flex-direction:column;gap:2px}.kpi b{font-size:24px;font-weight:600}
.src{font-size:10.5px;font-weight:600;color:#56615B;border:1px solid #DCE3DE;border-radius:6px;padding:1px 6px;white-space:nowrap}
.inp{height:42px;border:1px solid #D5DED8;border-radius:10px;padding:0 12px;font:400 13.5px 'Poppins',sans-serif;color:#17231D;background:#FFFFFF;display:flex;align-items:center;justify-content:space-between;box-sizing:border-box}
.tag{display:inline-flex;height:24px;padding:0 9px;border-radius:999px;background:#F1F4F1;font-size:11.5px;color:#4A5650;align-items:center;white-space:nowrap}
"""
I = {
 'brief': 'M5 7h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2zM8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18',
 'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z',
 'msg': 'M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z',
 'hist': 'M12 3a9 9 0 1 1-8.5 6M3 4v5h5M12 7v5l3 2',
 'comp': 'M4 5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1zM12 4v16',
 'pkg': 'M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8',
 'bldg': 'M5 3h14v18H5zM9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2',
 'user': 'M12 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM4 21a8 8 0 0 1 16 0',
 'book': 'M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5zM4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5',
 'search': 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5',
 'plus': 'M12 5v14M5 12h14', 'arrow': 'M5 12h14M13 6l6 6-6 6', 'check': 'm5 12 5 5 9-10',
 'globe': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18',
 'bookmark': 'M6 3h12v18l-6-4-6 4z', 'clip': 'M21 11.5 12.5 20a5 5 0 0 1-7-7L14 4.5a3.5 3.5 0 0 1 5 5L10.5 18a2 2 0 0 1-3-3L15 7.5',
 'send': 'M22 2 11 13M22 2l-7 20-4-9-9-4z', 'star': 'm12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z',
 'eye': 'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 1 0 6 3 3 0 0 1 0-6z',
 'target': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM12 7a5 5 0 1 1 0 10 5 5 0 0 1 0-10zM12 11a1 1 0 1 1 0 2 1 1 0 0 1 0-2z',
 'inbox': 'M4 13h4l2 3h4l2-3h4M5 5h14l2 8v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5z',
 'layers': 'm12 3 9 5-9 5-9-5zM3 13l9 5 9-5', 'video': 'M15 10l5-3v10l-5-3zM3 6h12v12H3z',
 'help': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01',
 'shield': 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z', 'card': 'M3 6h18v12H3zM3 10h18M7 15h4',
 'chat': 'M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z', 'mail': 'M3 5h18v14H3zM3 7l9 6 9-6',
 'pin': 'M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11zM12 7.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z',
}
def ic(n, s=18, c='currentColor', w=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="%s"/></svg>' % (s, s, c, w, I[n])
AR = ic('arrow', 14, w=2.2)

PERS = {'u': dict(modo='personal', persona='Samuel E.', ini='SE', var='personal', alto=832, H=900),
        'e': dict(modo='experta', persona='Laura G.', ini='LG', var='experta', alto=932, H=1000)}

def page(fn, title, who, activo, crumb, h1, sub, body, right=''):
    p = PERS[who]; H = p['H']
    t = """<!doctype html>
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
<style>%s</style>
</helmet>
<div style="width: 1280px; height: %dpx; background: #F6F8F6; position: relative; overflow: hidden;">
  <div style="display: flex; padding-top: 68px; height: %dpx; box-sizing: border-box;">
    <dc-import name="IntSidebar" modo="%s" activo="%s" alto="%d" hint-size="256px,%dpx"></dc-import>
    <main style="flex: 1; min-width: 0; padding: 20px 28px; display: flex; flex-direction: column; gap: 16px;">
      <div style="display: flex; align-items: flex-end; gap: 16px;"><div style="flex: 1;"><div style="font-size: 13px; color: #56615B;">%s</div><h1 style="margin: 0; font-size: 28px; font-weight: 600;">%s</h1><p style="margin: 2px 0 0; font-size: 13.5px; color: #4A5650;">%s</p></div>%s</div>
%s
    </main>
  </div>
  <div style="position: absolute; top: 0; left: 0; width: 1280px;">
    <dc-import name="IntHeader" persona="%s" iniciales="%s" color="#0E5A3A" variante="%s" hint-size="1280px,68px"></dc-import>
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
""" % (title, CSS, H, H, p['modo'], activo, p['alto'], p['alto'], crumb, h1, sub, right, body, p['persona'], p['ini'], p['var'], H)
    open(P + fn, 'w').write(t)
    return fn, H

def wrapper(fn, src, h, title):
    # Copia real (un tablero que importa otro tablero con componentes se queda en blanco en el canvas)
    import re as _re
    s = open(P + src + '.dc.html').read()
    open(P + fn, 'w').write(_re.sub(r'<title>.*?</title>', '<title>%s</title>' % title, s, count=1))
    return fn, h

B = {}  # fn -> (h, title, page, row, col)

# ===================== USUARIO =====================
U = []
# U1 Mi espacio (día a día)
body = """      <section class="card" style="flex-direction: row; align-items: center; gap: 18px; padding: 16px 20px;">
        <div style="display: flex; gap: 6px;"><span class="th" style="width: 56px; height: 56px; background: #FFF4DE;"></span><span class="th" style="width: 56px; height: 56px; background: #E5F1F7;"></span><span class="th" style="width: 56px; height: 56px; background: #EEF2E6;"></span></div>
        <div style="flex: 1; display: flex; flex-direction: column; gap: 2px;"><span class="k" style="font-weight: 600; letter-spacing: .05em;">CONTINÚA DONDE LO DEJASTE</span><span style="font-size: 17px; font-weight: 600;">Tablero «Nave 2 · broilers»</span><span class="k" style="font-size: 12.5px;">8 productos · 1 comparación · 3 propuestas recibidas</span></div>
        <a href="#" class="btnp">Abrir tablero</a>
      </section>
      <div style="display: grid; grid-template-columns: 1fr 1fr 300px; gap: 16px; align-items: start;">
        <section class="card">
          <div class="hd"><h2 class="h2">Tus proyectos</h2><a href="#">Ver todos""" + AR + """</a></div>
          <div class="row"><span class="ico">""" + ic('brief') + """</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Sistema de alimentación · Nave 2</strong><br><span class="k">4 propuestas · cierra en 12 días</span></span><span class="st nw">2 nuevas</span></div>
          <div class="row"><span class="ico">""" + ic('shield') + """</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Asesoría en bioseguridad</strong><br><span class="k">1 propuesta · cierra en 20 días</span></span><span class="st ok">Activo</span></div>
          <a href="#" class="btns">""" + ic('plus', 16) + """Nuevo proyecto</a>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Mensajes</h2><a href="#">Ir a Mensajes""" + AR + """</a></div>
          <div class="row"><span class="av" style="background: #1F3A5F;">AE</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">AgroExport SRL</strong><br><span class="k">«Te enviamos precio y plazo…»</span></span><span class="k">2 h</span></div>
          <div class="row"><span class="av" style="background: #C8102E;">Z</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Zucami</strong><br><span class="k">Propuesta para tu proyecto</span></span><span class="k">ayer</span></div>
          <div class="row"><span class="av" style="background: #4B3BA6; border-radius: 50%;">AR</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Dra. Ana Ruiz</strong><br><span class="k">Experta · te ha respondido</span></span><span class="k">3 d</span></div>
        </section>
        <div style="display: flex; flex-direction: column; gap: 16px;">
          <section class="card">
            <div class="hd"><h2 class="h2">Tus intereses</h2><a href="#">Editar</a></div>
            <span style="font-size: 12.5px; line-height: 1.5;"><strong style="font-weight: 600;">Avicultura · Porcino</strong><br><span class="k">Nutrición y aditivos · Equipamiento avícola · Bienestar animal · Conversión alimenticia · +3</span></span>
          </section>
          <section class="card">
            <div class="hd"><h2 class="h2">Tu plan</h2><span class="st ok">Gratis</span></div>
            <span class="k" style="display: flex; justify-content: space-between;">Proyectos activos <span>2 de 2</span></span><div class="bar"><span style="width: 100%;"></span></div>
            <a href="#" style="font-size: 12.5px;">Ver planes""" + AR + """</a>
          </section>
        </div>
      </div>
      <section class="card">
        <div class="hd"><h2 class="h2">Para ti · Avicultura · Bienestar animal</h2><a href="#">Ver más""" + AR + """</a></div>
        <div style="display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px;">""" + ''.join(
    '<div style="display: flex; flex-direction: column; gap: 5px;"><span class="th" style="background: %s;"></span><span style="font-size: 13px; font-weight: 600;">%s</span><span class="k">%s</span></div>' % x for x in [
        ('#FFF4DE', 'Ronozyme® ProAct', 'DSM-Firmenich · Enzimas'), ('#EEF2E6', 'Aviary Pro', 'Zucami · Aviarios'), ('#E5F1F7', 'Sensor NH₃ / CO₂', 'AgroNova · Sensores'),
        ('#F1EEFB', 'Dra. Ana Ruiz', 'Experta · Bienestar animal'), ('#F3EEE6', 'Guía: estrés térmico', 'Agrinews · 8 min')]) + """</div>
      </section>"""
U.append(page('UsrEspacio.dc.html', 'Intranet usuario · Mi espacio', 'u', 'Mi espacio', 'Mi espacio', 'Hola de nuevo, Samuel', 'Lo que tienes en marcha y lo nuevo para tus intereses.', body))

# U2 Mis proyectos
def pcard(emo, tit, est, estc, cat, meta, extra, btn):
    return ('<section class="card" style="flex-direction: row; align-items: center; gap: 16px;"><span style="width: 52px; height: 52px; border-radius: 14px; background: #F2F7F3; font-size: 26px; display: flex; align-items: center; justify-content: center; flex: none;">%s</span>'
            '<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 3px;"><span style="display: flex; align-items: center; gap: 10px;"><strong style="font-size: 15.5px; font-weight: 600;">%s</strong><span class="st %s">%s</span></span>'
            '<span class="k" style="font-size: 12.5px;">%s</span><span style="display: flex; gap: 16px; font-size: 12.5px; color: #33424C; margin-top: 2px;">%s</span></div>%s%s</section>') % (emo, tit, estc, est, cat, meta, extra, btn)
body = ("""      <div style="display: flex; align-items: center; gap: 12px;"><div class="tabs" style="flex: 1;"><span class="on">Activos 2</span><span>Borradores 1</span><span>Finalizados 0</span></div></div>
""" + pcard('🐔', 'Sistema de alimentación · Nave 2', 'Recibiendo propuestas', 'ok', 'Equipamiento › Sistemas de alimentación · Avicultura › Broilers · Lleida',
            '<span><strong style="font-weight: 600;">4</strong> propuestas</span><span>23 empresas lo han visto</span><span>Cierra en 12 días</span>', '<span class="st nw">2 nuevas</span>', '<a href="#" class="btnp">Ver propuestas</a>')
     + pcard('🧪', 'Asesoría en bioseguridad', 'Recibiendo propuestas', 'ok', 'Servicio › Consultoría veterinaria · Avicultura · Lleida',
            '<span><strong style="font-weight: 600;">1</strong> propuesta</span><span>4 expertos lo han visto</span><span>Cierra en 20 días</span>', '', '<a href="#" class="btn">Ver propuesta</a>')
     + pcard('🌬', 'Ventilación y cooling · Nave 1', 'Borrador', 'gr', 'Equipamiento › Ventilación', '<span>Falta el paso «Detalles»</span>', '', '<a href="#" class="btn">Continuar</a>') + """
      <section class="card" style="flex-direction: row; align-items: center; gap: 14px; background: #F4F7FB; border-color: #E2E8F0;"><span class="ico">""" + ic('grid') + """</span><span style="flex: 1; font-size: 13px;"><strong style="font-weight: 600;">Cada proyecto tiene su tablero.</strong> Las propuestas que te interesen se guardan allí con su estado.</span><a href="#" style="font-size: 13px;">Abrir tablero""" + AR + """</a></section>
      <section class="card" style="flex-direction: row; align-items: center; gap: 14px;"><span class="ico">""" + ic('help') + """</span><span style="flex: 1; font-size: 13px; color: #33424C;">Tu nombre no se muestra a las empresas hasta que respondes a una propuesta.</span><span class="k">Plan Gratis · 2 de 2 proyectos activos</span></section>""")
U.append(page('UsrProyectos.dc.html', 'Intranet usuario · Mis proyectos', 'u', 'Mis proyectos', 'Mi espacio › Mis proyectos', 'Mis proyectos', 'Publica lo que necesitas y recibe propuestas de empresas y expertos.', body, '<a href="#" class="btnp">' + ic('plus', 16) + 'Nuevo proyecto</a>'))

# U3 Mis tableros (reutiliza T1)
U.append(wrapper('UsrTableros.dc.html', 'TabMis', 900, 'Intranet usuario · Mis tableros'))

# U4 Mis comparaciones
def ccard(tit, tipo, n, cols, upd, cta):
    return ('<section class="card"><div class="hd"><span style="display: flex; flex-direction: column;"><strong style="font-size: 15px; font-weight: 600;">%s</strong><span class="k">Tipo: %s · %d productos</span></span><span class="k">%s</span></div>'
            '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 8px;">%s</div>'
            '<div style="display: flex; gap: 8px;"><a href="#" class="btnp">Abrir comparación</a>%s</div></section>') % (
        tit, tipo, n, upd, ''.join('<div style="border: 1px solid #E6EBE7; border-radius: 10px; padding: 8px; display: flex; flex-direction: column; gap: 4px;"><span style="height: 44px; border-radius: 8px; background: %s;"></span><span style="font-size: 12px; font-weight: 600;">%s</span><span class="k">%s</span></div>' % c for c in cols) +
        ('<div style="border: 1.5px dashed #CFD8D2; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #0E5A3A; font-size: 12.5px; font-weight: 500;">+ Añadir</div>' if len(cols) < 4 else ''), cta)
body = ("""      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px;">"""
        + ccard('Enzimas · fitasas', 'Enzimas', 3, [('#E6F0FA', 'Ronozyme® HiPhos', 'DSM-Firmenich'), ('#FDE9EC', 'Axtra® PHY', 'IFF'), ('#EEF2E6', 'Quantum® Blue', 'AB Vista')], 'Hoy', '<a href="#" class="btn">Solicitar información a los 3</a>')
        + ccard('Bebederos para broilers', 'Bebederos', 2, [('#E5F1F7', 'Nipple Pro', 'Fabricante A'), ('#F3EEE6', 'AquaLine', 'Fabricante B')], 'Hace 3 días', '<a href="#" class="btn">Guardar en tablero</a>')
        + ccard('Ventiladores de túnel', 'Sistemas de ventilación', 3, [('#DDE7E0', 'Turbo 50"', 'Fabricante C'), ('#EAF0EB', 'Cone Fan 54"', 'Fabricante D'), ('#F1EEFB', 'EcoFlow', 'Fabricante E')], '12 oct', '<a href="#" class="btn">Ver en tablero</a>')
        + """<section class="card" style="border: 1.5px dashed #CFD8D2; background: #FBFCFB; align-items: center; justify-content: center; text-align: center; gap: 8px;"><span class="ico">""" + ic('comp') + """</span><strong style="font-size: 15px; font-weight: 600;">Nueva comparación</strong><span class="k" style="max-width: 300px; line-height: 1.5;">Desde cualquier ficha pulsa «Comparar». Solo se comparan productos del mismo tipo; los datos salen de la ficha común y de los atributos del tipo.</span></section>
      </div>
      <p style="margin: 0; font-size: 12px; color: #56615B;">Plan Gratis: hasta 3 productos por comparación. Sin precios: para precio, «Solicitar información».</p>""")
U.append(page('UsrComparaciones.dc.html', 'Intranet usuario · Mis comparaciones', 'u', 'Mis comparaciones', 'Mi espacio › Mis comparaciones', 'Mis comparaciones', 'Tus comparativas guardadas, sueltas o dentro de un tablero.', body))

# U5 Historial
def hrow(icn, tipo, nom, meta, hora, saved=False):
    return ('<div class="row"><span class="ico" style="width: 36px; height: 36px;">%s</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">%s</strong> <span class="tag" style="height: 20px; font-size: 10.5px; margin-left: 6px;">%s</span><br><span class="k">%s</span></span><span class="k" style="width: 60px;">%s</span>%s</div>') % (
        ic(icn, 17), nom, tipo, meta, hora, '<span class="st ok">En «Nave 2»</span>' if saved else '<a href="#" class="btns" style="height: 32px; font-size: 12px;">' + ic('bookmark', 14) + 'Guardar en tablero</a>')
body = ("""      <div style="display: flex; align-items: center; gap: 8px;"><span class="chip on">Todo</span><span class="chip">Productos</span><span class="chip">Empresas</span><span class="chip">Expertos</span><span class="chip">Contenidos</span>
        <div style="margin-left: auto; display: flex; align-items: center; gap: 10px; font-size: 12.5px; color: #56615B;">Guardar historial <span style="width: 36px; height: 20px; border-radius: 999px; background: #0E5A3A; position: relative; display: inline-block;"><span style="position: absolute; top: 2px; right: 2px; width: 16px; height: 16px; border-radius: 50%; background: #FFF;"></span></span><a href="#" style="color: #A3271B;">Borrar todo</a></div></div>
      <section class="card"><span class="k" style="font-weight: 600; letter-spacing: .05em;">HOY</span>"""
        + hrow('pkg', 'Producto', 'Ronozyme® ProAct', 'DSM-Firmenich · Nutrición · Enzimas', '10:42')
        + hrow('bldg', 'Empresa', 'Zucami Poultry Equipment', 'Fabricante · Equipamiento avícola', '10:30', True)
        + hrow('book', 'Contenido', 'Cómo reducir el estrés térmico en broilers', 'Agrinews · Guía técnica', '09:15') + """</section>
      <section class="card"><span class="k" style="font-weight: 600; letter-spacing: .05em;">AYER</span>"""
        + hrow('user', 'Experto', 'Dra. Ana Ruiz', 'Veterinaria · Bienestar animal · Lleida', '18:02')
        + hrow('pkg', 'Producto', 'Sensor de ambiente NH₃ / CO₂', 'AgroNova · Tecnología · Sensores', '17:40') + """</section>
      <p style="margin: 0; font-size: 12px; color: #56615B;">Se guarda automáticamente lo que consultas durante 90 días. Solo lo ves tú.</p>""")
U.append(page('UsrHistorial.dc.html', 'Intranet usuario · Historial', 'u', 'Historial', 'Mi espacio › Historial', 'Historial', 'Todo lo que has consultado, sin hacer nada. Desde aquí lo pasas a un tablero.', body))

# U6 Mensajes
def conv(av, col, nom, ctx, last, t, on=False, unread=0, rnd='10px'):
    return ('<div style="display: flex; gap: 10px; padding: 12px; border-radius: 12px; %s"><span class="av" style="background: %s; border-radius: %s;">%s</span><span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 1px;">'
            '<span style="display: flex; justify-content: space-between; gap: 6px;"><strong style="font-size: 13.5px; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">%s</strong><span class="k">%s</span></span>'
            '<span class="k" style="white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">%s</span><span style="font-size: 12.5px; color: #33424C; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">%s</span></span>%s</div>') % (
        'background: #EEF6EE;' if on else '', col, rnd, av, nom, t, ctx, last, ('<span class="st nw" style="align-self: center;">%d</span>' % unread) if unread else '')
def bub(txt, me, t):
    return ('<div style="display: flex; justify-content: %s;"><div style="max-width: 70%%; padding: 10px 14px; border-radius: 14px; %s font-size: 13px; line-height: 1.5;">%s<div class="k" style="margin-top: 4px; %s">%s</div></div></div>') % (
        'flex-end' if me else 'flex-start', 'background: #0E5A3A; color: #FFFFFF; border-bottom-right-radius: 4px;' if me else 'background: #FFFFFF; border: 1px solid #E3E8E4; border-bottom-left-radius: 4px;', txt, 'color: #D6E8DC;' if me else '', t)
body = ("""      <div style="display: grid; grid-template-columns: 320px 1fr; gap: 0; flex: 1; min-height: 0; background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; overflow: hidden;">
        <div style="border-right: 1px solid #E3E8E4; padding: 12px; display: flex; flex-direction: column; gap: 4px;">
          <div class="inp" style="height: 38px; color: #8A948F; justify-content: flex-start; gap: 8px;">""" + ic('search', 16) + """Buscar conversación</div>
          <div style="display: flex; gap: 6px; padding: 8px 0;"><span class="chip on" style="height: 28px;">Todas</span><span class="chip" style="height: 28px;">Sin leer 2</span><span class="chip" style="height: 28px;">Proyectos</span></div>"""
        + conv('AE', '#1F3A5F', 'AgroExport SRL', 'Corrector vitamínico CV-20 · solicitud', 'Te enviamos precio y plazo de entrega…', '2 h', True, 1)
        + conv('Z', '#C8102E', 'Zucami', 'Proyecto · Sistema de alimentación Nave 2', 'Adjuntamos la propuesta en PDF', 'Ayer', False, 1)
        + conv('AR', '#4B3BA6', 'Dra. Ana Ruiz', 'Consulta · bienestar en broilers', 'Podemos hacer una visita la semana…', '3 d', rnd='50%')
        + conv('NC', '#2E8B57', 'Nutrivet Catalunya', 'Ronozyme® HiPhos · distribuidor de tu zona', 'Gracias, te llamamos mañana.', '12 oct') + """
        </div>
        <div style="display: flex; flex-direction: column; min-width: 0;">
          <div style="display: flex; align-items: center; gap: 12px; padding: 14px 18px; border-bottom: 1px solid #E3E8E4;"><span class="av" style="background: #1F3A5F;">AE</span><span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 15px; font-weight: 600;">AgroExport SRL</strong><span class="k">Carla Martín · Directora comercial · responde en 2 h de media</span></span><a href="#" class="btn" style="height: 34px;">Ver empresa</a></div>
          <div style="margin: 12px 18px 0; padding: 10px 12px; border-radius: 12px; background: #F4F7FB; border: 1px solid #E2E8F0; display: flex; align-items: center; gap: 10px; font-size: 12.5px;"><span class="th" style="width: 36px; height: 36px; border-radius: 8px; background: #FFF4DE;"></span><span style="flex: 1;"><strong style="font-weight: 600;">Sobre: Corrector vitamínico CV-20</strong> · Solicitud de información del 13 oct</span><a href="#">Ver producto</a><a href="#">Guardar en tablero</a></div>
          <div style="flex: 1; padding: 16px 18px; display: flex; flex-direction: column; gap: 10px; background: #F9FBF9;">"""
        + bub('Hola, querría precio y plazo para 2 t de CV-20 para broilers. Estoy en Lleida.', True, '13 oct · 09:12')
        + bub('Hola Samuel, gracias por tu interés. Para Lleida te sirve nuestro distribuidor Agropecuària del Segre. Te enviamos precio y plazo de entrega en el PDF adjunto.', False, 'Hoy · 08:40')
        + """<div style="display: flex;"><span style="display: inline-flex; align-items: center; gap: 8px; padding: 8px 12px; border-radius: 10px; background: #FFFFFF; border: 1px solid #E3E8E4; font-size: 12.5px;">""" + ic('clip', 15) + """Oferta_CV-20_Lleida.pdf · 240 KB</span></div>
          </div>
          <div style="display: flex; align-items: center; gap: 10px; padding: 12px 18px; border-top: 1px solid #E3E8E4;"><span style="color: #56615B;">""" + ic('clip') + """</span><div class="inp" style="flex: 1; color: #8A948F;">Escribe un mensaje…</div><a href="#" class="btnp" style="width: 42px; padding: 0;">""" + ic('send', 17) + """</a></div>
        </div>
      </div>""")
U.append(page('UsrMensajes.dc.html', 'Intranet usuario · Mensajes', 'u', 'Mensajes', 'Mi espacio › Mensajes', 'Mensajes', 'Conversaciones con empresas y expertos, ligadas a un producto o a un proyecto.', body))

# U7, U8 Mi perfil y Facturación (reutilizan C1 y C2)
U.append(wrapper('UsrPerfil.dc.html', 'CuentaPerfil', 1100, 'Intranet usuario · Mi perfil'))
U.append(wrapper('UsrFacturacion.dc.html', 'CuentaCompras', 980, 'Intranet usuario · Facturación'))

# U9 Idioma y zona
def field(lbl, val, hint='', glob=False):
    return ('<div style="display: flex; flex-direction: column; gap: 6px;"><span style="font-size: 13px; font-weight: 500; display: flex; align-items: center; gap: 8px;">%s%s</span><div class="inp">%s<span style="color: #56615B;">▾</span></div>%s</div>') % (
        lbl, ' <span class="src">Cuenta global</span>' if glob else '', val, ('<span class="k">%s</span>' % hint) if hint else '')
body = ("""      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start;">
        <section class="card" style="gap: 14px;"><h2 class="h2">Idioma</h2>"""
        + field('Idioma de la plataforma', 'Español', 'Menús, emails y avisos.', True)
        + """<div style="display: flex; flex-direction: column; gap: 6px;"><span style="font-size: 13px; font-weight: 500;">Idiomas de los contenidos</span><div style="display: flex; flex-wrap: wrap; gap: 6px;"><span class="chip on">Español</span><span class="chip on">Inglés</span><span class="chip">Portugués</span><span class="chip">Francés</span></div><span class="k">Fichas técnicas y documentos en estos idiomas primero.</span></div>
        </section>
        <section class="card" style="gap: 14px;"><h2 class="h2">Zona</h2>"""
        + field('País', 'España', '', True) + field('Provincia', 'Lleida', 'Para ver disponibilidad y el distribuidor de tu zona en cada producto.')
        + """<div style="display: flex; align-items: center; gap: 10px; padding: 10px 12px; border-radius: 12px; background: #F2F7F3; font-size: 12.5px;">""" + ic('pin', 16, '#0E5A3A') + """Verás «Disponible en España» y los distribuidores de Cataluña primero.</div>
        </section>
        <section class="card" style="gap: 14px;"><h2 class="h2">Formato</h2>""" + field('Unidades', 'Sistema métrico (kg, t, °C)') + field('Moneda de referencia', 'Euro (€)', 'Solo para precios orientativos de servicios y planes.') + """</section>
        <section class="card" style="gap: 10px;"><h2 class="h2">Zona horaria</h2>""" + field('Zona horaria', 'Europa/Madrid (GMT+2)', 'Para eventos, webinars y plazos de proyectos.') + """</section>
      </div>
      <div style="display: flex; justify-content: flex-end; gap: 10px;"><a href="#" class="btn">Cancelar</a><a href="#" class="btnp">Guardar cambios</a></div>""")
U.append(page('UsrIdioma.dc.html', 'Intranet usuario · Idioma y zona', 'u', 'Idioma y zona', 'Mi cuenta › Idioma y zona', 'Idioma y zona', 'Cómo ves Agroolink y qué te mostramos según dónde estás.', body))

# U10 Ayuda y contacto
def topic(icn, t, d):
    return '<a href="#" class="card" style="flex-direction: row; gap: 12px; color: #17231D; font-weight: 400;"><span class="ico">%s</span><span style="display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 14px; font-weight: 600;">%s</strong><span class="k" style="line-height: 1.45;">%s</span></span></a>' % (ic(icn), t, d)
body = ("""      <div class="inp" style="height: 52px; border-radius: 14px; color: #8A948F; justify-content: flex-start; gap: 10px; font-size: 14px;">""" + ic('search', 19) + """¿En qué podemos ayudarte? Ej.: «cómo comparo productos»</div>
      <div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px;">"""
        + topic('user', 'Primeros pasos', 'Cuenta, intereses y cómo moverte') + topic('brief', 'Proyectos y propuestas', 'Publicar, recibir y elegir propuestas')
        + topic('grid', 'Tableros y comparador', 'Guardar, comparar y compartir') + topic('card', 'Cuenta y facturación', 'Planes, pagos y facturas')
        + topic('shield', 'Privacidad y datos', 'Quién ve qué y cuándo') + topic('bldg', 'Para empresas y expertos', 'Crear ficha, productos y servicios') + """
      </div>
      <div style="display: grid; grid-template-columns: 1.4fr 1fr; gap: 16px; align-items: start;">
        <section class="card"><h2 class="h2">Preguntas frecuentes</h2>""" + ''.join('<div class="row" style="justify-content: space-between;"><span>%s</span><span style="color: #56615B;">▾</span></div>' % q for q in [
            '¿Las empresas ven mis datos cuando creo un proyecto?', '¿Por qué no veo precios en las fichas?', '¿Cómo cambio el país o la provincia?', '¿Mi cuenta es la misma que en Agrinews?', '¿Qué pasa si quito un interés?']) + """</section>
        <section class="card"><h2 class="h2">¿Hablamos?</h2>
          <div class="row">""" + ic('chat', 18, '#0E5A3A') + """<span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Chat</strong><br><span class="k">Lunes a viernes, 9:00–18:00</span></span><a href="#" class="btnp" style="height: 32px;">Abrir chat</a></div>
          <div class="row">""" + ic('mail', 18, '#0E5A3A') + """<span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Formulario</strong><br><span class="k">Respondemos en 24 h laborables</span></span><a href="#" class="btn" style="height: 32px;">Escribir</a></div>
          <div class="row">""" + ic('video', 18, '#0E5A3A') + """<span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Demo guiada</strong><br><span class="k">Para empresas: 20 minutos por videollamada</span></span><a href="#" class="btn" style="height: 32px;">Reservar</a></div>
        </section>
      </div>""")
U.append(page('UsrAyuda.dc.html', 'Intranet usuario · Ayuda y contacto', 'u', 'Ayuda y contacto', 'Mi cuenta › Ayuda y contacto', 'Ayuda y contacto', 'Guías rápidas, preguntas frecuentes y cómo hablar con nosotros.', body))

# ===================== EXPERTO =====================
E = []
# E1 Panel
body = ("""      <div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px;">""" + ''.join(
    '<section class="card" style="padding: 14px 16px;"><span class="k">%s</span><span class="kpi"><b>%s</b></span><span class="k" style="color: %s;">%s</span></section>' % k for k in [
        ('Apariciones en búsquedas', '1.240', '#0E5A3A', '+18 % esta semana'), ('Visitas al perfil', '128', '#0E5A3A', '+9 %'), ('Consultas', '3', '#56615B', '1 sin responder'), ('Candidaturas', '1 de 3', '#56615B', 'este mes · plan Gratis')]) + """</div>
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; align-items: start;">
        <section class="card">
          <div class="hd"><h2 class="h2">Consultas recibidas</h2><a href="#" style="color: #4B3BA6;">Ver todas""" + AR + """</a></div>
          <div class="row" style="align-items: flex-start;"><span class="av" style="background: #E3E8E4; color: #4A5650; border-radius: 50%;">GA</span><span style="flex: 1; line-height: 1.4;"><strong style="font-weight: 600;">Ganadero · Huesca</strong> <span class="st nw">Nueva</span><br><span class="k">Sobre «Auditoría nutricional de lotes de broilers»</span><br><span style="font-size: 12.5px;">«Tengo dos naves y el índice de conversión ha empeorado…»</span></span><a href="#" class="btnl" style="height: 32px;">Responder</a></div>
          <div class="row" style="align-items: flex-start;"><span class="av" style="background: #1F3A5F; border-radius: 50%;">IH</span><span style="flex: 1; line-height: 1.4;"><strong style="font-weight: 600;">Integradora · Huesca</strong><br><span class="k">Formación en bienestar · respondida ayer</span></span><span class="st ok">Respondida</span></div>
        </section>
        <section class="card">
          <div class="hd"><h2 class="h2">Oportunidades para ti</h2><a href="#" style="color: #4B3BA6;">Ver todas""" + AR + """</a></div>
          <div class="row"><span class="st li">94 %</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Plan de bioseguridad para 3 naves</strong><br><span class="k">Broilers · Lleida · cierra en 6 días</span></span><a href="#" class="btnl" style="height: 32px;">Candidatura</a></div>
          <div class="row"><span class="st li">87 %</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">Revisar 4 propuestas de alimentación</strong><br><span class="k">Broilers · Lleida · 300–500 €</span></span><a href="#" class="btn" style="height: 32px; color: #4B3BA6; border-color: #4B3BA6;">Ver</a></div>
        </section>
      </div>
      <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: start;">
        <section class="card"><div class="hd"><h2 class="h2">Tus servicios</h2><a href="#" style="color: #4B3BA6;">Gestionar</a></div>
          <div class="row"><span style="flex: 1;">Auditoría nutricional de lotes</span><span class="st ok">Publicado</span></div>
          <div class="row"><span style="flex: 1;">Revisión de propuestas</span><span class="st ok">Activo</span></div></section>
        <section class="card"><div class="hd"><h2 class="h2">Completa tu perfil</h2><span class="k">3 de 5</span></div><div class="bar"><span style="width: 60%; background: #4B3BA6;"></span></div>
          <span style="font-size: 12.5px; line-height: 1.6;">○ Añade una foto<br>○ Añade un caso de éxito</span></section>
        <section class="card" style="background: #FAF8FE; border-color: #E9E4F8;"><div class="hd"><h2 class="h2">Experta Gratis</h2><span class="st li">Plan</span></div>
          <span style="font-size: 12.5px; color: #4A5650; line-height: 1.45;">3 consultas y 3 candidaturas al mes. Con Experto Pro (19,90 €/mes), sin límite.</span><a href="#" style="font-size: 12.5px; color: #4B3BA6;">Ver Experto Pro""" + AR + """</a></section>
      </div>""")
E.append(page('ExpPanel.dc.html', 'Intranet experta · Panel', 'e', 'Panel de experta', 'Como experta › Panel', 'Hola, Laura', 'Cómo va tu perfil, qué te han preguntado y qué proyectos encajan contigo.',
              body, '<a href="#" class="btn" style="color: #4B3BA6; border-color: #4B3BA6;">' + ic('eye', 16) + 'Ver mi perfil público</a>'))

# E2 Oportunidades
def ocard(emo, pct, tit, who, whys, budget, plazo, cand, primary=True):
    return ('<section class="card" style="flex-direction: row; gap: 16px; align-items: flex-start;"><span style="width: 52px; height: 52px; border-radius: 14px; background: #F4F1FC; font-size: 26px; display: flex; align-items: center; justify-content: center; flex: none;">%s</span>'
            '<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span style="display: flex; align-items: center; gap: 10px;"><span class="st li" style="font-size: 12px;">%s encaje</span><strong style="font-size: 15.5px; font-weight: 600;">%s</strong></span>'
            '<span class="k" style="font-size: 12.5px;">%s</span><span style="display: flex; flex-wrap: wrap; gap: 6px; margin-top: 2px;">%s</span>'
            '<span style="display: flex; gap: 18px; font-size: 12.5px; color: #33424C; margin-top: 4px;"><span>%s</span><span>%s</span><span>%s</span></span></div>'
            '<div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-end;"><a href="#" class="%s">Enviar candidatura</a><a href="#" style="font-size: 12.5px; color: #4B3BA6;">Ver proyecto</a></div></section>') % (
        emo, pct, tit, who, ''.join('<span class="tag" style="background: #F4F1FC; color: #4B3BA6;">✓ %s</span>' % w for w in whys), budget, plazo, cand, 'btnl' if primary else 'btn')
body = ("""      <div class="tabs lila"><span class="on">Para ti 3</span><span>Todas</span><span>Mis candidaturas 1</span><span>Adjudicadas</span></div>
      <div style="display: flex; gap: 8px;"><span class="chip lon">Avicultura</span><span class="chip">Servicio › Consultoría</span><span class="chip">Formación</span><span class="chip">Hasta 100 km</span><span class="chip">A distancia</span></div>"""
        + ocard('🧪', '94 %', 'Plan de bioseguridad para 3 naves', 'Granja de broilers en Lleida · Servicio › Consultoría veterinaria · cierra en 6 días', ['Veterinaria · avicultura', 'Lleida, a 40 km', 'Bioseguridad en tu perfil'], 'A consultar', '2 meses', '1 de 5 candidaturas')
        + ocard('🐔', '87 %', 'Revisar 4 propuestas de alimentación', 'Granja de broilers en Lleida · Servicio › Revisión de propuestas · cierra en 12 días', ['Avicultura › Broilers', 'Revisión de propuestas activada'], '300 – 500 €', '2 semanas', '0 candidaturas')
        + ocard('🎓', '72 %', 'Formación en bienestar animal para el equipo', 'Integradora en Huesca · Servicio › Formación técnica · cierra en 20 días', ['Formación en tus servicios', 'A distancia'], '1.200 €', '1 mes', '2 de 5 candidaturas', False) + """
      <section class="card" style="flex-direction: row; align-items: center; gap: 14px; background: #FAF8FE; border-color: #E9E4F8;"><span class="ico l">""" + ic('target') + """</span><span style="flex: 1; font-size: 13px;"><strong style="font-weight: 600;">El encaje</strong> suma especialidad, especies, zona y objetivos de tu perfil. El ganadero no ve tu nombre hasta que envías la candidatura.</span><span class="k">1 de 3 candidaturas este mes</span></section>""")
E.append(page('ExpOportunidades.dc.html', 'Intranet experta · Oportunidades', 'e', 'Oportunidades', 'Como experta › Oportunidades', 'Oportunidades', 'Proyectos donde piden tu especialidad, tus especies y tu zona.', body))

# E3 Consultas recibidas
body = ("""      <div style="display: grid; grid-template-columns: 320px 1fr; flex: 1; min-height: 0; background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; overflow: hidden;">
        <div style="border-right: 1px solid #E3E8E4; padding: 12px; display: flex; flex-direction: column; gap: 4px;">
          <div style="display: flex; gap: 6px; padding: 4px 0 8px;"><span class="chip lon" style="height: 28px;">Nuevas 1</span><span class="chip" style="height: 28px;">En curso 1</span><span class="chip" style="height: 28px;">Cerradas</span></div>"""
        + conv('GA', '#9AA39E', 'Ganadero · Huesca', 'Auditoría nutricional de lotes de broilers', 'Tengo dos naves y el índice de conversión…', '5 h', True, 1, '50%').replace('#EEF6EE', '#F4F1FC')
        + conv('IH', '#1F3A5F', 'Integradora · Huesca', 'Formación en bienestar animal', 'Perfecto, ¿nos pasas fechas?', 'Ayer', rnd='50%')
        + conv('GP', '#2E8B57', 'Granja El Pinar', 'Revisión de propuestas', 'Gracias, muy útil la comparativa.', '8 oct', rnd='50%') + """
          <div style="margin-top: auto; padding: 10px; border-radius: 12px; background: #FAF8FE; font-size: 12px; color: #4A5650; line-height: 1.45;">Plan Gratis: 3 consultas al mes (1 usada). Con Experto Pro, sin límite.</div>
        </div>
        <div style="display: flex; flex-direction: column; min-width: 0;">
          <div style="display: flex; align-items: center; gap: 12px; padding: 14px 18px; border-bottom: 1px solid #E3E8E4;"><span class="av" style="background: #9AA39E; border-radius: 50%;">GA</span><span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 15px; font-weight: 600;">Ganadero · Huesca</strong><span class="k">Avicultura › Broilers · 2 naves · 40.000 aves</span></span><span class="st li">Nueva</span></div>
          <div style="margin: 12px 18px 0; padding: 10px 12px; border-radius: 12px; background: #FAF8FE; border: 1px solid #E9E4F8; font-size: 12.5px;"><strong style="font-weight: 600;">Servicio:</strong> Auditoría nutricional de lotes de broilers · desde 350 € · presencial o a distancia</div>
          <div style="flex: 1; padding: 16px 18px; display: flex; flex-direction: column; gap: 10px; background: #FBFAFE;">"""
        + bub('Hola, tengo dos naves de broilers y el índice de conversión ha empeorado en los dos últimos lotes (de 1,62 a 1,74). Cambiamos de pienso en agosto. ¿Podrías revisarlo?', False, 'Hoy · 07:58') + """
          </div>
          <div style="padding: 12px 18px; border-top: 1px solid #E3E8E4; display: flex; flex-direction: column; gap: 10px;">
            <div style="display: flex; gap: 8px;"><a href="#" class="chip">""" + ic('video', 14) + """Proponer videollamada</a><a href="#" class="chip">""" + ic('card', 14) + """Enviar presupuesto</a><a href="#" class="chip">Pedir datos del lote</a></div>
            <div style="display: flex; align-items: center; gap: 10px;"><div class="inp" style="flex: 1; color: #8A948F;">Responde a la consulta…</div><a href="#" class="btnl" style="width: 42px; padding: 0;">""" + ic('send', 17) + """</a></div>
          </div>
        </div>
      </div>""")
E.append(page('ExpConsultas.dc.html', 'Intranet experta · Consultas recibidas', 'e', 'Consultas recibidas', 'Como experta › Consultas recibidas', 'Consultas recibidas', 'Ganaderos y empresas que te escriben desde tu perfil o tus servicios.', body))

# E4 Mis servicios
def srv(tit, est, estc, esp, zon, mod, precio, stats):
    return ('<section class="card" style="flex-direction: row; gap: 16px; align-items: flex-start;"><span class="ico l" style="width: 48px; height: 48px;">%s</span>'
            '<div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 6px;"><span style="display: flex; align-items: center; gap: 10px;"><strong style="font-size: 15.5px; font-weight: 600;">%s</strong><span class="st %s">%s</span></span>'
            '<div style="display: grid; grid-template-columns: 90px 1fr; gap: 4px 10px; font-size: 12.5px;"><span class="k">Especies</span><span>%s</span><span class="k">Zonas</span><span>%s</span><span class="k">Modalidad</span><span>%s</span><span class="k">Precio</span><span>%s</span></div>'
            '<span class="k">%s</span></div><div style="display: flex; flex-direction: column; gap: 8px; align-items: flex-end;"><a href="#" class="btn" style="color: #4B3BA6; border-color: #4B3BA6;">Editar</a><a href="#" style="font-size: 12.5px; color: #4B3BA6;">Ver en perfil</a></div></section>') % (
        ic('layers', 20), tit, estc, est, esp, zon, mod, precio, stats)
body = (srv('Auditoría nutricional de lotes de broilers', 'Publicado', 'ok', 'Avicultura › Broilers, Pollos de crecimiento lento', 'Aragón · Cataluña · Navarra', 'Presencial o a distancia', 'Desde 350 € por lote', '42 visitas · 2 consultas este mes · dirigido a Granjeros, Veterinarios, Nutrólogos')
        + srv('Revisión de propuestas para ganaderos', 'Activo', 'ok', 'Avicultura · Porcino', 'España', 'A distancia', '300 – 500 € según propuestas', 'Te avisamos cuando un ganadero pide ayuda para comparar las propuestas de su proyecto')
        + """<section class="card" style="border: 1.5px dashed #CFD8D2; background: #FBFCFB; flex-direction: row; align-items: center; gap: 14px;"><span class="ico l">""" + ic('plus') + """</span><span style="flex: 1; display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 14.5px; font-weight: 600;">Añadir servicio</strong><span class="k">Especies, zonas, modalidad y a quién va dirigido. Plan Gratis: 2 servicios (2 de 2).</span></span><a href="#" class="btnl">Nuevo servicio</a></section>
      <section class="card" style="flex-direction: row; align-items: center; gap: 14px; background: #FAF8FE; border-color: #E9E4F8;"><span class="ico l">""" + ic('star') + """</span><span style="flex: 1; font-size: 13px;">Los servicios con especies y zonas completas aparecen en las búsquedas y en las <strong style="font-weight: 600;">Oportunidades</strong> que encajan.</span><a href="#" style="font-size: 13px; color: #4B3BA6;">Ver Experto Pro""" + AR + """</a></section>""")
E.append(page('ExpServicios.dc.html', 'Intranet experta · Mis servicios', 'e', 'Mis servicios', 'Como experta › Mis servicios', 'Mis servicios', 'Lo que ofreces, para qué especies y dónde lo prestas.', body, '<a href="#" class="btnl">' + ic('plus', 16) + 'Nuevo servicio</a>'))

# E5 Perfil de experta
def sec(t, v, ok=True):
    return '<div class="row"><span style="width: 22px; height: 22px; border-radius: 50%%; display: flex; align-items: center; justify-content: center; flex: none; %s">%s</span><span style="flex: 1; line-height: 1.35;"><strong style="font-weight: 600;">%s</strong><br><span class="k">%s</span></span><a href="#" style="font-size: 12.5px; color: #4B3BA6;">%s</a></div>' % (
        'background: #4B3BA6; color: #FFF;' if ok else 'border: 1.5px solid #CFC8EE;', ic('check', 12, '#FFFFFF', 3) if ok else '', t, v, 'Editar' if ok else 'Añadir')
body = ("""      <div style="display: grid; grid-template-columns: 1fr 360px; gap: 16px; align-items: start;">
        <section class="card">
          <div class="hd"><h2 class="h2">Tu perfil público</h2><span class="k">3 de 5 completado</span></div><div class="bar"><span style="width: 60%; background: #4B3BA6;"></span></div>"""
        + sec('Titular', 'Veterinaria · nutrición y bienestar en avicultura')
        + sec('Especialidad y especies', 'Nutrición animal, bienestar · Avicultura › Broilers, Gallinas ponedoras')
        + sec('Zonas', 'Aragón, Cataluña, Navarra · también a distancia')
        + sec('Colegiación', 'Colegio de Veterinarios de Huesca · verificada')
        + sec('Foto de perfil', 'Los perfiles con foto reciben el doble de consultas', False)
        + sec('Casos de éxito', 'Cuenta un resultado con datos (sin nombres de clientes)', False)
        + sec('Idiomas', 'Español, inglés')
        + """
        </section>
        <section class="card" style="padding: 0; overflow: hidden;">
          <div style="height: 70px; background: linear-gradient(135deg, #4B3BA6, #7A6BD0);"></div>
          <div style="padding: 0 18px 18px; display: flex; flex-direction: column; gap: 8px; margin-top: -30px;">
            <span style="width: 64px; height: 64px; border-radius: 50%; background: #F1EEFB; border: 3px solid #FFFFFF; color: #4B3BA6; font-size: 20px; font-weight: 600; display: flex; align-items: center; justify-content: center;">LG</span>
            <span style="display: flex; align-items: center; gap: 8px;"><strong style="font-size: 17px; font-weight: 600;">Laura Gil</strong><span class="st li">✓ Colegiada</span></span>
            <span style="font-size: 12.5px; color: #4A5650;">Veterinaria · nutrición y bienestar en avicultura</span>
            <span class="k" style="display: flex; align-items: center; gap: 4px;">""" + ic('pin', 13) + """Huesca · Aragón, Cataluña, Navarra · a distancia</span>
            <span style="display: flex; flex-wrap: wrap; gap: 5px;"><span class="tag">Broilers</span><span class="tag">Ponedoras</span><span class="tag">Bienestar animal</span><span class="tag">Conversión alimenticia</span></span>
            <div style="border-top: 1px solid #EEF1EE; padding-top: 8px; display: flex; flex-direction: column; gap: 6px;"><span class="k" style="font-weight: 600;">SERVICIOS</span><span style="font-size: 12.5px;">Auditoría nutricional de lotes · desde 350 €</span><span style="font-size: 12.5px;">Revisión de propuestas · 300–500 €</span></div>
            <a href="#" class="btnl" style="margin-top: 4px;">Enviar consulta</a>
            <span class="k" style="text-align: center;">Así te ven ganaderos y empresas</span>
          </div>
        </section>
      </div>""")
E.append(page('ExpPerfil.dc.html', 'Intranet experta · Perfil de experta', 'e', 'Perfil de experta', 'Como experta › Perfil de experta', 'Perfil de experta', 'Lo que ven ganaderos y empresas cuando te encuentran.',
              body, '<a href="#" class="btn" style="color: #4B3BA6; border-color: #4B3BA6;">' + ic('eye', 16) + 'Ver como público</a>'))

# ===================== índice =====================
c = json.load(open(P + 'canvas.json')); BO = c['boards']; N = c['notes']
for pid, name in [('intusuario', 'Intranet · Usuario (consolidada)'), ('intexperto', 'Intranet · Experto (consolidada)')]:
    if not any(p['id'] == pid for p in c['pages']):
        i = next(i for i, p in enumerate(c['pages']) if p['id'] == 'intranet')
        c['pages'].insert(i, {'id': pid, 'name': name})
for k in [k for k, b in BO.items() if b['page'] in ('intusuario', 'intexperto')]: del BO[k]
for k in [k for k, n in N.items() if n['page'] in ('intusuario', 'intexperto')]: del N[k]
UT = ['U1 · Mi espacio (día a día)', 'U2 · Mis proyectos', 'U3 · Mis tableros (= T1, enlazado)', 'U4 · Mis comparaciones', 'U5 · Historial', 'U6 · Mensajes',
      'U7 · Mi perfil (= C1, enlazado)', 'U8 · Facturación (= C2, enlazado)', 'U9 · Idioma y zona', 'U10 · Ayuda y contacto']
rows = [(0, 'MI ESPACIO · Samuel (usuario)', U[:6]), (1, 'MI CUENTA · común a todos los roles', U[6:])]
y = 0
for r, txt, items in rows:
    N['iu%d' % r] = {'kind': 'title1', 'maxW': 8000, 'page': 'intusuario', 'text': txt, 'w': 240, 'x': 0, 'y': y - 300}
    for n, (fn, h) in enumerate(items):
        BO[fn] = {'h': h, 'page': 'intusuario', 'title': UT[U.index((fn, h))], 'w': 1280, 'x': n * 1360, 'y': y}
    y += max(h for _, h in items) + 500
ET = ['E1 · Panel de experta', 'E2 · Oportunidades (proyectos que encajan)', 'E3 · Consultas recibidas', 'E4 · Mis servicios', 'E5 · Perfil de experta (editor + vista pública)']
N['ie0'] = {'kind': 'title1', 'maxW': 8000, 'page': 'intexperto', 'text': 'COMO EXPERTA · Laura Gil · Mi espacio, tableros, mensajes y Mi cuenta son los de usuario', 'w': 240, 'x': 0, 'y': -300}
for n, (fn, h) in enumerate(E):
    BO[fn] = {'h': h, 'page': 'intexperto', 'title': ET[n], 'w': 1280, 'x': n * 1360, 'y': 0}
for fn, _ in U + E:
    if fn not in c['order']: c['order'].append(fn)
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok', [f for f, _ in U + E])
