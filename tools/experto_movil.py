"""Intranet de experta en móvil (versión de los Exp* de 004a_LP_Intranet · Experto), en lila. Escribe dos tiras; movil_canvas.py las pone en «004a_MB_Intranet · Experto».
No repite lo que ya hay en móvil: Oportunidades es MB_ProyE2_Experto (001b_MB) y Mis servicios es MB_MS7–MS10 (MB_05).
Plan Experto Gratis según data/planes.json: consultas sin límite, 1 servicio, ve proyectos abiertos pero la candidatura es de Pro.
Uso: python3 tools/experto_movil.py <canvas.json>"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, svg, I, hdr, backbar, tabbar, av, W, DEST, LI
from usuario_movil import tira, CH

I.update({'clip': 'M21 11.5 12.5 20a5 5 0 0 1-7-7L14 4.5a3.5 3.5 0 0 1 5 5L10.5 18a2 2 0 0 1-3-3L15 7.5', 'video': 'M3 6h12v12H3zM15 10l6-3v10l-6-3', 'eur': 'M17 6a7 7 0 1 0 0 12M4 10h9M4 14h9',
          'doc': 'M6 3h9l4 4v14H6zM14 3v5h5', 'ok': 'M5 12l5 5 9-10', 'eye': 'M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z'})
SOFT, PROC = '#F1EEFB', 'background:#FFF4E0;color:#7A4B00'

def pagina(cuerpo, back=None, foot=''):
    top = backbar(*back) if back else hdr('Experta', LI)
    return SB + top + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + cuerpo + '</div>' + foot + tabbar('Tú', LI, avatar='LG')

def card(t, cuerpo, link=None, extra=''):
    hd = ('<div style="display:flex;align-items:baseline;gap:8px"><strong style="flex:1;font-size:15px">' + t + '</strong>' + extra + ('<span style="font-size:12.5px;color:' + LI + ';font-weight:600">' + link + '</span>' if link else '') + '</div>') if t else ''
    return '<div class="card">' + hd + cuerpo + '</div>'

def st(t, estilo='background:#EEF6EE;color:#0E5A3A'):
    return '<span class="st" style="' + estilo + '">' + t + '</span>'

def btn(t, prim=False, full=False):
    return '<span class="' + ('btnp' if prim else 'btn') + '" style="' + ('background:' + LI + ';' if prim else 'border-color:' + LI + ';color:' + LI + ';') + ('flex:1;' if full else '') + '">' + t + '</span>'

def fila(izq, t, d, der='', borde=True):
    return ('<div style="display:flex;gap:10px;align-items:center;padding:9px 0;' + ('border-top:1px solid #EEF1EE' if borde else '') + '">' + izq +
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:1px"><strong style="font-size:13.5px;font-weight:600">' + t + '</strong><span class="hint">' + d + '</span></span>' + der + '</div>')

def nota(t):
    return '<div style="padding:10px 12px;border-radius:12px;background:#FAF8FE;border:1px solid #E7E1F7;font-size:12.5px;color:#33424C;display:flex;gap:8px">' + svg(I['info'], 16) + '<span>' + t + '</span></div>'

def kpi(n, t):
    return '<div class="card" style="gap:0;padding:10px 12px"><span style="font-size:20px;font-weight:700">' + n + '</span><span class="hint">' + t + '</span></div>'

def chips(lista):
    return '<div style="display:flex;gap:6px;overflow:hidden">' + ''.join('<span class="chip" style="%s">%s</span>' % ('background:%s;border-color:%s;color:#FFFFFF' % (LI, LI) if i == 0 else '', t) for i, t in enumerate(lista)) + '</div>'

# ---------- E1 · Panel ----------
def panel():
    b = ('<div style="display:flex;align-items:flex-end;gap:10px"><span style="flex:1"><span class="hint">Como experta › Panel</span><h1 style="margin:0;font-size:22px;font-weight:700">Hola, Laura</h1></span>' + btn(svg(I['eye'], 16) + '&nbsp;Mi perfil') + '</div>'
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">' + kpi('1.240', 'Apariciones en búsquedas') + kpi('128', 'Visitas al perfil') + kpi('3', 'Consultas · sin límite') + kpi('Pro', 'Candidaturas a proyectos') + '</div>' +
         card('Consultas recibidas', fila(av('GA', LI, 34, '50%'), 'Ganadero · Huesca', 'Auditoría nutricional · «el índice de conversión ha empeorado…»', st('Nueva', 'background:#E5484D;color:#FFFFFF'), False) +
              fila(av('IH', '#7A6CC4', 34, '50%'), 'Integradora · Huesca', 'Formación en bienestar · respondida ayer', st('Respondida', 'background:#F2F5F3;color:#4A5650')) + btn('Responder', True), 'Ver todas') +
         card('Oportunidades para ti', fila(st('94 %', 'background:' + SOFT + ';color:' + LI), 'Plan de bioseguridad para 3 naves', 'Broilers · Lleida · cierra en 6 días', CH, False) +
              fila(st('87 %', 'background:' + SOFT + ';color:' + LI), 'Revisar 4 propuestas de alimentación', 'Broilers · Lleida · 300–500 €', CH) + '<span class="hint">Las ves todas; para enviar candidatura, Experto Pro.</span>', 'Ver todas') +
         card('Tus servicios', fila('', 'Auditoría nutricional de lotes', 'Publicado · 42 visitas', st('Publicado'), False) + fila('', 'Revisión de propuestas', 'Borrador · tu 2.º servicio', st('Necesita Pro', PROC)), 'Gestionar') +
         card('Completa tu perfil', '<span style="height:6px;border-radius:3px;background:#E3E8E4;overflow:hidden"><span style="display:block;width:60%;height:100%;background:' + LI + '"></span></span>'
              '<span style="font-size:13px">○ Añade una foto</span><span style="font-size:13px">○ Añade un caso de éxito</span>', extra='<span class="hint">3 de 5</span>') +
         '<div class="card" style="border-top:3px solid ' + LI + '"><span style="display:flex;justify-content:space-between"><strong style="font-size:15px">Experta Gratis</strong>' + st('Plan', 'background:' + SOFT + ';color:' + LI) + '</span>'
         '<span style="font-size:12.5px;color:#4A5650">Consultas sin límite y 1 servicio publicado. Con Experto Pro (19,90 €/mes): candidaturas a proyectos y servicios sin límite.</span><span style="font-size:12.5px;color:' + LI + ';font-weight:600">Ver Experto Pro</span></div>')
    return pagina(b)

# ---------- E3 · Consultas ----------
def hilo(ini, t, sobre, txt, cuando, n=0, on=False):
    return ('<div style="display:flex;gap:10px;padding:12px;border-radius:12px;' + ('background:' + SOFT if on else 'background:#FFFFFF;border:1px solid #E6EBE7') + '">' + av(ini, LI if on else '#7A6CC4', 40, '50%') +
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:1px"><span style="display:flex;justify-content:space-between"><strong style="font-size:13.5px">' + t + '</strong><span class="hint">' + cuando + '</span></span>'
            '<span class="hint" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + sobre + '</span><span style="font-size:12.5px;color:#33424C;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + txt + '</span></span>' +
            ('<span class="st" style="align-self:center;background:#E5484D;color:#FFFFFF">%d</span>' % n if n else '') + '</div>')

def consultas():
    b = ('<div><span class="hint">Como experta</span><h1 style="margin:0;font-size:22px;font-weight:700">Consultas recibidas</h1><span class="hint">Ganaderos y empresas que te escriben desde tu perfil o tus servicios.</span></div>' +
         chips(['Nuevas 1', 'En curso 1', 'Cerradas']) +
         hilo('GA', 'Ganadero · Huesca', 'Auditoría nutricional de lotes de broilers', 'Tengo dos naves y el índice de conversión…', '5 h', 1, True) +
         hilo('IH', 'Integradora · Huesca', 'Formación en bienestar animal', 'Perfecto, ¿nos pasas fechas?', 'Ayer') +
         hilo('GP', 'Granja El Pinar', 'Revisión de propuestas', 'Gracias, muy útil la comparativa.', '8 oct') +
         nota('Consultas sin límite en todos los planes. Con Experto Pro, además, estados y notas.') +
         nota('Las respuestas van siempre por Mensajes: teléfonos, emails, webs o redes no se envían.'))
    return pagina(b)

def burbuja(t, cuando, mio):
    return ('<div style="display:flex;justify-content:' + ('flex-end' if mio else 'flex-start') + '"><div style="max-width:84%;padding:10px 13px;border-radius:14px;font-size:13px;line-height:1.38;' +
            ('background:' + LI + ';color:#FFFFFF;border-bottom-right-radius:4px' if mio else 'background:#FFFFFF;border:1px solid #E3E8E4;border-bottom-left-radius:4px') + '">' + t +
            '<div class="hint" style="margin-top:4px;' + ('color:#DCD6F5' if mio else '') + '">' + cuando + '</div></div></div>')

def consulta():
    top = ('<div class="top" style="padding-left:6px"><span class="ib">' + svg(I['back'], 22, 2) + '</span>' + av('GA', LI, 34, '50%') +
           '<span style="flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2;margin-left:6px"><strong style="font-size:15px">Ganadero · Huesca</strong><span class="hint">Avicultura › Broilers · 2 naves · 40.000 aves</span></span><span class="ib">' + svg(I['dots']) + '</span></div>')
    b = ('<div style="margin:10px 12px 0;padding:9px 11px;border-radius:12px;background:#FAF8FE;border:1px solid #E7E1F7;font-size:12.5px"><strong>Servicio: Auditoría nutricional de lotes de broilers</strong><br><span class="hint">Desde 350 € · presencial o a distancia</span></div>'
         '<div style="padding:14px 12px;display:flex;flex-direction:column;gap:10px">' +
         burbuja('Hola, tengo dos naves de broilers y el índice de conversión ha empeorado en los dos últimos lotes (de 1,62 a 1,74). Cambiamos de pienso en agosto. ¿Podrías revisarlo?', 'Hoy · 07:58', False) +
         '<span class="hint" style="margin-top:4px">Respuestas rápidas</span><div style="display:flex;flex-wrap:wrap;gap:6px">' +
         ''.join('<span class="chip" style="border-color:' + LI + ';color:' + LI + '">' + svg(I[k], 15) + '&nbsp;' + t + '</span>' for k, t in [('video', 'Proponer videollamada'), ('eur', 'Enviar presupuesto'), ('doc', 'Pedir datos del lote')]) + '</div></div>')
    foot = ('<div style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 12px 30px;display:flex;gap:8px;align-items:center"><span class="ib" style="width:36px;color:#56615B">' + svg(I['clip'], 20) + '</span>'
            '<span style="flex:1;height:42px;border:1px solid #D5DED8;border-radius:21px;display:flex;align-items:center;padding:0 14px;color:#8A948F;font-size:13.5px">Responde a la consulta…</span>'
            '<span style="width:42px;height:42px;border-radius:50%;background:' + LI + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg(I['send'], 18) + '</span></div>')
    return SB + top + b + foot

# ---------- E5 · Perfil ----------
def perfil():
    item = lambda t, v, acc='Editar', borde=True: fila('', t, v, '<span style="font-size:12.5px;color:' + LI + ';font-weight:600">' + acc + '</span>', borde)
    b = ('<div style="display:flex;align-items:flex-end;gap:10px"><span style="flex:1"><span class="hint">Como experta</span><h1 style="margin:0;font-size:22px;font-weight:700">Perfil de experta</h1></span>' + btn(svg(I['eye'], 16) + '&nbsp;Ver como público') + '</div>' +
         card('Tu perfil público', '<span style="height:6px;border-radius:3px;background:#E3E8E4;overflow:hidden"><span style="display:block;width:60%;height:100%;background:' + LI + '"></span></span>' +
              item('Titular', 'Veterinaria · nutrición y bienestar en avicultura') + item('Especialidad y especies', 'Nutrición animal, bienestar · Broilers, Gallinas ponedoras') +
              item('Zonas', 'Aragón, Cataluña, Navarra · también a distancia') + item('Colegiación', 'Colegio de Veterinarios de Huesca · verificada') + item('Idiomas', 'Español, inglés'), extra='<span class="hint">3 de 5</span>') +
         card('Te falta', item('Foto de perfil', 'Los perfiles con foto reciben el doble de consultas', 'Añadir', False) + item('Caso de éxito', 'Un resultado con datos, sin nombres de clientes · 1 en Gratis', 'Añadir')) +
         nota('En tu perfil no se muestran teléfono, email, web ni redes: te escriben por Mensajes.'))
    return pagina(b)

def publico():
    tag = lambda t: '<span class="chip" style="height:28px;background:' + SOFT + ';border-color:' + SOFT + ';color:' + LI + '">' + t + '</span>'
    b = ('<div style="padding:8px 12px;border-radius:10px;background:' + SOFT + ';color:' + LI + ';font-size:12.5px;font-weight:600;text-align:center">Así te ven ganaderos y empresas</div>'
         '<div class="card" style="align-items:center;text-align:center;gap:6px;padding:18px 14px">' + av('LG', LI, 72, '50%') + '<strong style="font-size:18px">Laura Gil</strong>'
         '<span class="st" style="background:#EEF6EE;color:#0E5A3A">✓ Colegiada</span><span style="font-size:13px">Veterinaria · nutrición y bienestar en avicultura</span><span class="hint">Huesca · Aragón, Cataluña, Navarra · a distancia</span>'
         '<div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center;margin-top:4px">' + tag('Broilers') + tag('Ponedoras') + tag('Bienestar animal') + tag('Conversión alimenticia') + '</div></div>' +
         card('Servicios', fila('', 'Auditoría nutricional de lotes', 'Desde 350 € · presencial o a distancia', CH, False)) +
         card('Casos de éxito', '<span class="hint">Todavía no hay casos publicados.</span>'))
    foot = '<div class="foot" style="bottom:84px;padding-bottom:10px"><span class="btnp" style="flex:1;background:' + LI + '">Enviar consulta</span></div>'
    return pagina(b, ('Laura Gil', 'Vista pública'), foot)

PANT = [('MB_ExpPanel', 'Móvil · Panel de experta', 1400, panel), ('MB_ExpConsultas', 'Móvil · Consultas recibidas', 844, consultas), ('MB_ExpConsulta', 'Móvil · Una consulta', 844, consulta),
        ('MB_ExpPerfil', 'Móvil · Perfil de experta', 990, perfil), ('MB_ExpPublico', 'Móvil · Vista pública', 844, publico)]
TIRAS = [('MB_ExpTiraPanel', 'Panel y consultas', ['MB_ExpPanel', 'MB_ExpConsultas', 'MB_ExpConsulta']),
         ('MB_ExpTiraPerfil', 'Perfil de experta', ['MB_ExpPerfil', 'MB_ExpPublico'])]
if __name__ == '__main__':
    alto = dict(a.split('=') for a in sys.argv[2:] if '=' in a)
    PANT = [(k, t, int(alto.get(k, h)), f) for k, t, h, f in PANT]
    for k, t, keys in TIRAS:
        html = tira(t, keys, PANT)
        open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
    print('ok', len(TIRAS))
