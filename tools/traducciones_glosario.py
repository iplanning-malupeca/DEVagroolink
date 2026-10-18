"""Tablero del superadmin: glosario del sector, términos que no se traducen y fichas con traducciones sin revisar (19/10/2026)."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = json.load(open(W + '/data/producto.json'))['traduccion']
L = ['es', 'en', 'pt', 'fr']
filas = ''.join('<div style="display: grid; grid-template-columns: repeat(4, minmax(0,1fr)) 60px; gap: 12px; padding: 9px 14px; border-top: 1px solid #EEF1EE; font-size: 13.5px;">' + ''.join('<span>' + g[l] + '</span>' for l in L) + '<span style="color: #1D4E89; font-size: 12.5px;">Editar</span></div>' for g in T['glosario'])
nt = ''.join('<span style="display: inline-flex; align-items: center; height: 30px; padding: 0 12px; border-radius: 999px; background: #F2F5F3; font-size: 13px;">' + x + '</span>' for x in T['no_traducir'])
pend = [('Vacuna aviar (ejemplo)', 'Hipra Ibérica', 'Vacuna', 'EN · PT · FR', '6 sensibles sin revisar', '#FFF4E0', '#7A4B00'),
        ('Pienso de puesta (ejemplo)', 'NutriAves', 'Alimentos', 'PT', '1 desactualizada', '#FFF4E0', '#7A4B00'),
        ('Mycofix® Plus', 'DSM-Firmenich', 'Nutrición', 'EN · FR', '12 automáticas', '#F1F3F6', '#4A5560')]
pf = ''.join(f'<div style="display: grid; grid-template-columns: 1.4fr 1fr 0.8fr 0.8fr 1.1fr 70px; gap: 12px; align-items: center; padding: 10px 14px; border-top: 1px solid #EEF1EE; font-size: 13.5px;"><strong style="font-weight: 600;">{a}</strong><span>{b}</span><span>{c}</span><span>{d}</span><span style="justify-self: start; font-size: 11.5px; font-weight: 600; padding: 3px 9px; border-radius: 999px; background: {f}; color: {g};">{e}</span><span style="color: #1D4E89; font-size: 12.5px;">Ver</span></div>' for a, b, c, d, e, f, g in pend)
reglas = ''.join('<li>' + r + '</li>' for r in T['reglas'])
html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Superadmin · Traducciones</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>body{{margin:0;line-height:1.35;font-family:'Poppins',sans-serif;color:#17231D}}</style>
</helmet>
<div style="width: 1280px; height: 1180px; background: #F6F8F6; display: flex; flex-direction: column; overflow: hidden;">
  <div style="height: 60px; background: #17231D; color: #FFFFFF; display: flex; align-items: center; gap: 14px; padding: 0 28px;"><span style="background: #FFFFFF; border-radius: 8px; padding: 4px 8px; display: flex;"><img src="/_blob/efc8ad652a1438d78ae82dbb2369ee52" alt="Agroolink" style="height: 22px;"></span><strong style="font-size: 15px; font-weight: 600;">Superadmin</strong><span style="font-size: 13px; opacity: .7;">Contenido › Traducciones</span></div>
  <div style="padding: 24px 28px; display: flex; flex-direction: column; gap: 18px;">
    <div><h1 style="margin: 0; font-size: 26px; font-weight: 700;">Traducciones</h1><p style="margin: 4px 0 0; font-size: 14px; color: #4A5650; max-width: 980px;">La IA traduce el texto libre de los usuarios a español, inglés, portugués y francés con este glosario. Las categorías, especies, enfermedades y opciones ya están traducidas en el modelo y no pasan por la IA.</p></div>
    <div style="display: grid; grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); gap: 18px;">
      <section style="background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; overflow: hidden;">
        <div style="display: flex; align-items: center; gap: 10px; padding: 14px;"><strong style="flex: 1; font-size: 16px;">Glosario del sector</strong><span style="height: 36px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; padding: 0 12px; font-size: 13px; color: #8A948F; width: 220px;">Buscar término</span><span style="height: 36px; padding: 0 14px; border-radius: 10px; background: #17231D; color: #FFFFFF; display: flex; align-items: center; font-size: 13px; font-weight: 600;">+ Añadir término</span></div>
        <div style="display: grid; grid-template-columns: repeat(4, minmax(0,1fr)) 60px; gap: 12px; padding: 8px 14px; background: #F6F8F6; font-size: 11px; font-weight: 600; color: #56615B; letter-spacing: .04em;"><span>ESPAÑOL</span><span>INGLÉS</span><span>PORTUGUÉS</span><span>FRANCÉS</span><span></span></div>
        {filas}
        <div style="padding: 10px 14px; border-top: 1px solid #EEF1EE; font-size: 12.5px; color: #56615B;">La IA usa siempre estas equivalencias. Un cambio aquí se aplica a las traducciones automáticas nuevas; las editadas a mano no se tocan.</div>
      </section>
      <section style="background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; padding: 14px; display: flex; flex-direction: column; gap: 10px;">
        <strong style="font-size: 16px;">No se traducen</strong>
        <div style="display: flex; flex-wrap: wrap; gap: 6px;">{nt}</div>
        <span style="font-size: 12.5px; color: #56615B;">Además, cualquier palabra marcada como marca registrada (®, ™) se deja tal cual.</span>
        <span style="height: 36px; align-self: flex-start; padding: 0 14px; border-radius: 10px; border: 1px solid #D5DED8; display: flex; align-items: center; font-size: 13px;">+ Añadir a la lista</span>
      </section>
    </div>
    <section style="background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; overflow: hidden;">
      <div style="display: flex; align-items: center; gap: 10px; padding: 14px;"><strong style="flex: 1; font-size: 16px;">Fichas con traducciones sin revisar</strong><span style="font-size: 13px; color: #56615B;">Primero las de fármacos, vacunas y biocidas</span></div>
      <div style="display: grid; grid-template-columns: 1.4fr 1fr 0.8fr 0.8fr 1.1fr 70px; gap: 12px; padding: 8px 14px; background: #F6F8F6; font-size: 11px; font-weight: 600; color: #56615B; letter-spacing: .04em;"><span>FICHA</span><span>EMPRESA</span><span>FAMILIA</span><span>IDIOMAS</span><span>PENDIENTE</span><span></span></div>
      {pf}
    </section>
    <section style="background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; padding: 14px 18px;"><strong style="font-size: 16px;">Reglas</strong><ul style="margin: 8px 0 0; padding-left: 18px; font-size: 13.5px; color: #33424C; display: flex; flex-direction: column; gap: 4px;">{reglas}</ul></section>
  </div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1280,"height":1180}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
open(W + '/project/ProdTradGlosario.dc.html', 'w').write(html); print('ok')
