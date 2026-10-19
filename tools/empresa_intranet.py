"""Intranet de empresa (escritorio, AgroExport SRL · Carla): EM5 Solicitudes, EM6 Equipo, EM7 Estadísticas, EM8 Plan y facturación.
Mismo armazón que EM1 (IntSidebar modo empresa + IntHeader). Límites según data/planes.json (empresa).
Sin contactos visibles: el comprador nunca ve teléfonos, emails ni webs; todo va por Mensajes.
Uso: python3 tools/empresa_intranet.py <carpeta>/project   → escribe EmpSolicitudes, EmpEquipo, EmpEstadisticas, EmpPlan"""
import os, sys
DEST = sys.argv[1].rstrip('/') + '/'
AZ = '#1D4E89'
CSS = """body{margin:0;line-height:1.3;font-family:'Poppins',sans-serif;color:#17231D}
a{color:#1D4E89;text-decoration:none;font-weight:500}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-sizing:border-box;min-width:0}
.h2{margin:0;font-size:16px;font-weight:600}
.hint{font-size:12px;color:#56615B}
.row{display:flex;align-items:center;gap:12px;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13px}
.av{width:36px;height:36px;border-radius:50%;background:#E9F0F9;color:#1D4E89;font-size:12px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none}
.st{font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;white-space:nowrap}
.ok{background:#EEF6EE;color:#0E5A3A}.wn{background:#FFF4E0;color:#7A4B00}.gr{background:#F1F3F6;color:#4A5560}.az{background:#E9F0F9;color:#1D4E89}.er{background:#FDECEA;color:#A3271B}
.chip{display:inline-flex;align-items:center;gap:6px;height:32px;padding:0 13px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12.5px;white-space:nowrap;color:#17231D}
.chip.on{background:#1D4E89;border-color:#1D4E89;color:#FFFFFF}
.btn{height:38px;padding:0 16px;border-radius:10px;border:1.5px solid #1D4E89;color:#1D4E89;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap;box-sizing:border-box}
.btnp{height:38px;padding:0 16px;border-radius:10px;background:#1D4E89;color:#FFFFFF;font-size:13px;font-weight:500;display:inline-flex;align-items:center;justify-content:center;gap:6px;white-space:nowrap}
.nota{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;background:#F4F7FB;border:1px solid #E2E8F0;font-size:12.5px;color:#33424C}
.pro{display:flex;gap:10px;align-items:center;padding:10px 14px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:12.5px;color:#33424C}
.th{display:grid;gap:12px;padding:0 0 8px;font-size:11px;font-weight:600;letter-spacing:.04em;color:#56615B}
.tr{display:grid;gap:12px;align-items:center;padding:11px 0;border-top:1px solid #EEF1EE;font-size:13px}"""

def svg(d, s=16, w=1.9):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="%s"/></svg>' % (s, s, w, d)
I = {'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01', 'lock': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4', 'mas': 'M12 5v14M5 12h14',
     'msg': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6', 'ok': 'M5 12l5 5 9-10', 'flecha': 'M5 12h14M13 6l6 6-6 6', 'x': 'M6 6l12 12M18 6 6 18'}

def pagina(titulo, activo, cab, cuerpo, h=900):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + titulo + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n'
            '<div style="width: 1280px; height: ' + str(h) + 'px; background: #F6F8F6; position: relative; overflow: hidden;">\n'
            '  <div style="display: flex; padding-top: 68px; height: ' + str(h) + 'px; box-sizing: border-box;">\n'
            '    <dc-import name="IntSidebar" modo="empresa" activo="' + activo + '" alto="' + str(h - 68) + '" hint-size="256px,' + str(h - 68) + 'px"></dc-import>\n'
            '    <main style="flex: 1; min-width: 0; padding: 22px 28px; display: flex; flex-direction: column; gap: 16px;">' + cab + cuerpo + '</main>\n'
            '  </div>\n  <div style="position: absolute; top: 0; left: 0; width: 1280px;">\n'
            '    <dc-import name="IntHeader" persona="Carla M." iniciales="CM" color="#1D4E89" variante="empresa" hint-size="1280px,68px"></dc-import>\n  </div>\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

def cabecera(miga, h1, sub, acciones=''):
    return ('<div style="display: flex; align-items: flex-end; gap: 16px;"><div style="flex: 1; min-width: 0;"><div style="font-size: 13px; color: #56615B;">AgroExport SRL › ' + miga + '</div>'
            '<h1 style="margin: 2px 0 0; font-size: 28px; font-weight: 600;">' + h1 + '</h1><p style="margin: 2px 0 0; font-size: 13.5px; color: #4A5650;">' + sub + '</p></div>' + acciones + '</div>')

# ---------- EM5 · Solicitudes ----------
def solicitudes():
    cols = 'grid-template-columns: minmax(0,1.45fr) minmax(0,1.25fr) minmax(0,1.15fr) 118px 70px;'
    fila = lambda ini, quien, zona, pide, prod, asig, est, cls, cuando, on=False: (
        '<div class="tr" style="' + cols + (' background: #F3F7FC; margin: 0 -12px; padding: 11px 12px; border-radius: 10px; border-top-color: transparent;' if on else '') + '">'
        '<span style="display: flex; gap: 10px; align-items: center; min-width: 0;"><span class="av">' + ini + '</span><span style="min-width: 0;"><strong style="font-weight: 600;">' + quien + '</strong><br><span class="hint">' + zona + '</span></span></span>'
        '<span style="min-width: 0;">' + pide + '<br><span class="hint">' + prod + '</span></span><span style="min-width: 0;">' + asig + '</span><span><span class="st ' + cls + '">' + est + '</span></span><span class="hint">' + cuando + '</span></div>')
    bloq = lambda zona: ('<div class="tr" style="' + cols + ' color: #8A948F;"><span style="display: flex; gap: 10px; align-items: center;"><span class="av" style="background: #F1F3F6; color: #8A948F;">' + svg(I['lock'], 15) + '</span><span>Comprador de ' + zona + '<br><span class="hint">Guardada · se ve con Empresa Pro</span></span></span>'
                         '<span style="filter: blur(3px);">Pide información de un producto</span><span>—</span><span><span class="st gr">Guardada</span></span><span class="hint">—</span></div>')
    tabla = ('<section class="card" style="flex: 1; min-width: 0; padding-top: 14px;">'
             '<div class="th" style="' + cols + '"><span>COMPRADOR</span><span>QUÉ PIDE</span><span>LA ATIENDE</span><span>ESTADO</span><span>CUÁNDO</span></div>' +
             fila('GA', 'Ganadero', 'Lleida · Avicultura · broilers', 'Precio y plazo', 'Corrector vitamínico CV-20', 'Agropecuària del Segre<br><span class="hint">distribuidor de la zona</span>', 'Nueva', 'az', '2 h', True) +
             fila('TE', 'Técnico de explotación', 'Segovia · Porcino', 'Distribuidor en su zona', 'Premezcla P-40', 'Jorge Pérez<br><span class="hint">comercial · Castilla y León</span>', 'Sin respuesta 52 h', 'er', '3 d') +
             fila('IN', 'Integradora', 'Huesca · Avicultura', 'Muestra para prueba', 'Corrector vitamínico CV-20', 'Carla Martín<br><span class="hint">Dirección comercial</span>', 'En conversación', 'ok', '5 d') +
             bloq('Zaragoza') + bloq('Murcia') +
             '<span class="hint" style="padding-top: 8px;">Plan Gratis: ves las solicitudes de 3 compradores. Las siguientes se guardan y las ves al pasar a Pro.</span></section>')
    detalle = ('<aside class="card" style="width: 330px; flex: none; gap: 12px;">'
               '<span style="display: flex; align-items: center; justify-content: space-between;"><span class="st az">Nueva</span><span class="hint">hace 2 h · por la ficha del producto</span></span>'
               '<span style="display: flex; gap: 10px; align-items: center;"><span class="av">GA</span><span><strong style="font-size: 15px;">Ganadero · Lleida</strong><br><span class="hint">Avicultura · broilers · 2 naves</span></span></span>'
               '<div style="padding: 10px 12px; border-radius: 12px; background: #F6F8F6; font-size: 13px; line-height: 1.4;">«Querría precio y plazo para 2 t de CV-20 para broilers. Estoy en Lleida.»</div>'
               '<div class="row" style="border-top: 0; padding: 0;"><span class="hint" style="flex: 1;">Producto</span><strong style="font-weight: 500;">Corrector vitamínico CV-20</strong></div>'
               '<div style="display: flex; flex-direction: column; gap: 5px;"><span style="font-size: 12.5px; font-weight: 600;">La atiende</span><span style="height: 40px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; justify-content: space-between; padding: 0 12px; font-size: 13px;">Agropecuària del Segre · zona Lleida<span class="hint">▾</span></span>'
               '<span class="hint">Por zona: el distribuidor de Lleida. Puedes reasignarla a alguien del equipo.</span></div>'
               '<a href="#" class="btnp" style="height: 42px;">' + svg(I['msg'], 16) + 'Responder en Mensajes</a>'
               '<div class="pro">' + svg(I['lock'], 16) + '<span><strong>Estados, notas y asignación avanzada</strong> con Empresa Pro.</span></div>'
               '<span class="hint">El comprador ve «AgroExport» y el nombre de pila de quien responde; nunca teléfonos ni emails.</span></aside>')
    cab = cabecera('Solicitudes', 'Solicitudes', 'Lo que piden los compradores por tus productos y tu ficha. Cada una abre un hilo en Mensajes.',
                   '<a href="#" class="btn">Ver en Mensajes</a>')
    cuerpo = ('<div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><span class="chip on">Nuevas 1</span><span class="chip">Sin respuesta · más de 48 h 1</span><span class="chip">En conversación 1</span><span class="chip">Cerradas 24</span>'
              '<span style="flex: 1;"></span><span class="chip">Producto ▾</span><span class="chip">Zona ▾</span><span class="chip">La atiende ▾</span></div>'
              '<div style="display: flex; gap: 16px; flex: 1; min-height: 0;">' + tabla + detalle + '</div>'
              '<div class="pro">' + svg(I['lock'], 16) + '<span style="flex: 1;"><strong>2 solicitudes guardadas</strong> de compradores de Zaragoza y Murcia. Con Empresa Pro las ves todas y sin límite.</span><a href="#" class="btn" style="height: 34px;">Ver Empresa Pro</a></div>')
    return pagina('Intranet empresa · Solicitudes', 'Solicitudes', cab, cuerpo)

# ---------- EM6 · Equipo ----------
def equipo():
    cols = 'grid-template-columns: minmax(0,1.6fr) minmax(0,1.1fr) minmax(0,1.3fr) 110px 70px;'
    m = lambda ini, n, cargo, rol, zona, est, cls, color='#E9F0F9', tinta=AZ: ('<div class="tr" style="' + cols + '"><span style="display: flex; gap: 10px; align-items: center;"><span class="av" style="background: ' + color + '; color: ' + tinta + ';">' + ini + '</span>'
                                                                         '<span><strong style="font-weight: 600;">' + n + '</strong><br><span class="hint">' + cargo + '</span></span></span><span>' + rol + '</span><span class="hint" style="font-size: 12.5px;">' + zona + '</span><span><span class="st ' + cls + '">' + est + '</span></span><a href="#" style="font-size: 12.5px;">Editar</a></div>')
    tabla = ('<section class="card" style="flex: 1; min-width: 0;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 class="h2">4 personas</h2><span class="hint">Miembros sin límite en todos los planes</span></div>'
             '<div class="th" style="' + cols + ' padding-top: 4px;"><span>PERSONA</span><span>ROL</span><span>ATIENDE</span><span>ESTADO</span><span></span></div>' +
             m('CM', 'Carla Martín (tú)', 'Directora comercial', 'Administradora', 'Todas las solicitudes', 'Activa', 'ok', AZ, '#FFFFFF') +
             m('JP', 'Jorge Pérez', 'Comercial', 'Comercial', 'Castilla y León, Madrid', 'Activo', 'ok') +
             m('AS', 'Ana Soler', 'Técnica de producto', 'Lectura', 'Responde dudas técnicas cuando la asignan', 'Activa', 'ok') +
             m('MV', 'Marc Vidal', 'Comercial', 'Comercial', 'Cataluña', 'Invitación enviada', 'wn', '#F1F3F6', '#4A5560') +
             '<div style="display: flex; gap: 10px; padding-top: 8px; align-items: center;"><span style="flex: 1; height: 40px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; padding: 0 12px; font-size: 13px; color: #8A948F;">Nombre o email de trabajo del compañero</span>'
             '<span class="chip" style="height: 40px;">Comercial ▾</span><a href="#" class="btnp" style="height: 40px;">' + svg(I['mas'], 16) + 'Invitar</a></div></section>')
    rol = lambda t, d: '<div class="row" style="align-items: flex-start;"><strong style="width: 120px; flex: none; font-weight: 600;">' + t + '</strong><span style="color: #33424C; line-height: 1.35;">' + d + '</span></div>'
    lado = ('<aside style="width: 340px; flex: none; display: flex; flex-direction: column; gap: 14px;"><section class="card" style="gap: 2px;"><h2 class="h2" style="padding-bottom: 6px;">Qué puede hacer cada rol</h2>' +
            rol('Administrador', 'Edita la ficha, los productos, el equipo y el plan. Ve todas las solicitudes y estadísticas.').replace('border-top: 1px solid #EEF1EE;', '', 1) +
            rol('Comercial', 'Responde las solicitudes que le llegan (por zona o asignadas) y ve sus estadísticas.') + rol('Lectura', 'Ve la ficha, los productos y las solicitudes; responde solo si se las asignan.') + '</section>'
            '<div class="nota">' + svg(I['info'], 16) + '<span>Cada alta avisa a las administradoras (copia al superadmin), que pueden quitar el acceso.</span></div>'
            '<div class="pro" style="background: #FFFFFF; border-color: #E3E8E4;">' + svg(I['lock'], 16) + '<span>Los compradores nunca ven el email ni el teléfono de tu equipo: solo el nombre de pila de quien responde.</span></div>'
            '<section class="card" style="gap: 6px;"><h2 class="h2">Fuera de tu equipo</h2><span style="font-size: 13px; color: #33424C;">Tu distribuidor <strong>Agropecuària del Segre</strong> atiende la zona de Lleida. Se gestiona en Distribuidores, no aquí.</span><a href="#" style="font-size: 12.5px;">Ver distribuidores →</a></section></aside>')
    cab = cabecera('Equipo', 'Equipo', 'Quién gestiona la ficha de AgroExport en Agroolink y qué solicitudes atiende cada uno.')
    return pagina('Intranet empresa · Equipo', 'Equipo', cab, '<div style="display: flex; gap: 16px; align-items: flex-start;">' + tabla + lado + '</div>')

# ---------- EM7 · Estadísticas ----------
def estadisticas():
    kpi = lambda n, t, d, cls='ok': ('<div class="card" style="gap: 2px; padding: 14px 16px;"><span style="font-size: 26px; font-weight: 600;">' + n + '</span><span style="font-size: 12.5px; color: #4A5650;">' + t + '</span>'
                                    '<span class="st ' + cls + '" style="align-self: flex-start; margin-top: 4px;">' + d + '</span></div>')
    sem = [42, 55, 48, 61, 70, 66, 82, 95]
    barras = ''.join('<span style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px;"><span style="font-size: 11px; color: #56615B;">' + str(v) + '</span>'
                     '<span style="width: 100%; height: ' + str(int(v * 1.6)) + 'px; border-radius: 6px 6px 0 0; background: ' + (AZ if i == len(sem) - 1 else '#B9CCE6') + ';"></span>'
                     '<span style="font-size: 11px; color: #56615B;">S' + str(i + 35) + '</span></span>' for i, v in enumerate(sem))
    graf = ('<section class="card" style="flex: 1; min-width: 0;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 class="h2">Visitas a la ficha por semana</h2><span class="hint">últimas 8 semanas</span></div>'
            '<div style="display: flex; gap: 12px; align-items: flex-end; height: 190px; padding-top: 8px;">' + barras + '</div></section>')
    p = lambda n, v, s, b: '<div class="row"><span style="flex: 1;"><strong style="font-weight: 600;">' + n + '</strong></span><span style="width: 70px; text-align: right;">' + v + '</span><span style="width: 80px; text-align: right;">' + s + '</span><span style="width: 90px; text-align: right;" class="hint">' + b + '</span></div>'
    top = ('<section class="card" style="width: 420px; flex: none; gap: 0;"><h2 class="h2" style="padding-bottom: 8px;">Tus productos</h2>'
           '<div class="row" style="border-top: 0; font-size: 11px; font-weight: 600; letter-spacing: .04em; color: #56615B;"><span style="flex: 1;">PRODUCTO</span><span style="width: 70px; text-align: right;">VISITAS</span><span style="width: 80px; text-align: right;">SOLICITUDES</span><span style="width: 90px; text-align: right;">EN BÚSQUEDAS</span></div>' +
           p('Corrector vitamínico CV-20', '180', '6', '1.920') + p('Premezcla P-40', '74', '2', '980') + p('Acidificante AQ-7', '32', '1', '520') + '</section>')
    quien = ('<section class="card" style="gap: 8px;"><div style="display: flex; align-items: baseline; justify-content: space-between;"><h2 class="h2">Quién te visita</h2><span class="st wn">Avanzadas · con Pro</span></div>'
             '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; filter: blur(2.5px);"><span style="font-size: 13px;">Ganaderos 62 % · técnicos 21 % · integradoras 17 %</span><span style="font-size: 13px;">Cataluña 41 % · Aragón 22 % · Castilla y León 14 %</span><span style="font-size: 13px;">Avicultura 70 % · porcino 30 %</span></div>'
             '<span class="hint">Por tipo de comprador, zona y especie. Nunca se muestran nombres ni contactos de los compradores.</span></section>')
    cab = cabecera('Estadísticas', 'Estadísticas', 'Cómo te encuentran y qué piden. Plan Gratis: estadísticas básicas.',
                   '<span style="display: flex; gap: 6px;"><span class="chip">7 días</span><span class="chip on">30 días</span><span class="chip">12 meses</span></span>')
    cuerpo = ('<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px;">' + kpi('3.420', 'Apariciones en búsquedas', '+12 % vs. mes anterior') + kpi('286', 'Visitas a la ficha', '+18 %') +
              kpi('9', 'Solicitudes recibidas', '3 visibles en Gratis', 'wn') + kpi('7 h', 'Tiempo medio de respuesta', 'compromiso 24 h') + '</div>'
              '<div style="display: flex; gap: 16px;">' + graf + top + '</div>' + quien)
    return pagina('Intranet empresa · Estadísticas', 'Estadísticas', cab, cuerpo)

# ---------- EM8 · Plan y facturación ----------
def plan():
    filas = [('Solicitudes de compradores', 'De 3 compradores', 'Ilimitadas', 'Ilimitadas'), ('Productos publicados', '15', '100', 'Ilimitados'), ('Miembros del equipo', 'Ilimitados', 'Ilimitados', 'Ilimitados'),
             ('Solicitudes organizadas (estados, notas)', '—', 'Sí', 'Sí'), ('Oportunidades (proyectos)', 'Solo el número', '2 al mes', 'Ilimitadas + encaje'), ('Estadísticas', 'Básicas', 'Avanzadas', 'Avanzadas + comparativa'),
             ('Contenido vinculado', '—', '5 al mes', 'Ilimitado'), ('Destacar productos', '—', 'Extra de pago', '4 al mes'), ('Adjuntos en propuestas y mensajes', '—', '—', 'Sí · revisados'),
             ('Exportar informes de solicitudes', '—', '—', 'Sí'), ('Gestor de cuenta', '—', '—', 'Sí')]
    cols = 'grid-template-columns: minmax(0,1.6fr) repeat(3, minmax(0,1fr));'
    cab_t = lambda t, p, sub, on=False, prim=False: ('<span style="display: flex; flex-direction: column; gap: 4px; padding: 14px; border-radius: 14px; ' + ('border: 2px solid ' + AZ + '; background: #F3F7FC;' if on else 'border: 1px solid #E3E8E4; background: #FFFFFF;') + '">'
                                                   '<span style="display: flex; justify-content: space-between; align-items: center;"><strong style="font-size: 16px;">' + t + '</strong>' + ('<span class="st az">Tu plan</span>' if on else '') + '</span>'
                                                   '<span style="font-size: 20px; font-weight: 600;">' + p + '</span><span class="hint">' + sub + '</span>' +
                                                   ('' if on else '<a href="#" class="' + ('btnp' if prim else 'btn') + '" style="margin-top: 6px; height: 36px;">Pasar a ' + t.split()[-1] + '</a>') + '</span>')
    tabla = ('<section class="card" style="gap: 0;"><div style="display: grid; gap: 12px; ' + cols + ' padding-bottom: 12px;"><span></span>' +
             cab_t('Empresa Gratis', '0 €', 'Sin tarjeta', True) + cab_t('Empresa Pro', '79 €/mes', 'Sin permanencia', False, True) + cab_t('Empresa Premium', '199 €/mes', 'Sin permanencia') + '</div>' +
             ''.join('<div class="tr" style="' + cols + '"><span>' + a + '</span><span style="font-weight: 600;">' + b + '</span><span>' + c + '</span><span>' + d + '</span></div>' for a, b, c, d in filas) + '</section>')
    lado = ('<aside style="width: 300px; flex: none; display: flex; flex-direction: column; gap: 14px;">'
            '<section class="card" style="gap: 6px;"><h2 class="h2">Facturación de la empresa</h2><span style="font-size: 13px; color: #33424C;">Aún no hay facturas: estás en Empresa Gratis.</span>'
            '<div class="row"><span class="hint" style="flex: 1;">Se factura a</span><strong style="font-weight: 500; text-align: right;">AgroExport SRL<br><span class="hint">sociedad del CRM</span></strong></div>'
            '<span class="hint">Los datos fiscales vienen del CRM y solo los cambia el superadmin. <a href="#">Pedir un cambio</a></span></section>'
            '<section class="card" style="gap: 6px;"><h2 class="h2">Sucursales y filiales</h2><span style="font-size: 13px; color: #33424C;">El alta de sucursales es gratis. Para un grupo con varias, un plan de grupo a medida.</span><a href="#" style="font-size: 12.5px;">Pedir plan de grupo →</a></section>'
            '<div class="nota">' + svg(I['info'], 16) + '<span>Sin permanencia: si cancelas, sigues con el plan hasta el final del periodo pagado.</span></div></aside>')
    cab = cabecera('Plan y facturación', 'Plan y facturación', 'Qué incluye tu plan y qué ganas al cambiar. Lo que pagas a Agroolink se factura a la sociedad del CRM.')
    return pagina('Intranet empresa · Plan y facturación', 'Plan y facturación', cab, '<div style="display: flex; gap: 16px; align-items: flex-start;"><div style="flex: 1; min-width: 0;">' + tabla + '</div>' + lado + '</div>', 980)

PANT = [('EmpSolicitudes', 'EM5 · Solicitudes de la empresa: todas, quién las atiende, reasignar y lo guardado hasta Pro', solicitudes, 900),
        ('EmpEquipo', 'EM6 · Equipo: miembros sin límite, roles e invitar', equipo, 900),
        ('EmpEstadisticas', 'EM7 · Estadísticas: búsquedas, visitas, solicitudes y productos (avanzadas con Pro)', estadisticas, 900),
        ('EmpPlan', 'EM8 · Plan y facturación de la empresa: Gratis, Pro y Premium', plan, 980)]
if __name__ == '__main__':
    for k, t, f, h in PANT:
        open(DEST + k + '.dc.html', 'w').write(f())
    print('ok', len(PANT))
