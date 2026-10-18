"""001: repite la pantalla 5 (L4) con «Represento una empresa» elegida (5b) y su «Cuenta lista» (6b), que llevan a 006–010."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); PR = W + '/project/'
s = open(PR + 'Login4Empezar.dc.html').read()
s = s.replace('<title>Login · ¿Cómo quieres empezar?</title>', '<title>Login · ¿Cómo quieres empezar? · Empresa</title>')
s = s.replace('¿Cómo quieres empezar, Samuel?', '¿Cómo quieres empezar, Carla?')
on = ' style="border: 1.5px solid #0B4A35; background: #F2F7F4;"'
a, b = s.index('<label class="opt"' + on + '>'), s.index('<label class="opt">')
s = s.replace('<label class="opt"' + on + '>', '<label class="opt">', 1)
s = s.replace('<input type="radio" name="inicio" defaultChecked="{{ yes }}">', '<input type="radio" name="inicio">', 1)
i = s.index('<span class="tt">Represento una empresa</span>')
j = s.rindex('<label class="opt">', 0, i)
s = s[:j] + '<label class="opt"' + on + '>' + s[j + len('<label class="opt">'):]
s = s.replace('Gestionar el perfil de Granja Los Olmos, publicar productos y recibir consultas. Gratis.</span></span>\n        <input type="radio" name="inicio">',
              'Gestionar el perfil de tu empresa, publicar productos y recibir consultas. Gratis.</span><span style="font-size: 11.5px; color: #0B4A35; font-weight: 600; margin-top: 3px;">Sugerido por tu cargo: Comercial</span></span>\n        <input type="radio" name="inicio" defaultChecked="{{ yes }}">', 1)
assert s.count('defaultChecked') == 1 and 'Sugerido por tu cargo' in s
s = s.replace('<option selected>Granjero</option>', '<option>Granjero</option>').replace('<option>Comercial</option>', '<option selected>Comercial</option>', 1)
open(PR + 'Login4Empresa.dc.html', 'w').write(s)
open(PR + 'Login5Empresa.dc.html', 'w').write('''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Login · Cuenta creada · Empresa</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>body{margin:0;line-height:1.3}</style>
</helmet>
<div style="width: 960px; height: 760px;">
  <dc-import name="Login5Creada" variante="Represento una empresa" hint-size="960px,760px"></dc-import>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"$preview":{"width":960,"height":760}}'>
class Component extends DCLogic {
  renderVals() { return {}; }
}
</script>
</body>
</html>
''')
l5 = open(PR + 'Login5Creada.dc.html').read()
l5 = l5.replace("boxTitle: 'Siguiente: busca Granja Los Olmos',\n        boxText: 'Si ya está en Agroolink podrás reclamarla o unirte; si no, la creas en 2 minutos.',",
                "boxTitle: 'Siguiente: escribe el nombre de tu organización',\n        boxText: 'Si ya está en Agroolink te unes a ella; si no, la creas en 2 minutos.',")
open(PR + 'Login5Creada.dc.html', 'w').write(l5)
c = json.load(open(PR + 'canvas.json')); B = c['boards']
B['Login4Empresa.dc.html'] = {'w': 960, 'h': 760, 'page': 'alta', 'x': 3120, 'y': 1300, 'title': '5b · L4 · ¿Cómo quieres empezar? · «Represento una empresa» elegida'}
B['Login5Empresa.dc.html'] = {'w': 960, 'h': 760, 'page': 'alta', 'x': 4160, 'y': 1300, 'title': '6b · L5 · Cuenta lista → seguir con la empresa (006–010)'}
for k in ('Login4Empresa.dc.html', 'Login5Empresa.dc.html'):
    if k not in c['order']: c['order'].insert(c['order'].index('Login5Creada.dc.html') + 1 + (k == 'Login5Empresa.dc.html'), k)
n = dict(c['notes']['altaL1b']); n.update(x=3120, y=1000, text='Represento una empresa: 5b → 6b → sigue en 006–010, empezando por el nombre de tu organización')
c['notes']['altaEmpresa'] = n
json.dump(c, open(PR + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
