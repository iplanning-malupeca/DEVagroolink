"""Panel de empresa en móvil (versión de EM1 · IntS3Empresa). Escribe MB_EmpPanel; movil_canvas.py lo pone en «004b_MB_Intranet · Empresa».
Uso: python3 tools/empresa_panel_movil.py <canvas.json>"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, svg, I, wrap, tabbar, hdr, W, DEST, AZ, EMP_TABS
def lead(ini, t, d, cuando, prim):
    return ('<div style="display:flex;gap:10px;align-items:flex-start;padding:10px 0;border-top:1px solid #EEF1EE"><span style="width:36px;height:36px;border-radius:50%;background:#E9F0F9;color:' + AZ + ';font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none">' + ini + '</span>'
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:2px"><strong style="font-size:13.5px">' + t + '</strong><span class="hint">' + d + ' · ' + cuando + '</span>'
            '<span class="' + ('btnp' if prim else 'btn') + '" style="height:34px;align-self:flex-start;margin-top:4px;' + ('background:' + AZ if prim else 'border:1px solid ' + AZ + ';color:' + AZ) + '">Responder</span></span></div>')
def kpi(n, sub, t, link):
    return ('<div class="card" style="gap:2px;padding:12px"><span style="font-size:22px;font-weight:700">' + n + ' <span style="font-size:13px;font-weight:400;color:#56615B">' + sub + '</span></span><span class="hint" style="font-size:12.5px;color:#4A5650">' + t + '</span><span style="font-size:12.5px;color:' + AZ + ';font-weight:600;margin-top:4px">' + link + '</span></div>')
def panel():
    h = ('<div style="display:flex;align-items:center;gap:12px"><span style="width:46px;height:46px;border-radius:12px;background:' + AZ + ';color:#FFFFFF;font-weight:700;display:flex;align-items:center;justify-content:center">AE</span><span style="display:flex;flex-direction:column"><span class="hint">AgroExport SRL › Panel · Plan Gratis</span><h1 style="margin:0;font-size:22px;font-weight:700">Hola, Carla</h1></span></div>'
         '<div style="display:flex;gap:8px"><span class="btnp" style="flex:1;height:44px;background:' + AZ + '">' + svg(I['mas'], 16, 2.2) + 'Publicar producto</span><span class="btn" style="flex:1;height:44px;border:1px solid ' + AZ + ';color:' + AZ + '">Editar ficha</span></div>'
         '<div class="card" style="gap:2px"><div style="display:flex;align-items:baseline"><strong style="flex:1;font-size:15px">4 consultas sin responder</strong><span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Ver todas</span></div>'
         '<span class="hint" style="margin-bottom:4px">Plan Gratis: ves las consultas de 3 compradores; las siguientes se guardan y las ves con Pro.</span>' +
         lead('GA', 'Ganadero · Lleida · Avicultura', 'Pide precio de un corrector para broilers', 'hace 3 días', True) +
         lead('TE', 'Técnico de explotación · Segovia · Porcino', 'Pregunta por distribuidores en Castilla y León', 'hace 5 días', False) + '</div>'
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + kpi('1', 'de 15', 'Productos publicados', 'Añadir productos') + kpi('[n]', '', 'Visitas al perfil esta semana', 'Ver estadísticas') + '</div>' +
         kpi('1', '· sin límite', 'Miembros del equipo', 'Invitar a un compañero'))
    return SB + hdr('Empresa', AZ) + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + h + '</div>' + tabbar('Panel', AZ, EMP_TABS, 'AE')
if __name__ == '__main__':
    html = wrap('Móvil · Panel de empresa', 920, panel())
    open(DEST + 'MB_EmpPanel.dc.html', 'w').write(html); open(W + '/project/MB_EmpPanel.dc.html', 'w').write(html)
    print('ok')
