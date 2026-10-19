"""Catálogos de producto en móvil (versión de 011a–011e), una pantalla por tablero, para el canvas «Agroolink · Móvil».
No repite lo que ya hay en 011_MB_Alta de producto: el menú ⋯ de un producto es ME2 y la edición por bloques ME3; «Duplicar → copia» solo se dibuja en 011a.
Sin contactos visibles: ni «Visitar su tienda», ni enlaces a tiendas, ni WhatsApp; las solicitudes llegan por Mensajes.
Uso: python3 tools/catalogos_movil.py <carpeta-movil>/project/canvas.json [clave=alto …]   → escribe los tableros, añade las páginas 011a–011e_MB y reescribe /_blob/ con tools/blobs_movil.json."""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import svg, I, wrap, W, DEST, AZ
from empresa_config_movil import card, st, btn, fila, nota, campo, chips, paso, pie, pantalla, asistente, emp, AZST, WN, GR, SOFT

OK = 'background:#EEF6EE;color:#0E5A3A'; ER = 'background:#FDECEA;color:#A3271B'
SA = '<span style="font-size:10px;font-weight:700;letter-spacing:.04em;background:#17231D;color:#FFFFFF;border-radius:999px;padding:1px 7px;margin-left:6px">SUPERADMIN</span>'
I.update({'up': 'M12 16V4M7 9l5-5 5 5M4 20h16', 'dup': 'M8 8h12v12H8zM4 16V4h12', 'eye': 'M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12zM12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6z', 'pin': 'M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z'})

def prod(code, nombre, sub, est, estilo, extra='', borde=True, bg='#E9F0F9', fg=AZ):
    return ('<div style="display:flex;gap:10px;align-items:center;padding:10px 0;' + ('border-top:1px solid #EEF1EE' if borde else '') + '">'
            '<span style="width:42px;height:42px;border-radius:10px;background:' + bg + ';color:' + fg + ';font-size:10.5px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:none">' + code + '</span>'
            '<span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:1px"><strong style="font-size:13.5px">' + nombre + '</strong><span class="hint">' + sub + '</span>' + extra + '</span>'
            '<span style="display:flex;flex-direction:column;align-items:flex-end;gap:4px">' + st(est, estilo) + '<span style="color:#56615B">' + svg(I['dots'], 18, 2.4) + '</span></span></div>')
def barra(p):
    return '<span style="display:block;width:64px;height:5px;border-radius:3px;background:#E8ECE9;overflow:hidden;margin-top:3px"><span style="display:block;width:%d%%;height:100%%;background:%s"></span></span>' % (p, AZ if p >= 80 else '#C98A12')
def buscador(t):
    return '<div style="height:44px;border:1px solid #D5DED8;border-radius:10px;background:#FFFFFF;display:flex;align-items:center;gap:8px;padding:0 12px;color:#8A948F;font-size:13.5px">' + svg(I['lupa'], 17) + t + '</div>'
def cab(eb, t, sub, acciones=''):
    return ('<div style="display:flex;align-items:flex-end;gap:10px"><span style="flex:1;min-width:0"><span class="hint" style="font-weight:600;letter-spacing:.06em">' + eb + '</span>'
            '<h1 style="margin:2px 0 0;font-size:22px;font-weight:700">' + t + '</h1></span>' + acciones + '</div>' + ('<span style="font-size:13px;color:#4A5650;margin-top:-6px">' + sub + '</span>' if sub else ''))
def nuevo_btn(t='Nuevo'):
    return btn(svg(I['mas'], 16, 2.2) + '&nbsp;' + t, True)
def aviso(t):
    return nota(t, '#FFF8EC', '#F3DFB8')
def opcion(icono, t, d, on=False, tag=''):
    return ('<div style="display:flex;gap:12px;align-items:flex-start;padding:13px 14px;border-radius:14px;' + ('border:1.5px solid ' + AZ + ';background:#F3F7FC' if on else 'border:1px solid #DCE3DE;background:#FFFFFF') + '">'
            '<span style="width:38px;height:38px;border-radius:10px;background:' + SOFT + ';color:' + AZ + ';display:flex;align-items:center;justify-content:center;flex:none">' + svg(I[icono], 18, 2) + '</span>'
            '<span style="flex:1;display:flex;flex-direction:column;gap:3px"><strong style="font-size:14px">' + t + tag + '</strong><span style="font-size:12.5px;color:#4A5650;line-height:1.35">' + d + '</span></span>'
            '<span style="width:20px;height:20px;border-radius:50%;border:1.5px solid ' + (AZ if on else '#C9D2CC') + ';flex:none;display:flex;align-items:center;justify-content:center;margin-top:2px">' + ('<span style="width:10px;height:10px;border-radius:50%;background:' + AZ + '"></span>' if on else '') + '</span></div>')
def pasos_publicar(lista):
    return card('Qué pasa al publicarlo', ''.join('<div style="display:flex;gap:10px;font-size:12.5px;line-height:1.38"><span style="width:22px;height:22px;border-radius:50%;background:' + AZ + ';color:#FFFFFF;font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none">' + str(i + 1) + '</span><span>' + t + '</span></div>' for i, t in enumerate(lista)))
def vista_comprador(t, quien, sub, cta, extra=''):
    return card('Así lo ve el comprador', '<div style="border-radius:14px;background:#EAF1FA;padding:8px;display:flex;flex-direction:column;gap:8px"><span style="display:flex;gap:6px;align-items:center;font-size:12.5px;font-weight:600;color:' + AZ + '">' + svg(I['pin'], 15) + t + '</span>'
                '<div style="background:#FFFFFF;border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:8px"><span style="display:flex;gap:8px;align-items:center">' + emp(quien[:2].upper(), AZ, 34) + '<span style="font-size:12px"><strong>' + quien + '</strong><br><span style="color:' + AZ + '">● ' + sub + '</span></span></span>'
                '<span class="btnp" style="background:' + AZ + ';height:38px">' + cta + '</span></div></div>' + extra + '<span class="hint">Sin teléfonos, emails ni webs: la solicitud llega por Mensajes.</span>')
def ficha_cab(code, nombre, sub, est='Publicado', pct=None):
    return ('<div style="display:flex;gap:12px;align-items:center"><span style="width:50px;height:50px;border-radius:12px;background:#FFF6DD;border:1px solid #EAD9A6;color:#7A4B00;font-size:10.5px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:none">' + code + '</span>'
            '<span style="flex:1;min-width:0"><span style="display:flex;gap:8px;align-items:center"><strong style="font-size:18px">' + nombre + '</strong>' + st(est, OK) + '</span><span class="hint">' + sub + '</span>' +
            ('<span style="display:flex;gap:8px;align-items:center;font-size:11.5px;color:#4A5650"><strong style="color:#17231D">' + str(pct) + ' %</strong> completa ' + barra(pct) + '</span>' if pct else '') + '</span></div>')
def tabs(lista, on):
    return '<div style="display:flex;gap:18px;border-bottom:1px solid #E3E8E4;font-size:13px;color:#56615B;white-space:nowrap;overflow:hidden">' + ''.join('<span style="padding-bottom:9px;%s">%s</span>' % ('color:' + AZ + ';font-weight:600;border-bottom:2px solid ' + AZ + ';margin-bottom:-1px' if t == on else '', t) for t in lista) + '</div>'
def pais(cod, t, d, est, estilo, borde=True):
    return fila('<span style="width:30px;height:20px;border-radius:4px;background:#EEF1EE;font-size:10px;font-weight:700;color:#2F3D36;display:flex;align-items:center;justify-content:center;flex:none">' + cod + '</span>', t, d, st(est, estilo), borde)
def guardar_pie(t='Guardar cambios'):
    return '<div class="foot" style="bottom:84px;padding-bottom:10px">' + btn('Vista previa') + '<span class="btnp" style="flex:1;height:44px;background:' + AZ + '">' + t + '</span></div>'
P = lambda b, foot='', av='ML': pantalla(b, tab='Productos', foot=foot, avatar=av, pad=180 if foot else 110)

# ---------- 011a · Fabricante con distribuidores (DSM-Firmenich) ----------
def a_catalogo():
    b = (cab('MÓDULO PRODUCTOS', 'Catálogo', 'Una ficha base por producto; tus distribuidores la usan para su versión local.', nuevo_btn()) +
         tabs(['Catálogo 248', 'Acuerdos 4', 'Importaciones'], 'Catálogo 248') + buscador('Nombre, referencia o principio activo') +
         chips(['Todos 248', 'Publicados 212', 'Borradores 23', 'Con avisos 13']) +
         card('', prod('HYD', 'Hy-D®', 'Vitaminas · 14 países · 22 distribuidores', 'Publicado', OK, barra(96), False) +
              prod('ROV', 'Rovabio® Advance', 'Enzimas · 18 países · 25 distribuidores', 'Publicado', OK, barra(90)) +
              prod('RHP', 'Ronozyme® HiPhos', 'Falta ficha técnica en PT', 'Con avisos', WN, barra(74)) +
              prod('BAL', 'Balancius™', 'Sin distribuidor en 6 países', 'Borrador', GR, barra(62)) +
              prod('VER', 'Veramaris® Oil', 'Faltan imágenes', 'Borrador', GR, barra(55))) +
         '<span class="hint" style="text-align:center">1–5 de 248 · ordenado por completitud. El menú ⋯ de cada producto es el de ME2 (Editar, Duplicar, Ocultar, Archivar).</span>')
    return P(b)
def a_copia():
    b = (cab('MÓDULO PRODUCTOS', 'Catálogo', '') +
         '<div class="card" style="flex-direction:row;align-items:center;gap:10px;background:#EEF6EE;border-color:#CFE5D3"><span style="color:#0E5A3A">' + svg(I['dup'], 20) + '</span><span style="flex:1;font-size:13px"><strong>Borrador creado:</strong> «Rovabio® Advance (copia)». Cambia lo que necesites.</span></div>' +
         btn('Editar la copia', True) +
         card('', prod('ROV', 'Rovabio® Advance (copia)', 'Enzimas · 18 países · 25 distribuidores', 'Borrador', GR, barra(90), False, '#FFF4E0', '#7A4B00') +
              prod('HYD', 'Hy-D®', 'Vitaminas · 14 países', 'Publicado', OK, barra(96)) + prod('ROV', 'Rovabio® Advance', 'Enzimas · 18 países', 'Publicado', OK, barra(90))) +
         '<span class="hint">La copia sale arriba del catálogo hasta que la publiques. Igual en 011b (Zucami).</span>')
    return P(b)
def a_nuevo():
    b = (paso('Módulo productos · nuevo', 'Añadir un producto', 'Una ficha base por producto, común a todos los países.') +
         opcion('mas', 'Crear la ficha paso a paso', 'General, variantes, beneficios, especificaciones, documentación y mercados. Puedes guardarla como borrador.', True, ' ' + st('Recomendado', AZST)) +
         opcion('up', 'Importar desde Excel', 'Para muchos productos a la vez. Si la referencia ya existe, se actualiza.', False, SA) +
         opcion('dup', 'Duplicar un producto parecido', 'Por ejemplo, copia Rovabio® Advance y cambia lo que haga falta.') +
         pasos_publicar(['La ficha base se publica en los países donde la tengas registrada.', 'Tus distribuidores con <strong>acuerdo en esa línea y zona</strong> la reciben y añaden su versión local.', 'El comprador ve <strong>«¿Dónde comprar?»</strong> con el distribuidor de su zona.']))
    return asistente(b, pie('Continuar', 'Cancelar'))
def a_importar():
    b = (cab('MÓDULO PRODUCTOS', 'Importaciones' + SA, 'Carga masiva del catálogo; actualiza por referencia.') +
         '<div style="display:flex;gap:6px;font-size:12px;color:#56615B"><span style="color:' + AZ + ';font-weight:600">✓ Archivo</span>·<span style="color:' + AZ + ';font-weight:600">✓ Columnas</span>·<strong style="color:' + AZ + '">3 Revisar</strong>·<span>4 Importar</span></div>' +
         card('', fila('<span style="width:38px;height:38px;border-radius:10px;background:#E8F0F9;color:#1D6B3F;font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center">XLS</span>', 'catalogo_dsm_2026.xlsx', '248 filas · plantilla de Agroolink', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Cambiar</span>', False)) +
         card('Cómo se cruzan los datos', '<span style="font-size:13px">● <strong>Actualizar por referencia</strong> <span class="hint">· si existe se actualiza; si no, se crea</span></span><span style="font-size:13px;color:#4A5650">○ Crear todos como nuevos</span><span style="font-size:13px">☑ Las celdas vacías no borran lo que ya hay</span>') +
         card('Resultado de la revisión', fila(st('230', OK), 'Listos para importar', '', '', False) + fila(st('12', WN), 'Con avisos', 'Faltan imágenes', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Ver</span>') +
              fila(st('6', ER), 'No se importan', 'Línea no reconocida', '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">Corregir</span>')) +
         card('Imágenes y documentos', '<span class="hint">Un ZIP con los archivos nombrados por referencia (HYD-25_1.jpg, HYD-25_ficha_ES.pdf). Se revisan al subirlos: sin teléfonos, emails ni webs.</span>' + btn(svg(I['up'], 16) + '&nbsp;Subir ZIP')))
    return P(b, guardar_pie('Importar 242 productos'))
def a_mercados():
    b = (ficha_cab('Hy-D®', 'Hy-D®', 'Ref. HYD-25 · Vitaminas · ficha base', pct=96) +
         nota('<strong>Ficha base:</strong> la usan tus distribuidores en 14 países. Al guardar, los cambios llegan a sus versiones locales.') +
         tabs(['General', 'Especificaciones', 'Documentación', 'Mercados y dónde comprar'], 'Mercados y dónde comprar') +
         chips(['14 países', '22 distribuidores', '2 sin distribuidor'], (0,)) +
         card('', pais('ES', 'España', 'NutriGan · Zona Centro, AgroVet · Aragón, +2', 'Sincronizada', OK, False) + pais('PT', 'Portugal', 'PortuNutri Lda · todo el país', 'Cambios locales', WN) +
              pais('FR', 'Francia', 'NutriFrance · todo el país', 'Sincronizada', OK) + pais('MA', 'Marruecos', 'Sin distribuidor', 'Registrado', GR) + pais('MX', 'México', 'Sin distribuidor · registro en trámite', 'En trámite', WN) +
              '<span class="hint">Los distribuidores llegan de tus acuerdos por línea y zona. <span style="color:' + AZ + ';font-weight:600">+ Excepción solo para este producto</span></span>') +
         card('Si no hay distribuidor en el país del comprador', '<span style="font-size:13px">☑ Contactar con DSM-Firmenich <span class="hint">· llega a Desarrollo de negocio</span></span><span style="font-size:13px">☑ Solicitar ser distribuidor</span><span style="font-size:13px">☑ Avisarme cuando haya disponibilidad</span>') +
         vista_comprador('Disponible en España · comprador en Madrid', 'NutriGan Distribuciones', 'Distribuidor autorizado · Zona Centro', 'Contactar con NutriGan'))
    return P(b, guardar_pie())
def a_acuerdos():
    ac = lambda ini, t, z, l, n, est, estilo, borde=True: fila(emp(ini, AZ, 36), t, z + ' · ' + l, '<span style="display:flex;flex-direction:column;align-items:flex-end;gap:3px"><strong style="font-size:13px">' + n + '</strong>' + st(est, estilo) + '</span>', borde)
    b = (cab('MÓDULO PRODUCTOS', 'Acuerdos de distribución', '', nuevo_btn()) +
         nota('Con catálogos grandes, asigna distribuidores <strong>por línea y zona</strong>, no producto a producto. Cada ficha recibe sus distribuidores de aquí.') +
         card('4 acuerdos · 1 por validar', ac('NG', 'NutriGan Distribuciones', 'España › Zona Centro', 'Vitaminas, Enzimas', '58', 'Activo', OK, False) + ac('AI', 'AgroVet Ibérica', 'Aragón, Navarra, La Rioja', 'Todo aves', '96', 'Activo', OK) +
              ac('PL', 'PortuNutri Lda', 'Portugal', 'Todo el catálogo', '248', 'Activo', OK) + ac('NF', 'NewFarms', 'España, Portugal', 'Añadió 3 productos', '3', 'Por validar', WN)))
    return P(b)
def a_acuerdo():
    b = ('<div style="display:flex;gap:10px;align-items:center">' + emp('NG', AZ, 44) + '<span style="flex:1"><strong style="font-size:17px">NutriGan Distribuciones</strong><br><span class="hint">Distribuidor autorizado desde mar 2025</span></span>' + st('Activo', OK) + '</div>' +
         card('Zona · el comprador ve a NutriGan si está aquí', chips(['España', 'Madrid ×', 'Toledo ×', 'Guadalajara ×', 'Cuenca ×', 'Ciudad Real ×', '+2'], (0,)) + '<span style="font-size:12.5px;color:' + AZ + ';font-weight:600">+ Provincia</span>') +
         card('Productos del acuerdo', '<span class="hint">Por regla: los productos nuevos que la cumplan se añaden solos</span>' + fila('', 'Líneas', 'Vitaminas · Enzimas', '', False) + fila('', 'Especies', 'Aves · Porcino') + fila('', 'Excepto', 'Balancius™') +
              '<span style="font-size:13px"><strong>= 58 productos hoy</strong> · <span style="color:' + AZ + ';font-weight:600">ver lista</span></span>') +
         card('', fila('', 'Recibe las solicitudes', 'Laura García · técnico-comercial · no se muestra al comprador', '', False) + fila('', 'Puede crear su versión local', 'Sí') + fila('', 'Exclusiva en esta zona', 'No · solo administradores de la Sede')))
    return pantalla(b, ('NutriGan Distribuciones', 'Acuerdo de distribución'), tab='Productos', foot=guardar_pie('Guardar acuerdo'), avatar='ML', pad=180)

# ---------- 011b · Fabricante con comerciales (Zucami) ----------
def c_catalogo():
    b = (cab('MÓDULO PRODUCTOS', 'Catálogo', 'Sin distribuidores: cada solicitud llega por Agroolink al comercial de la zona del comprador.', nuevo_btn()) +
         aviso('<strong>Portugal no tiene comercial:</strong> sus solicitudes llegan a la oficina comercial de Valladolid. <span style="color:' + AZ + ';font-weight:600">Asignar comercial →</span>') +
         buscador('Nombre o referencia') + chips(['Todos 36', 'Publicados 31', 'Borradores 3', 'Con avisos 2']) +
         card('', prod('ZAP', 'Zucami Aviary Pro', 'Aviarios · ES FR PT · comercial de la zona · 14 solicitudes', 'Publicado', OK, barra(94), False) +
              prod('ZNP', 'Zucami Nest Pro', 'Nidales · ES FR PT · 9 solicitudes', 'Publicado', OK, barra(91)) +
              prod('ZEF', 'Zucami EggFlow', 'Recogida de huevos · especialista: Javier Ruiz', 'Publicado', OK, barra(85)) +
              prod('ZFL', 'Zucami FeedLine', 'Falta ficha técnica', 'Con avisos', WN, barra(76)) + prod('ZCL', 'Zucami ClimaLine', 'Sin mercados', 'Borrador', GR, barra(48))))
    return P(b, av='JO')
def c_nuevo():
    b = (paso('Módulo productos · nuevo', 'Añadir un producto', 'Cada solicitud llega al comercial de la zona del comprador.') +
         opcion('mas', 'Crear la ficha paso a paso', 'General, variantes, beneficios, especificaciones, documentación y mercados.', True, ' ' + st('Recomendado', AZST)) +
         opcion('up', 'Importar desde Excel', 'Para muchos productos a la vez. Si la referencia ya existe, se actualiza.', False, SA) +
         opcion('dup', 'Duplicar un producto parecido', 'Por ejemplo, copia Zucami Nest Pro y cambia lo que haga falta.') +
         pasos_publicar(['El producto se publica en tus mercados.', 'Cada solicitud llega por Agroolink al <strong>comercial de la zona</strong> del comprador. El comprador no ve sus datos.', 'Si lo lleva un especialista, lo indicas en «Quién lo atiende» solo para este producto.']))
    return asistente(b, pie('Continuar', 'Cancelar'))
def c_mercados():
    z = lambda cod, t, quien, est, estilo, borde=True: pais(cod, t, quien, est, estilo, borde)
    b = (ficha_cab('ZAP', 'Zucami Aviary Pro', 'Ref. ZAP-01 · Aviarios', pct=94) +
         nota('Sin distribuidores: las solicitudes llegan a tu equipo comercial según la zona del comprador.') +
         tabs(['General', 'Especificaciones', 'Documentación', 'Mercados y quién lo atiende'], 'Mercados y quién lo atiende') +
         card('', z('ES', 'Cataluña, Navarra, País Vasco, Aragón', 'Laura García · aviarios', 'Activo', OK, False) + z('ES', 'Teruel, C. Valenciana', 'Javier Ruiz', 'Activo', OK) +
              z('ES', 'Castilla y León, Madrid', 'Pedro Lima · sin cuenta', 'Por email', AZST) + z('ES', 'Andalucía, Murcia', 'Ana Torres', 'Activo', OK) + z('FR', 'Francia', 'Marc Dubois', 'Activo', OK) +
              z('PT', 'Portugal', 'Sin comercial', '—', GR) + '<span class="hint">El reparto viene de tu equipo comercial (zona y línea). <span style="color:' + AZ + ';font-weight:600">+ Especialista solo para este producto</span></span>') +
         card('Si no hay comercial en la zona', '<span style="font-size:13px">● Llega a la oficina comercial · Valladolid</span><span style="font-size:13px">☑ Avisar al comercial en la app y por email · no se muestra al comprador</span><span style="font-size:13px">☑ Copia al responsable comercial</span>') +
         vista_comprador('Disponible en Cataluña · comprador en Lleida', 'Equipo comercial de Zucami', 'Te atiende el comercial de tu zona', 'Contactar con Zucami'))
    return P(b, guardar_pie(), av='JO')

# ---------- 011c · Sede con sucursales (Big Dutchman) ----------
def b_catalogo():
    b = (cab('MÓDULO PRODUCTOS', 'Catálogo de la Sede', 'Tú creas la ficha base; cada sucursal la activa en sus países.', nuevo_btn()) +
         aviso('<strong>BD DrinkTech</strong> se envió a las 6 sucursales hace 2 días y ninguna lo ha activado. <span style="color:' + AZ + ';font-weight:600">Recordar →</span>') +
         tabs(['Catálogo 64', 'Activación · 9', 'Importaciones'], 'Catálogo 64') + buscador('Nombre o referencia') +
         card('', prod('BDA', 'BD Aviary Pro', 'Activado en 5 de 6 · falta LATAM · 2 con cambios', 'Publicado', OK, barra(92), False) +
              prod('BDC', 'BD Aviary Compact', 'Activado en 6 de 6 · 1 con cambios', 'Publicado', OK, barra(89)) +
              prod('BDF', 'BD FeedLine', 'Falta vídeo · 3 de 6', 'Con avisos', WN, barra(78)) +
              prod('BDD', 'BD DrinkTech', '0 de 6 · enviado hace 2 días', 'Pendiente', WN, barra(84)) + prod('BDK', 'BD ClimaKit', 'Faltan imágenes', 'Borrador', GR, barra(52))))
    return P(b, av='AB')
def b_nuevo():
    b = (paso('Módulo productos · nuevo', 'Añadir un producto', 'La Sede crea la ficha base. Cada sucursal la activa en sus países y añade su versión local.') +
         opcion('mas', 'Crear la ficha base', 'Nombre, fotos, variantes, especificaciones y documentación. Es la misma para todas las sucursales.', True, ' ' + st('Solo la Sede', AZST)) +
         opcion('up', 'Importar desde Excel', 'Para todo el catálogo. Si la referencia ya existe, se actualiza.', False, SA) +
         opcion('dup', 'Duplicar un producto parecido', 'Por ejemplo, copia BD Aviary Compact.') +
         pasos_publicar(['La ficha base llega a tus 6 sucursales como «Pendiente de activar».', 'Cada sucursal la activa en sus países y adapta precio, plazo, documentos y contacto.', 'El comprador ve «Contactar» con la sucursal de su país; si ninguna lo vende, llega a la Sede.']) +
         nota('Las sucursales no cambian la ficha base: si ven un error, avisan a la Sede.'))
    return asistente(b, pie('Continuar', 'Cancelar'))
def b_mercados():
    b = (ficha_cab('BD', 'BD Aviary Pro', 'Ref. BDA-PRO · Aviarios · ficha base de la Sede', pct=92) +
         tabs(['General', 'Especificaciones', 'Mercados y quién lo vende'], 'Mercados y quién lo vende') + chips(['40 países', '5 sucursales', '1 pendiente'], (0,)) +
         card('', pais('DE', 'Alemania, Austria, Suiza', 'Sede global · Vechta', 'Ficha base', AZST, False) + pais('NL', 'Benelux, Polonia', 'Big Dutchman Europe', 'Sincronizada', OK) +
              pais('US', 'EE. UU., Canadá', 'Big Dutchman USA', 'Cambios locales', WN) + pais('MX', 'México, Centroamérica', 'Big Dutchman México', 'Cambios locales', WN) +
              pais('BR', 'Brasil, Colombia, Perú', 'Big Dutchman LATAM', 'Pendiente', WN) + pais('CN', 'China, Vietnam, Tailandia', 'Asia · sin administrador: lo atiende la Sede', 'Sede', GR)) +
         card('Si la sucursal del país no lo activa', '<span style="font-size:13px">● Lo atiende la Sede · el comprador ve «Contactar con Big Dutchman»</span><span style="font-size:13px">☑ Recordar a la sucursal cada 7 días</span><span style="font-size:13px;color:#4A5650">☐ Ocultar el producto en esos países</span>') +
         vista_comprador('Disponible en México · comprador en Querétaro', 'Big Dutchman México', 'Sucursal oficial · Querétaro', 'Contactar con Big Dutchman México'))
    return P(b, guardar_pie(), av='AB')
def b_activacion():
    m = {'✓': ('✓', OK), 'C': ('Cambios', WN), 'P': ('Pendiente', WN), 'N': ('No lo vende', GR), 'S': ('Sede', AZST)}
    filas = [('BD Aviary Pro', 'S ✓ ✓ C C P'), ('BD Nest Pro', '✓ ✓ ✓ N P S'), ('BD FeedLine', '✓ ✓ N P N S'), ('BD DrinkTech', '✓ P P P P S')]
    suc = ['Sede', 'Europe', 'USA', 'México', 'LATAM', 'Asia']
    b = (cab('MÓDULO PRODUCTOS', 'Activación por sucursal', 'Qué ha activado cada sucursal en sus países.') + buscador('Producto') + chips(['Todas', 'Solo pendientes'], (1,)) +
         ''.join(card(p, '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">' + ''.join('<span style="display:flex;flex-direction:column;gap:2px;font-size:11px;color:#56615B">' + s + st(*m[v]) + '</span>' for s, v in zip(suc, cs.split())) + '</div>') for p, cs in filas) +
         card('9 activaciones pendientes', '<span class="hint">En 5 sucursales; cada una recibe un aviso con su lista.</span>' + btn('Recordar a las sucursales', True)))
    return P(b, av='AB')
def b_local():
    b = (ficha_cab('BD', 'BD Aviary Pro', 'Versión de México · de la Sede · Aviarios', 'Activado') +
         nota('Sincronizada con la ficha base. Último cambio de la Sede hace 3 días: nuevas fotos del modelo 2027.') +
         card('Lo que adaptas en tu país', campo('Precio orientativo', 'Desde 38 USD por ave alojada', 'opcional') + campo('Plazo de entrega', '10–12 semanas desde Querétaro') +
              campo('Descripción para México', 'Aviario de varios pisos para ponedoras, con recogida automática de huevo…') + '<span style="font-size:12.5px;font-weight:600">Países donde lo activas</span>' + chips(['México', 'Guatemala', 'Honduras', 'El Salvador', '+ País'], (0, 1, 2, 3)) +
              '<span style="font-size:12.5px;font-weight:600">Documentos locales</span>' + chips(['Certificado NOM.pdf', 'Garantía México.pdf', '+ Añadir'], ()) + fila('', 'Recibe las solicitudes', 'Equipo comercial México · 3 personas · no se muestra al comprador', '')) +
         card('Viene de la Sede · no lo editas', '<span class="hint">Nombre, fotos y vídeo · variantes · especificaciones · ficha técnica</span><span style="font-size:12.5px;color:' + AZ + ';font-weight:600">¿Ves un error? Avisa a la Sede</span>'))
    return pantalla(b, ('BD Aviary Pro · México', 'Productos de la Sede'), tab='Productos', foot=guardar_pie('Guardar versión local'), avatar='CM', pad=180)

# ---------- 011d · Sucursal de un grupo (Aviagen Ibérica) ----------
def p_catalogo():
    b = (cab('MÓDULO PRODUCTOS', 'Catálogo', 'Viene de la Sede (Aviagen). Actívalo en tus países y añade lo de España y Portugal.', nuevo_btn('Añadir')) +
         aviso('La Sede ha añadido <strong>3 productos</strong>. Hasta que los actives no se ven en España ni Portugal; sus solicitudes llegan a la Sede. <span style="color:' + AZ + ';font-weight:600">Revisar →</span>') +
         chips(['Todos 20', 'Activados 15', 'Pendientes 3', 'Locales 2']) +
         card('', prod('308', 'Ross 308', 'De la Sede · ES PT · cambios locales · 12 solicitudes', 'Activado', OK, '', False) + prod('708', 'Ross 708', 'De la Sede · ES PT · sincronizada', 'Activado', OK) +
              prod('IR', 'Indian River', 'De la Sede · nuevo', 'Pendiente', WN) + prod('RG', 'Ranger Gold™', 'De la Sede · nuevo · crecimiento lento', 'Pendiente', WN) +
              prod('LOC', 'Ross 308 · incubadora local', 'Producto local · ES · 4 solicitudes', 'Publicado', OK, '', True, '#EEF6EE', '#0E5A3A')))
    return P(b, av='PR')
def p_nuevo():
    b = (paso('Módulo productos · nuevo', 'Añadir un producto', 'Lo normal es activar los de la Sede. Si en tu país vendes algo propio, puedes crearlo.') +
         opcion('ok', 'Activar productos de la Sede', 'Eliges cuáles vendes en España y Portugal y adaptas su versión local. La ficha base no se toca.', True, ' ' + st('Lo normal', AZST)) +
         opcion('mas', 'Crear un producto local', 'Solo para tus países, con la marca Aviagen. La Sede recibe un aviso y lo ve en su catálogo.') +
         opcion('send', 'Pedir a la Sede un producto nuevo', 'Si es para todo el grupo, que lo cree la Sede. Le llega tu propuesta por Mensajes.') +
         pasos_publicar(['Lo activado se ve en tus países con tu versión local.', 'Los productos locales se publican al momento; la Sede y el superadmin reciben un aviso.', 'El comprador ve «Contactar con Aviagen Ibérica»; la solicitud llega a tu equipo por Agroolink.']))
    return asistente(b, pie('Continuar', 'Cancelar'))
def p_local():
    b = (ficha_cab('308', 'Ross 308', 'Versión Ibérica · de la Sede · reproductora broiler', 'Activado') +
         nota('Sincronizada con la ficha de la Sede. Último cambio hace 5 días: nuevos objetivos de rendimiento 2027.') +
         card('Lo que adaptas en tu zona', campo('Disponibilidad', 'Pedidos con 12 semanas de antelación') + campo('Entrega', 'Desde incubadora en España') +
              campo('Descripción en portugués', 'Reprodutora broiler com excelente conversão alimentar…', 'la Sede la tiene en inglés y español') +
              '<span style="font-size:12.5px;font-weight:600">Países donde lo activas</span>' + chips(['España', 'Portugal'], (0, 1)) +
              '<span style="font-size:12.5px;font-weight:600">Documentos locales</span>' + chips(['Certificado sanitario ES.pdf', 'Guia de maneio PT.pdf', '+ Añadir'], ()) +
              fila('', 'Recibe las solicitudes', 'Equipo comercial Ibérica · 4 personas · no se muestra al comprador', '')) +
         card('Viene de la Sede · no lo editas', '<span class="hint">Nombre, fotos y vídeo · objetivos de rendimiento · guía de manejo · especificaciones</span><span style="font-size:12.5px;color:' + AZ + ';font-weight:600">¿Ves un error? Avisa a la Sede</span>'))
    return pantalla(b, ('Ross 308 · Ibérica', 'Productos de la Sede'), tab='Productos', foot=guardar_pie('Guardar versión local'), avatar='PR', pad=180)

# ---------- 011e · Distribuidor multimarca (NewFarms) ----------
def d_catalogo():
    b = (cab('MÓDULO PRODUCTOS', 'Catálogo', 'Productos de las marcas que distribuyes y los tuyos.', nuevo_btn('Añadir')) +
         aviso('<strong>3 productos de Zucami</strong> esperan la validación de la marca. Mientras, se ven como «Distribuido» sin el sello de distribuidor autorizado.') +
         chips(['Todos 95', 'De marcas 37', 'Subidos 46', 'Propios 12']) +
         card('', prod('HYD', 'Hy-D®', 'DSM-Firmenich · ficha oficial · ES PT · 8 solicitudes', 'Validado', OK, '', False) +
              prod('ZAP', 'Zucami Aviary Pro', 'Zucami · ficha oficial · ES PT', 'Pendiente', WN) +
              prod('FMX', 'Comedero Feedmax', 'Roxell (no está en Agroolink) · subida por ti', 'Subida', GR) +
              prod('NFP', 'NewFarms Premix Porcino', 'Marca propia · ES PT CL PE · 6 solicitudes', 'Propio', AZST, '', True, '#EEF6EE', '#0E5A3A') +
              prod('NFC', 'NewFarms Corrector Ovino', 'Faltan imágenes', 'Borrador', GR, '', True, '#EEF6EE', '#0E5A3A')))
    return P(b, av='LG')
def d_nuevo():
    b = (paso('Módulo productos · nuevo', 'Añadir un producto', 'Tu catálogo mezcla productos de las marcas que distribuyes y, si los tienes, los tuyos.') +
         opcion('lupa', 'Elegir de una marca que está en Agroolink', 'Usas la ficha oficial: no la editas, añades tu versión local. La marca recibe un aviso para validarte.', True, ' ' + st('Lo más rápido', AZST)) +
         opcion('up', 'Subir un producto de una marca que no está', 'Creas la ficha tú. Si la marca llega a Agroolink, puede reclamarla.') +
         opcion('mas', 'Producto de marca propia', 'Tus productos con la marca NewFarms. Ficha completa, como un fabricante.') +
         pasos_publicar(['Entra en tu catálogo como «Distribuido» (o «Propio»).', 'Eliges en qué zonas lo vendes y quién lo atiende.', 'La marca te ve en su «¿Dónde comprar?» cuando valida el acuerdo.']) +
         nota('Elegir y subir están en 005d_MB · Distribuidor (X3 y X4).'))
    return asistente(b, pie('Continuar', 'Cancelar'))
def d_local():
    b = (ficha_cab('HYD', 'Hy-D®', 'Tu versión local · de DSM-Firmenich · ES y PT', 'Publicada') +
         nota('Sincronizada con la ficha de DSM-Firmenich. Último cambio de la marca hace 3 días: nueva ficha técnica en francés.') +
         card('Lo que puedes adaptar', campo('Descripción corta en portugués', 'Fonte de 25-OH-D3 com melhor absorção…', 'la marca la tiene en ES, EN y FR') +
              '<span style="font-size:12.5px;font-weight:600">Presentaciones que vendes</span>' + chips(['✓ Saco 25 kg', '✓ Big bag 500 kg', 'Saco 5 kg · no'], (0, 1)) +
              '<span style="font-size:12.5px;font-weight:600">Documentos locales</span>' + chips(['Certificado de registro PT.pdf', '+ Añadir'], ()) +
              fila('', 'Recibe las solicitudes', 'Laura García · técnico-comercial · no se muestra al comprador', '')) +
         card('Viene de DSM-Firmenich · no lo editas', '<span class="hint">Nombre, subtítulo y galería · beneficios y aplicación · especificaciones y ficha técnica</span><span style="font-size:12.5px;color:' + AZ + ';font-weight:600">¿Ves un error? Avisa a la marca</span>') +
         vista_comprador('Disponible a través de NewFarms', 'NewFarms', 'Distribuidor autorizado · España, Portugal', 'Solicitar información a NewFarms'))
    return pantalla(b, ('Hy-D® · versión local', 'Productos · de DSM-Firmenich'), tab='Productos', foot=guardar_pie('Guardar versión local'), avatar='LG', pad=180)

PAGINAS = [('cat11a', '011a_MB_Productos · Fabricante con distribuidores (DSM-Firmenich)', 'Catálogo del fabricante con distribuidores en móvil · el menú ⋯ es ME2 (011_MB) · tools/catalogos_movil.py',
            [('MB_CatFab_Catalogo', 'PA1 · Catálogo', a_catalogo), ('MB_CatFab_Copia', 'PA1c · Tras «Duplicar»: la copia', a_copia), ('MB_CatFab_Nuevo', 'PA2 · Nuevo producto', a_nuevo),
             ('MB_CatFab_Importar', 'PA3 · Importaciones (superadmin)', a_importar), ('MB_CatFab_Mercados', 'PA4 · Mercados y dónde comprar', a_mercados),
             ('MB_CatFab_Acuerdos', 'PA5 · Acuerdos de distribución', a_acuerdos), ('MB_CatFab_Acuerdo', 'PA5b · Un acuerdo: zona y productos', a_acuerdo)]),
           ('cat11b', '011b_MB_Productos · Fabricante con comerciales (Zucami)', 'Catálogo del fabricante con comerciales · menú ⋯ y copia como en 011a',
            [('MB_CatCom_Catalogo', 'PC1 · Catálogo y quién lo atiende', c_catalogo), ('MB_CatCom_Nuevo', 'PC2 · Nuevo producto', c_nuevo), ('MB_CatCom_Mercados', 'PC3 · Mercados y quién lo atiende', c_mercados)]),
           ('cat11c', '011c_MB_Productos · Sede con sucursales (Big Dutchman)', 'Catálogo de la Sede y versión local de una sucursal',
            [('MB_CatSede_Catalogo', 'PB1 · Catálogo de la Sede', b_catalogo), ('MB_CatSede_Nuevo', 'PB2 · Nuevo: la ficha base', b_nuevo), ('MB_CatSede_Mercados', 'PB3 · Mercados y quién lo vende', b_mercados),
             ('MB_CatSede_Activacion', 'PB4 · Activación por sucursal', b_activacion), ('MB_CatSede_Local', 'PB5 · Versión local de México', b_local)]),
           ('cat11d', '011d_MB_Productos · Sucursal de un grupo (Aviagen Ibérica)', 'Catálogo de la sucursal: lo de la Sede y lo local',
            [('MB_CatSuc_Catalogo', 'PS1 · Catálogo de la sucursal', p_catalogo), ('MB_CatSuc_Nuevo', 'PS2 · Añadir: activar, local o pedir', p_nuevo), ('MB_CatSuc_Local', 'PS3 · Versión local (Ross 308)', p_local)]),
           ('cat11e', '011e_MB_Productos · Distribuidor multimarca (NewFarms)', 'Catálogo del distribuidor: marcas, subidos y propios',
            [('MB_CatDis_Catalogo', 'PD1 · Catálogo', d_catalogo), ('MB_CatDis_Nuevo', 'PD2 · Añadir producto', d_nuevo), ('MB_CatDis_Local', 'PD3 · Versión local (Hy-D®)', d_local)])]
ALTOS = {'MB_CatFab_Catalogo': 980, 'MB_CatFab_Copia': 844, 'MB_CatFab_Nuevo': 900, 'MB_CatFab_Importar': 1040, 'MB_CatFab_Mercados': 1350, 'MB_CatFab_Acuerdos': 844, 'MB_CatFab_Acuerdo': 1110, 'MB_CatCom_Catalogo': 980, 'MB_CatCom_Nuevo': 890, 'MB_CatCom_Mercados': 1330, 'MB_CatSede_Catalogo': 930, 'MB_CatSede_Nuevo': 920, 'MB_CatSede_Mercados': 1280, 'MB_CatSede_Activacion': 1130, 'MB_CatSede_Local': 1120, 'MB_CatSuc_Catalogo': 910, 'MB_CatSuc_Nuevo': 930, 'MB_CatSuc_Local': 1100, 'MB_CatDis_Catalogo': 900, 'MB_CatDis_Nuevo': 990, 'MB_CatDis_Local': 1220}   # medidas en el navegador
if __name__ == '__main__':
    alto = dict(ALTOS, **{k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    BLOBS = json.load(open(W + '/tools/blobs_movil.json'))
    c = json.load(open(sys.argv[1])); B = c['boards']; nuevos = []
    ids = [p['id'] for p in c['pages']]
    pos = ids.index('mb1') + 1 if 'mb1' in ids else len(ids)
    for n, (pid, nombre, tit, pant) in enumerate(PAGINAS):
        if pid not in ids: c['pages'].insert(pos + n, {'id': pid, 'name': nombre})
        c['notes']['t_' + pid] = {'kind': 'title1', 'maxW': 3600, 'page': pid, 'w': 240, 'x': 0, 'y': -300, 'text': tit}
        for i, (k, t, f) in enumerate(pant):
            h = int(alto.get(k, 1100))
            html = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: '/_blob/' + BLOBS.get(m.group(1), m.group(1)), wrap('Móvil · ' + t, h, f()))
            open(DEST + k + '.dc.html', 'w').write(html)
            B[k + '.dc.html'] = {'w': 390, 'h': h, 'page': pid, 'x': i * 470, 'y': 0, 'title': t}
            if k + '.dc.html' not in c['order']: c['order'].append(k + '.dc.html')
            nuevos.append(k + '.dc.html')
    json.dump(c, open(sys.argv[1], 'w'), ensure_ascii=False, indent=1)
    json.dump(nuevos, open(DEST + '../nuevos.json', 'w'))
    print('ok', len(nuevos), len(c['pages']), 'páginas')
