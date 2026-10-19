"""Intranet de experta en móvil (versión de E6–E9): consultas organizadas, mis candidaturas, estadísticas y plan, una pantalla por tablero, para «Agroolink · Móvil».
Va en la fila de experta de «004_MB_Intranet» detrás de MB_ExpPublico. Las imágenes se reescriben con tools/blobs_movil.json.
Uso: python3 tools/experto_intranet_movil.py <carpeta-movil>/project/canvas.json [clave=alto …]"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import svg, I, wrap, W, DEST, LI
from experto_movil import pagina, card, st, btn, fila, nota, chips

OK = 'background:#EEF6EE;color:#0E5A3A'; WN = 'background:#FFF4E0;color:#7A4B00'; GR = 'background:#F1F3F6;color:#4A5560'; LIST = 'background:#F1EEFB;color:#4B3BA6'
I.update({'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4'})
def pro(t):
    return '<div style="padding:10px 12px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:12.5px;color:#33424C;display:flex;gap:8px"><span style="flex:none">' + svg(I['lock'], 16) + '</span><span>' + t + '</span></div>'
def titulo(miga, t, sub=''):
    return '<div><span class="hint">Como experta › ' + miga + '</span><h1 style="margin:0;font-size:22px;font-weight:700">' + t + '</h1>' + ('<span style="font-size:13px;color:#4A5650">' + sub + '</span>' if sub else '') + '</div>'

def consultas():
    c = lambda quien, t, extra, estado, estilo, borde=True: fila('', t, quien + extra, st(estado, estilo), borde)
    b = (titulo('Consultas recibidas', 'Consultas organizadas', 'Estados, etiquetas y notas · así se ve con Pro') +
         pro('En Gratis recibes y respondes consultas <strong>sin límite</strong>. Estados y notas privadas, con <strong>Experto Pro · 19,90 €/mes</strong>.') +
         chips(['Todas 7', 'Nueva 1', 'En curso 2', 'Presupuesto 1', 'Cerrada 3']) +
         card('', c('Ganadero · Huesca · 5 h', 'Auditoría nutricional de broilers', ' · Broilers', 'Nueva', LIST, False) +
              c('Integradora · Huesca · ayer', 'Formación en bienestar animal', ' · Formación', 'En curso', WN) +
              c('Cooperativa · Teruel · 3 d', 'Plan de vacunación de ponedoras', ' · Nota: pedir histórico', 'En curso', WN) +
              c('Técnico · Lleida · 6 d', 'Revisión de la fórmula de arranque', ' · 350 €', 'Presupuesto', GR) +
              c('Granja El Pinar · 8 oct', 'Revisión de propuestas', '', 'Contratada', OK)) +
         card('Notas privadas · Auditoría nutricional', '<span style="font-size:13px;color:#33424C;line-height:1.4">Cambió de pienso en agosto. Pedir índices de los 3 últimos lotes antes de presupuestar.</span><span class="hint">Solo las ves tú.</span>'))
    return pagina(b)

def candidaturas():
    c = lambda t, quien, prop, est, estilo, borde=True: fila('', t, quien + ' · ' + prop, st(est, estilo), borde)
    b = (titulo('Oportunidades', 'Mis candidaturas', 'Tus propuestas a proyectos y su estado') +
         pro('En Gratis ves los proyectos abiertos; para presentarte necesitas <strong>Experto Pro</strong>. Así se ve con Pro.') +
         chips(['Todas 4', 'Enviadas 1', 'Preseleccionadas 1', 'Adjudicadas 1']) +
         card('', c('Reducir el índice de conversión · Nave 2', 'Ganadero · Lleida', '1.200 €', 'Enviada', LIST, False) +
              c('Plan de bioseguridad para 3 granjas', 'Integradora · Huesca', '2.400 €', 'Preseleccionada', WN) +
              c('Formación en bienestar animal', 'Cooperativa · Teruel', '900 €', 'Adjudicada', OK) +
              c('Raciones en ponedoras', 'Granja · Zaragoza', '600 €', 'No elegida', GR)) +
         card('Reducir el índice de conversión · Nave 2', fila('', '1.200 € · 6 semanas', '6 candidaturas · enviada hace 2 d', '', False) +
              '<div style="display:flex;gap:8px">' + btn('Editar', False, True) + btn('Retirar', False, True) + '</div>') +
         nota('Puedes editarla hasta que el ganadero elija. Si lleva un contacto (teléfono, email, web, @usuario), no se envía.'))
    return pagina(b)

def estadisticas():
    kpi = lambda n, t, d, estilo=OK: '<div class="card" style="gap:2px;padding:12px"><span style="font-size:22px;font-weight:700">' + n + '</span><span class="hint" style="font-size:12px;color:#4A5650">' + t + '</span><span style="margin-top:4px">' + st(d, estilo) + '</span></div>'
    sem = [18, 22, 20, 27, 31, 29, 36, 41]
    barras = ''.join('<span style="flex:1;display:flex;flex-direction:column;align-items:center;gap:4px"><span style="width:100%;height:' + str(int(v * 2.6)) + 'px;border-radius:5px 5px 0 0;background:' + (LI if i == len(sem) - 1 else '#CFC7EE') + '"></span><span style="font-size:10px;color:#56615B">S' + str(i + 35) + '</span></span>' for i, v in enumerate(sem))
    b = (titulo('Estadísticas', 'Estadísticas', 'Últimos 30 días · básicas en Gratis') +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + kpi('1.240', 'Apariciones en búsquedas', '+9 %') + kpi('224', 'Visitas al perfil', '+15 %') +
         kpi('6', 'Consultas', 'sin límite') + kpi('5 h', 'Respuesta media', 'compromiso 24 h') + '</div>' +
         card('Visitas por semana', '<div style="display:flex;gap:6px;align-items:flex-end;height:120px">' + barras + '</div>') +
         card('Tu servicio', fila('', 'Auditoría nutricional de broilers', '96 visitas · 4 consultas · 11 en tableros', '', False)) +
         pro('<strong>Quién te busca y con qué palabras</strong>, y salir como recomendada en búsquedas, con Experto Pro. Nunca nombres ni contactos.'))
    return pagina(b)

def plan():
    fil = [('Consultas', 'Ilimitadas', 'Ilimitadas'), ('Servicios', '1', 'Ilimitados'), ('Candidaturas', 'Solo ver', 'Ilimitadas'), ('Portfolio', '1', 'Ilimitado'),
           ('Estados y notas', '—', 'Sí'), ('Publicar contenido', '—', 'Sí'), ('Recomendada', '—', 'Sí'), ('Estadísticas', 'Básicas', 'Avanzadas'), ('Comprador Pro', '—', 'Incluido')]
    tabla = ('<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:6px;font-size:12px;align-items:center"><span></span><strong style="color:' + LI + '">Gratis</strong><strong>Pro</strong>' +
             ''.join('<span style="color:#4A5650;padding:6px 0;border-top:1px solid #EEF1EE">' + a + '</span><span style="padding:6px 0;border-top:1px solid #EEF1EE;font-weight:600">' + b + '</span><span style="padding:6px 0;border-top:1px solid #EEF1EE">' + c + '</span>' for a, b, c in fil) + '</div>')
    caja = lambda t, p, on=False: ('<div class="card" style="gap:4px;' + ('border:2px solid ' + LI + ';background:#F6F4FC' if on else '') + '"><span style="display:flex;justify-content:space-between"><strong style="font-size:15px">' + t + '</strong>' + (st('Tu plan', LIST) if on else '') + '</span>'
                                   '<span style="font-size:18px;font-weight:700">' + p + '</span>' + ('' if on else btn('Pasar a Pro', True)) + '</div>')
    b = (titulo('Plan y facturación', 'Plan y facturación') + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + caja('Experto Gratis', '0 €', True) + caja('Experto Pro', '19,90 €/mes') + '</div>' +
         card('Qué incluye cada plan', tabla) +
         card('Facturación', fila('', 'Se factura a', 'Laura Gil · tus datos de Mi cuenta', '', False) + '<span class="hint">Aún no hay facturas: estás en Experto Gratis.</span>') +
         nota('Sin permanencia: si cancelas, sigues con Pro hasta el final del periodo pagado.'))
    return pagina(b, ('Plan y facturación', 'Tú'))

PANT = [('MB_ExpConsultasOrg', 'E6 · Consultas organizadas (Pro)', consultas), ('MB_ExpCandidaturas', 'E7 · Mis candidaturas (Pro)', candidaturas),
        ('MB_ExpEstadisticas', 'E8 · Estadísticas de experta', estadisticas), ('MB_ExpPlan', 'E9 · Plan y facturación de experta', plan)]
ALTOS = {'MB_ExpConsultasOrg': 930, 'MB_ExpCandidaturas': 1000, 'MB_ExpEstadisticas': 930, 'MB_ExpPlan': 1030}   # medidas en el navegador
if __name__ == '__main__':
    alto = dict(ALTOS, **{k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    BLOBS = json.load(open(W + '/tools/blobs_movil.json'))
    c = json.load(open(sys.argv[1])); B = c['boards']
    ref = B['MB_ExpPublico.dc.html']; x0 = ref['x'] + 470
    nuevos = []
    for i, (k, t, f) in enumerate(PANT):
        h = int(alto.get(k, 1100))
        html = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '/_blob/' + BLOBS.get(m.group(1), m.group(1)), wrap('Móvil · ' + t, h, f()))
        open(DEST + k + '.dc.html', 'w').write(html)
        B[k + '.dc.html'] = {'w': 390, 'h': h, 'page': ref['page'], 'x': x0 + i * 470, 'y': ref['y'], 'title': t}
        if k + '.dc.html' not in c['order']: c['order'].append(k + '.dc.html')
        nuevos.append(k + '.dc.html')
    json.dump(c, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    print('ok', len(nuevos), ref['page'], ref['y'])
