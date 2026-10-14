import os, sys, re
D = sys.argv[1]
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_ref = open(os.path.join(D, 'ComEquipo.dc.html')).read()
CSS = re.search(r'<style>\n(.*?)</style>', _ref, re.S).group(1)
def ic(d, s=18, w=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, w, d)
I = {'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>', 'pin': '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>'}
from especies import TREE
I['plus'] = '<path d="M12 5v14M5 12h14"/>'
I['globe'] = '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>'
I['search'] = '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>'
I['lab'] = '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.7 3h10.6a2 2 0 0 0 1.7-3l-5-9V3"/>'
I['users'] = '<path d="M9 4.5a3.5 3.5 0 1 1 0 7 3.5 3.5 0 0 1 0-7zM2 20a7 7 0 0 1 14 0M16 4.5a3.5 3.5 0 0 1 0 7M18 14a7 7 0 0 1 4 6"/>'
I['chart'] = '<path d="M4 19V9M10 19V5M16 19v-7M22 19H2"/>'
I['doc'] = '<path d="M6 3h9l3 3v15H6z"/><path d="M9 9h6M9 13h6M9 17h4"/>'
I['cap'] = '<path d="M22 9 12 4 2 9l10 5zM6 11v5c3 2 9 2 12 0v-5"/>'
I['gear'] = '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1"/>'
I['truck'] = '<path d="M3 6h11v10H3zM14 9h4l3 4v3h-7M7 19a2 2 0 1 0 0-.1M17 19a2 2 0 1 0 0-.1"/>'

def page(name, title, body, atras='Volver a servicios', sig='Guardar servicio', pie=True):
    html = '''<!doctype html>
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
%s</style>
</helmet>
<div style="width: 1280px; height: 940px; position: relative; overflow: hidden;">
  <div style="position: absolute; inset: 0;"><dc-import name="FabShell" activo="{{ n }}" empresa="AgroNova" persona="Laura García" iniciales="LG" paso4="Marcas" pie="{{ pie }}" atras="{{ atras }}" siguiente="{{ sig }}" hint-size="1280px,940px"></dc-import></div>
  <div style="position: absolute; top: 64px; left: 260px; right: 0; bottom: %s; padding: 22px 28px 20px 32px; display: flex; gap: 22px;">
%s
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1280,"height":940}}'>
class Component extends DCLogic {
  renderVals() { return { yes: true, n: 10, pie: %s, atras: %r, sig: %r }; }
}
</script>
</body>
</html>
''' % (title, CSS, '72px' if pie else '0', body, 'true' if pie else 'false', atras, sig)
    open(os.path.join(D, name + '.dc.html'), 'w').write(html)

SERV = [('users', 'Asesoramiento técnico', 'Consultoría veterinaria', 'Avicultura, Porcino, Bovino', 'Presencial · España, Portugal', 'Equipo técnico (4)', ('ok', 'Publicado'), 7),
        ('chart', 'Auditoría nutricional', 'Consultoría nutricional', 'Avicultura, Porcino', 'Presencial · España · Remoto', 'Equipo de nutrición (2)', ('ok', 'Publicado'), 4),
        ('doc', 'Diseño de programas de alimentación', 'Consultoría nutricional', 'Avicultura, Porcino, Bovino', 'Remoto · todo el mundo', 'Equipo de nutrición (2)', ('ok', 'Publicado'), 3),
        ('cap', 'Formación técnica', 'Formación técnica', 'Todas', 'Presencial y online · España, Latinoamérica', 'Laura García', ('ok', 'Publicado'), 2),
        ('gear', 'Seguimiento de implantación', 'Servicios de mantenimiento', 'Avicultura, Porcino', 'Presencial · España', 'Equipo técnico (4)', ('dr', 'Borrador'), 0),
        ('truck', 'Logística y suministro', 'Logística', 'Todas', 'España, Portugal · 3 almacenes', 'Logística', ('ok', 'Publicado'), 5)]

def head(eb, t, sub, right=''):
    return '''      <div style="display: flex; align-items: flex-end; gap: 14px;"><div style="flex: 1; min-width: 0;"><span class="eb">%s</span><h1 style="margin: 4px 0 0; font-size: 27px; font-weight: 700; letter-spacing: -.01em;">%s</h1><p style="margin: 4px 0 0; font-size: 13.5px; color: #4A5650;">%s</p></div>%s</div>''' % (eb, t, sub, right)

# ============ V1 · Lista de servicios ============
G = 'grid-template-columns: 36px minmax(0,1.5fr) minmax(0,1.1fr) minmax(0,1.3fr) 92px 56px;'
rows = '\n'.join('''        <div style="display: grid; %s gap: 10px; align-items: center; padding: 9px 14px; border-top: 1px solid #EEF1EE; font-size: 12.5px;%s"><span style="width: 34px; height: 34px; border-radius: 9px; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center;">%s</span><span style="display: flex; flex-direction: column; min-width: 0;"><strong style="font-weight: 600;">%s</strong><span style="font-size: 11px; color: #56615B;">%s</span></span><span style="font-size: 12px; color: #2F3D36;">%s</span><span style="font-size: 12px; color: #2F3D36;">%s</span><span class="st %s">%s</span><span style="text-align: right; font-size: 12px; color: #4A5650;">%s</span></div>''' % (G, ' background: #F5FAF6; box-shadow: inset 3px 0 0 #0E5A3A;' if i == 1 else '', ic(I[k], 17), n, t, e, z, s[0], s[1], str(sol) if sol else '—') for i, (k, n, t, e, z, q, s, sol) in enumerate(SERV))
v1 = '''    <div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 14px;">
%s
      <div style="display: flex; gap: 8px; align-items: center;"><span style="flex: 1; height: 36px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; gap: 8px; padding: 0 11px; color: #8A948F; font-size: 12.5px; background: #FFFFFF;">%s Buscar servicio</span><span class="btn" style="font-weight: 400;">Especie ▾</span><span class="btn" style="font-weight: 400;">Zona ▾</span><span class="btn" style="font-weight: 400;">Modalidad ▾</span></div>
      <div style="background: #FFFFFF; border: 1px solid #E6EBE7; border-radius: 16px; overflow: hidden;">
        <div style="display: grid; %s gap: 10px; padding: 8px 14px; background: #F6F8F6; font-size: 11px; font-weight: 600; color: #56615B; letter-spacing: .03em;"><span></span><span>SERVICIO</span><span>ESPECIES</span><span>DÓNDE</span><span>ESTADO</span><span style="text-align: right;">SOLIC.</span></div>
%s
      </div>
      <section class="card" style="gap: 8px;">
        <p class="h" style="font-size: 13.5px;">Cómo se muestran en tu ficha</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;"><label class="lbl">Título de la pestaña<input class="inp" type="text" value="Servicios de valor añadido"></label><label class="lbl">Subtítulo<input class="inp" type="text" value="Te acompañamos en todas las fases de tu proyecto"></label></div>
        <span class="hint">Cada comprador ve primero los servicios disponibles para su especie y su zona.</span>
      </section>
    </div>''' % (head('MÓDULO SERVICIOS', 'Servicios', 'Lo que ofreces además de tus productos. Cada servicio tiene su botón «Solicitar».', '<button type="button" class="btnp">%s Nuevo servicio</button>' % ic(I['plus'], 16, 2.2)), ic(I['search'], 15), G, rows)
page('ServLista', 'Servicios · Lista', v1, pie=False)

# ============ V2 · Editor de un servicio ============
def chip(t, on, extra=''):
    return '<span style="display: inline-flex; align-items: center; gap: 4px; height: 28px; padding: 0 11px; border-radius: 999px; font-size: 12px; white-space: nowrap; %s">%s%s%s</span>' % ('background: #0E5A3A; color: #FFFFFF; font-weight: 500;' if on else 'background: #F2F5F3; color: #17231D;', '✓ ' if on else '', t, extra)
esp = ''.join(chip(e, e in ('Avicultura', 'Porcino'), ' <span style="opacity:.75;font-weight:400">· 3</span>' if e == 'Avicultura' else (' <span style="opacity:.75;font-weight:400">· todas</span>' if e == 'Porcino' else '')) for e, _ in TREE)
avcats = ''.join(chip(c, c in ('Pollos de engorde', 'Gallinas ponedoras', 'Reproductoras')) for c, _ in dict(TREE)['Avicultura'])
tok = lambda t, d: '<span style="display: inline-flex; align-items: center; gap: 5px; height: 30px; padding: 0 10px; border-radius: 999px; background: #EEF6EE; color: #0E5A3A; border: 1px solid #CFE0D5; font-size: 12px; font-weight: 500; white-space: nowrap;">%s<span style="color: #4A5650; font-weight: 400;">· %s</span> ×</span>' % (t, d)
v2form = '''    <form style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 9px;">
%s
      <section class="card" style="gap: 9px;">
        <div style="display: grid; grid-template-columns: 1.3fr 1fr; gap: 10px;"><label class="lbl">Nombre<input class="inp" type="text" value="Auditoría nutricional"></label><label class="lbl">Tipo de servicio<select class="inp"><option>Consultoría nutricional</option></select></label></div>
        <label class="lbl"><span>Descripción <span class="hint">· máx. 300</span></span><input class="inp" type="text" value="Analizamos tus dietas, materias primas y resultados y te proponemos mejoras concretas."></label>
      </section>
      <section class="card" style="gap: 8px;">
        <div style="display: flex; align-items: baseline; gap: 8px;"><p class="h" style="font-size: 13.5px;">Especies</p><span class="hint">· marca la especie; afina si el servicio es solo para algunas categorías</span></div>
        <div style="display: flex; flex-wrap: wrap; gap: 6px;">%s</div>
        <div style="display: flex; gap: 8px; align-items: flex-start; background: #F6F8F6; border-radius: 10px; padding: 8px 10px;"><span style="font-size: 11.5px; color: #4A5650; width: 74px; flex: none; padding-top: 6px;">Avicultura</span><span style="display: flex; flex-wrap: wrap; gap: 5px;">%s</span></div>
      </section>
      <section class="card" style="gap: 8px;">
        <p class="h" style="font-size: 13.5px;">Dónde lo prestas</p>
        <div style="display: flex; gap: 8px; align-items: flex-start;"><label class="cc" style="width: 104px; flex: none; padding-top: 6px;"><input type="checkbox" defaultChecked="{{ yes }}">Presencial</label><span style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;">%s%s<a href="#" style="font-size: 12px;">+ Zona</a></span></div>
        <div style="display: flex; gap: 8px; align-items: flex-start;"><label class="cc" style="width: 104px; flex: none; padding-top: 6px;"><input type="checkbox" defaultChecked="{{ yes }}">A distancia</label><span style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;">%s<span class="hint">· en español y portugués</span></span></div>
      </section>
      <section class="card" style="gap: 8px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px;"><label class="lbl">Plazo de respuesta<select class="inp"><option>48 horas</option></select></label><label class="lbl">Precio<select class="inp"><option>A consultar</option><option>Desde…</option></select></label><label class="lbl">«Solicitar» llega a<select class="inp"><option>Equipo de nutrición (2)</option></select></label></div>
      </section>
    </form>''' % (head('MÓDULO SERVICIOS · EDITAR', 'Auditoría nutricional', 'Con especies y zonas, cada comprador ve los servicios que de verdad puede contratar.'), esp, avcats,
       tok('España', 'Cataluña, Aragón, Navarra'), tok('Portugal', 'Norte'), tok('Todo el mundo', 'excepto Asia'))
v2prev = '''    <aside aria-label="Vista previa" style="width: 340px; flex: none; align-self: stretch; overflow: hidden; background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 20px; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 12px; box-shadow: 0 10px 30px rgba(16,40,28,.06);">
      <div style="display: flex; align-items: flex-start; gap: 10px;"><span style="width: 36px; height: 36px; border-radius: 50%%; background: #0E5A3A; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none;">%s</span><span style="flex: 1; display: flex; flex-direction: column; gap: 1px;"><strong style="font-size: 14.5px; font-weight: 600;">Vista previa</strong><span style="font-size: 11.5px; color: #56615B;">Un comprador de Lleida con broilers</span></span></div>
      <div style="border: 1px solid #E6EBE7; border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 8px;">
        <span style="width: 34px; height: 34px; border-radius: 9px; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center;">%s</span>
        <strong style="font-size: 15px;">Auditoría nutricional</strong>
        <span style="font-size: 11.5px; color: #4A5650; line-height: 1.45;">Analizamos tus dietas, materias primas y resultados y te proponemos mejoras concretas.</span>
        <span style="display: flex; flex-wrap: wrap; gap: 4px;"><span style="font-size: 10.5px; background: #F2F5F3; border-radius: 999px; padding: 2px 8px;">Pollos de engorde</span><span style="font-size: 10.5px; background: #F2F5F3; border-radius: 999px; padding: 2px 8px;">Ponedoras</span><span style="font-size: 10.5px; background: #F2F5F3; border-radius: 999px; padding: 2px 8px;">Porcino</span></span>
        <span style="display: flex; align-items: center; gap: 6px; font-size: 11.5px; color: #0E5A3A; font-weight: 500;">%s Disponible en tu zona · presencial y a distancia</span>
        <span style="font-size: 11px; color: #56615B;">Respuesta en 48 h · precio a consultar</span>
        <span style="height: 34px; border-radius: 9px; background: #0E5A3A; color: #FFFFFF; font-size: 12px; font-weight: 500; display: flex; align-items: center; justify-content: center;">Solicitar →</span>
      </div>
      <div style="border: 1px dashed #DCE3DE; border-radius: 12px; padding: 10px; font-size: 11px; color: #4A5650; line-height: 1.45;"><strong style="color: #17231D;">Comprador en Sevilla:</strong> no ve la visita presencial; ve «Disponible a distancia».</div>
      <div style="border: 1px dashed #DCE3DE; border-radius: 12px; padding: 10px; font-size: 11px; color: #4A5650; line-height: 1.45;"><strong style="color: #17231D;">Comprador de vacuno:</strong> el servicio no aparece en su búsqueda.</div>
    </aside>''' % (ic(I['eye'], 17), ic(I['chart'], 17), ic(I['pin'], 13))
page('ServEditor', 'Servicios · Editar un servicio', v2form + '\n' + v2prev)
print('ok')
