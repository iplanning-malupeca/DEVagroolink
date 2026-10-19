"""Alta de usuario en móvil (390 px), versión móvil de 003_LP_Alta_usuario: los diálogos pasan a pantalla completa.
Escribe MB_Alta*; movil_canvas.py los coloca en «003_MB_Alta_usuario». Uso: python3 tools/alta_usuario_movil.py <canvas.json>"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, LOGO, svg, I, wrap, tabbar, VE, hdr, W, DEST
CK = svg('m5 12 5 5 9-10', 12, 3)
def top(paso=''):
    return ('<div class="top" style="padding:0 6px 0 16px"><span style="flex:1;display:flex;align-items:center">' + LOGO + '</span>' +
            ('<span style="font-size:11.5px;font-weight:600;color:%s;background:#E8F2EC;border-radius:999px;padding:4px 10px;margin-right:6px">%s</span>' % (VE, paso) if paso else '') +
            '<span class="ib" aria-label="Cerrar">' + svg('M6 6l12 12M18 6 6 18', 20, 2) + '</span></div>')
def icono(d):
    return '<span style="width:60px;height:60px;border-radius:50%;background:#E8F2EC;color:' + VE + ';display:flex;align-items:center;justify-content:center;align-self:center">' + svg(d, 26) + '</span>'
def tit(t, sub, centro=True):
    a = 'center' if centro else 'left'
    return '<div style="text-align:%s;display:flex;flex-direction:column;gap:6px"><h1 style="margin:0;font-size:22px;font-weight:700;line-height:1.2">%s</h1><p style="margin:0;font-size:14px;color:#56615B">%s</p></div>' % (a, t, sub)
def btnp(t, extra=''):
    return '<span class="btnp" style="height:50px;background:' + VE + ';font-size:15px;width:100%' + extra + '">' + t + '</span>'
def cuerpo(h, pb=40):
    return '<div style="padding:24px 20px %dpx;display:flex;flex-direction:column;gap:18px;background:#FFFFFF;min-height:780px">%s</div>' % (pb, h)
INP = lambda ph: '<span style="height:50px;border:1px solid #D3D9DE;border-radius:12px;padding:0 14px;display:flex;align-items:center;font-size:15px;color:#8A948F">' + ph + '</span>'
NOTA = lambda t, d='M5 11h14v10H5zM8 11V8a4 4 0 0 1 8 0v3': '<div style="display:flex;gap:10px;align-items:flex-start;font-size:12.5px;color:#56615B;background:#F2F7F4;border-radius:12px;padding:10px 12px"><span style="color:' + VE + '">' + svg(d, 16) + '</span><span>' + t + '</span></div>'
def email():
    return SB + top() + cuerpo(icono('M3 5h18v14H3zM3 7l9 6 9-6') + tit('Accede para continuar', 'Introduce tu email y te enviaremos un código de verificación si ya tienes una cuenta.') +
        '<label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;font-weight:600">Email <span style="color:#D23C3C;display:none"></span>' + INP('nombre@empresa.com') + '</label>' + btnp('Continuar') + NOTA('Tus datos están seguros. Solo los usamos para identificar tu cuenta.'))
def codigo():
    otp = '<div style="display:flex;justify-content:space-between">' + ''.join('<span style="width:48px;height:56px;border:%s;border-radius:12px;font-size:22px;font-weight:700;display:flex;align-items:center;justify-content:center">%s</span>' % ('2px solid ' + VE if i == 4 else '1px solid #D3D9DE', d) for i, d in enumerate('4829  ')) + '</div>'
    return SB + top() + cuerpo(icono('M5 11h14v10H5zM8 11V8a4 4 0 0 1 8 0v3M12 15v2') + tit('Introduce tu código', 'Te hemos enviado un código de 6 cifras a<br><strong style="color:#17231D">samuel@granjalosolmos.es</strong> · <span style="color:' + VE + ';font-weight:600">Cambiar</span>') +
        otp + btnp('Entrar') + '<span style="font-size:13px;color:#56615B;text-align:center">¿No te ha llegado? Revisa el spam o <strong style="color:' + VE + '">reenviar código</strong> en 0:42</span>' +
        NOTA('Es tu cuenta de Agrinews. Si es la primera vez que entras en Agroolink, te preguntaremos cómo quieres empezar.', 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8h.01M11 12h1v4h1'))
def sincuenta():
    li = ''.join('<span style="display:flex;gap:8px;align-items:center;font-size:13.5px"><span style="color:' + VE + '">' + svg('m5 12 5 5 9-10', 14, 2.4) + '</span>' + t + '</span>' for t in ['Accede a fichas técnicas y contenido exclusivo', 'Guarda productos en tus tableros', 'Recibe recomendaciones personalizadas'])
    return SB + top() + cuerpo(icono('M10 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM3 21a7 7 0 0 1 12.5-4.3M19 14v6M16 17h6') + tit('Parece que todavía no tienes una cuenta', 'Para continuar, crea una cuenta gratuita. Solo te llevará un minuto.') +
        '<div style="background:#F2F7F4;border-radius:12px;padding:14px;display:flex;flex-direction:column;gap:10px">' + li + '</div>' + btnp('Crear cuenta') +
        '<span class="btn" style="height:50px;border:1.5px solid ' + VE + ';color:' + VE + ';font-size:15px">Ya tengo una cuenta</span><span class="hint" style="text-align:center">Crear cuenta abre el registro de Agrinews y vuelve aquí, a «Tus intereses».</span>')
def ch(t, on=False):
    return '<span style="display:inline-flex;align-items:center;gap:5px;height:34px;padding:0 13px;border-radius:999px;font-size:13px;font-weight:600;white-space:nowrap;%s">%s%s</span>' % ('background:%s;color:#FFFFFF;border:1px solid %s' % (VE, VE) if on else 'background:#FFFFFF;border:1px solid #DDE3E7', CK if on else '', t)
def sub(lbl, items):
    return '<div style="display:flex;flex-wrap:wrap;gap:5px;align-items:center;padding:8px 10px;border-radius:12px;background:#F3F8F2"><span style="font-size:11.5px;font-weight:700;color:' + VE + '">' + lbl + ' ›</span>' + ''.join('<span style="height:26px;padding:0 9px;border-radius:999px;font-size:12px;display:inline-flex;align-items:center;%s">%s</span>' % ('background:#DDF0D8;color:#0E5A3A;border:1px solid #C9E3C3' if on else 'background:#FFFFFF;color:#56615B;border:1px solid #D5DED8', t) for t, on in items) + '</div>'
def grupo(t, d, chips, extra=''):
    return '<div style="display:flex;flex-direction:column;gap:8px"><strong style="font-size:15px">' + t + ' <span style="font-size:12px;font-weight:400;color:#56615B">· ' + d + '</span></strong><div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join(ch(*c) for c in chips) + '</div>' + extra + '</div>'
def intereses():
    esp = [('Avicultura', 1), ('Porcino', 1), ('Bovino',), ('Ovino',), ('Caprino',), ('Acuicultura',), ('Cunicultura',)]
    cat = [('Nutrición y aditivos', 1), ('Materias primas',), ('Salud y bioseguridad',), ('Genética',), ('Equipamiento',), ('Equipamiento avícola', 1), ('Equipamiento porcino',), ('Sostenibilidad',), ('Tecnología',)]
    obj = [('Bienestar animal', 1), ('Rendimiento',), ('Conversión alimenticia', 1), ('Salud intestinal',), ('Reducción antibióticos',), ('Reducción de costes', 1), ('Sostenibilidad', 1), ('Huevo campero', 1), ('Producción ecológica',), ('One Health',)]
    h = (tit('¿Qué te interesa, Samuel?', 'Lo usamos para recomendarte productos, contenidos y proyectos. Puedes cambiarlo cuando quieras en tu perfil.', False) +
         grupo('Especies', 'al elegirla se incluyen sus producciones', esp, sub('Avicultura', [('Pollos de engorde', 1), ('Ponedoras', 1), ('Reproductoras', 1), ('Pavos', 1), ('Patos', 1), ('Ocas', 1), ('Perdices', 1), ('Ornamentales', 0)]) + sub('Porcino', [('Todas sus producciones', 1)])) +
         grupo('Categorías', 'se incluyen todos sus tipos', cat, sub('Equipamiento avícola', [('7 de 8 tipos', 1), ('Procesamiento avícola', 0)])) + grupo('Objetivos y tendencias', 'se actualizan con el sector', obj))
    return (SB + top('Solo la primera vez') + cuerpo(h, 120) +
            '<div class="foot" style="align-items:center"><span style="font-size:13.5px;color:' + VE + ';font-weight:600">Saltar</span><span class="hint" style="flex:1;text-align:center">9 seleccionados</span><span class="btnp" style="height:46px;background:' + VE + ';padding:0 24px">Continuar</span></div>')
def opt(ic, bg, col, t, d, on, extra=''):
    return ('<div style="display:flex;gap:12px;align-items:center;padding:14px;border-radius:14px;%s"><span style="width:42px;height:42px;border-radius:12px;background:%s;color:%s;display:flex;align-items:center;justify-content:center;flex:none">%s</span><span style="flex:1;display:flex;flex-direction:column;gap:2px"><strong style="font-size:14.5px">%s</strong><span style="font-size:12.5px;color:#56615B">%s</span>%s</span><span style="width:20px;height:20px;border-radius:50%%;border:1.5px solid %s;flex:none;display:flex;align-items:center;justify-content:center">%s</span></div>'
            % ('border:1.5px solid %s;background:#F2F7F4' % VE if on else 'border:1px solid #DDE3E7', bg, col, svg(ic, 20), t, d, extra, VE if on else '#C9D2CC', '<span style="width:10px;height:10px;border-radius:50%;background:' + VE + '"></span>' if on else ''))
def empezar(empresa=False):
    nom = 'Carla' if empresa else 'Samuel'
    sug = '<span style="font-size:11px;font-weight:600;color:' + VE + ';background:#E8F2EC;border-radius:999px;padding:2px 8px;align-self:flex-start;margin-top:3px">Sugerido por tu cargo: Comercial</span>' if empresa else ''
    h = (tit('¿Cómo quieres empezar, ' + nom + '?', 'Siempre tendrás tu perfil personal. Empresa y experto se añaden a él, ahora o cuando quieras.', False) +
         '<div style="display:flex;flex-direction:column;gap:8px">' +
         opt('M12 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM4 21a8 8 0 0 1 16 0', '#FFFFFF', VE, 'Solo para mí', 'Buscar productos, comparar, crear tableros y seguir empresas.', not empresa) +
         opt('M5 3h14v18H5zM9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2', '#E8F2EC', VE, 'Represento una empresa', ('Gestionar el perfil de tu empresa' if empresa else 'Gestionar el perfil de Granja Los Olmos') + ', publicar productos y recibir consultas. Gratis.', empresa, sug) +
         opt('M22 9 12 4 2 9l10 5zM6 11v5c3 2 9 2 12 0v-5', '#F1EEFB', '#4B3BA6', 'Soy experto o consultor', 'Ofrecer servicios, publicar contenido y participar en proyectos. Gratis.', False) + '</div>'
         '<label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;font-weight:600"><span>Tu cargo <span style="font-size:11px;color:' + VE + ';background:#E8F2EC;border-radius:999px;padding:2px 8px">De tu cuenta Agrinews</span></span>' +
         '<span style="height:50px;border:1px solid #CFE0D5;border-radius:12px;padding:0 14px;display:flex;align-items:center;justify-content:space-between;font-size:15px;font-weight:500">' + ('Comercial' if empresa else 'Granjero') + svg('m6 9 6 6 6-6', 16, 2) + '</span><span class="hint" style="font-weight:400">Si lo cambias, cambia en Agrinews y en Agroolink.</span></label>')
    return (SB + top('Último paso') + cuerpo(h, 150) +
            '<div class="foot" style="flex-direction:column;gap:10px">' + btnp('Crear mi cuenta') + '<span class="hint" style="text-align:center;font-size:13px">Decidir más tarde</span></div>')
def creada(empresa=False):
    if empresa:
        s, bt, bx, p, sec = 'Tu perfil personal está listo. Ahora vamos con tu empresa.', 'Siguiente: escribe el nombre de tu organización', 'Si ya está en Agroolink te unes a ella; si no, la creas en 2 minutos.', 'Continuar con mi empresa', 'Hacerlo más tarde y volver a donde estaba'
    else:
        s, bt, bx, p, sec = 'Ya puedes acceder a Agroolink y disfrutar de todas sus funcionalidades.', 'Ahora vuelve a la página donde estabas', 'Te hemos guardado tu acción para que puedas continuar.', 'Volver a Agroolink', 'Ir a mi espacio'
    return SB + top() + cuerpo('<span style="width:72px;height:72px;border-radius:50%;background:#E8F2EC;display:flex;align-items:center;justify-content:center;align-self:center"><span style="width:48px;height:48px;border-radius:50%;background:' + VE + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg('m5 12 5 5 9-10', 24, 2.6) + '</span></span>' +
        tit('¡Cuenta creada con éxito!', s) + '<div style="display:flex;gap:12px;align-items:flex-start;padding:12px 14px;border:1px solid #DCE9E1;background:#F2F7F4;border-radius:12px"><span style="color:' + VE + '">' + svg('M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM8 12l3 3 5-6', 20) + '</span><span style="display:flex;flex-direction:column;gap:2px"><strong style="font-size:13.5px">' + bt + '</strong><span class="hint">' + bx + '</span></span></div>' +
        btnp(p + ' →') + '<span style="font-size:13px;text-align:center;color:' + VE + ';text-decoration:underline">' + sec + '</span>')
def miespacio():
    paso = lambda t, ok: '<div style="display:flex;gap:10px;align-items:center;font-size:13.5px;padding:6px 0"><span style="width:22px;height:22px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;' + ('background:' + VE + ';color:#FFFFFF">' + svg('m5 12 5 5 9-10', 12, 3) if ok else 'border:1.5px solid #C9D2CC">') + '</span><span style="' + ('color:#8A948F;text-decoration:line-through' if ok else '') + '">' + t + '</span></div>'
    h = ('<div class="card" style="flex-direction:row;align-items:center;gap:12px;border-color:#CFE0D5;background:#F5FAF6"><span style="width:44px;height:44px;border-radius:12px;background:#1E4FA0;color:#FFFFFF;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;flex:none">dsm</span><span style="flex:1;min-width:0;display:flex;flex-direction:column"><span class="hint" style="font-weight:600;letter-spacing:.06em">ESTABAS CONSULTANDO</span><strong style="font-size:13.5px">Ronozyme® HiPhos</strong><span class="hint">DSM-Firmenich · Enzimas</span></span><span class="btnp" style="height:34px;background:' + VE + '">Volver</span></div>'
         '<div><span class="hint" style="font-weight:600;letter-spacing:.08em">MI ESPACIO</span><h1 style="margin:2px 0 0;font-size:22px;font-weight:700">Bienvenido, Samuel</h1><span class="hint" style="font-size:13px">Desde aquí guardas, comparas y pides propuestas.</span></div>'
         '<div class="card"><div style="display:flex;align-items:center"><strong style="flex:1;font-size:14.5px">Tus intereses</strong><span style="font-size:13px;color:' + VE + ';font-weight:600">Editar</span></div>'
         '<span style="font-size:12.5px"><strong>Especies:</strong> Avicultura (7 de 8 producciones) · Porcino</span><span style="font-size:12.5px"><strong>Categorías:</strong> Nutrición y aditivos · Equipamiento avícola</span><span style="font-size:12.5px"><strong>Objetivos:</strong> Bienestar animal · Conversión alimenticia · Huevo campero · Reducción de costes · Sostenibilidad</span></div>'
         '<div class="card" style="background:#F7FBEA;border-color:#E2EDB8"><strong style="font-size:14.5px">¿Necesitas algo concreto?</strong><span class="hint" style="font-size:12.5px;color:#4A5650">Publica un proyecto y recibe propuestas de empresas y expertos de tu zona. Tus datos de contacto nunca se muestran.</span><span class="btnp" style="background:' + VE + ';align-self:flex-start">Crear proyecto</span></div>'
         '<div class="card"><div style="display:flex;align-items:center"><strong style="flex:1;font-size:14.5px">Primeros pasos</strong><span class="hint">1 de 4</span></div>' +
         paso('Guarda un producto en un tablero', True) + paso('Compara dos productos', False) + paso('Sigue a una empresa o experto', False) + paso('Publica tu primer proyecto', False) + '</div>')
    return SB + hdr() + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + h + '</div>' + tabbar('Tú')
def consulta():
    h = ('<div style="display:flex;gap:12px;align-items:center"><span style="width:44px;height:44px;border-radius:12px;background:#1F3A5F;color:#FFFFFF;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center">AE</span><span style="display:flex;flex-direction:column"><strong style="font-size:16px">Consulta a AgroExport SRL</strong><span class="hint">Sobre: Adsorbente de micotoxinas</span></span></div>'
         '<label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;font-weight:600">Tu mensaje<span style="border:1px solid #D3D9DE;border-radius:12px;padding:12px 14px;font-size:14px;font-weight:400;line-height:1.45">Hola, me interesa este producto para una granja de broilers. ¿Podéis enviarme precio y disponibilidad?</span></label>'
         '<div style="background:#F2F7F4;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:10px"><span style="font-size:13px"><strong>Solo esta vez:</strong> AgroExport ya verá tu nombre, Granja Los Olmos y tu cargo. Para responderte mejor, añade:</span>'
         '<label style="display:flex;flex-direction:column;gap:5px;font-size:12.5px;font-weight:600">Provincia de la explotación<span style="height:46px;border:1px solid #D3D9DE;border-radius:10px;background:#FFFFFF;padding:0 12px;display:flex;align-items:center;justify-content:space-between;font-weight:500;font-size:14px">Lleida' + svg('m6 9 6 6 6-6', 16, 2) + '</span></label>'
         '<label style="display:flex;flex-direction:column;gap:5px;font-size:12.5px;font-weight:600">Tamaño <span style="font-weight:400;color:#56615B">(opcional)</span><span style="height:46px;border:1px solid #D3D9DE;border-radius:10px;background:#FFFFFF;padding:0 12px;display:flex;align-items:center;justify-content:space-between;font-weight:400;font-size:14px;color:#8A948F">Selecciona' + svg('m6 9 6 6 6-6', 16, 2) + '</span></label></div>' +
         NOTA('AgroExport SRL verá tu nombre, tu empresa, tu cargo y estos datos. Nunca tu teléfono ni tu email: te responde por Mensajes.'))
    return (SB + '<div class="top" style="padding-left:6px"><span class="ib">' + svg('M6 6l12 12M18 6 6 18', 20, 2) + '</span><strong style="flex:1;font-size:15.5px">Primera consulta</strong><span style="font-size:11px;font-weight:600;color:' + VE + ';background:#E8F2EC;border-radius:999px;padding:3px 9px;margin-right:8px">✓ Email verificado</span></div>' +
            cuerpo(h, 120) + '<div class="foot">' + btnp(svg(I['send'], 16, 2) + ' Enviar consulta') + '</div>')
B = {'MB_Alta1_Email': ('Móvil · Accede con tu email', 844, email()), 'MB_Alta2_Codigo': ('Móvil · Ya registrado: código por email', 844, codigo()),
     'MB_Alta2b_SinCuenta': ('Móvil · Todavía no tienes cuenta', 844, sincuenta()), 'MB_Alta3_Intereses': ('Móvil · Tus intereses (solo la 1.ª vez)', 1180, intereses()),
     'MB_Alta4_Empezar': ('Móvil · ¿Cómo quieres empezar?', 960, empezar()), 'MB_Alta4b_Empresa': ('Móvil · ¿Cómo quieres empezar? · empresa', 980, empezar(True)),
     'MB_Alta5_Creada': ('Móvil · Cuenta lista', 844, creada()), 'MB_Alta5b_Empresa': ('Móvil · Cuenta lista → seguir con la empresa', 844, creada(True)),
     'MB_Alta6_MiEspacio': ('Móvil · Mi espacio (primer inicio)', 1080, miespacio()), 'MB_Alta7_Consulta': ('Móvil · Primera consulta', 960, consulta())}
if __name__ == '__main__':
    alt = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
    for k, (t, h, body) in B.items():
        html = wrap(t, alt.get(k, h), body)
        open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
    print('ok', len(B))
