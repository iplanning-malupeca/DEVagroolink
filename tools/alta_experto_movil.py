"""Alta de experto en móvil (390 px), versión móvil de 003a_LP_Alta_Experto, en lila.
Escribe MB_Exp*; movil_canvas.py los coloca en «003a_MB_Alta_Experto». Uso: python3 tools/alta_experto_movil.py <canvas.json> [alturas.json]"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, LOGO, svg, I, wrap, tabbar, hdr, W, DEST, LI
CK = svg('m5 12 5 5 9-10', 12, 3)
SOFT = '#F1EEFB'
def top(paso='', cerrar=True):
    return ('<div class="top" style="padding:0 6px 0 16px"><span style="flex:1;display:flex;align-items:center;gap:8px">' + LOGO + '<span style="font-size:11px;font-weight:600;color:' + LI + ';background:' + SOFT + ';border-radius:999px;padding:2px 9px">Expertos</span></span>' +
            ('<span class="hint" style="margin-right:6px">' + paso + '</span>' if paso else '') + ('<span class="ib" aria-label="Cerrar">' + svg('M6 6l12 12M18 6 6 18', 20, 2) + '</span>' if cerrar else '') + '</div>')
def barra(n):
    return '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6px">' + ''.join('<span style="height:5px;border-radius:3px;background:%s"></span>' % (LI if i < n else '#DCE3DE') for i in range(3)) + '</div>'
def tit(t, sub, centro=False):
    return '<div style="text-align:%s;display:flex;flex-direction:column;gap:6px"><h1 style="margin:0;font-size:22px;font-weight:700;line-height:1.2">%s</h1><p style="margin:0;font-size:14px;color:#56615B">%s</p></div>' % ('center' if centro else 'left', t, sub)
def btnp(t):
    return '<span class="btnp" style="height:50px;background:' + LI + ';font-size:15px;width:100%">' + t + '</span>'
def cuerpo(h, pb=40, bg='#FFFFFF'):
    return '<div style="padding:22px 20px %dpx;display:flex;flex-direction:column;gap:16px;background:%s">%s</div>' % (pb, bg, h)
def foot(h):
    return '<div class="foot" style="flex-direction:column;gap:10px">' + h + '</div>'
def chip(t, on=False):
    return '<span style="display:inline-flex;align-items:center;gap:5px;height:34px;padding:0 13px;border-radius:999px;font-size:13px;font-weight:600;white-space:nowrap;%s">%s%s</span>' % ('background:%s;color:#FFFFFF;border:1px solid %s' % (LI, LI) if on else 'background:#FFFFFF;border:1px solid #DDE3E7', CK if on else '', t)
def opt(ic, t, d, on, extra=''):
    return ('<div style="display:flex;gap:12px;align-items:center;padding:14px;border-radius:14px;%s"><span style="width:42px;height:42px;border-radius:12px;background:%s;color:%s;display:flex;align-items:center;justify-content:center;flex:none">%s</span><span style="flex:1;display:flex;flex-direction:column;gap:2px"><strong style="font-size:14.5px">%s</strong><span style="font-size:12.5px;color:#56615B">%s</span>%s</span><span style="width:20px;height:20px;border-radius:50%%;border:1.5px solid %s;flex:none;display:flex;align-items:center;justify-content:center">%s</span></div>'
            % ('border:1.5px solid %s;background:#F6F4FD' % LI if on else 'border:1px solid #DDE3E7', '#FFFFFF' if on else SOFT, LI, svg(ic, 20), t, d, extra, LI if on else '#C9D2CC', '<span style="width:10px;height:10px;border-radius:50%;background:' + LI + '"></span>' if on else ''))
def tarjeta_perfil():
    return ('<div class="card" style="gap:10px"><span class="hint" style="font-weight:600;letter-spacing:.06em">ASÍ TE VERÁN LOS COMPRADORES</span><div style="display:flex;gap:12px;align-items:center"><span style="width:48px;height:48px;border-radius:50%;background:' + LI + ';color:#FFFFFF;font-weight:600;display:flex;align-items:center;justify-content:center">LG</span>'
            '<span style="display:flex;flex-direction:column"><strong style="font-size:15px">Laura Gil</strong><span class="hint" style="font-size:12.5px">Veterinaria especialista en nutrición avícola · Cataluña, Aragón</span></span></div>'
            '<div style="display:flex;gap:5px;flex-wrap:wrap">' + ''.join('<span style="font-size:11.5px;font-weight:500;background:' + SOFT + ';color:' + LI + ';border-radius:999px;padding:3px 10px">' + t + '</span>' for t in ['Avicultura', 'Nutrición', 'Bioseguridad']) + '</div></div>')
# ---------- pantallas ----------
def empezar():
    h = (tit('¿Cómo quieres empezar, Laura?', 'Siempre tendrás tu perfil personal. Empresa y experto se añaden a él, ahora o cuando quieras.') +
         '<div style="display:flex;flex-direction:column;gap:8px">' +
         opt('M12 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM4 21a8 8 0 0 1 16 0', 'Solo para mí', 'Buscar productos, comparar, crear tableros y seguir empresas.', False) +
         opt('M5 3h14v18H5zM9 7h2M13 7h2M9 11h2M13 11h2M9 15h2M13 15h2', 'Represento una empresa', 'Gestionar el perfil de mi empresa, publicar productos y recibir consultas. Gratis.', False) +
         opt('M22 9 12 4 2 9l10 5zM6 11v5c3 2 9 2 12 0v-5', 'Soy experto o consultor', 'Ofrecer servicios, publicar contenido y participar en proyectos. Gratis.', True, '<span style="font-size:11.5px;color:' + LI + ';font-weight:600;margin-top:3px">Sugerido por tu cargo: Veterinaria</span>') + '</div>')
    return SB + top('Último paso') + cuerpo(h, 150) + foot(btnp('Crear mi cuenta') + '<span class="hint" style="text-align:center;font-size:13px">Decidir más tarde</span>')
def creada():
    pasos = ''.join('<span style="display:flex;gap:10px;align-items:center;font-size:13.5px"><span style="width:24px;height:24px;border-radius:50%;border:1.5px solid #C9C0EE;color:' + LI + ';font-size:11.5px;font-weight:700;display:flex;align-items:center;justify-content:center">' + str(i + 1) + '</span>' + t + '</span>' for i, t in enumerate(['Tu especialidad y zona', 'Tus servicios (opcional)', 'Revisar y publicar']))
    h = ('<span style="width:72px;height:72px;border-radius:50%;background:' + SOFT + ';display:flex;align-items:center;justify-content:center;align-self:center"><span style="width:48px;height:48px;border-radius:50%;background:' + LI + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg('m5 12 5 5 9-10', 24, 2.6) + '</span></span>' +
         tit('¡Cuenta creada, Laura!', 'Tu perfil personal está listo. Ahora vamos con tu perfil de experto.', True) +
         '<div style="background:#F6F4FD;border:1px solid #E2DCF7;border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:10px"><strong style="font-size:14px">3 pasos · unos 4 minutos</strong>' + pasos + '</div>' +
         btnp('Crear mi perfil de experto →') + '<span style="font-size:13px;text-align:center;color:' + LI + ';text-decoration:underline">Hacerlo más tarde y volver a donde estaba</span>')
    return SB + top() + cuerpo(h)
def especialidad():
    h = ('<div style="display:flex;flex-direction:column;gap:6px"><span class="hint" style="font-weight:600">Paso 1 de 3 · Especialidad</span>' + barra(1) + '</div>' +
         tit('Crea tu perfil de experto', 'Es gratis y usa tu misma cuenta. Las explotaciones podrán encontrarte y escribirte.') +
         '<label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;font-weight:600">Profesión <span class="hint" style="font-weight:400">Heredado de tu cargo · <span style="color:' + LI + ';font-weight:600">Cambiar</span></span><span style="height:48px;border:1px solid #D3D9DE;border-radius:12px;padding:0 14px;display:flex;align-items:center;font-weight:500">Veterinario/a</span></label>'
         '<label style="display:flex;flex-direction:column;gap:6px;font-size:13.5px;font-weight:600">Titular profesional<span style="height:48px;border:1px solid #D3D9DE;border-radius:12px;padding:0 14px;display:flex;align-items:center;font-weight:400;font-size:14px">Especialista en nutrición avícola</span></label>'
         '<div style="display:flex;flex-direction:column;gap:8px"><strong style="font-size:13.5px">Especialidades <span class="hint" style="font-weight:400">· hasta 5</span></strong><div style="display:flex;flex-wrap:wrap;gap:6px">' +
         ''.join(chip(t, on) for t, on in [('Avicultura', 1), ('Nutrición', 1), ('Bioseguridad', 1), ('Porcino', 0), ('Bienestar animal', 0), ('Sanidad', 0), ('+ Otra', 0)]) + '</div></div>'
         '<div style="display:flex;flex-direction:column;gap:8px"><strong style="font-size:13.5px">Zona donde trabajas</strong><div style="display:flex;flex-wrap:wrap;gap:6px"><span style="height:32px;padding:0 12px;border-radius:999px;background:' + SOFT + ';color:' + LI + ';font-size:12.5px;font-weight:500;display:inline-flex;align-items:center">España · Cataluña, Aragón ×</span><span style="font-size:13px;color:' + LI + ';font-weight:600;align-self:center">+ Zona</span></div></div>' +
         tarjeta_perfil())
    return SB + top('Terminar más tarde', False) + cuerpo(h, 120) + foot(btnp('Continuar'))
def servicios():
    h = ('<div style="display:flex;flex-direction:column;gap:6px"><span class="hint" style="font-weight:600">Paso 2 de 3 · Servicios (opcional)</span>' + barra(2) + '</div>' +
         tit('¿Qué ofreces a las explotaciones?', 'Tus servicios se crean con el asistente de servicios: tipo, especies, a quién, dónde, detalles y precio.') +
         '<div class="card" style="flex-direction:row;align-items:center;gap:12px;border-color:#E2DCF7"><span style="width:40px;height:40px;border-radius:12px;background:' + SOFT + ';color:' + LI + ';display:flex;align-items:center;justify-content:center;flex:none">' + svg(I['prod'], 20) + '</span><span style="flex:1;min-width:0;display:flex;flex-direction:column"><strong style="font-size:14px">Auditoría nutricional de lotes de broilers</strong><span class="hint">Consultoría nutricional · Avicultura · Cataluña, Aragón</span></span><span class="st ok">Listo</span></div>'
         '<div style="display:flex;align-items:center;gap:10px;padding:14px;border:1.5px dashed #C9C0EE;border-radius:14px;color:' + LI + ';font-weight:600;font-size:14px">' + svg(I['mas'], 18, 2) + 'Añadir un servicio<span class="hint" style="margin-left:auto;font-weight:400">abre el asistente (MB_05)</span></div>'
         '<div style="display:flex;gap:10px;align-items:flex-start;font-size:12.5px;color:#56615B;background:#F6F4FD;border-radius:12px;padding:10px 12px"><span style="color:' + LI + '">' + svg(I['info'], 16) + '</span><span>Con Experto Gratis publicas 1 servicio; con Experto Pro, ilimitados. Puedes saltar este paso y crearlos después en «Mis servicios».</span></div>')
    return SB + top('Terminar más tarde', False) + cuerpo(h, 150) + foot('<div style="display:flex;gap:8px"><span class="btn" style="height:50px;flex:1">Saltar</span><span class="btnp" style="height:50px;flex:2;background:' + LI + '">Continuar</span></div>')
def publicar():
    ok = lambda t, a: '<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1px solid #EEF1EE;font-size:14px"><span style="width:22px;height:22px;border-radius:50%;background:' + LI + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg('m5 12 5 5 9-10', 12, 3) + '</span><span style="flex:1">' + t + '</span><span style="color:' + LI + ';font-weight:600;font-size:13px">' + a + '</span></div>'
    h = ('<div style="display:flex;flex-direction:column;gap:6px"><span class="hint" style="font-weight:600">Paso 3 de 3 · Revisar y publicar</span>' + barra(3) + '</div>' + tit('Todo listo para publicar', '') +
         '<div>' + ok('Especialidad y zona', 'Editar') + ok('1 servicio', 'Editar') + '<div style="display:flex;align-items:center;gap:12px;padding:12px 0;border-top:1px solid #EEF1EE;border-bottom:1px solid #EEF1EE;font-size:14px"><span style="width:22px;height:22px;border-radius:50%;border:1.5px solid #B9CBBF"></span><span style="flex:1">Foto de perfil <span class="hint">(recomendada)</span></span><span style="color:' + LI + ';font-weight:600;font-size:13px">Subir foto</span></div></div>'
         '<div class="card" style="gap:10px"><strong style="font-size:14px">Verificación profesional</strong><span style="height:46px;border:1px solid #D3D9DE;border-radius:10px;padding:0 12px;display:flex;align-items:center;font-size:14px">Colegio de Veterinarios de Zaragoza</span><span style="height:46px;border:1px solid #D3D9DE;border-radius:10px;padding:0 12px;display:flex;align-items:center;font-size:14px;color:#8A948F">Nº de colegiada</span><span class="hint" style="font-size:12.5px">Lo comprobamos en 24–48 h. Tu perfil se publica ya; el sello «Colegiada verificada» aparece al confirmarlo.</span></div>' +
         ''.join('<label style="display:flex;gap:10px;align-items:center;font-size:13.5px"><span style="width:20px;height:20px;border-radius:5px;background:' + LI + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg('m5 12 5 5 9-10', 12, 3) + '</span>' + t + '</label>' for t in ['Acepto consultas de explotaciones y empresas', 'Quiero ver proyectos abiertos que encajen conmigo']) + tarjeta_perfil())
    return SB + top('Terminar más tarde', False) + cuerpo(h, 120) + foot(btnp('Publicar mi perfil'))
def publicado():
    h = ('<span style="width:72px;height:72px;border-radius:50%;background:' + SOFT + ';display:flex;align-items:center;justify-content:center;align-self:center"><span style="width:48px;height:48px;border-radius:50%;background:' + LI + ';color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg('m5 12 5 5 9-10', 24, 2.6) + '</span></span>' +
         tit('Tu perfil de experto está publicado', 'Ya apareces en búsquedas de <strong>nutrición y bioseguridad avícola</strong> en <strong>Cataluña y Aragón</strong>.', True) +
         '<div style="display:flex;flex-direction:column;gap:8px"><strong style="font-size:13.5px">Comparte tu perfil</strong><div style="display:flex;gap:8px"><span style="flex:1;height:44px;border:1px solid #D3D9DE;border-radius:10px;background:#F6F8F6;padding:0 12px;display:flex;align-items:center;font-size:13px;color:#2F3D36;overflow:hidden;white-space:nowrap">agroolink.com/expertos/laura-gil</span><span class="btnp" style="height:44px;background:' + LI + '">Compartir</span></div>'
         '<span class="hint">Se comparte el enlace a tu perfil, nunca tu teléfono ni tu email: quien te escribe lo hace por Mensajes.</span></div>'
         '<div style="display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:12px;background:#FFF8E6;font-size:13px;color:#5A4A14">' + svg('M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 7v5l3 2', 16) + 'Colegiación en revisión (24–48 h). Te avisaremos al confirmarla.</div>' +
         btnp('Ir a mi espacio') + '<span class="btn" style="height:48px;border:1px solid ' + LI + ';color:' + LI + '">Ver perfil público</span>')
    return SB + top('', False) + cuerpo(h)
def semana():
    item = lambda ic, t, d, b, prim: '<div style="display:flex;gap:10px;align-items:flex-start;padding:10px 0;border-top:1px solid #EEF1EE"><span style="width:36px;height:36px;border-radius:10px;background:' + SOFT + ';color:' + LI + ';display:flex;align-items:center;justify-content:center;flex:none;font-size:12px;font-weight:600">' + ic + '</span><span style="flex:1;min-width:0;display:flex;flex-direction:column;gap:2px"><strong style="font-size:13.5px">' + t + '</strong><span class="hint">' + d + '</span><span class="' + ('btnp' if prim else 'btn') + '" style="height:34px;align-self:flex-start;margin-top:4px;' + ('background:' + LI if prim else 'border:1px solid ' + LI + ';color:' + LI) + '">' + b + '</span></span></div>'
    h = ('<div style="display:flex;gap:10px;align-items:center;padding:10px 12px;border-radius:12px;background:#F6F4FD;border:1px solid #E2DCF7;font-size:13px"><span style="color:' + LI + '">' + svg('M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM8 12l3 3 5-6', 18, 2) + '</span><span><strong>Colegiación verificada.</strong> Tu perfil ya muestra el sello.</span></div>'
         '<div style="display:flex;align-items:baseline"><h1 style="margin:0;font-size:22px;font-weight:700;flex:1">Hola, Laura</h1><span style="font-size:13px;color:' + LI + ';font-weight:600">Mi perfil público</span></div>'
         '<div class="card" style="gap:2px"><div style="display:flex;align-items:center"><strong style="flex:1;font-size:15px">Consultas recibidas</strong><span class="hint">sin límite</span></div>' +
         item('GA', 'Ganadero · Huesca · Avicultura', 'Sobre «Auditoría nutricional de lotes de broilers» · «Tengo dos naves y el índice de conversión ha empeorado…» · hace 5 h', 'Responder', True) + '</div>'
         '<div class="card" style="gap:2px"><div style="display:flex;align-items:center"><strong style="flex:1;font-size:15px">Proyectos que encajan contigo</strong></div>' +
         item(svg('M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8zM14 3v5h5M9 13h6M9 17h6', 16), 'Plan de bioseguridad para granja de ponedoras', 'Lleida · cierra en 6 días · 2 propuestas', 'Presentar propuesta', False) + '</div>'
         '<div class="card"><div style="display:flex;align-items:center"><strong style="flex:1;font-size:15px">Completa tu perfil</strong><span class="hint">3 de 5</span></div><div style="height:5px;border-radius:3px;background:#E3E8E4;overflow:hidden"><div style="width:60%;height:100%;background:' + LI + '"></div></div>'
         '<span style="font-size:13.5px">○ Añade una foto</span><span style="font-size:13.5px">○ Añade un caso de éxito</span></div>')
    return SB + hdr('Experta', LI) + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + h + '</div>' + tabbar('Tú', LI, avatar='LG')
def aviso():
    h = ('<div><span class="hint" style="font-weight:600;letter-spacing:.08em">MI ESPACIO</span><h1 style="margin:2px 0 0;font-size:22px;font-weight:700">Hola de nuevo, Laura</h1></div>'
         '<div class="card" style="background:#F6F4FD;border-color:#E2DCF7;gap:8px"><strong style="font-size:15px">Laura, ¿asesoras a explotaciones?</strong><span style="font-size:13px;color:#4A5650">Crea tu perfil de experta y las granjas de avicultura podrán encontrarte y escribirte. Es gratis y usa tu misma cuenta.</span><div style="display:flex;gap:8px"><span class="btnp" style="background:' + LI + '">Crear perfil de experta</span><span class="btn">Ahora no</span></div></div>'
         '<div class="card"><span class="hint" style="font-weight:600;letter-spacing:.06em">CONTINÚA DONDE LO DEJASTE</span><strong style="font-size:14px">Tablero «Clientes · nutrición broilers»</strong><span class="hint">8 productos · 2 comparaciones</span><span class="btn" style="align-self:flex-start;height:34px">Abrir tablero</span></div>')
    return SB + hdr() + '<div style="padding:14px 16px 110px;display:flex;flex-direction:column;gap:12px">' + h + '</div>' + tabbar('Tú')
def intro():
    ben = [('M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5', 'Apareces en las búsquedas', 'de explotaciones y empresas de tu zona y especialidad.'), (I['mail'], 'Recibes consultas', 'en tus mismos Mensajes.'), (I['proy'], 'Ves proyectos abiertos', 'que encajan contigo y puedes presentar propuesta.')]
    h = (tit('Ofrece tus servicios como experta', 'Gratis · 3 pasos · unos 4 minutos') +
         ''.join('<div style="display:flex;gap:12px;align-items:flex-start"><span style="width:40px;height:40px;border-radius:12px;background:' + SOFT + ';color:' + LI + ';display:flex;align-items:center;justify-content:center;flex:none">' + svg(d, 20) + '</span><span style="font-size:14px"><strong>' + t + '</strong> ' + x + '</span></div>' for d, t, x in ben) +
         '<div class="card" style="gap:6px"><strong style="font-size:14px">Qué cambia en tu cuenta</strong><span style="font-size:13px;color:#4A5650">Nada de lo que ya tienes. Tu menú gana una sección <strong>«Como experta»</strong>; tus tableros, guardados y mensajes siguen igual. Puedes ocultar el perfil cuando quieras.</span></div>'
         '<div class="card" style="gap:8px;background:#F6F4FD;border-color:#E2DCF7"><strong style="font-size:14px">Ya lo rellenamos con lo que sabemos de ti</strong><div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join(chip(t, True) for t in ['Veterinaria', 'Avicultura', 'Nutrición', 'Aragón']) + '</div></div>')
    return SB + top() + cuerpo(h, 130) + foot('<div style="display:flex;gap:8px"><span class="btn" style="height:50px;flex:1">Ahora no</span><span class="btnp" style="height:50px;flex:2;background:' + LI + '">Empezar →</span></div>')
B = {'MB_Exp1_Empezar': ('Móvil · ¿Cómo quieres empezar? → Experto', 880, empezar()), 'MB_Exp2_Creada': ('Móvil · Cuenta creada → perfil de experto', 880, creada()),
     'MB_Exp3_Especialidad': ('Móvil · Paso 1 · Especialidad', 1180, especialidad()), 'MB_Exp4_Servicios': ('Móvil · Paso 2 · Servicios (abre el asistente de servicios)', 880, servicios()),
     'MB_Exp5_Publicar': ('Móvil · Paso 3 · Revisar y publicar', 1240, publicar()), 'MB_Exp6_Publicado': ('Móvil · Perfil publicado', 900, publicado()),
     'MB_Exp7_Semana': ('Móvil · Mi espacio como experta, primera semana', 1000, semana()), 'MB_ExpP1_Aviso': ('Móvil · De comprador a experta: aviso en Mi espacio', 844, aviso()),
     'MB_ExpP2_Intro': ('Móvil · «Ofrecer mis servicios»: qué cambia y qué gana', 900, intro())}
if __name__ == '__main__':
    alt = json.load(open(sys.argv[2])) if len(sys.argv) > 2 else {}
    for k, (t, h, body) in B.items():
        html = wrap(t, alt.get(k, h), body)
        open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
    print('ok', len(B))
