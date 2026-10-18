"""Quita la página «Alta solo para mí» (18/10/2026): M1/M2/M5 solo importaban L4, L5 y AltaConsulta;
M3, M4 y M6 ya están en 004 (T3, C1/C3) y en 002 (U1). La primera consulta pasa a 001 como paso 8."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/canvas.json'; c = json.load(open(P)); B = c['boards']
quitar = [k for k, b in B.items() if b.get('page') == 'solo' and k != 'AltaConsulta.dc.html']
for k in quitar: del B[k]
c['order'] = [k for k in c['order'] if k not in quitar]
B['AltaConsulta.dc.html'].update(page='alta', x=2720, y=2620, title='8 · «Más tarde» → primera consulta (los datos se piden solo esta vez)')
c['notes'] = {k: n for k, n in c['notes'].items() if n.get('page') != 'solo'}
c['pages'] = [p for p in c['pages'] if p['id'] != 'solo']
n = c['notes']['altaTitulo2']
n['text'] = '7 · Solo para mí → Mi espacio · 8 · «Más tarde» → primera consulta. «Represento una empresa» sigue en 006–010 (según cómo vende la empresa); experto, en su página'
n['maxW'] = max(n.get('maxW', 4000), 4080)
json.dump(c, open(P, 'w'), ensure_ascii=False, indent=1)
print(' '.join(sorted(quitar)))
