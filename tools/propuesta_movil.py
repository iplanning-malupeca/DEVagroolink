"""Versión móvil (390 px) de J6 · enviar propuesta, J6b · la propuesta en Mensajes y J6c · propuesta bloqueada por contactos.
Escribe MB_PropuestaMovil, MB_PropuestaMensajes y MB_PropuestaBloqueada; movil_canvas.py los coloca en MB_07 Proyectos.
Uso: python3 tools/propuesta_movil.py <canvas.json>"""
import os, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST = os.path.dirname(sys.argv[1]) + '/'
AZ = '#1D4E89'
CSS = """*{box-sizing:border-box}body{margin:0}.m{font-family:'Poppins',system-ui,sans-serif;color:#17231D;font-size:14px;line-height:1.38}
.sb{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 26px 0 30px;font-size:15px;font-weight:600;background:#FFFFFF}
.top{height:56px;display:flex;align-items:center;gap:8px;padding:0 8px;background:#FFFFFF;border-bottom:1px solid #E3E8E4}
.ib{width:44px;height:44px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;color:#17231D;position:relative;flex:none}
.bdg{position:absolute;top:5px;right:3px;min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:#D93A3A;color:#FFFFFF;font-size:10.5px;font-weight:600;display:flex;align-items:center;justify-content:center;border:2px solid #FFFFFF}
.card{background:#FFFFFF;border:1px solid #E6EBE7;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.lbl{font-size:12.5px;font-weight:600}
.hint{font-size:11.5px;color:#56615B}
.ta{border:1px solid #D5DED8;border-radius:12px;padding:10px 12px;font-size:13.5px;line-height:1.5;background:#FFFFFF}
.tok{display:inline-flex;align-items:center;height:30px;padding:0 11px;border-radius:999px;background:#E9F0F9;color:#1D4E89;border:1px solid #C8D8EE;font-size:12px;font-weight:500;white-space:nowrap}
.inp{height:42px;border:1px solid #D5DED8;border-radius:10px;padding:0 12px;display:flex;align-items:center;font-size:13.5px;background:#FFFFFF;flex:1;min-width:0}
.btnp{height:48px;border-radius:12px;background:#1D4E89;color:#FFFFFF;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px;flex:1}
.btn{height:48px;border-radius:12px;border:1px solid #D2DAE3;background:#FFFFFF;font-weight:500;display:flex;align-items:center;justify-content:center;padding:0 16px}
.foot{position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 16px 30px;display:flex;flex-direction:column;gap:8px}
mark{background:#FDECEA;color:#A3271B;border-radius:4px;padding:0 3px;text-decoration:underline wavy #A3271B;text-underline-offset:3px}
"""
SB = ('<div class="sb"><span>9:41</span><span style="display:flex;gap:6px;align-items:center"><svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="1" fill="#17231D"/><rect x="5" y="5" width="3" height="7" rx="1" fill="#17231D"/><rect x="10" y="2.5" width="3" height="9.5" rx="1" fill="#17231D"/><rect x="15" y="0" width="3" height="12" rx="1" fill="#17231D"/></svg>'
      '<svg width="26" height="12" viewBox="0 0 26 12" aria-hidden="true"><rect x=".5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="#17231D" opacity=".4"/><rect x="2" y="2" width="17" height="8" rx="2" fill="#17231D"/></svg></span></div>')
BACK = '<span class="ib" aria-label="Atrás"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg></span>'
MSG = '<span class="ib" aria-label="Mensajes, 3 sin leer"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6"/></svg><span class="bdg">3</span></span>'
SEND = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 2 11 13M22 2l-7 20-4-9-9-4z"/></svg>'
def top(t, sub):
    return '<div class="top">' + BACK + '<span style="flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2"><strong style="font-size:15.5px">' + t + '</strong><span class="hint" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + sub + '</span></span>' + MSG + '</div>'
def wrap(title, h, body):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n<div class="m" style="width: 390px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":390,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')
TOKS = '<div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join('<span class="tok">' + t + ' ×</span>' for t in ['Roxell Feedmax', 'Silo 20 t', 'Montaje y puesta en marcha', 'Seguimiento']) + '<span style="font-size:12.5px;color:#1D4E89;font-weight:500;align-self:center">+ Añadir</span></div>'
PRECIO = ('<div class="card"><span class="lbl">Precio orientativo</span><div style="display:flex;gap:6px;align-items:center"><span class="inp">48.000</span><span>–</span><span class="inp">55.000</span><span>€</span></div>'
          '<div style="display:flex;gap:8px"><span style="flex:1;display:flex;flex-direction:column;gap:4px"><span class="hint">Plazo</span><span class="inp">8 semanas</span></span><span style="flex:1;display:flex;flex-direction:column;gap:4px"><span class="hint">Garantía</span><span class="inp">2 años</span></span></div></div>')
ADJ = ('<div class="card" style="flex-direction:row;align-items:center;gap:10px"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#4B3BA6" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none"><path d="M6 11h12v10H6zM8 11V8a4 4 0 0 1 8 0v3"/></svg>'
       '<span style="flex:1;font-size:12.5px">Adjuntos<br><span class="hint">Solo Empresa Premium · se revisan</span></span><span style="font-size:11px;font-weight:600;padding:3px 9px;border-radius:999px;background:#F1EEFB;color:#4B3BA6">Premium</span></div>')
NOTA = '<span class="hint" style="display:flex;gap:6px;align-items:flex-start"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#1D4E89" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none;margin-top:1px"><path d="M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6"/></svg>Al enviarla se abre un hilo en Mensajes con el ganadero; ahí resolvéis las dudas.</span>'
SUB = 'Granja de broilers en Lleida · 40.000 aves'
def propuesta(bloqueada):
    if bloqueada:
        msg = ('<div class="card" style="border:1.5px solid #A3271B"><span class="lbl">Mensaje</span><div class="ta" style="border-color:#A3271B">Incluimos el montaje con técnicos de Lleida. Para cerrar fechas llámame al <mark>seis uno dos · 34 56 78</mark> o escríbeme a <mark>laura (arroba) agronova.es</mark>. Más en <mark>agronova punto es</mark> y <mark>@agronova_feed</mark>.</div>'
               '<div style="display:flex;gap:8px;align-items:flex-start;background:#FDECEA;border-radius:12px;padding:10px 12px;color:#7A1D13;font-size:12.5px;line-height:1.4"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none;margin-top:1px"><path d="M12 9v4M12 17h.01M10.3 3.9 1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/></svg><span><strong>No se puede enviar: hay datos de contacto.</strong> Teléfono, email, web y red social, aunque estén escritos con letras. Quítalos para enviar.</span></div>'
               '<span style="height:40px;border-radius:10px;border:1px solid #A3271B;color:#A3271B;font-weight:600;font-size:13px;display:flex;align-items:center;justify-content:center">Quitar los 4 datos marcados</span></div>'
               '<div class="card" style="background:#FFF6F5;border-color:#F3C9C4;gap:4px"><strong style="font-size:13px;color:#A3271B">Política de contactos</strong><span class="hint" style="color:#4A5650">No se envía nada con teléfonos, emails, webs, WhatsApp, redes o QR. <strong style="color:#17231D">Intento registrado · 1 de 3.</strong> Al tercero en 30 días se pausan tus propuestas y el superadmin revisa la cuenta.</span></div>')
        send = '<div style="display:flex;gap:8px"><span class="btn">Borrador</span><span class="btnp" style="opacity:.4">' + SEND + 'Enviar propuesta</span></div>'
    else:
        msg = '<div class="card"><span class="lbl">Mensaje</span><div class="ta">Incluimos el montaje con técnicos de Lleida y 2 visitas de seguimiento el primer año. Podemos visitar la granja la semana que viene.</div></div>'
        send = NOTA + '<div style="display:flex;gap:8px"><span class="btn">Borrador</span><span class="btnp">' + SEND + 'Enviar propuesta</span></div>'
    body = (SB + top('Tu propuesta', SUB) + '<div style="padding:12px 16px 170px;display:flex;flex-direction:column;gap:10px">' + msg +
            '<div class="card"><span class="lbl">Qué ofreces <span class="hint" style="font-weight:400">· de tu catálogo</span></span>' + TOKS + '</div>' + PRECIO + ADJ + '</div>'
            '<div class="foot">' + send + '</div>')
    return body
def burbuja(ini, col, who, txt, mio=False):
    return ('<div style="display:flex;gap:8px;align-items:flex-end;' + ('flex-direction:row-reverse;' if mio else '') + '"><span style="width:28px;height:28px;border-radius:50%;background:' + col + ';color:#FFFFFF;font-size:10px;font-weight:600;display:flex;align-items:center;justify-content:center;flex:none">' + ini + '</span>'
            '<span style="display:flex;flex-direction:column;gap:3px;max-width:82%;' + ('align-items:flex-end;' if mio else '') + '"><span class="hint">' + who + '</span><span style="background:' + ('#E9F0F9' if mio else '#FFFFFF') + ';border:1px solid ' + ('#C8D8EE' if mio else '#E3E8E4') + ';border-radius:14px;padding:9px 12px;font-size:13px">' + txt + '</span></span></div>')
def reg(t):
    return '<div style="align-self:center;max-width:94%;background:#F6F8F6;border:1px dashed #CFD8D2;border-radius:12px;padding:7px 10px;font-size:11.5px;color:#33424C"><strong>Registro</strong> · ' + t + '</div>'
def tarjeta(v, precio, extra, actual=False):
    return ('<div style="align-self:flex-end;width:88%;background:#FFFFFF;border:1.5px solid #1D4E89;border-radius:14px;padding:10px 12px;display:flex;flex-direction:column;gap:4px;font-size:12.5px"><span style="display:flex;gap:6px;align-items:center"><strong style="flex:1">Propuesta · ' + v + '</strong>' +
            ('<span style="font-size:10.5px;font-weight:600;padding:2px 8px;border-radius:999px;background:#EEF6EE;color:#0E5A3A">Actual</span>' if actual else '') + '</span><span>Roxell Feedmax · silo 20 t · montaje · seguimiento</span><span><strong>' + precio + '</strong> · 8 semanas · garantía 2 años</span><span style="color:#4A5650">' + extra + '</span><span style="color:#1D4E89;font-weight:500">Ver propuesta</span></div>')
def mensajes():
    return (SB + top('Granja Los Olmos', 'Propuesta · Nave 2 de broilers · Lleida') +
            '<div style="padding:12px 14px 150px;display:flex;flex-direction:column;gap:10px">' +
            reg('AgroNova envía una propuesta al proyecto · se abre este hilo · ayer 17:40') + tarjeta('v1', '48.000 – 55.000 €', 'Montaje con técnicos de Lleida y 2 visitas de seguimiento.') +
            burbuja('GO', '#7A6A2A', '<strong style="color:#17231D">Samuel</strong> · 10:42', '¿El precio incluye el transporte de los silos? ¿Y las 8 semanas cuentan desde el pedido?') +
            burbuja('LG', '#2E7D4F', '<strong style="color:#17231D">Laura</strong> · AgroNova · 10:55', 'Sí, desde el pedido. El transporte no estaba: lo añado y te mando la propuesta actualizada.', True) +
            reg('Propuesta actualizada a v2 · 48.000 → 49.500 € · 10:58') + tarjeta('v2', '49.500 – 55.000 €', 'Cambio: transporte de los silos incluido.', True) + '</div>'
            '<div class="foot"><span class="hint">El ganadero ve «AgroNova» y tu nombre de pila; nunca teléfonos ni emails.</span><div style="display:flex;gap:8px"><span class="inp" style="color:#8A948F">Escribe un mensaje…</span><span class="btn" style="height:42px;padding:0 12px;font-size:12.5px">Actualizar</span><span class="btnp" style="height:42px;flex:none;width:46px">' + SEND + '</span></div></div>')
B = {'MB_PropuestaMovil': ('Móvil · Enviar una propuesta', 844, propuesta(False)),
     'MB_PropuestaMensajes': ('Móvil · La propuesta en Mensajes', 920, mensajes()),
     'MB_PropuestaBloqueada': ('Móvil · Propuesta bloqueada por datos de contacto', 1040, propuesta(True))}
for k, (t, h, body) in B.items():
    html = wrap(t, h, body)
    open(DEST + k + '.dc.html', 'w').write(html); open(W + '/project/' + k + '.dc.html', 'w').write(html)
print('ok', list(B))
