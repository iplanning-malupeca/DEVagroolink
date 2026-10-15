"""Intereses = especies + categorías principales + objetivos/tendencias.
Genera LoginIntereses (alta) y SelIntereses (componente), y aplica el cambio en Mi espacio, L3 y ficha de producto."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
TEND = json.load(open(W + '/tools/intereses.json'))['tendencias']
ESP = ['Avicultura', 'Porcino', 'Bovino', 'Ovino', 'Caprino', 'Acuicultura', 'Cunicultura']
CAT = ['Nutrición y aditivos', 'Materias primas', 'Salud y bioseguridad', 'Genética y reproducción', 'Equipamiento e instalaciones',
       'Equipamiento avícola', 'Equipamiento porcino', 'Equipamiento rumiantes', 'Sostenibilidad y energía', 'Tecnología y software']
ON = {'Avicultura', 'Porcino', 'Nutrición y aditivos', 'Equipamiento avícola', 'Bienestar animal', 'Conversión alimenticia',
      'Huevo campero', 'Reducción de costes', 'Sostenibilidad'}
CHK = '<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>'

def chips(lst, cls='ch'):
    return ''.join('<button type="button" class="%s%s" aria-pressed="%s">%s%s</button>' % (cls, ' on' if x in ON else '', 'true' if x in ON else 'false', CHK if x in ON else '', x) for x in lst)

TAIL = """</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":%d,"height":%d}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
"""

# ---------- Alta · paso 4 · Tus intereses ----------
t = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Login · Tus intereses</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;font-family:'Plus Jakarta Sans',sans-serif;color:#0F2A1F}
a{color:#0B4A35;text-decoration:none;font-weight:600}a:hover{text-decoration:underline}
.ch{display:inline-flex;align-items:center;gap:5px;height:30px;padding:0 11px;border:1px solid #DDE3E7;border-radius:999px;background:#FFFFFF;font:600 12px 'Plus Jakarta Sans',sans-serif;color:#0F2A1F;cursor:pointer;white-space:nowrap}
.ch.on{background:#0B4A35;border-color:#0B4A35;color:#FFFFFF}
.lg{display:flex;align-items:baseline;gap:8px;margin:0 0 7px;font-size:13.5px;font-weight:700}
.lg span{font-size:11.5px;font-weight:500;color:#55636E}
.wr{display:flex;flex-wrap:wrap;gap:6px}
</style>
</helmet>
<div style="width: 960px; height: 760px; background: #E6EAF0; display: flex; align-items: center; justify-content: center;">
  <form role="dialog" aria-modal="true" aria-labelledby="ti" style="width: 660px; box-sizing: border-box; background: #FFFFFF; border-radius: 16px; box-shadow: 0 20px 50px rgba(15, 30, 40, 0.16); padding: 22px 28px; display: flex; flex-direction: column; gap: 15px;">
    <div style="display: flex; align-items: center; justify-content: space-between;">
      <img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height: 24px; width: auto; display: block;">
      <span style="font-size: 11.5px; font-weight: 600; color: #0B4A35; background: #E8F2EC; border-radius: 999px; padding: 4px 10px;">Solo la primera vez</span>
    </div>
    <div style="display: flex; flex-direction: column; gap: 4px;">
      <h1 id="ti" style="margin: 0; font-size: 20px; font-weight: 700;">¿Qué te interesa, Samuel?</h1>
      <p style="margin: 0; font-size: 13px; color: #55636E; line-height: 1.5;">Lo usamos para recomendarte productos, contenidos y proyectos. Puedes cambiarlo cuando quieras en tu perfil.</p>
    </div>
    <fieldset style="border: 0; padding: 0; margin: 0;"><legend class="lg">Especies <span>Incluye todas sus producciones</span></legend><div class="wr">%s</div></fieldset>
    <fieldset style="border: 0; padding: 0; margin: 0;"><legend class="lg">Categorías principales <span>Qué tipo de soluciones buscas</span></legend><div class="wr">%s</div></fieldset>
    <fieldset style="border: 0; padding: 0; margin: 0;"><legend class="lg">Objetivos y tendencias <span>Se actualiza con lo que se mueve en el sector</span></legend><div class="wr">%s</div></fieldset>
    <div style="display: flex; align-items: center; gap: 14px; border-top: 1px solid #EEF1F3; padding-top: 14px;">
      <a href="#" style="font-size: 13px;">Saltar por ahora</a>
      <span style="margin-left: auto; font-size: 12.5px; color: #55636E;">9 seleccionados</span>
      <button type="submit" style="height: 44px; padding: 0 26px; border-radius: 10px; background: #0B4A35; color: #FFFFFF; border: 0; font: 600 14px 'Plus Jakarta Sans', sans-serif; cursor: pointer;">Continuar</button>
    </div>
  </form>
</div>
""" % (chips(ESP), chips(CAT), chips(TEND))
open(P + 'LoginIntereses.dc.html', 'w').write(t + TAIL % (960, 760))

# ---------- Componente · Selector de intereses ----------
def lst(items):
    return '<ul>' + ''.join('<li>%s</li>' % i for i in items) + '</ul>'
t = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Componente · Selector de intereses</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>
body{margin:0;font-family:'Poppins',sans-serif;color:#17231D}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;min-width:0}
.h{margin:0;font-size:15.5px;font-weight:600}
.hint{font-size:12px;color:#56615B;line-height:1.45;margin:0}
.ch{display:inline-flex;align-items:center;gap:5px;height:30px;padding:0 11px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font:500 12px 'Poppins',sans-serif;color:#17231D;white-space:nowrap}
.ch.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}
.wr{display:flex;flex-wrap:wrap;gap:6px}
.eb{font-size:11px;font-weight:600;letter-spacing:.08em;color:#56615B}
ul{margin:0;padding-left:18px;display:flex;flex-direction:column;gap:5px;font-size:12px;color:#2F3D36;line-height:1.45}
</style>
</helmet>
<div style="width: 1280px; height: 900px; box-sizing: border-box; background: #F6F8F6; padding: 26px 36px; display: flex; flex-direction: column; gap: 16px; overflow: hidden;">
  <div><span class="eb">COMPONENTE COMÚN</span><h1 style="margin: 4px 0 0; font-size: 28px; font-weight: 700;">Selector de intereses</h1><p style="margin: 4px 0 0; font-size: 13.5px; color: #4A5650; max-width: 980px;">El interés de una persona no es solo la especie: también las categorías principales y los objetivos o tendencias que persigue. Se eligen una vez al entrar por primera vez y se editan desde el perfil. Las tres listas se cruzan con productos, contenidos, expertos y proyectos.</p></div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1.25fr; gap: 16px; align-items: start;">
    <section class="card"><span class="eb">1 · ESPECIES</span><p class="h">Las 7 del árbol común</p><p class="hint">Mismo árbol que el selector de especies. Aquí basta con la especie: incluye todas sus producciones.</p><div class="wr">%s</div></section>
    <section class="card"><span class="eb">2 · CATEGORÍAS PRINCIPALES</span><p class="h">Las 10 familias de producto</p><p class="hint">Las mismas familias del modelo de producto y del menú de categorías.</p><div class="wr">%s</div></section>
    <section class="card"><span class="eb">3 · OBJETIVOS Y TENDENCIAS</span><p class="h">Lista viva, editable por Agroolink</p><p class="hint">Se añaden, reordenan o retiran según las tendencias. Retirar no borra: deja de ofrecerse y se conserva donde ya se usa.</p><div class="wr">%s</div></section>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; align-items: start;">
    <section class="card"><p class="h">Dónde se elige</p>%s</section>
    <section class="card"><p class="h">Dónde se usa</p>%s</section>
    <section class="card"><p class="h">Reglas</p>%s</section>
  </div>
</div>
""" % (chips(ESP), chips(CAT), chips(TEND),
       lst(['Alta · paso 4 «¿Qué te interesa?» (solo la primera vez, se puede saltar)', 'Móvil · pantalla «Tus intereses»',
            'Perfil › Mis intereses (web) y Menú › Mis intereses (móvil)', 'Mi espacio · tarjeta «Tus intereses» con Editar']),
       lst(['Recomendaciones «Para ti» en Mi espacio y home', 'Buscador: bloque «Tendencias del sector» y filtro por objetivo',
            'Ficha de producto: «Objetivos principales» se eligen de esta lista (más objetivos propios)', 'Proyectos: el encaje suma objetivos además de especie, categoría y zona',
            'Contenidos y alertas de Agrinews etiquetados con la misma lista']),
       lst(['Nada es obligatorio; sin intereses, usamos lo que la persona consulta', 'Sin límite de elección', 'Una lista por idioma, mismo identificador',
            'Producto: mínimo 1 objetivo de la lista para aparecer en recomendaciones por objetivo']))
open(P + 'SelIntereses.dc.html', 'w').write(t + TAIL % (1280, 900))

# ---------- Mi espacio: tarjeta Tus intereses ----------
f = P + 'Alta4MiEspacio.dc.html'; s = open(f).read()
a = s[s.index('          <section class="card" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 10px;">'):]
a = a[:a.index('</section>') + len('</section>')]
def mini(lst):
    return ''.join('<span style="height: 26px; padding: 0 10px; border-radius: 999px; background: #EEF6EE; color: #0E5A3A; font-size: 12px; font-weight: 500; display: inline-flex; align-items: center; white-space: nowrap;">%s</span>' % x for x in lst)
row = '<div style="display: flex; gap: 12px; align-items: center;"><span style="width: 92px; flex: none; font-size: 12px; color: #56615B;">%s</span><div style="display: flex; flex-wrap: wrap; gap: 6px;">%s</div></div>'
b = ('          <section class="card" style="padding: 16px 20px; display: flex; flex-direction: column; gap: 10px;">\n'
     '            <div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 style="margin: 0; font-size: 16px; font-weight: 600;">Tus intereses</h2><span style="font-size: 12px; color: #56615B;">Lo usamos para tus recomendaciones · <a href="#">Editar</a></span></div>\n'
     + row % ('Especies', mini(['Avicultura', 'Porcino'])) + '\n'
     + row % ('Categorías', mini(['Nutrición y aditivos', 'Equipamiento avícola'])) + '\n'
     + row % ('Objetivos', mini(['Bienestar animal', 'Conversión alimenticia', 'Huevo campero', 'Reducción de costes', 'Sostenibilidad'])) + '\n'
     '          </section>')
s = s.replace(a, b)
s = s.replace('Para ti · Avicultura</h2>', 'Para ti · Avicultura · Bienestar animal</h2>')
open(f, 'w').write(s)

# ---------- L3: texto del paso siguiente ----------
f = P + 'Login3Crear.dc.html'; s = open(f).read()
a = 'Después pasa a <strong>L4 · ¿Cómo quieres empezar?</strong> (solo la primera vez en Agroolink) y sigue con las opciones.'
assert a in s
s = s.replace(a, 'Después, solo la primera vez en Agroolink: <strong>4 · Tus intereses</strong> y <strong>5 · ¿Cómo quieres empezar?</strong>; luego sigue con las opciones.')
open(f, 'w').write(s)

# ---------- Ficha de producto: objetivos de la lista ----------
f = P + 'ProdFichaBeneficios.dc.html'; s = open(f).read()
X = ' <span aria-hidden="true" style="color: #6B8F7B;">×</span></span>'
a = ('<span>Objetivos principales</span><div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;"><span class="chip">Salud ósea' + X +
     '<span class="chip">Rendimiento' + X + '<span class="chip">Calidad de cáscara' + X + '<span class="chip">Bienestar' + X + '<a href="#" style="font-size: 12.5px;">+ Añadir</a></div>')
assert a in s
b = ('<span>Objetivos principales <span class="hint">· de la lista de tendencias, más los tuyos</span></span><div style="display: flex; gap: 6px; flex-wrap: wrap; align-items: center;"><span class="chip">Rendimiento' + X +
     '<span class="chip">Bienestar animal' + X + '<a href="#" style="font-size: 12.5px;">+ De la lista</a>'
     '<span class="chip" style="background: #FFFFFF; border-style: dashed;">Salud ósea' + X + '<span class="chip" style="background: #FFFFFF; border-style: dashed;">Calidad de cáscara' + X + '<a href="#" style="font-size: 12.5px;">+ Propio</a></div>')
s = s.replace(a, b)
P1 = '<span style="background: #EEF6EE; color: #0E5A3A; border-radius: 999px; padding: 3px 8px;">'
a = P1 + 'Salud ósea</span>' + P1 + 'Rendimiento</span>' + P1 + 'Calidad de cáscara</span>' + P1 + 'Bienestar</span>'
assert a in s
s = s.replace(a, P1 + 'Rendimiento</span>' + P1 + 'Bienestar animal</span>' + P1 + 'Salud ósea</span>' + P1 + 'Calidad de cáscara</span>')
open(f, 'w').write(s)

# ---------- índice ----------
c = json.load(open(P + 'canvas.json'))
B, N = c['boards'], c['notes']
B['LoginIntereses.dc.html'] = {'h': 760, 'page': 'alta', 'title': '4 · Tus intereses · especies, categorías y objetivos (solo la 1.ª vez)', 'w': 960, 'x': 2080, 'y': 0}
B['Login4Empezar.dc.html'].update(x=3120, title='5 · L4 · ¿Cómo quieres empezar? · solo la 1.ª vez en Agroolink')
B['Login5Creada.dc.html'].update(x=4160, title='6 · L5 · Cuenta lista (según elección)')
B['Login3Crear.dc.html']['title'] = '3b · L3 · Registro actual de Agrinews (no se diseña) → 4'
for k in ['Alta4MiEspacio.dc.html', 'AltaEmpresa.dc.html', 'AltaExperto.dc.html', 'AltaConsulta.dc.html']:
    B[k]['title'] = B[k]['title'].replace('6 · ', '7 · ', 1)
N['altaTitulo']['text'] = 'Alta · 1 email → ya registrado: 2a código → 4 intereses → 5 «¿Cómo quieres empezar?» → 6 (4 y 5 solo la 1.ª vez)'
N['altaL1b']['text'] = 'Sin cuenta: 2b → 3b registro de Agrinews → vuelve a 4'
N['altaTitulo2']['text'] = '7 · Adónde lleva cada opción de L4'
B['SelIntereses.dc.html'] = {'h': 900, 'page': 'componentes', 'title': 'Selector de intereses · especies, categorías y objetivos', 'w': 1280, 'x': 4080, 'y': 0}
N['selT1']['text'] = 'Componentes comunes · especies, mercados, rama de negocio, cargo e intereses'
N['selT1']['maxW'] = 5400
o = c['order']
for k, after in [('LoginIntereses.dc.html', 'Login1bCodigo.dc.html'), ('SelIntereses.dc.html', 'SelRamasCargos.dc.html')]:
    if k in o: o.remove(k)
    o.insert(o.index(after) + 1 if after in o else len(o), k)
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
