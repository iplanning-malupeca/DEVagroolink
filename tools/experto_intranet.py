"""Intranet de experta (escritorio, Laura Gil · plan Gratis): E6 Consultas organizadas, E7 Mis candidaturas, E8 Estadísticas, E9 Plan y facturación.
Mismo armazón que E1–E5 (IntSidebar modo experta + IntHeader). Límites según data/planes.json (experto: Gratis y Pro · 19,90 €).
Sin contactos visibles: todo va por Mensajes; el filtro bloquea teléfonos, emails, webs, @usuario y QR.
Uso: python3 tools/experto_intranet.py <carpeta>/project   → escribe ExpConsultasOrg, ExpCandidaturas, ExpEstadisticas, ExpPlan"""
import os, sys
DEST = sys.argv[1].rstrip('/') + '/'
AZ = '#4B3BA6'
CSS = """body{margin:0;line-height:1.3;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#4B3BA6;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-sizing:border-box;min-width:0}
.h2{margin:0;font-size:16px;font-weight:600}
.hint{font-size:12px;color:#56615B}
.row{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13px}
.av{width:36px;height:36px;border-radius:50%;background:#F1EEFB;color:#4B3BA6;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none}
.st{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap}
.ok{background:#EEF6EE;color:#0E5A3A}.wn{background:#FFF4E0;color:#7A4B00}.gr{background:#F1F3F6;color:#4A5560}.az{background:#F1EEFB;color:#4B3BA6}.er{background:#FDECEA;color:#A3271B}
.chip{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 13px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12.5px;white-space:nowrap;color:#17231D}
.chip.on{background:#4B3BA6;border-color:#4B3BA6;color:#FFFFFF}
.btn{height:38px;padding:0 16px;border-radius:10px;border:1.5px solid #4B3BA6;color:#4B3BA6;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;box-sizing:border-box}
.btnp{height:38px;padding:0 16px;border-radius:10px;background:#4B3BA6;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.nota{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;background:#F6F4FC;border:1px solid #E4DFF5;font-size:12.5px;color:#33424C}
.pro{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:12.5px;color:#33424C}
.th{display:grid;gap:12px;padding:0 0 8px;font-size:11px;font-weight:600;letter-spacing:.04em;color:#56615B}
.tr{display:grid;gap:12px;align-items:center;padding:11px 0;border-top:1px solid #EEF1EE;font-size:13px}"""

def svg(d, s=16, w=1.9):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="%s"/></svg>' % (s, s, w, d)
I = {'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01', 'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4', 'mas': 'M12 5v14M5 12h14',
     'msg': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6', 'ok': 'M5 12l5 5 9-10', 'flecha': 'M5 12h14M13 6l6 6-6 6', 'x': 'M6 6l12 12M18 6 6 18'}

def pagina(titulo, activo, cab, cuerpo, h=1000, sub=''):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + titulo + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n'
            '<div style="width: 1280px; height: ' + str(h) + 'px; background: #F6F8F6; position: relative; overflow: hidden;">\n'
            '  <div style="display: flex; padding-top: 68px; height: ' + str(h) + 'px; box-sizing: border-box;">\n'
            '    <dc-import name="IntSidebar" modo="experta" activo="' + activo + '"' + (' sub="' + sub + '"' if sub else '') + ' alto="' + str(h - 68) + '" hint-size="256px,' + str(h - 68) + 'px"></dc-import>\n'
            '    <main style="flex: 1; min-width: 0; padding: 22px 28px; display: flex; flex-direction: column; gap: 16px;">' + cab + cuerpo + '</main>\n'
            '  </div>\n  <div style="position: absolute; top: 0; left: 0; width: 1280px;">\n'
            '    <dc-import name="IntHeader" persona="Laura G." iniciales="LG" color="#4B3BA6" variante="experta" hint-size="1280px,68px"></dc-import>\n  </div>\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

def cabecera(miga, h1, sub, acciones=''):
    return ('<div style="display: flex; align-items: flex-end; gap: 16px;"><div style="flex: 1; min-width: 0;"><div style="font-size: 13px; color: #56615B;">Como experta › ' + miga + '</div>'
            '<h1 style="margin: 2px 0 0; font-size: 28px; font-weight: 600;">' + h1 + '</h1><p style="margin: 2px 0 0; font-size: 13.5px; color: #4A5650;">' + sub + '</p></div>' + acciones + '</div>')

# ---------- E6 · Consultas organizadas (Pro) ----------
def consultas():
    tarjeta = lambda ini, quien, t, extra, on=False: ('<div style="background: #FFFFFF; border: ' + ('2px solid ' + AZ if on else '1px solid #E3E8E4') + '; border-radius: 12px; padding: 10px 12px; display: flex; flex-direction: column; gap: 6px;">'
                                                      '<span style="display: flex; gap: 8px; align-items: center;"><span class="av" style="width: 28px; height: 28px; font-size: 11px;">' + ini + '</span><span class="hint">' + quien + '</span></span>'
                                                      '<strong style="font-size: 13px; font-weight: 600; line-height: 1.35;">' + t + '</strong>' + extra + '</div>')
    et = lambda t: '<span class="st gr" style="align-self: flex-start;">' + t + '</span>'
    col = lambda t, n, cards: ('<section style="flex: 1; min-width: 0; background: #EEF0F3; border-radius: 14px; padding: 10px; display: flex; flex-direction: column; gap: 8px;">'
                              '<span style="display: flex; justify-content: space-between; font-size: 12.5px; font-weight: 600; padding: 2px 4px;"><span>' + t + '</span><span class="hint">' + n + '</span></span>' + cards + '</section>')
    tablero = ('<div style="display: flex; gap: 12px; align-items: flex-start;">' +
               col('Nueva', '1', tarjeta('GA', 'Ganadero · Huesca · 5 h', 'Auditoría nutricional de lotes de broilers', et('Broilers') + '<span class="hint">Responder antes de 24 h</span>', True)) +
               col('En curso', '2', tarjeta('IH', 'Integradora · Huesca · ayer', 'Formación en bienestar animal', et('Formación')) + tarjeta('CO', 'Cooperativa · Teruel · 3 d', 'Plan de vacunación de ponedoras', et('Ponedoras') + '<span class="hint">Nota: pedir histórico de bajas</span>')) +
               col('Presupuesto enviado', '1', tarjeta('TE', 'Técnico · Lleida · 6 d', 'Revisión de la fórmula de arranque', '<span class="hint">350 € · sin respuesta 4 d</span>')) +
               col('Cerrada', '3', tarjeta('GP', 'Granja El Pinar · 8 oct', 'Revisión de propuestas', '<span class="st ok" style="align-self: flex-start;">Contratada</span>') + '<span class="hint" style="padding: 0 4px;">+ 2 más</span>') + '</div>')
    detalle = ('<section class="card" style="flex-direction: row; gap: 20px; align-items: flex-start;"><div style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 8px;">'
               '<span style="display: flex; gap: 8px; align-items: center;"><span class="st az">Nueva</span><strong style="font-size: 15px;">Auditoría nutricional de lotes de broilers</strong></span>'
               '<span class="hint">Ganadero · Huesca · Avicultura › Broilers · 2 naves · 40.000 aves · desde tu servicio «Auditoría nutricional»</span>'
               '<span style="display: flex; gap: 8px; flex-wrap: wrap;"><span class="chip on">Nueva</span><span class="chip">En curso</span><span class="chip">Presupuesto enviado</span><span class="chip">Cerrada</span></span>'
               '<span style="display: flex; gap: 8px;"><a href="#" class="btnp">Abrir conversación</a><a href="#" class="btn">Enviar presupuesto</a></span></div>'
               '<div style="width: 360px; flex: none; display: flex; flex-direction: column; gap: 6px;"><span style="font-size: 12.5px; font-weight: 600;">Notas privadas</span>'
               '<span style="min-height: 78px; border: 1px solid #D5DED8; border-radius: 10px; padding: 8px 12px; font-size: 13px; color: #33424C; line-height: 1.4;">Cambió de pienso en agosto. Pedir índices de los 3 últimos lotes antes de presupuestar.</span>'
               '<span class="hint">Solo las ves tú. El ganadero no las ve.</span></div></section>')
    cab = cabecera('Consultas recibidas', 'Consultas organizadas', 'Mueve cada consulta por estados y apunta notas. Así se ve con Experto Pro.',
                   '<span style="display: flex; gap: 6px;"><span class="chip">Lista</span><span class="chip on">Tablero</span></span>')
    cuerpo = ('<div class="pro">' + svg(I['lock'], 16) + '<span style="flex: 1;">En Gratis recibes y respondes consultas sin límite, en una lista. Estados, etiquetas y notas privadas llegan con <strong>Experto Pro · 19,90 €/mes</strong>.</span><a href="#" class="btnp" style="height: 34px;">Pasar a Pro</a></div>'
              + tablero + detalle)
    return pagina('Intranet experta · Consultas organizadas', 'Consultas recibidas', cab, cuerpo)

# ---------- E7 · Mis candidaturas ----------
def candidaturas():
    cols = 'grid-template-columns: minmax(0,1fr) 84px 118px 44px;'
    fila = lambda t, quien, prop, est, cls, cuando, on=False: ('<div class="tr" style="' + cols + (' background: #F6F4FC; margin: 0 -12px; padding: 11px 12px; border-radius: 10px; border-top-color: transparent;' if on else '') + '">'
                                                              '<span><strong style="font-weight: 600;">' + t + '</strong><br><span class="hint">' + quien + '</span></span><span>' + prop + '</span><span><span class="st ' + cls + '">' + est + '</span></span><span class="hint">' + cuando + '</span></div>')
    tabla = ('<section class="card" style="flex: 1; min-width: 0; padding-top: 14px;"><div class="th" style="' + cols + '"><span>PROYECTO</span><span>PROPUESTA</span><span>ESTADO</span><span>CUÁNDO</span></div>' +
             fila('Asesoría para reducir el índice de conversión · Nave 2', 'Ganadero · Lleida', '1.200 €', 'Enviada', 'az', '2 d', True) +
             fila('Plan de bioseguridad para 3 granjas', 'Integradora · Huesca', '2.400 €', 'Preseleccionada', 'wn', '5 d') +
             fila('Formación del personal en bienestar animal', 'Cooperativa · Teruel', '900 €', 'Adjudicada', 'ok', '12 d') +
             fila('Revisión de raciones en ponedoras', 'Granja · Zaragoza', '600 €', 'No elegida', 'gr', '20 d') + '</section>')
    det = ('<aside class="card" style="width: 340px; flex: none; gap: 10px;"><span style="display: flex; justify-content: space-between;"><span class="st az">Enviada</span><span class="hint">hace 2 d</span></span>'
           '<strong style="font-size: 15px;">Asesoría para reducir el índice de conversión · Nave 2</strong><span class="hint">Ganadero · Lleida · Avicultura › Broilers · 6 candidaturas</span>'
           '<div class="row" style="border-top: 0; padding: 0;"><span class="hint" style="flex: 1;">Precio</span><strong style="font-weight: 500;">1.200 €</strong></div>'
           '<div class="row" style="padding: 6px 0 0;"><span class="hint" style="flex: 1;">Plazo</span><strong style="font-weight: 500;">6 semanas</strong></div>'
           '<div style="padding: 10px 12px; border-radius: 12px; background: #F6F8F6; font-size: 13px; line-height: 1.45;">«Propongo revisar la fórmula y el manejo de los 3 últimos lotes y una visita a la nave…»</div>'
           '<span style="display: flex; gap: 8px;"><a href="#" class="btn" style="flex: 1;">Editar</a><a href="#" class="btn" style="flex: 1;">Retirar</a></span>'
           '<span class="hint">Puedes editarla hasta que el ganadero elija. Si lleva un contacto, no se envía.</span></aside>')
    cab = cabecera('Oportunidades › Mis candidaturas', 'Mis candidaturas', 'Tus propuestas a proyectos de ganaderos y empresas, y en qué punto están.')
    cuerpo = ('<div class="pro">' + svg(I['lock'], 16) + '<span style="flex: 1;">En Gratis ves los proyectos abiertos; para presentar candidaturas necesitas <strong>Experto Pro</strong>. Así se ve con Pro.</span><a href="#" class="btnp" style="height: 34px;">Pasar a Pro</a></div>'
              '<div style="display: flex; gap: 8px;"><span class="chip on">Todas 4</span><span class="chip">Enviadas 1</span><span class="chip">Preseleccionadas 1</span><span class="chip">Adjudicadas 1</span><span class="chip">No elegidas 1</span></div>'
              '<div style="display: flex; gap: 16px; align-items: flex-start;">' + tabla + det + '</div>')
    return pagina('Intranet experta · Mis candidaturas', 'Oportunidades', cab, cuerpo, sub='Mis candidaturas')

# ---------- E8 · Estadísticas ----------
def estadisticas():
    kpi = lambda n, t, d, cls='ok': ('<div class="card" style="gap: 2px; padding: 14px 16px;"><span style="font-size: 26px; font-weight: 600;">' + n + '</span><span style="font-size: 12.5px; color: #4A5650;">' + t + '</span>'
                                    '<span class="st ' + cls + '" style="align-self: flex-start; margin-top: 4px;">' + d + '</span></div>')
    sem = [18, 22, 20, 27, 31, 29, 36, 41]
    barras = ''.join('<span style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px;"><span style="font-size: 11px; color: #56615B;">' + str(v) + '</span>'
                     '<span style="width: 100%; height: ' + str(int(v * 3.6)) + 'px; border-radius: 6px 6px 0 0; background: ' + (AZ if i == len(sem) - 1 else '#CFC7EE') + ';"></span>'
                     '<span style="font-size: 11px; color: #56615B;">S' + str(i + 35) + '</span></span>' for i, v in enumerate(sem))
    graf = ('<section class="card" style="flex: 1; min-width: 0;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 class="h2">Visitas a tu perfil por semana</h2><span class="hint">últimas 8 semanas</span></div>'
            '<div style="display: flex; gap: 12px; align-items: flex-end; height: 190px; padding-top: 8px;">' + barras + '</div></section>')
    srv = ('<section class="card" style="width: 400px; flex: none; gap: 0;"><h2 class="h2" style="padding-bottom: 8px;">Tu servicio</h2>'
           '<div class="row" style="border-top: 0;"><span style="flex: 1;"><strong style="font-weight: 600;">Auditoría nutricional de lotes de broilers</strong><br><span class="hint">1 de 1 en Gratis</span></span></div>'
           '<div class="row"><span style="flex: 1;">Visitas</span><strong>96</strong></div><div class="row"><span style="flex: 1;">Consultas desde el servicio</span><strong>4</strong></div>'
           '<div class="row"><span style="flex: 1;">Guardado en tableros</span><strong>11</strong></div></section>')
    av = ('<section class="card" style="gap: 8px;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 class="h2">Quién te busca y con qué palabras</h2><span class="st wn">Avanzadas · con Pro</span></div>'
          '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; filter: blur(2.5px);"><span style="font-size: 13px;">Ganaderos 58 % · integradoras 24 % · técnicos 18 %</span><span style="font-size: 13px;">Aragón 46 % · Cataluña 31 % · Navarra 9 %</span><span style="font-size: 13px;">«índice de conversión», «nutrición broilers», «bienestar»</span></div>'
          '<span class="hint">Por tipo, zona y búsqueda. Nunca se muestran nombres ni contactos. Con Pro, además, apareces como recomendada en búsquedas.</span></section>')
    cab = cabecera('Estadísticas', 'Estadísticas', 'Cómo te encuentran y qué te piden. Plan Gratis: estadísticas básicas.',
                   '<span style="display: flex; gap: 6px;"><span class="chip">7 días</span><span class="chip on">30 días</span><span class="chip">12 meses</span></span>')
    cuerpo = ('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px;">' + kpi('1.240', 'Apariciones en búsquedas', '+9 % vs. mes anterior') + kpi('224', 'Visitas a tu perfil', '+15 %') +
              kpi('6', 'Consultas recibidas', 'sin límite') + kpi('5 h', 'Tiempo medio de respuesta', 'compromiso 24 h') + '</div>'
              '<div style="display: flex; gap: 16px;">' + graf + srv + '</div>' + av)
    return pagina('Intranet experta · Estadísticas', 'Estadísticas', cab, cuerpo)

# ---------- E9 · Plan y facturación ----------
def plan():
    filas = [('Recibir y responder consultas', 'Ilimitadas', 'Ilimitadas'), ('Servicios publicados', '1', 'Ilimitados'), ('Candidaturas a proyectos', 'Solo ver proyectos abiertos', 'Ilimitadas'),
             ('Portfolio / casos', '1', 'Ilimitado'), ('Consultas organizadas (estados y notas)', '—', 'Sí'), ('Publicar contenido', '—', 'Sí'), ('Recomendada en búsquedas', '—', 'Sí'),
             ('Estadísticas', 'Básicas', 'Avanzadas'), ('Ventajas de Comprador Pro', '—', 'Incluidas')]
    cols = 'grid-template-columns: minmax(0,1.6fr) repeat(2, minmax(0,1fr));'
    cab_t = lambda t, p, sub, on=False: ('<span style="display: flex; flex-direction: column; gap: 4px; padding: 14px; border-radius: 14px; ' + ('border: 2px solid ' + AZ + '; background: #F6F4FC;' if on else 'border: 1px solid #E3E8E4; background: #FFFFFF;') + '">'
                                         '<span style="display: flex; justify-content: space-between; align-items: center;"><strong style="font-size: 16px;">' + t + '</strong>' + ('<span class="st az">Tu plan</span>' if on else '') + '</span>'
                                         '<span style="font-size: 20px; font-weight: 600;">' + p + '</span><span class="hint">' + sub + '</span>' +
                                         ('' if on else '<a href="#" class="btnp" style="margin-top: 6px; height: 36px;">Pasar a Pro</a>') + '</span>')
    tabla = ('<section class="card" style="gap: 0;"><div style="display: grid; gap: 12px; ' + cols + ' padding-bottom: 12px;"><span></span>' +
             cab_t('Experto Gratis', '0 €', 'Sin tarjeta', True) + cab_t('Experto Pro', '19,90 €/mes', 'Sin permanencia') + '</div>' +
             ''.join('<div class="tr" style="' + cols + '"><span>' + a + '</span><span style="font-weight: 600;">' + b + '</span><span>' + c + '</span></div>' for a, b, c in filas) + '</section>')
    lado = ('<aside style="width: 320px; flex: none; display: flex; flex-direction: column; gap: 14px;">'
            '<section class="card" style="gap: 6px;"><h2 class="h2">Facturación</h2><span style="font-size: 13px; color: #33424C;">Aún no hay facturas: estás en Experto Gratis.</span>'
            '<div class="row"><span class="hint" style="flex: 1;">Se factura a</span><strong style="font-weight: 500; text-align: right;">Laura Gil<br><span class="hint">tus datos de Mi cuenta</span></strong></div>'
            '<a href="#" style="font-size: 12.5px;">Editar datos de facturación →</a></section>'
            '<section class="card" style="gap: 6px;"><h2 class="h2">Lo que más usas</h2><span style="font-size: 13px; color: #33424C; line-height: 1.4;">Tienes 1 de 1 servicio y 3 proyectos que encajan contigo a los que aún no puedes presentarte.</span></section>'
            '<div class="nota">' + svg(I['info'], 16) + '<span>Sin permanencia: si cancelas, sigues con Pro hasta el final del periodo pagado.</span></div></aside>')
    cab = cabecera('Plan y facturación', 'Plan y facturación', 'Qué incluye tu plan de experta y qué ganas con Pro.')
    return pagina('Intranet experta · Plan y facturación', 'Plan y facturación', cab, '<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="flex: 1; min-width: 0;">' + tabla + '</div>' + lado + '</div>')

PANT = [('ExpConsultasOrg', 'E6 · Consultas organizadas: estados, etiquetas y notas privadas (Experto Pro)', consultas),
        ('ExpCandidaturas', 'E7 · Mis candidaturas: propuestas a proyectos y su estado (Experto Pro)', candidaturas),
        ('ExpEstadisticas', 'E8 · Estadísticas de experta: básicas en Gratis, avanzadas con Pro', estadisticas),
        ('ExpPlan', 'E9 · Plan y facturación de experta: Gratis y Pro · 19,90 €', plan)]
if __name__ == '__main__':
    for k, t, f in PANT:
        open(DEST + k + '.dc.html', 'w').write(f())
    print('ok', len(PANT))
