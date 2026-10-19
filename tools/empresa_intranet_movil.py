"""Intranet de empresa en móvil (versión de EM5–EM8): solicitudes, equipo, estadísticas y plan, una pantalla por tablero, para «Agroolink · Móvil».
Menú de empresa: Panel · Solicitudes · Productos · Empresa. Las imágenes se reescriben con tools/blobs_movil.json.
Uso: python3 tools/empresa_intranet_movil.py <carpeta-movil>/project/canvas.json [clave=alto …]"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import svg, I, wrap, W, DEST, AZ
from empresa_config_movil import card, st, btn, fila, nota, chips, pantalla, emp, AZST, WN, GR

OK = 'background:#EEF6EE;color:#0E5A3A'; ER = 'background:#FDECEA;color:#A3271B'
I.update({'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4'})
def pro(t):
    return '<div style="padding:10px 12px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:12.5px;color:#33424C;display:flex;gap:8px"><span style="flex:none">' + svg(I['lock'], 16) + '</span><span>' + t + '</span></div>'
def titulo(miga, t, sub=''):
    return '<div><span class="hint">AgroExport SRL › ' + miga + '</span><h1 style="margin:0;font-size:22px;font-weight:700">' + t + '</h1>' + ('<span style="font-size:13px;color:#4A5650">' + sub + '</span>' if sub else '') + '</div>'
def av(ini, bg='#E9F0F9', tinta=AZ):
    return '<span style="width:36px;height:36px;border-radius:50%;background:' + bg + ';color:' + tinta + ';font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none">' + ini + '</span>'

def solicitudes():
    sol = lambda ini, quien, pide, asig, est, estilo, cuando, borde=True: (
        '<div style="display:flex;gap:10px;align-items:flex-start;padding:11px 0;' + ('border-top:1px solid #EEF1EE' if borde else '') + '">' + av(ini) +
        '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:2px"><span style="display:flex;justify-content:space-between;gap:6px"><strong style="font-size:13.5px">' + quien + '</strong><span class="hint">' + cuando + '</span></span>'
        '<span style="font-size:12.5px;color:#33424C">' + pide + '</span><span class="hint">La atiende: ' + asig + '</span><span style="margin-top:3px">' + st(est, estilo) + '</span></span></div>')
    bloq = lambda zona: ('<div style="display:flex;gap:10px;align-items:center;padding:11px 0;border-top:1px solid #EEF1EE;color:#8A948F">' + av(svg(I['lock'], 15), '#F1F3F6', '#8A948F') +
                         '<span style="flex:1"><strong style="font-size:13.5px;color:#56615B">Comprador de ' + zona + '</strong><br><span class="hint">Guardada · se ve con Empresa Pro</span></span></div>')
    b = (titulo('Solicitudes', 'Solicitudes', 'Cada una abre un hilo en Mensajes.') + chips(['Nuevas 1', 'Sin respuesta +48 h 1', 'En conversación 1', 'Cerradas 24']) +
         card('', sol('GA', 'Ganadero · Lleida', 'Precio y plazo · Corrector CV-20', 'Agropecuària del Segre (distribuidor)', 'Nueva', AZST, '2 h', False) +
              sol('TE', 'Técnico · Segovia', 'Distribuidor en su zona · Premezcla P-40', 'Jorge Pérez', 'Sin respuesta 52 h', ER, '3 d') +
              sol('IN', 'Integradora · Huesca', 'Muestra para prueba · CV-20', 'Carla Martín', 'En conversación', OK, '5 d') + bloq('Zaragoza') + bloq('Murcia')) +
         pro('<strong>2 solicitudes guardadas.</strong> Plan Gratis: ves las de 3 compradores; con Empresa Pro, todas.') +
         nota('El comprador ve «AgroExport» y el nombre de pila de quien responde; nunca teléfonos ni emails.'))
    return pantalla(b, tab='Solicitudes', avatar='AE')

def equipo():
    m = lambda ini, n, cargo, rol, est, estilo, borde=True, bg='#E9F0F9', tinta=AZ: fila(av(ini, bg, tinta), n, cargo + ' · ' + rol, st(est, estilo), borde)
    rol = lambda t, d, borde=True: fila('', t, d, '', borde)
    b = (titulo('Equipo', 'Equipo', 'Miembros sin límite en todos los planes.') +
         card('4 personas', m('CM', 'Carla Martín (tú)', 'Directora comercial', 'Administradora', 'Activa', OK, False, AZ, '#FFFFFF') + m('JP', 'Jorge Pérez', 'Comercial', 'Castilla y León', 'Activo', OK) +
              m('AS', 'Ana Soler', 'Técnica', 'Lectura', 'Activa', OK) + m('MV', 'Marc Vidal', 'Comercial', 'Cataluña', 'Invitado', WN, True, '#F1F3F6', '#4A5560')) +
         '<div style="display:flex;gap:8px"><span style="flex:1;height:44px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;padding:0 12px;font-size:13px;color:#8A948F">Nombre o email de trabajo</span>' + btn(svg(I['mas'], 16, 2.2) + '&nbsp;Invitar', True) + '</div>' +
         card('Qué puede hacer cada rol', rol('Administrador', 'Ficha, productos, equipo y plan; todas las solicitudes', False) + rol('Comercial', 'Responde las solicitudes de su zona o las asignadas') + rol('Lectura', 'Lo ve todo; responde solo si se lo asignan')) +
         nota('Cada alta avisa a las administradoras (copia al superadmin). Los compradores nunca ven el email ni el teléfono de tu equipo.'))
    return pantalla(b, ('Equipo', 'Empresa'), tab='Empresa', avatar='AE')

def estadisticas():
    kpi = lambda n, t, d, estilo=OK: '<div class="card" style="gap:2px;padding:12px"><span style="font-size:22px;font-weight:700">' + n + '</span><span class="hint" style="font-size:12px;color:#4A5650">' + t + '</span><span style="margin-top:4px">' + st(d, estilo) + '</span></div>'
    sem = [42, 55, 48, 61, 70, 66, 82, 95]
    barras = ''.join('<span style="flex:1;display:flex;flex-direction:column;align-items:center;gap:4px"><span style="width:100%;height:' + str(int(v * 1.1)) + 'px;border-radius:5px 5px 0 0;background:' + (AZ if i == len(sem) - 1 else '#B9CCE6') + '"></span><span style="font-size:10px;color:#56615B">S' + str(i + 35) + '</span></span>' for i, v in enumerate(sem))
    prod = lambda n, v, s, borde=True: fila('', n, v + ' visitas · ' + s + ' solicitudes', '', borde)
    b = (titulo('Estadísticas', 'Estadísticas', 'Últimos 30 días · básicas en Gratis') + chips(['7 días', '30 días', '12 meses'], (1,)) +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + kpi('3.420', 'Apariciones en búsquedas', '+12 %') + kpi('286', 'Visitas a la ficha', '+18 %') +
         kpi('9', 'Solicitudes', '3 visibles en Gratis', WN) + kpi('7 h', 'Respuesta media', 'compromiso 24 h') + '</div>' +
         card('Visitas por semana', '<div style="display:flex;gap:6px;align-items:flex-end;height:120px">' + barras + '</div>') +
         card('Tus productos', prod('Corrector vitamínico CV-20', '180', '6', False) + prod('Premezcla P-40', '74', '2') + prod('Acidificante AQ-7', '32', '1')) +
         pro('<strong>Quién te visita</strong> (tipo de comprador, zona y especie) con Empresa Pro. Nunca nombres ni contactos.'))
    return pantalla(b, tab='Panel', avatar='AE')

def plan():
    fil = [('Solicitudes de compradores', 'De 3', 'Ilimitadas', 'Ilimitadas'), ('Productos', '15', '100', 'Ilimitados'), ('Miembros', 'Ilimitados', 'Ilimitados', 'Ilimitados'),
           ('Estados y notas', '—', 'Sí', 'Sí'), ('Oportunidades', 'Solo el número', '2 al mes', 'Ilimitadas'), ('Estadísticas', 'Básicas', 'Avanzadas', '+ comparativa'), ('Adjuntos en mensajes', '—', '—', 'Sí · revisados')]
    tabla = ('<div style="display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:6px;font-size:11.5px;align-items:center">'
             '<span></span><strong style="color:' + AZ + '">Gratis</strong><strong>Pro</strong><strong>Premium</strong>' +
             ''.join('<span style="color:#4A5650;padding:6px 0;border-top:1px solid #EEF1EE">' + a + '</span><span style="padding:6px 0;border-top:1px solid #EEF1EE;font-weight:600">' + b + '</span><span style="padding:6px 0;border-top:1px solid #EEF1EE">' + c + '</span><span style="padding:6px 0;border-top:1px solid #EEF1EE">' + d + '</span>' for a, b, c, d in fil) + '</div>')
    caja = lambda t, p, on=False, prim=False: ('<div class="card" style="gap:4px;' + ('border:2px solid ' + AZ + ';background:#F3F7FC' if on else '') + '"><span style="display:flex;justify-content:space-between"><strong style="font-size:15px">' + t + '</strong>' + (st('Tu plan', AZST) if on else '') + '</span>'
                                              '<span style="font-size:18px;font-weight:700">' + p + '</span>' + ('' if on else btn('Pasar a ' + t.split()[-1], prim)) + '</div>')
    b = (titulo('Plan y facturación', 'Plan y facturación') + caja('Empresa Gratis', '0 € · sin tarjeta', True) +
         '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + caja('Empresa Pro', '79 €/mes', False, True) + caja('Empresa Premium', '199 €/mes') + '</div>' +
         card('Qué incluye cada plan', tabla) +
         card('Facturación de la empresa', fila('', 'Se factura a', 'AgroExport SRL · sociedad del CRM', '', False) + '<span class="hint">Los datos fiscales vienen del CRM y solo los cambia el superadmin.</span>') +
         nota('Sin permanencia: si cancelas, sigues con el plan hasta el final del periodo pagado. Sucursales: alta gratis; plan de grupo a medida.'))
    return pantalla(b, ('Plan y facturación', 'Empresa'), tab='Empresa', avatar='AE')

PANT = [('MB_EmpSolicitudes', 'EM5 · Solicitudes de la empresa', solicitudes), ('MB_EmpEquipo', 'EM6 · Equipo', equipo),
        ('MB_EmpEstadisticas', 'EM7 · Estadísticas', estadisticas), ('MB_EmpPlan', 'EM8 · Plan y facturación', plan)]
ALTOS = {'MB_EmpSolicitudes': 1040, 'MB_EmpEquipo': 990, 'MB_EmpEstadisticas': 1100, 'MB_EmpPlan': 1140}   # medidas en el navegador
if __name__ == '__main__':
    alto = dict(ALTOS, **{k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    BLOBS = json.load(open(W + '/tools/blobs_movil.json'))
    c = json.load(open(sys.argv[1])); B = c['boards']
    fila_emp = [k for k in ('MB_EmpPanel.dc.html', 'MB_EEM1.dc.html', 'MB_EEM2.dc.html', 'MB_EEM3.dc.html') if k in B]
    ref = B[fila_emp[0]]; x0 = max(B[k]['x'] for k in fila_emp) + 470
    nuevos = []
    for i, (k, t, f) in enumerate(PANT):
        h = int(alto.get(k, 1100))
        html = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '/_blob/' + BLOBS.get(m.group(1), m.group(1)), wrap('Móvil · ' + t, h, f()))
        open(DEST + k + '.dc.html', 'w').write(html)
        B[k + '.dc.html'] = {'w': 390, 'h': h, 'page': ref['page'], 'x': x0 + i * 470, 'y': ref['y'], 'title': t}
        if k + '.dc.html' not in c['order']: c['order'].append(k + '.dc.html')
        nuevos.append(k + '.dc.html')
    json.dump(c, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    json.dump(nuevos, open(DEST + '../nuevos.json', 'w'))
    print('ok', len(nuevos), ref['page'], ref['y'])
