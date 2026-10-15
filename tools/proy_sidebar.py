"""Proyectos (J1–J7): cabecera y menú lateral comunes (IntHeader + IntSidebar con desplegable)."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'
CFG = {
 'ProyCrear': ('personal', 'Mis proyectos', '', 900), 'ProyDestinatarios': ('personal', 'Mis proyectos', '', 900),
 'ProyMis': ('personal', 'Mis proyectos', 'Activos', 900), 'ProyDetalle': ('personal', 'Mis proyectos', 'Activos', 900),
 'ProyOportunidades': ('empresa', 'Oportunidades', 'Recomendadas', 1000), 'ProyPropuesta': ('empresa', 'Oportunidades', 'Recomendadas', 1000),
 'ProyExperto': ('experta', 'Oportunidades', 'Para ti', 1000)}
HDR = {'personal': ('Samuel E.', 'SE', '#0E5A3A', 'personal'), 'empresa': ('Laura García', 'LG', '#1F3A5F', 'empresa'), 'experta': ('Laura G.', 'LG', '#0E5A3A', 'experta')}
c = json.load(open(P + 'canvas.json'))
for f, (modo, act, sub, H) in CFG.items():
    p = P + f + '.dc.html'; s = open(p).read()
    if 'name="IntSidebar"' in s:
        continue
    s, n1 = re.subn(r'\n  <header style="height: 64px;.*?</header>', '', s, count=1, flags=re.S)
    s, n2 = re.subn(r'\n  <nav style="position: absolute; top: 64px;.*?</nav>', '', s, count=1, flags=re.S)
    assert n1 == 1 and n2 == 1, f
    per, ini, col, var = HDR[modo]
    alto = H - 68
    imp = ('\n  <div style="position: absolute; top: 68px; left: 0;"><dc-import name="IntSidebar" modo="%s" activo="%s" sub="%s"%s alto="%d" hint-size="256px,%dpx"></dc-import></div>'
           '\n  <div style="position: absolute; top: 0; left: 0; width: 1280px; z-index: 2;"><dc-import name="IntHeader" persona="%s" iniciales="%s" color="%s" variante="%s" hint-size="1280px,68px"></dc-import></div>') % (
        modo, act, sub, ' empresa="AgroNova"' if modo == 'empresa' else '', alto, alto, per, ini, col, var)
    s = s.replace('<main style="position: absolute; top: 64px; left: 240px;', '<main style="position: absolute; top: 68px; left: 256px;', 1)
    s = s.replace('</main>\n', '</main>' + imp + '\n', 1)
    s = s.replace('<div style="width: 1280px; height: 900px; position: relative;', '<div style="width: 1280px; height: %dpx; position: relative;' % H, 1)
    s = s.replace('"$preview":{"width":1280,"height":900}', '"$preview":{"width":1280,"height":%d}' % H)
    open(p, 'w').write(s)
    c['boards'][f + '.dc.html']['h'] = H
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
