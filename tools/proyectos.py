import os, sys
D = sys.argv[1]

CSS = """body{margin:0;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#0E5A3A;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E6EBE7;border-radius:16px;padding:14px 16px;box-shadow:0 1px 2px rgba(16,40,28,.04);display:flex;flex-direction:column;gap:10px;min-width:0}
.h{font-size:14.5px;font-weight:600;margin:0}
.hint{font-weight:400;color:#56615B;font-size:11.5px}
.lbl{font-size:12.5px;font-weight:500;display:flex;flex-direction:column;gap:5px;min-width:0}
.inp{height:38px;border:1px solid #D5DED8;border-radius:10px;padding:0 12px;font:400 13px 'Poppins',sans-serif;color:#17231D;background:#FFFFFF;width:100%;box-sizing:border-box}
.ta{border:1px solid #D5DED8;border-radius:10px;padding:9px 12px;font:400 13px 'Poppins',sans-serif;color:#17231D;resize:none;line-height:1.45;width:100%;box-sizing:border-box}
.on{display:inline-flex;align-items:center;gap:4px;height:28px;padding:0 11px;border-radius:999px;background:#0E5A3A;color:#FFFFFF;font-size:12px;font-weight:500;white-space:nowrap}
.off{display:inline-flex;align-items:center;gap:4px;height:28px;padding:0 11px;border-radius:999px;background:#F2F5F3;color:#17231D;font-size:12px;white-space:nowrap}
.tok{display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 10px;border-radius:999px;background:#EEF6EE;color:#0E5A3A;border:1px solid #CFE0D5;font-size:12px;font-weight:500;white-space:nowrap}
.st{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap;display:inline-flex;align-items:center}
.ok{background:#EEF6EE;color:#0E5A3A}.dr{background:#F2F5F3;color:#4A5650}.wn{background:#FFF4E0;color:#7A4B00}.nw{background:#E7EEFB;color:#2A4A8C}.lila{background:#F1EEFB;color:#4B3BA6}
.btn{height:36px;padding:0 14px;border-radius:10px;border:1px solid #DCE3DE;background:#FFFFFF;color:#17231D;font:500 12.5px 'Poppins',sans-serif;display:inline-flex;align-items:center;gap:7px;white-space:nowrap;box-sizing:border-box}
.btnp{height:38px;padding:0 16px;border-radius:10px;border:0;background:#0E5A3A;color:#FFFFFF;font:600 13px 'Poppins',sans-serif;display:inline-flex;align-items:center;gap:7px;white-space:nowrap}
.eb{font-size:11.5px;font-weight:600;letter-spacing:.09em;color:#56615B}
.cc{display:flex;align-items:center;gap:8px;font-size:12.5px}
.cc input{accent-color:#0E5A3A;margin:0}
.opt{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border:1px solid #DCE3DE;border-radius:12px;font-size:12px;background:#FFFFFF}
.opt.sel{border:1.5px solid #0E5A3A;background:#F5FAF6}
.opt input{accent-color:#0E5A3A;margin:2px 0 0}
.tabs{display:flex;gap:22px;border-bottom:1px solid #E3E8E4;font-size:13px;color:#56615B;white-space:nowrap}
.tabs span{padding-bottom:9px}
.tabs .t-on{color:#0E5A3A;font-weight:600;border-bottom:2px solid #0E5A3A;margin-bottom:-1px}
.why{display:inline-flex;align-items:center;gap:4px;font-size:11px;color:#0E5A3A;background:#EEF6EE;border-radius:6px;padding:2px 7px;white-space:nowrap}
"""

def ic(d, s=18, w=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>' % (s, s, w, d)
I = {
 'home': '<path d="M3 11 12 4l9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>', 'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/>',
 'grid': '<path d="M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z"/>', 'cmp': '<path d="M4 5a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v14a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1zM12 4v16"/>',
 'proj': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h4"/>', 'msg': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 'user': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>', 'bell': '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
 'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>', 'inbox': '<path d="M4 13h4l2 3h4l2-3h4M5 5h14l2 8v5a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-5z"/>',
 'pkg': '<path d="M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8"/>', 'bldg': '<path d="M5 3h14v18H5zM9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2"/>',
 'layers': '<path d="m12 3 9 5-9 5-9-5zM3 13l9 5 9-5"/>', 'cap': '<path d="M22 9 12 4 2 9l10 5zM6 11v5c3 2 9 2 12 0v-5"/>', 'plus': '<path d="M12 5v14M5 12h14"/>',
 'pin': '<path d="M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/>', 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'euro': '<path d="M17 6a7 7 0 1 0 0 12M4 10h9M4 14h9"/>', 'lock': '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
 'eye': '<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>', 'bm': '<path d="M6 3h12v18l-6-4-6 4z"/>', 'check': '<path d="m5 12 5 5 9-10"/>',
 'send': '<path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/>', 'doc': '<path d="M6 3h9l3 3v15H6z"/><path d="M9 9h6M9 13h6M9 17h4"/>', 'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
}
CROWN = '<svg width="20" height="20" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 8l4 3 5-6 5 6 4-3-2 10H5z" fill="#F2B530" stroke="#D99A12" stroke-width="1" stroke-linejoin="round"/></svg>'

def shell(title, space, main, active, h=900):
    S = SPACES[space]
    items = ''.join('<a href="#" style="display: flex; align-items: center; gap: 11px; height: 40px; padding: 0 12px; border-radius: 10px; font-size: 13.5px; text-decoration: none; %s">%s<span style="flex: 1;">%s</span>%s</a>%s' % (
        ('background: %s; color: %s; font-weight: 600;' % (S['soft'], S['acc'])) if t == active else 'color: #17231D; font-weight: 400;', ic(I[k], 19), t,
        ('<span style="min-width: 20px; height: 20px; border-radius: 999px; background: %s; color: %s; font-size: 11px; font-weight: 600; display: flex; align-items: center; justify-content: center; padding: 0 5px; box-sizing: border-box;">%s</span>' % (S['acc'] if b != 'NUEVO' else '#B5D334', '#FFFFFF' if b != 'NUEVO' else '#17231D', b)) if b else '',
        ''.join('<a href="#" style="display: block; padding: 5px 12px 5px 42px; font-size: 12.5px; text-decoration: none; %s">%s</a>' % (('color: %s; font-weight: 600;' % S['acc']) if s == active else 'color: #4A5650; font-weight: 400;', s) for s in subs) if subs and (t == active or active in subs) else '')
        for k, t, b, subs in S['items'])
    return '''<!doctype html>
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
<div style="width: 1280px; height: %dpx; position: relative; overflow: hidden; background: #F6F8F6;">
  <header style="height: 64px; box-sizing: border-box; padding: 0 24px; display: flex; align-items: center; gap: 18px; background: #FFFFFF; border-bottom: 1px solid #E8ECE9;">
    <img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height: 28px; width: auto; display: block;">
    <span style="margin-left: 40px; flex: 1; max-width: 520px; height: 40px; border: 1px solid #DCE3DE; border-radius: 999px; background: #F7F9F7; display: flex; align-items: center; gap: 8px; padding: 0 14px; font-size: 13px; color: #8A948F;">%s %s</span>
    <span style="margin-left: auto; display: flex; align-items: center; gap: 16px;"><span style="color: #4A5650; display: flex; position: relative;">%s<span style="position: absolute; top: -1px; right: -1px; width: 8px; height: 8px; border-radius: 50%%; background: #D93A3A; border: 2px solid #FFFFFF;"></span></span><span style="display: flex; align-items: center; gap: 10px;"><span style="width: 36px; height: 36px; border-radius: %s; background: %s; color: #FFFFFF; font-size: 13px; font-weight: 600; display: flex; align-items: center; justify-content: center;">%s</span><span style="display: flex; flex-direction: column; line-height: 1.2;"><span style="font-size: 13.5px; font-weight: 500;">%s</span><span style="font-size: 11px; color: #56615B;">%s</span></span></span></span>
  </header>
  <nav style="position: absolute; top: 64px; left: 0; bottom: 0; width: 240px; box-sizing: border-box; background: #FFFFFF; border-right: 1px solid #E8ECE9; padding: 18px 12px; display: flex; flex-direction: column; gap: 2px;">
    <span class="eb" style="padding: 0 12px 10px;">%s</span>
    %s
    <div style="margin-top: auto; background: #F2F6F3; border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 6px;"><span style="display: flex; align-items: center; gap: 8px;">%s<span style="font-size: 13px; font-weight: 600;">%s</span></span><span style="font-size: 11.5px; color: #4A5650; line-height: 1.4;">%s</span><a href="#" style="font-size: 12px;">%s →</a></div>
  </nav>
  <main style="position: absolute; top: 64px; left: 240px; right: 0; bottom: 0; padding: 22px 28px; display: flex; flex-direction: column; gap: 14px;">
%s
  </main>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":1280,"height":%d}}'>
class Component extends DCLogic {
  renderVals() { return { yes: true }; }
}
</script>
</body>
</html>
''' % (title, CSS, h, ic(I['search'], 15), S['search'], ic(I['bell'], 20), S['radius'], S['acc'], S['ini'], S['name'], S['role'], S['eb'], items, CROWN, S['plan'], S['plantxt'], S['planbtn'], main, h)

SPACES = {
 'personal': {'acc': '#0E5A3A', 'soft': '#EEF6EE', 'ini': 'SE', 'radius': '50%', 'name': 'Samuel Esteban', 'role': 'Granjero · Granja Los Olmos', 'search': 'Buscar productos, empresas, expertos…', 'eb': 'MI ESPACIO',
              'items': [('home', 'Inicio', '', []), ('search', 'Buscar', '', []), ('proj', 'Mis proyectos', 'NUEVO', ['Activos', 'Borradores', 'Finalizados']), ('grid', 'Mis tableros', '', []), ('cmp', 'Mis comparaciones', '', []), ('msg', 'Mensajes', '3', []), ('user', 'Mi perfil', '', [])],
              'plan': 'Plan Gratis', 'plantxt': '1 de 2 proyectos activos. Con Comprador Pro, ilimitados.', 'planbtn': 'Ver planes'},
 'empresa': {'acc': '#0E5A3A', 'soft': '#EEF6EE', 'ini': 'AN', 'radius': '10px', 'name': 'AgroNova', 'role': 'Laura García · Admin', 'search': 'Buscar oportunidades, empresas…', 'eb': 'AGRONOVA · EMPRESA',
             'items': [('home', 'Panel', '', []), ('target', 'Oportunidades', '6', ['Recomendadas', 'Todas', 'Mis propuestas', 'Adjudicadas']), ('inbox', 'Solicitudes', '4', []), ('pkg', 'Productos', '', []), ('layers', 'Servicios', '', []), ('bldg', 'Perfil de empresa', '', []), ('msg', 'Mensajes', '', [])],
             'plan': 'Plan Gratis', 'plantxt': '2 de 3 propuestas este mes. Con Empresa Pro, ilimitadas.', 'planbtn': 'Ver planes'},
 'experto': {'acc': '#4B3BA6', 'soft': '#F1EEFB', 'ini': 'LG', 'radius': '50%', 'name': 'Laura Gil', 'role': 'Veterinaria · Experta', 'search': 'Buscar proyectos, temas, empresas…', 'eb': 'COMO EXPERTA',
             'items': [('home', 'Panel de experta', '', []), ('target', 'Proyectos', '3', ['Para ti', 'Todos', 'Mis candidaturas', 'Adjudicados']), ('inbox', 'Consultas recibidas', '1', []), ('layers', 'Mis servicios', '', []), ('cap', 'Perfil de experta', '', []), ('msg', 'Mensajes', '', [])],
             'plan': 'Experta Gratis', 'plantxt': '1 de 3 candidaturas este mes. Con Experto Pro, ilimitadas.', 'planbtn': 'Cambiar de plan'},
}

def write(n, html):
    open(os.path.join(D, n + '.dc.html'), 'w').write(html)

def head(eb, t, sub, right=''):
    return '    <div style="display: flex; align-items: flex-end; gap: 14px;"><div style="flex: 1; min-width: 0;"><span class="eb">%s</span><h1 style="margin: 4px 0 0; font-size: 26px; font-weight: 700; letter-spacing: -.01em;">%s</h1><p style="margin: 3px 0 0; font-size: 13px; color: #4A5650;">%s</p></div>%s</div>' % (eb, t, sub, right)

STEPS = ['Qué necesitas', 'Para qué animales y dónde', 'Detalles', 'A quién se lo enviamos', 'Revisar y publicar']
def stepper(cur):
    return '<div style="width: 210px; flex: none; display: flex; flex-direction: column; gap: 4px;">' + ''.join('<div style="display: flex; align-items: center; gap: 10px; padding: 9px 10px; border-radius: 10px; font-size: 12.5px; %s"><span style="width: 24px; height: 24px; border-radius: 50%%; flex: none; display: flex; align-items: center; justify-content: center; font-size: 11px; font-weight: 600; box-sizing: border-box; %s">%s</span>%s</div>' % (
        'background: #EEF6EE; color: #0E5A3A; font-weight: 600;' if i == cur else ('color: #17231D;' if i < cur else 'color: #56615B;'),
        'background: #0E5A3A; color: #FFFFFF;' if i < cur else ('border: 2px solid #0E5A3A; color: #0E5A3A;' if i == cur else 'border: 1.5px solid #CFD8D2; color: #8A948F;'), '✓' if i < cur else i, t) for i, t in enumerate(STEPS, 1)) + '</div>'

# ===================== P1 · Crear proyecto · paso 1 =====================
p1 = head('MIS PROYECTOS · NUEVO', 'Cuéntanos tu proyecto', 'Lo enviamos a empresas y expertos que encajan. Gratis y sin compromiso.') + '''
    <div style="display: flex; gap: 20px; flex: 1; min-height: 0;">
      %s
      <form style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 12px;">
        <section class="card" style="gap: 8px;">
          <p class="h">¿Qué necesitas?</p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
            <label class="opt sel"><input type="radio" name="tipo" defaultChecked="{{ yes }}"><span><strong style="font-size: 13px; font-weight: 600;">Productos o equipos</strong><br><span style="color: #4A5650;">Comprar o renovar</span></span></label>
            <label class="opt"><input type="radio" name="tipo"><span><strong style="font-size: 13px; font-weight: 600;">Un servicio</strong><br><span style="color: #4A5650;">Asesoría, análisis, formación…</span></span></label>
            <label class="opt"><input type="radio" name="tipo"><span><strong style="font-size: 13px; font-weight: 600;">Un proyecto completo</strong><br><span style="color: #4A5650;">Nave nueva o reforma llave en mano</span></span></label>
            <label class="opt"><input type="radio" name="tipo"><span><strong style="font-size: 13px; font-weight: 600;">No lo sé</strong><br><span style="color: #4A5650;">Te ayuda un experto a definirlo</span></span></label>
          </div>
        </section>
        <section class="card" style="gap: 10px;">
          <label class="lbl">Categoría <span class="hint" style="margin-top: -3px;">Usamos el mismo catálogo de productos y servicios de Agroolink</span><select class="inp"><option>Equipamiento e instalaciones › Sistemas de alimentación automática</option></select></label>
          <div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;"><span class="hint">Otras que suelen ir juntas:</span><span class="off">+ Bebederos</span><span class="off">+ Sistemas de ventilación</span><span class="off">+ Montaje</span></div>
          <label class="lbl">Título<input class="inp" type="text" value="Sistema de alimentación para nave nueva de broilers"></label>
          <label class="lbl">Descripción<textarea class="ta" rows="4">Construimos una segunda nave de 40.000 broilers en Lleida. Buscamos un sistema de alimentación completo (silos, transporte y líneas de comederos) con montaje y buen servicio técnico en la zona.</textarea></label>
        </section>
      </form>
      <aside style="width: 290px; flex: none; display: flex; flex-direction: column; gap: 12px;">
        <section class="card" style="gap: 8px; background: #F2F7F3; border-color: #DCE9DF;">
          <span style="display: flex; align-items: center; gap: 8px; color: #0E5A3A;">%s<strong style="font-size: 13.5px; color: #17231D;">Ya encajan</strong></span>
          <strong style="font-size: 30px; font-weight: 700; color: #0E5A3A; line-height: 1;">27 <span style="font-size: 13px; font-weight: 500; color: #2F3D36;">empresas</span></strong>
          <span style="font-size: 12px; color: #4A5650; line-height: 1.45;">tienen sistemas de alimentación en su catálogo. Lo afinamos en los pasos siguientes con especie y zona.</span>
        </section>
        <section class="card" style="gap: 6px;"><p class="h" style="font-size: 13.5px;">Consejos</p><ul style="margin: 0; padding-left: 18px; font-size: 12px; color: #2F3D36; line-height: 1.55;"><li>Di el tamaño y el plazo: recibirás propuestas más concretas.</li><li>Puedes adjuntar planos o fotos en «Detalles».</li><li>Tus datos de contacto no se muestran hasta que respondas a una propuesta.</li></ul></section>
      </aside>
    </div>
    <div style="display: flex; justify-content: flex-end; gap: 10px;"><button type="button" class="btn" style="height: 42px;">Guardar borrador</button><button type="button" class="btnp" style="height: 42px;">Siguiente →</button></div>''' % (stepper(1), ic(I['target'], 18))
write('ProyCrear', shell('Proyectos · Crear proyecto', 'personal', p1, 'Mis proyectos'))

# ===================== P2 · Crear proyecto · paso 4 =====================
p2 = head('MIS PROYECTOS · NUEVO', 'A quién se lo enviamos', 'Decides quién lo ve. Por defecto, solo empresas y expertos que encajan con tu proyecto.') + '''
    <div style="display: flex; gap: 20px; flex: 1; min-height: 0;">
      %s
      <form style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 11px;">
        <section class="card" style="gap: 7px; padding: 12px 16px;">
          <span class="hint">De los pasos anteriores</span>
          <div style="display: flex; flex-wrap: wrap; gap: 6px;"><span class="tok">Sistemas de alimentación automática</span><span class="tok">Avicultura · Broilers</span><span class="tok">%s Lleida, España</span><span class="tok">40.000 aves</span><span class="tok">Antes de marzo de 2027</span></div>
        </section>
        <section class="card" style="gap: 9px;">
          <p class="h">Quién puede responder</p>
          <div style="display: flex; gap: 8px; align-items: flex-start;"><label class="cc" style="width: 110px; flex: none; padding-top: 5px;"><input type="checkbox" defaultChecked="{{ yes }}"><strong style="font-weight: 600;">Empresas</strong></label><span style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;"><span class="on">✓ Instalación Equipo <span style="opacity:.75;font-weight:400">· Equipamientos</span></span><span class="on">✓ Distribuidor</span><span class="on">✓ Montador</span><a href="#" style="font-size: 12px;">+ Rama</a></span></div>
          <div style="display: flex; gap: 8px; align-items: flex-start;"><label class="cc" style="width: 110px; flex: none; padding-top: 5px;"><input type="checkbox" defaultChecked="{{ yes }}"><strong style="font-weight: 600;">Expertos</strong></label><span style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;"><span class="on" style="background: #4B3BA6;">✓ Consultor</span><span class="on" style="background: #4B3BA6;">✓ Director Técnico</span><a href="#" style="font-size: 12px; color: #4B3BA6;">+ Cargo</a></span></div>
          <div style="display: flex; gap: 8px; align-items: flex-start;"><span style="width: 110px; flex: none; font-size: 12.5px; padding-top: 5px; font-weight: 600;">Zona</span><span style="display: flex; flex-direction: column; gap: 5px;"><label class="cc"><input type="radio" name="zona" defaultChecked="{{ yes }}">Que trabajen en Lleida <span class="hint">· por su zona, sus comerciales o sus distribuidores</span></label><label class="cc"><input type="radio" name="zona">Toda España</label></span></div>
        </section>
        <section class="card" style="gap: 8px;">
          <p class="h">Visibilidad</p>
          <label class="opt sel"><input type="radio" name="vis" defaultChecked="{{ yes }}"><span><strong style="font-size: 13px; font-weight: 600;">Abierto a quien encaje</strong> <span class="st ok" style="margin-left: 4px;">Recomendado</span><br><span style="color: #4A5650;">Lo ven las 23 empresas y 4 expertos que encajan. Puedes invitar a más.</span></span></label>
          <label class="opt"><input type="radio" name="vis"><span><strong style="font-size: 13px; font-weight: 600;">Solo a quien invite</strong><br><span style="color: #4A5650;">Por ejemplo, las 3 empresas de tu tablero «Nave 2 · broilers».</span></span></label>
          <label class="cc"><input type="checkbox" defaultChecked="{{ yes }}">Cerrar cuando reciba 10 propuestas <span class="hint">· puedes ampliarlo</span></label>
        </section>
      </form>
      <aside style="width: 290px; flex: none; display: flex; flex-direction: column; gap: 12px;">
        <section class="card" style="gap: 10px;">
          <p class="h" style="font-size: 13.5px;">Lo recibirán</p>
          <div style="display: flex; align-items: baseline; gap: 14px;"><span><strong style="font-size: 28px; color: #0E5A3A;">23</strong> <span style="font-size: 12px;">empresas</span></span><span><strong style="font-size: 28px; color: #4B3BA6;">4</strong> <span style="font-size: 12px;">expertos</span></span></div>
          <div style="display: flex; flex-direction: column; gap: 5px; font-size: 11.5px; color: #2F3D36;"><span>14 fabricantes con comercial o distribuidor en Lleida</span><span>6 distribuidores de la zona</span><span>3 montadores</span></div>
          <span style="font-size: 11.5px; color: #56615B; line-height: 1.45;">Los fabricantes con red de distribuidores lo reciben junto a su distribuidor de la zona.</span>
        </section>
        <section class="card" style="gap: 6px; background: #F2F7F3; border-color: #DCE9DF;"><span style="display: flex; align-items: center; gap: 8px; color: #0E5A3A;">%s<strong style="font-size: 13px; color: #17231D;">Tu privacidad</strong></span><span style="font-size: 12px; color: #4A5650; line-height: 1.45;">Verán «Granja de broilers en Lleida». Tu nombre y tu contacto, solo cuando respondas a una propuesta.</span></section>
      </aside>
    </div>
    <div style="display: flex; justify-content: space-between;"><button type="button" class="btn" style="height: 42px;">← Atrás</button><button type="button" class="btnp" style="height: 42px;">Siguiente: revisar →</button></div>''' % (stepper(4), ic(I['pin'], 13), ic(I['lock'], 16))
write('ProyDestinatarios', shell('Proyectos · A quién se lo enviamos', 'personal', p2, 'Mis proyectos'))

# ===================== P3 · Mis proyectos =====================
def pcard(title, cat, st, stc, props, newp, vistas, close, extra):
    return '''      <article class="card" style="flex-direction: row; align-items: center; gap: 16px;">
        <span style="width: 92px; height: 74px; border-radius: 12px; background: linear-gradient(135deg,#F6D9B8,#E9B98A); display: flex; align-items: center; justify-content: center; font-size: 30px; flex: none;">%s</span>
        <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 4px;"><span style="display: flex; align-items: center; gap: 8px;"><strong style="font-size: 15px; font-weight: 600;">%s</strong><span class="st %s">%s</span></span><span style="font-size: 12px; color: #56615B;">%s</span>
          <span style="display: flex; gap: 16px; font-size: 12px; color: #2F3D36; margin-top: 2px;"><span>%s</span><span>%s</span><span>%s</span></span></span>
        %s
      </article>''' % (extra, title, stc, st, cat, props, vistas, close, newp)
p3 = head('MI ESPACIO', 'Mis proyectos', 'Publica lo que necesitas y recibe propuestas de empresas y expertos.', '<button type="button" class="btnp">%s Nuevo proyecto</button>' % ic(I['plus'], 16, 2.2)) + '''
    <div class="tabs"><span class="t-on">Activos 2</span><span>Borradores 1</span><span>Finalizados 0</span></div>
%s
%s
%s
    <section class="card" style="flex-direction: row; align-items: center; gap: 14px; background: #F2F7F3; border-color: #DCE9DF;"><span style="color: #0E5A3A; display: flex;">%s</span><span style="flex: 1; font-size: 12.5px;"><strong style="font-weight: 600;">Ligado a tu tablero «Nave 2 · broilers».</strong> Las propuestas que te interesen se guardan allí con su estado.</span><a href="#" style="font-size: 12.5px;">Abrir tablero</a></section>''' % (
    pcard('Sistema de alimentación · Nave 2', 'Equipamiento › Sistemas de alimentación · Avicultura › Broilers · Lleida', 'Recibiendo propuestas', 'ok', '<strong>4</strong> propuestas', '<span style="display: flex; flex-direction: column; align-items: flex-end; gap: 6px;"><span class="st nw">2 nuevas</span><button type="button" class="btnp" style="height: 34px;">Ver propuestas</button></span>', '23 empresas lo han visto', 'Cierra en 12 días', '🐔'),
    pcard('Asesoría en bioseguridad', 'Servicio › Consultoría veterinaria · Avicultura · Lleida', 'Recibiendo propuestas', 'ok', '<strong>1</strong> propuesta', '<span style="display: flex; flex-direction: column; align-items: flex-end; gap: 6px;"><button type="button" class="btn" style="height: 34px;">Ver propuesta</button></span>', '4 expertos lo han visto', 'Cierra en 20 días', '🧪'),
    pcard('Ventilación y cooling · Nave 1', 'Equipamiento › Ventilación · borrador', 'Borrador', 'dr', 'Falta el paso «Detalles»', '<span style="display: flex; flex-direction: column; align-items: flex-end; gap: 6px;"><button type="button" class="btn" style="height: 34px;">Continuar</button></span>', '', '', '🌬'),
    ic(I['grid'], 18))
write('ProyMis', shell('Proyectos · Mis proyectos', 'personal', p3, 'Activos'))

# ===================== P4 · Detalle y propuestas =====================
PR = [('AN', '#1E8A3C', 'AgroNova', 'Distribuidor validado de Roxell · Lleida', 'Roxell Feedmax + silos y transporte, montaje incluido', '48.000 – 55.000 €', '8 semanas', '2 años', 'nw', 'Nueva', 96),
      ('ZU', '#1E8A3C', 'Zucami', 'Fabricante · comercial Zona Nordeste', 'FeedLine con transporte en espiral y control por peso', '52.000 – 60.000 €', '10 semanas', '3 años', 'nw', 'Nueva', 91),
      ('BD', '#C8102E', 'Big Dutchman', 'Fabricante · distribuidor en Cataluña', 'Línea FlexVey con comederos de plato', 'A consultar', '12 semanas', '2 años', 'wn', 'Te ha escrito', 88),
      ('MT', '#5B4B9E', 'Montajes Segre', 'Montador · Lleida', 'Solo montaje y puesta en marcha', '9.000 €', '3 semanas', '1 año', 'dr', 'Vista', 74)]
GP = 'grid-template-columns: minmax(0,1.45fr) minmax(0,1.6fr) 118px 84px 64px 150px;'
prow = '\n'.join('''        <div style="display: grid; %s gap: 12px; align-items: center; padding: 10px 14px; border-top: 1px solid #EEF1EE; font-size: 12.5px;%s"><span style="display: flex; align-items: center; gap: 10px; min-width: 0;"><span style="width: 34px; height: 34px; border-radius: 9px; background: %s; color: #FFFFFF; font-size: 11px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">%s</span><span style="display: flex; flex-direction: column; min-width: 0;"><strong style="font-weight: 600;">%s</strong><span style="font-size: 10.5px; color: #56615B;">%s</span></span></span><span style="color: #2F3D36; font-size: 12px; line-height: 1.35;">%s</span><span style="font-weight: 600;">%s</span><span>%s</span><span>%s</span><span style="display: flex; align-items: center; gap: 6px; justify-content: flex-end;"><span class="st %s">%s</span><span style="font-size: 11px; color: #0E5A3A; font-weight: 600;">%d%%</span></span></div>''' % (GP, ' background: #F5FAF6;' if i == 0 else '', c, ini, n, sub, sol, pr, pl, ga, s, stt, m) for i, (ini, c, n, sub, sol, pr, pl, ga, s, stt, m) in enumerate(PR))
p4 = '''    <a href="#" style="font-size: 12.5px; color: #56615B; font-weight: 400;">← Mis proyectos</a>
    <div style="display: flex; gap: 16px; align-items: center;">
      <span style="width: 80px; height: 64px; border-radius: 12px; background: linear-gradient(135deg,#F6D9B8,#E9B98A); display: flex; align-items: center; justify-content: center; font-size: 28px; flex: none;">🐔</span>
      <div style="flex: 1; min-width: 0;"><div style="display: flex; align-items: center; gap: 10px;"><h1 style="margin: 0; font-size: 24px; font-weight: 700;">Sistema de alimentación · Nave 2</h1><span class="st ok">Recibiendo propuestas</span></div><span style="font-size: 12.5px; color: #56615B;">Avicultura › Broilers · 40.000 aves · Lleida · antes de marzo de 2027 · cierra en 12 días</span></div>
      <span style="display: flex; gap: 8px;"><button type="button" class="btn">Editar</button><button type="button" class="btn">Invitar a más</button></span>
    </div>
    <div style="display: flex; gap: 10px;">''' + ''.join('<div class="card" style="flex: 1; padding: 10px 14px; gap: 2px; flex-direction: row; align-items: baseline; gap: 8px;"><strong style="font-size: 22px; color: %s;">%s</strong><span style="font-size: 12px; color: #4A5650;">%s</span></div>' % c for c in [('#0E5A3A', '23', 'empresas lo han visto'), ('#0E5A3A', '4', 'propuestas recibidas'), ('#7A4B00', '2', 'sin leer'), ('#4B3BA6', '1', 'experto interesado')]) + '''</div>
    <div class="tabs"><span>Resumen</span><span class="t-on">Propuestas 4</span><span>Mensajes 1</span><span>Actividad</span></div>
    <div style="background: #FFFFFF; border: 1px solid #E6EBE7; border-radius: 16px; overflow: hidden;">
      <div style="display: grid; %s gap: 12px; padding: 8px 14px; background: #F6F8F6; font-size: 11px; font-weight: 600; color: #56615B; letter-spacing: .03em;"><span>EMPRESA</span><span>SOLUCIÓN</span><span>PRECIO ORIENTATIVO</span><span>PLAZO</span><span>GARANTÍA</span><span style="text-align: right;">ESTADO · ENCAJE</span></div>
%s
    </div>
    <div style="display: flex; gap: 12px; align-items: stretch;">
      <section class="card" style="flex: 1; flex-direction: row; align-items: center; gap: 12px;"><span style="color: #0E5A3A; display: flex;">%s</span><span style="flex: 1; font-size: 12.5px;"><strong style="font-weight: 600;">AgroNova</strong> · «Incluimos el montaje con técnicos de Lleida y 2 visitas de seguimiento el primer año.»</span><span style="display: flex; gap: 8px;"><button type="button" class="btn">Ver propuesta</button><button type="button" class="btnp" style="height: 36px;">Responder</button></span></section>
      <section class="card" style="width: 300px; flex: none; gap: 6px; background: #F1EEFB; border-color: #E3DDF6;"><strong style="font-size: 13px; color: #4B3BA6;">¿Dudas al comparar?</strong><span style="font-size: 12px; color: #4A5650; line-height: 1.45;">Laura Gil, veterinaria, se ha ofrecido a revisar las propuestas contigo.</span><a href="#" style="font-size: 12px; color: #4B3BA6;">Ver su oferta →</a></section>
    </div>
    <span style="font-size: 11.5px; color: #56615B;">Al responder a una propuesta, esa empresa ve tu nombre y tu contacto. Las demás, no. Adjudicar cierra el proyecto y avisa a todas.</span>''' % (GP, prow, ic(I['msg'], 18))
write('ProyDetalle', shell('Proyectos · Detalle y propuestas', 'personal', p4, 'Activos'))

# ===================== P5 · Oportunidades (empresa) =====================
def opp(m, title, who, cat, budget, plazo, whys, props, cta, acc='#0E5A3A', soft='#EEF6EE', emo='🐔'):
    return '''      <article class="card" style="flex-direction: row; gap: 14px; align-items: stretch;">
        <span style="width: 96px; border-radius: 12px; background: linear-gradient(135deg,#F6D9B8,#E9B98A); display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; flex: none; position: relative; font-size: 30px;">%s<span style="position: absolute; top: 6px; left: 6px; font-size: 10.5px; font-weight: 700; background: %s; color: #FFFFFF; border-radius: 6px; padding: 2px 6px;">%d%%</span></span>
        <span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 5px;">
          <span style="display: flex; align-items: center; gap: 8px;"><strong style="font-size: 14.5px; font-weight: 600;">%s</strong><span style="margin-left: auto; color: #8A948F; display: flex;">%s</span></span>
          <span style="font-size: 12px; color: #4A5650;">%s · %s</span>
          <span style="display: flex; flex-wrap: wrap; gap: 5px;">%s</span>
          <span style="display: flex; gap: 14px; font-size: 11.5px; color: #2F3D36; align-items: center;"><span style="display: flex; align-items: center; gap: 4px;">%s %s</span><span style="display: flex; align-items: center; gap: 4px;">%s %s</span><span>%s</span><button type="button" class="btnp" style="height: 34px; margin-left: auto; background: %s;">%s</button></span>
        </span>
      </article>''' % (emo, acc, m, title, ic(I['bm'], 17), who, cat, ''.join('<span class="why" style="color: %s; background: %s;">✓ %s</span>' % (acc, soft, w) for w in whys), ic(I['euro'], 13), budget, ic(I['clock'], 13), plazo, props, acc, cta)
p5 = head('AGRONOVA', 'Oportunidades para tu empresa', 'Proyectos de ganaderos y empresas que encajan con tu catálogo, tus especies y tu zona.') + '''
    <div style="display: flex; align-items: center; gap: 16px;"><div class="tabs" style="flex: 1;"><span class="t-on">Recomendadas 6</span><span>Todas</span><span>Mis propuestas 2</span><span>Adjudicadas 1</span></div><span class="btn" style="height: 32px; font-weight: 400;">Especie ▾</span><span class="btn" style="height: 32px; font-weight: 400;">Zona ▾</span></div>
%s
%s
%s
    <section class="card" style="flex-direction: row; align-items: center; gap: 12px; padding: 12px 16px;"><span style="color: #0E5A3A; display: flex;">%s</span><span style="flex: 1; font-size: 12.5px;"><strong style="font-weight: 600;">Recibe más oportunidades:</strong> completa los mercados de 12 productos y añade zonas a 2 servicios.</span><a href="#" style="font-size: 12.5px;">Completar</a></section>''' % (
    opp(96, 'Sistema de alimentación · nave de 40.000 broilers', 'Granja de broilers en Lleida', 'Equipamiento › Sistemas de alimentación', 'No indicado', 'Antes de mar 2027', ['Tienes Roxell Feedmax en tu catálogo', 'Avicultura › Broilers', 'Lleida está en tu zona'], '4 de 10 propuestas', 'Preparar propuesta'),
    opp(85, 'Cambio de bebederos en 4 naves', 'Integradora en Huesca', 'Equipamiento › Bebederos', '15.000 – 25.000 €', '3 meses', ['Bebederos en tu catálogo', 'Huesca está en tu zona'], '1 de 10 propuestas', 'Preparar propuesta', emo='💧'),
    opp(78, 'Programa nutricional para cerdas', 'Granja porcina en Teruel', 'Servicio › Consultoría nutricional', 'A consultar', '1 mes', ['Diseño de programas de alimentación', 'Porcino', 'A distancia'], '0 propuestas', 'Preparar propuesta', emo='🐖'),
    ic(I['spark'], 18))
write('ProyOportunidades', shell('Proyectos · Oportunidades (empresa)', 'empresa', p5, 'Recomendadas'))

# ===================== P6 · Enviar propuesta (empresa) =====================
p6 = head('OPORTUNIDADES · PROPUESTA', 'Tu propuesta', 'Sistema de alimentación · nave de 40.000 broilers · Granja de broilers en Lleida') + '''
    <div style="display: flex; gap: 20px; flex: 1; min-height: 0;">
      <form style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 11px;">
        <section class="card" style="gap: 8px;"><label class="lbl">Mensaje<textarea class="ta" rows="3">Incluimos el montaje con técnicos de Lleida y 2 visitas de seguimiento el primer año. Podemos visitar la granja la semana que viene.</textarea></label></section>
        <section class="card" style="gap: 8px;">
          <div style="display: flex; align-items: baseline; gap: 8px;"><p class="h" style="font-size: 13.5px;">Qué ofreces</p><span class="hint">· de tu catálogo y tus servicios</span></div>
          <div style="display: flex; flex-wrap: wrap; gap: 6px; align-items: center;"><span class="tok">%s Roxell Feedmax ×</span><span class="tok">%s Silo 20 t ×</span><span class="tok">%s Montaje y puesta en marcha ×</span><span class="tok">%s Seguimiento de implantación ×</span><a href="#" style="font-size: 12px;">+ Añadir</a></div>
        </section>
        <section class="card" style="gap: 8px;">
          <div style="display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 10px;"><label class="lbl">Precio orientativo<span style="display: flex; gap: 6px; align-items: center;"><input class="inp" type="text" value="48.000"><span>–</span><input class="inp" type="text" value="55.000"><span>€</span></span></label><label class="lbl">Plazo<select class="inp"><option>8 semanas</option></select></label><label class="lbl">Garantía<select class="inp"><option>2 años</option></select></label></div>
          <label class="cc"><input type="checkbox">Prefiero no dar precio todavía <span class="hint">· se mostrará «A consultar»</span></label>
        </section>
        <section class="card" style="flex-direction: row; align-items: center; gap: 10px; padding: 12px 16px;"><span style="color: #0E5A3A; display: flex;">%s</span><span style="flex: 1; font-size: 12.5px;">Adjuntos <span class="hint">· oferta, planos, referencias</span></span><span class="tok" style="background: #FFFFFF;">Oferta_Nave2.pdf</span><button type="button" class="btn" style="height: 32px;">Subir</button></section>
        <div style="display: flex; justify-content: flex-end; gap: 10px;"><button type="button" class="btn" style="height: 42px;">Guardar borrador</button><button type="button" class="btnp" style="height: 42px;">%s Enviar propuesta</button></div>
      </form>
      <aside style="width: 330px; flex: none; display: flex; flex-direction: column; gap: 12px;">
        <section class="card" style="gap: 8px;">
          <span style="display: flex; align-items: center; gap: 8px; color: #0E5A3A;">%s<strong style="font-size: 13.5px; color: #17231D;">Así la verá el ganadero</strong></span>
          <div style="border: 1px solid #E6EBE7; border-radius: 12px; padding: 10px; display: flex; flex-direction: column; gap: 6px; font-size: 11.5px;">
            <span style="display: flex; align-items: center; gap: 8px;"><span style="width: 30px; height: 30px; border-radius: 8px; background: #1E8A3C; color: #FFFFFF; font-size: 10.5px; font-weight: 700; display: flex; align-items: center; justify-content: center;">AN</span><span><strong style="font-size: 12.5px;">AgroNova</strong><br><span style="color: #0E5A3A; font-weight: 600;">● Distribuidor validado de Roxell</span></span></span>
            <span style="color: #2F3D36;">Roxell Feedmax · silos · montaje · seguimiento</span>
            <span><strong>48.000 – 55.000 €</strong> · 8 semanas · garantía 2 años</span>
          </div>
        </section>
        <section class="card" style="gap: 6px;"><p class="h" style="font-size: 13.5px;">Sobre el proyecto</p><span style="font-size: 12px; color: #4A5650; line-height: 1.5;">Granja de broilers en Lleida · nave nueva de 40.000 aves · silos, transporte y comederos con montaje · antes de marzo de 2027.</span><span style="font-size: 11.5px; color: #56615B;">El nombre y el contacto del ganadero aparecen si responde a tu propuesta.</span></section>
        <section class="card" style="gap: 6px; background: #FFFBEF; border-color: #EFE6C6;"><span style="font-size: 12px; color: #4A5650; line-height: 1.45;"><strong style="color: #17231D;">Plan Gratis:</strong> esta es tu propuesta 3 de 3 este mes.</span><a href="#" style="font-size: 12px;">Empresa Pro: ilimitadas →</a></section>
      </aside>
    </div>''' % (ic(I['pkg'], 13), ic(I['pkg'], 13), ic(I['layers'], 13), ic(I['layers'], 13), ic(I['doc'], 17), ic(I['send'], 15), ic(I['eye'], 17))
write('ProyPropuesta', shell('Proyectos · Enviar propuesta (empresa)', 'empresa', p6, 'Recomendadas'))

# ===================== P7 · Proyectos para ti (experta) =====================
LI, LS = '#4B3BA6', '#F1EEFB'
p7 = head('COMO EXPERTA', 'Proyectos para ti', 'Proyectos donde piden tu especialidad, tus especies y tu zona.') + '''
    <div class="tabs"><span class="t-on" style="color: #4B3BA6; border-color: #4B3BA6;">Para ti 3</span><span>Todos</span><span>Mis candidaturas 1</span><span>Adjudicados</span></div>
%s
%s
%s
    <section class="card" style="flex-direction: row; align-items: center; gap: 12px; padding: 12px 16px; background: %s; border-color: #E3DDF6;"><span style="color: %s; display: flex;">%s</span><span style="flex: 1; font-size: 12.5px;"><strong style="font-weight: 600;">Ayuda a comparar:</strong> los ganaderos pueden pedirte que revises las propuestas que reciben. Actívalo en «Mis servicios».</span><a href="#" style="font-size: 12.5px; color: %s;">Activar</a></section>''' % (
    opp(94, 'Plan de bioseguridad para 3 naves', 'Granja de broilers en Lleida', 'Servicio › Consultoría veterinaria', 'A consultar', '2 meses', ['Veterinaria · avicultura', 'Lleida a 40 km de ti', 'Bioseguridad en tu perfil'], '1 de 5 candidaturas', 'Enviar candidatura', LI, LS, '🧪'),
    opp(87, 'Revisar 4 propuestas de alimentación', 'Granja de broilers en Lleida', 'Servicio › Consultoría', '300 – 500 €', '2 semanas', ['Avicultura › Broilers', 'Revisión de propuestas activada'], '0 candidaturas', 'Enviar candidatura', LI, LS, '🐔'),
    opp(72, 'Formación en bienestar animal para el equipo', 'Integradora en Huesca', 'Servicio › Formación técnica', '1.200 €', '1 mes', ['Formación en tus servicios', 'A distancia'], '2 de 5 candidaturas', 'Enviar candidatura', LI, LS, '🎓'),
    LS, LI, ic(I['spark'], 18), LI)
write('ProyExperto', shell('Proyectos · Proyectos para ti (experta)', 'experto', p7, 'Para ti'))
print('ok')
