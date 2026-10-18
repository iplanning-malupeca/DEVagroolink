"""Mensajería con constancia (18/10/2026): cada solicitud y cada relación de trabajo (fabricante–distribuidor,
Sede–sucursal, dirección comercial–comercial) tiene su hilo en Agroolink; los avisos quedan escritos en el hilo
y el historial no se borra. Pantallas en 006, 007, 008, 009 y 010."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__))); PR = W + '/project/'
A = '#1D4E89'
TAG = {'Solicitud': ('#FFF4E0', '#7A4B00'), 'Distribuidor': ('#E9F0F9', A), 'Fabricante': ('#E9F0F9', A), 'Sucursal': ('#EEF6EE', '#0E5A3A'), 'Sede': ('#EEF6EE', '#0E5A3A'),
       'Equipo comercial': ('#F1EEFB', '#4B3BA6'), 'Agroolink': ('#F1F3F6', '#4A5560')}
def tag(t): f, c = TAG.get(t, ('#F1F3F6', '#4A5560')); return f'<span style="font-size: 10.5px; font-weight: 600; padding: 2px 8px; border-radius: 999px; background: {f}; color: {c}; white-space: nowrap;">{t}</span>'
def av(ini, col, s=34): return f'<span style="width: {s}px; height: {s}px; border-radius: 50%; background: {col}; color: #FFFFFF; font-size: {11 if s > 30 else 10}px; font-weight: 600; display: flex; align-items: center; justify-content: center; flex: none;">{ini}</span>'
def item(it):
    sel = it.get('sel')
    return (f'<div style="display: flex; gap: 10px; padding: 10px; border-radius: 12px; {"background: #F3F7FC; box-shadow: inset 3px 0 0 " + A + ";" if sel else ""}">' + av(it['ini'], it['col']) +
            f'<span style="flex: 1; min-width: 0; display: flex; flex-direction: column; gap: 2px;"><span style="display: flex; align-items: center; gap: 6px;"><strong style="font-size: 13px; font-weight: 600; flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{it["n"]}</strong><span style="font-size: 11px; color: #8A948F; white-space: nowrap;">{it["t"]}</span></span>'
            f'<span style="display: flex; align-items: center; gap: 6px;">{tag(it["tag"])}{"<span style=&quot;width: 8px; height: 8px; border-radius: 50%; background: #E5484D;&quot;></span>" if it.get("nuevo") else ""}</span>'
            f'<span style="font-size: 12px; color: #4A5650; overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">{it["ult"]}</span></span></div>').replace('&quot;', '"')
def msg(m):
    if m[0] == 'evt':
        return (f'<div style="display: flex; gap: 10px; align-items: flex-start; align-self: center; max-width: 92%; background: #F6F8F6; border: 1px dashed #CFD8D2; border-radius: 12px; padding: 8px 12px; font-size: 12px; color: #33424C;">'
                '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="#56615B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none; margin-top: 1px;"><path d="M12 8v4l3 2M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18z"/></svg>'
                f'<span style="flex: 1;"><strong style="font-weight: 600;">Registro</strong> · {m[1]}</span><span style="color: #8A948F; white-space: nowrap;">{m[2]}</span></div>')
    _, quien, ini, col, rol, txt, hora, mio = m
    burb = f'<div style="max-width: 78%; background: {"#E9F0F9" if mio else "#FFFFFF"}; border: 1px solid {"#C8D8EE" if mio else "#E3E8E4"}; border-radius: 14px; padding: 9px 12px; font-size: 13px; line-height: 1.38;">{txt}</div>'
    cab = f'<span style="font-size: 11.5px; color: #56615B;"><strong style="color: #17231D; font-weight: 600;">{quien}</strong> · {rol} · {hora}</span>'
    return (f'<div style="display: flex; gap: 8px; align-items: flex-end; {"flex-direction: row-reverse;" if mio else ""}">' + av(ini, col, 28) +
            f'<span style="display: flex; flex-direction: column; gap: 3px; {"align-items: flex-end;" if mio else ""}">{cab}{burb}</span></div>')
def board(f, d):
    lista = ''.join(item(x) for x in d['lista'])
    hilo = ''.join(msg(m) for m in d['hilo'])
    ctx = ''.join(f'<div style="display: flex; flex-direction: column; gap: 1px; padding: 6px 0; border-top: 1px solid #EEF1EE;"><span style="font-size: 11px; color: #56615B;">{k}</span><span style="font-size: 12.5px; font-weight: 500;">{v}</span></div>' for k, v in d['ctx'])
    part = ''.join(f'<div style="display: flex; align-items: center; gap: 8px; font-size: 12px;">{av(i, c, 24)}<span style="flex: 1; min-width: 0;"><strong style="font-weight: 600;">{n}</strong><br><span style="color: #56615B;">{r}</span></span></div>' for i, c, n, r in d['part'])
    hist = ''.join(f'<div style="display: grid; grid-template-columns: 54px 1fr; gap: 6px; font-size: 11.5px; padding: 4px 0;"><span style="color: #8A948F;">{a}</span><span><strong style="font-weight: 600;">{b}</strong> · {c}</span></div>' for a, b, c in d['hist'])
    nota = d.get('nota', '')
    html = f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Mensajes · {d["titulo"]}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>body{{margin:0;line-height:1.3;font-family:'Poppins',sans-serif;color:#17231D}} a{{color:{A};text-decoration:none;font-weight:500}}
.chip{{display:inline-flex;align-items:center;height:28px;padding:0 11px;border:1px solid #D5DED8;border-radius:999px;background:#FFFFFF;font-size:12px;white-space:nowrap;color:#17231D}} .chip.on{{background:{A};border-color:{A};color:#FFFFFF}}</style>
</helmet>
<div style="width: 1280px; height: 940px; background: #F6F8F6; position: relative; overflow: hidden;">
  <div style="display: flex; padding-top: 68px; height: 940px; box-sizing: border-box;">
    <dc-import name="IntSidebar" modo="empresa" activo="Mensajes" empresa="{d["empresa"]}" alto="872" hint-size="256px,872px"></dc-import>
    <main style="flex: 1; min-width: 0; padding: 18px 24px; display: flex; flex-direction: column; gap: 12px;">
      <div><div style="font-size: 13px; color: #56615B;">{d["empresa"]} › Mensajes</div><h1 style="margin: 0; font-size: 26px; font-weight: 700;">Mensajes</h1><p style="margin: 2px 0 0; font-size: 13px; color: #4A5650;">Cada solicitud y cada relación de trabajo tiene su hilo. Los avisos quedan escritos aquí y nada se borra: solo se archiva.</p></div>
      <div style="display: grid; grid-template-columns: 270px minmax(0,1fr) 230px; flex: 1; min-height: 0; background: #FFFFFF; border: 1px solid #E3E8E4; border-radius: 16px; overflow: hidden;">
        <div style="border-right: 1px solid #E3E8E4; padding: 10px; display: flex; flex-direction: column; gap: 4px; min-width: 0;">
          <div style="height: 36px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; gap: 8px; padding: 0 10px; font-size: 12.5px; color: #8A948F;"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5"/></svg>Buscar en mensajes</div>
          <div style="display: flex; gap: 5px; flex-wrap: wrap; padding: 6px 0;"><span class="chip on">Todos</span><span class="chip">Solicitudes</span><span class="chip">{d["chip"]}</span><span class="chip">Archivados</span></div>
          {lista}
        </div>
        <div style="display: flex; flex-direction: column; min-width: 0;">
          <div style="padding: 12px 16px; border-bottom: 1px solid #E3E8E4; display: flex; align-items: center; gap: 10px;">{av(d["h_ini"], d["h_col"])}<span style="flex: 1; min-width: 0;"><span style="display: flex; align-items: center; gap: 8px;"><strong style="font-size: 15px; font-weight: 600;">{d["h_nombre"]}</strong>{tag(d["h_tag"])}</span><span style="font-size: 12px; color: #56615B;">{d["h_sub"]}</span></span><span style="font-size: 12px; color: #56615B; display: flex; align-items: center; gap: 4px;"><svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7h18M5 7v12h14V7M9 3h6v4H9z"/></svg>Archivar</span></div>
          <div style="flex: 1; min-height: 0; overflow: hidden; padding: 14px 16px; display: flex; flex-direction: column; gap: 10px; background: #FBFCFB;">{hilo}</div>
          <div style="border-top: 1px solid #E3E8E4; padding: 10px 14px; display: flex; flex-direction: column; gap: 6px;">{nota}<div style="display: flex; gap: 8px; align-items: center;"><span style="flex: 1; height: 38px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; padding: 0 12px; font-size: 13px; color: #8A948F;">Escribe un mensaje…</span><span style="height: 38px; padding: 0 12px; border: 1px solid #D5DED8; border-radius: 10px; display: flex; align-items: center; font-size: 12.5px;">Adjuntar</span><span style="height: 38px; padding: 0 16px; border-radius: 10px; background: {A}; color: #FFFFFF; display: flex; align-items: center; font-size: 13px; font-weight: 600;">Enviar</span></div></div>
        </div>
        <aside style="border-left: 1px solid #E3E8E4; padding: 12px 14px; display: flex; flex-direction: column; gap: 10px; min-width: 0; overflow: hidden;">
          <strong style="font-size: 13px;">Sobre este hilo</strong><div>{ctx}</div>
          <strong style="font-size: 13px;">Participantes</strong><div style="display: flex; flex-direction: column; gap: 6px;">{part}</div>
          <strong style="font-size: 13px;">Historial</strong><div>{hist}</div>
          <span style="margin-top: auto; font-size: 11px; color: #56615B; line-height: 1.35; background: #F6F8F6; border-radius: 10px; padding: 8px;">Fecha, autor y cambio quedan guardados. No se puede borrar; el superadmin puede consultarlo si hay un desacuerdo.</span>
        </aside>
      </div>
    </main>
  </div>
  <div style="position: absolute; left: 0; top: 0; right: 0;"><dc-import name="IntHeader" persona="{d["persona"]}" iniciales="{d["ini"]}" color="{d["color"]}" variante="empresa" hint-size="1280px,68px"></dc-import></div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1280,"height":940}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
    open(PR + f + '.dc.html', 'w').write(html)

NOTA_COMPRADOR = '<span style="font-size: 11.5px; color: #56615B;">El comprador ve «Zucami» y el nombre de pila de quien responde; nunca teléfonos ni emails. Todo queda en este hilo.</span>'
B = {}
B['MsgFabDistribuidor'] = ('fabdist', 'DM1 · Mensajes (bandeja común): hilo fabricante ↔ distribuidor ligado al acuerdo, con los avisos de cambios por escrito', dict(
    titulo='DSM-Firmenich ↔ NutriGan', empresa='DSM-Firmenich', persona='Marta L.', ini='ML', color='#00A0A8', chip='Distribuidores',
    lista=[dict(ini='NG', col=A, n='NutriGan Distribuciones', t='10:42', tag='Distribuidor', ult='Versión local revisada. ¿Cambia la tarifa?', sel=1, nuevo=1),
           dict(ini='GO', col='#7A6A2A', n='Granja Los Olmos', t='ayer', tag='Solicitud', ult='Atiende NutriGan · Hy-D® 1,25 % · Lleida'),
           dict(ini='PL', col='#5C7F5A', n='PortuNutri Lda', t='lun', tag='Distribuidor', ult='Registro: acuerdo renovado hasta 2027'),
           dict(ini='NF', col='#2E7D4F', n='NewFarms', t='16 oct', tag='Distribuidor', ult='Registro: añadió 3 productos · por validar'),
           dict(ini='AG', col='#17231D', n='Agroolink', t='14 oct', tag='Agroolink', ult='Tu ficha de Rovabio® está publicada')],
    h_ini='NG', h_col=A, h_nombre='NutriGan Distribuciones', h_tag='Distribuidor', h_sub='Acuerdo de distribución · Vitaminas y Enzimas · Aves y Porcino · Zona Centro',
    hilo=[('evt', 'Acuerdo creado por Marta López: Vitaminas y Enzimas · Zona Centro · 58 productos', '12 mar'),
          ('evt', 'Cambio en la ficha base de <strong>Hy-D® 1,25 %</strong>: Presentación «Saco 25 kg» → «Saco 20 kg». La versión local de NutriGan queda en «Revisar cambios del fabricante».', '09:15'),
          ('m', 'Laura García', 'LG', '#2E7D4F', 'NutriGan', 'Visto. Actualizo nuestra versión local. ¿Cambia el precio de tarifa con el saco de 20 kg?', '10:02', False),
          ('evt', 'NutriGan revisó su versión local de Hy-D® 1,25 %', '10:40'),
          ('m', 'Marta López', 'ML', '#00A0A8', 'DSM-Firmenich', 'Sí, os mando la tarifa nueva por aquí antes del viernes.', '10:42', True)],
    ctx=[('Acuerdo', 'Vitaminas, Enzimas · Aves y Porcino'), ('Zona', 'España › Zona Centro · 7 provincias'), ('Vigencia', 'Hasta 31/12/2027'), ('Solicitudes de compradores', '12 abiertas · las ves en «Solicitudes»')],
    part=[('ML', '#00A0A8', 'Marta López', 'DSM-Firmenich · administradora'), ('LG', '#2E7D4F', 'Laura García', 'NutriGan · recibe las solicitudes')],
    hist=[('09:15', 'Sistema', 'cambio de ficha y aviso'), ('10:40', 'NutriGan', 'versión local revisada'), ('12 mar', 'Marta López', 'acuerdo creado')]))
B['MsgComSolicitud'] = ('comerciales', 'KM1 · Mensajes: la solicitud de un comprador es un hilo; la atiende el comercial de la zona y la Dirección comercial lo ve', dict(
    titulo='Solicitud de Avícola Montsià', empresa='Zucami', persona='Javier O.', ini='JO', color='#1E8A3C', chip='Equipo comercial',
    lista=[dict(ini='AM', col='#8A5A2B', n='Avícola Montsià', t='11:20', tag='Solicitud', ult='Laura: «¿Os viene bien el jueves a las 10?»', sel=1),
           dict(ini='LG', col='#2E7D4F', n='Laura García', t='09:05', tag='Equipo comercial', ult='Registro: 1 solicitud reasignada a Pedro Lima', nuevo=1),
           dict(ini='GO', col='#7A6A2A', n='Granja Los Olmos', t='ayer', tag='Solicitud', ult='Sin respuesta · 20 h · aviso a las 48 h'),
           dict(ini='PL', col='#7A6A2A', n='Pedro Lima', t='ayer', tag='Equipo comercial', ult='Registro: perfil sin cuenta · email enviado')],
    h_ini='AM', h_col='#8A5A2B', h_nombre='Avícola Montsià', h_tag='Solicitud', h_sub='Zucami Aviary Pro · nave nueva · 60.000 aves · Tarragona · atiende Laura García',
    hilo=[('evt', 'Solicitud recibida por la ficha de Zucami Aviary Pro · zona Cataluña → Laura García', 'ayer 16:02'),
          ('m', 'Avícola Montsià', 'AM', '#8A5A2B', 'comprador', 'Queremos pasar de jaula a aviario en 2027. ¿Podéis visitarnos?', 'ayer 16:02', False),
          ('m', 'Laura', 'LG', '#2E7D4F', 'Zucami', 'Hola, encantada. Puedo ir la semana que viene. ¿Os viene bien el jueves a las 10?', '11:20', True),
          ('evt', 'Javier Ortega (Dirección comercial) ha leído la conversación', '11:31')],
    nota=NOTA_COMPRADOR,
    ctx=[('Producto', 'Zucami Aviary Pro'), ('Comprador', 'Avícola Montsià · Tarragona · ponedoras'), ('Estado', 'En conversación · respondida en 19 h'), ('Plazo de respuesta', 'Compromiso de Zucami: 24 h')],
    part=[('AM', '#8A5A2B', 'Avícola Montsià', 'comprador'), ('LG', '#2E7D4F', 'Laura García', 'comercial de la zona'), ('JO', '#1E8A3C', 'Javier Ortega', 'Dirección comercial · lectura')],
    hist=[('16:02', 'Sistema', 'asignada por zona'), ('11:20', 'Laura García', 'primera respuesta'), ('11:31', 'Javier Ortega', 'leída')]))
B['MsgComInterno'] = ('comerciales', 'KM2 · Hilo interno Dirección comercial ↔ comercial: reasignaciones, avisos de 48 h y cambios de zona por escrito', dict(
    titulo='Dirección comercial ↔ Laura García', empresa='Zucami', persona='Javier O.', ini='JO', color='#1E8A3C', chip='Equipo comercial',
    lista=[dict(ini='LG', col='#2E7D4F', n='Laura García', t='09:05', tag='Equipo comercial', ult='Registro: 1 solicitud reasignada a Pedro Lima', sel=1),
           dict(ini='AM', col='#8A5A2B', n='Avícola Montsià', t='11:20', tag='Solicitud', ult='Laura: «¿Os viene bien el jueves a las 10?»'),
           dict(ini='JR', col='#3E6C8F', n='Javier Ruiz', t='lun', tag='Equipo comercial', ult='Registro: suplente de Laura del 20 al 27 oct'),
           dict(ini='PL', col='#7A6A2A', n='Pedro Lima', t='ayer', tag='Equipo comercial', ult='Registro: perfil sin cuenta · email enviado')],
    h_ini='LG', h_col='#2E7D4F', h_nombre='Laura García', h_tag='Equipo comercial', h_sub='Comercial · Cataluña, Aragón, Navarra, País Vasco y La Rioja · suplente: Javier Ruiz',
    hilo=[('evt', 'Zona cambiada por Javier Ortega: + La Rioja', '2 oct'),
          ('evt', 'Granja del Segre lleva 48 h sin respuesta · aviso a Dirección comercial', 'ayer 18:00'),
          ('m', 'Javier Ortega', 'JO', '#1E8A3C', 'Dirección comercial', 'Laura, ¿la puedes atender hoy o se la paso a Pedro?', 'ayer 18:05', True),
          ('m', 'Laura García', 'LG', '#2E7D4F', 'comercial', 'Pásasela a Pedro, esta semana estoy en ferias.', '08:50', False),
          ('evt', 'Solicitud de Granja del Segre reasignada de Laura García a Pedro Lima por Javier Ortega', '09:05')],
    ctx=[('Zona', 'Cataluña, Aragón, Navarra, País Vasco, La Rioja'), ('Solicitudes abiertas', '3 · media de respuesta 9 h'), ('Suplente', 'Javier Ruiz')],
    part=[('JO', '#1E8A3C', 'Javier Ortega', 'Dirección comercial'), ('LG', '#2E7D4F', 'Laura García', 'comercial')],
    hist=[('09:05', 'Javier Ortega', 'reasignó 1 solicitud'), ('ayer', 'Sistema', 'aviso de 48 h'), ('2 oct', 'Javier Ortega', 'cambió la zona')]))
B['MsgSedeSucursal'] = ('sucursales', 'SM1 · Hilo Sede ↔ sucursal: activaciones, versiones locales y cambios de la ficha base quedan por escrito', dict(
    titulo='Sede ↔ Big Dutchman LATAM', empresa='Big Dutchman', persona='Anna B.', ini='AB', color='#B5121B', chip='Sucursales',
    lista=[dict(ini='BL', col='#2F6F8F', n='Big Dutchman LATAM', t='12:10', tag='Sucursal', ult='Activado ChickBox en México', sel=1, nuevo=1),
           dict(ini='BI', col='#B5121B', n='Big Dutchman Ibérica', t='ayer', tag='Sucursal', ult='Registro: Lucía Pérez se unió (invitada)'),
           dict(ini='BA', col='#8A1020', n='Big Dutchman Asia', t='lun', tag='Sucursal', ult='Pide a la Sede: ficha de EcoNest'),
           dict(ini='GR', col='#7A6A2A', n='Granjas del Bajío', t='lun', tag='Solicitud', ult='Atiende Big Dutchman LATAM · México')],
    h_ini='BL', h_col='#2F6F8F', h_nombre='Big Dutchman LATAM', h_tag='Sucursal', h_sub='Sucursal · México, Colombia, Perú · 18 productos activos',
    hilo=[('evt', 'Nueva versión de la ficha base <strong>ChickBox</strong> (capacidad y consumo). La versión local de México queda en «Revisar cambios de la Sede».', 'lun'),
          ('m', 'Carlos Méndez', 'CM', '#2F6F8F', 'Big Dutchman LATAM', 'Revisado. En México lo vendemos con ventilación reforzada, lo añado en nuestra versión.', '11:58', False),
          ('evt', 'Big Dutchman LATAM activó ChickBox en México con versión local (+ dato propio: ventilación reforzada)', '12:10'),
          ('m', 'Anna Becker', 'AB', '#B5121B', 'Sede', 'Perfecto. Si algún cliente pregunta por Perú, nos lo pasáis por aquí.', '12:14', True)],
    ctx=[('Sucursal', 'Big Dutchman LATAM, S.A. de C.V.'), ('Países', 'México, Colombia, Perú'), ('Qué decide la sucursal', 'Activar productos, versión local, precios y contacto')],
    part=[('AB', '#B5121B', 'Anna Becker', 'Sede · administradora'), ('CM', '#2F6F8F', 'Carlos Méndez', 'LATAM · administrador')],
    hist=[('12:10', 'Carlos Méndez', 'activó ChickBox (MX)'), ('lun', 'Sistema', 'cambio de ficha base'), ('3 oct', 'Anna Becker', 'añadió Perú')]))
B['MsgSucursalSede'] = ('sucursal', 'U2 · Mensajes de la sucursal: su hilo con la Sede guarda el alta, los avisos y lo que pide la Sede', dict(
    titulo='Aviagen Ibérica ↔ Sede', empresa='Aviagen Ibérica', persona='Pablo R.', ini='PR', color='#C8102E', chip='Sede',
    lista=[dict(ini='AV', col='#8A1020', n='Aviagen · Sede', t='10:30', tag='Sede', ult='La Sede publicó Ross 308 (nueva versión)', sel=1, nuevo=1),
           dict(ini='GA', col='#7A6A2A', n='Granja Avícola del Duero', t='ayer', tag='Solicitud', ult='Pablo: «Te paso disponibilidad de pollitos»'),
           dict(ini='AG', col='#17231D', n='Agroolink', t='15 oct', tag='Agroolink', ult='Te has unido a Aviagen Ibérica')],
    h_ini='AV', h_col='#8A1020', h_nombre='Aviagen · Sede', h_tag='Sede', h_sub='Sede del grupo · la marca, el catálogo y las especies vienen de aquí',
    hilo=[('evt', 'Pablo Ruiz se unió a Aviagen Ibérica (sucursal) y entró directamente · aviso a la Sede y al superadmin', '15 oct'),
          ('m', 'Emma Clark', 'EC', '#8A1020', 'Sede', 'Bienvenido, Pablo. Activa Ross 308 y Ross 708 para España y Portugal cuando tengas la versión local.', '15 oct', False),
          ('evt', 'La Sede publicó una nueva versión de <strong>Ross 308</strong> (índices 2026). Tu versión local queda en «Revisar cambios de la Sede».', '10:30'),
          ('m', 'Pablo Ruiz', 'PR', '#C8102E', 'Aviagen Ibérica', 'Recibido. Lo reviso hoy y actualizo la versión de España.', '10:41', True)],
    ctx=[('Sucursal', 'Aviagen Ibérica, S.L. · España y Portugal'), ('Productos', '2 activos · 1 por revisar'), ('La Sede decide', 'Marca, catálogo base y especies')],
    part=[('PR', '#C8102E', 'Pablo Ruiz', 'Aviagen Ibérica · administrador'), ('EC', '#8A1020', 'Emma Clark', 'Sede · administradora')],
    hist=[('10:30', 'Sistema', 'cambio de ficha base'), ('15 oct', 'Sistema', 'alta de la sucursal'), ('15 oct', 'Emma Clark', 'mensaje')]))
B['MsgDisFabricante'] = ('distmulti', 'XM1 · Hilo distribuidor ↔ fabricante: la validación de la marca y sus motivos quedan por escrito', dict(
    titulo='NewFarms ↔ Zucami', empresa='NewFarms', persona='Laura G.', ini='LG', color='#2E7D4F', chip='Marcas',
    lista=[dict(ini='ZU', col='#1E8A3C', n='Zucami', t='13:05', tag='Fabricante', ult='Validó 2 productos y rechazó 1', sel=1, nuevo=1),
           dict(ini='DF', col='#00A0A8', n='DSM-Firmenich', t='lun', tag='Fabricante', ult='Registro: acuerdo activo · 3 productos'),
           dict(ini='HE', col='#8A5A2B', n='Huevos del Ebro SL', t='ayer', tag='Solicitud', ult='Atiende la delegación de Zaragoza'),
           dict(ini='GO', col='#7A6A2A', n='Granja Los Olmos', t='lun', tag='Solicitud', ult='Atiende la delegación de Lleida')],
    h_ini='ZU', h_col='#1E8A3C', h_nombre='Zucami', h_tag='Fabricante', h_sub='Marca que vendes · 3 productos enviados a validar',
    hilo=[('evt', 'NewFarms añadió 3 productos de Zucami a su catálogo · pendientes de validación de la marca', '16 oct'),
          ('evt', 'Zucami validó <strong>Aviary Pro</strong> y <strong>Nest Pro</strong> · rechazó <strong>ClimaLine</strong>', '13:05'),
          ('m', 'Javier Ortega', 'JO', '#1E8A3C', 'Zucami', 'ClimaLine solo lo vende nuestro equipo comercial en Aragón. Los otros dos, adelante.', '13:05', False),
          ('m', 'Laura García', 'LG', '#2E7D4F', 'NewFarms', 'Entendido, lo quitamos de Aragón. ¿Podemos ofrecerlo en Navarra?', '13:20', True)],
    ctx=[('Marca', 'Zucami · fabricante'), ('Productos', '2 validados · 1 rechazado'), ('Zonas', 'NewFarms: España y Portugal')],
    part=[('LG', '#2E7D4F', 'Laura García', 'NewFarms · administradora'), ('JO', '#1E8A3C', 'Javier Ortega', 'Zucami · Dirección comercial')],
    hist=[('13:05', 'Javier Ortega', 'validó 2, rechazó 1'), ('16 oct', 'Laura García', 'añadió 3 productos')]))
B['MsgDisSolicitud'] = ('distmulti', 'XM2 · Solicitud atendida por una delegación: el comprador escribe a NewFarms y queda todo en el hilo', dict(
    titulo='Solicitud de Huevos del Ebro', empresa='NewFarms', persona='Laura G.', ini='LG', color='#2E7D4F', chip='Marcas',
    lista=[dict(ini='HE', col='#8A5A2B', n='Huevos del Ebro SL', t='12:40', tag='Solicitud', ult='Delegación Zaragoza: «Os mando oferta»', sel=1),
           dict(ini='ZU', col='#1E8A3C', n='Zucami', t='13:05', tag='Fabricante', ult='Validó 2 productos y rechazó 1', nuevo=1),
           dict(ini='GO', col='#7A6A2A', n='Granja Los Olmos', t='lun', tag='Solicitud', ult='Atiende la delegación de Lleida')],
    h_ini='HE', h_col='#8A5A2B', h_nombre='Huevos del Ebro SL', h_tag='Solicitud', h_sub='Zucami EggFlow (vendido por NewFarms) · Zaragoza · atiende la delegación de Zaragoza',
    hilo=[('evt', 'Solicitud recibida por la ficha de Zucami EggFlow · comprador en Zaragoza → delegación de Zaragoza', 'ayer 09:12'),
          ('m', 'Huevos del Ebro', 'HE', '#8A5A2B', 'comprador', 'Necesitamos reponer la recogida de huevos de dos naves. ¿Plazo de entrega?', 'ayer 09:12', False),
          ('m', 'Sergio', 'SM', '#2E7D4F', 'NewFarms · Zaragoza', 'Hola, tenemos stock para una nave; la segunda en 3 semanas. Os mando oferta hoy.', '12:40', True)],
    nota=NOTA_COMPRADOR.replace('Zucami', 'NewFarms'),
    ctx=[('Producto', 'Zucami EggFlow · marca validada'), ('Delegación', 'Zaragoza'), ('Estado', 'En conversación')],
    part=[('HE', '#8A5A2B', 'Huevos del Ebro SL', 'comprador'), ('SM', '#2E7D4F', 'Sergio Martín', 'NewFarms · delegación de Zaragoza'), ('LG', '#2E7D4F', 'Laura García', 'NewFarms · lectura')],
    hist=[('09:12', 'Sistema', 'asignada a Zaragoza'), ('12:40', 'Sergio Martín', 'primera respuesta')]))
for f, (pg, t, d) in B.items(): board(f, d)
c = json.load(open(PR + 'canvas.json')); BB = c['boards']
porpag = {}
for f, (pg, t, d) in B.items(): porpag.setdefault(pg, []).append((f, t))
for pg, lst in porpag.items():
    y0 = max(b['y'] + b['h'] for k, b in BB.items() if b['page'] == pg and not k.startswith('Msg')) + 400
    for i, (f, t) in enumerate(lst):
        BB[f + '.dc.html'] = {'w': 1280, 'h': 940, 'page': pg, 'x': i * 1360, 'y': y0, 'title': t}
        if f + '.dc.html' not in c['order']: c['order'].append(f + '.dc.html')
    c['notes']['msg_' + pg] = {'kind': 'title1', 'maxW': 4000, 'page': pg, 'w': 240, 'x': 0, 'y': y0 - 300,
        'text': 'Mensajes con constancia · cada solicitud y cada relación de trabajo tiene su hilo; los avisos quedan escritos en él y nada se borra (solo se archiva). Misma bandeja en todas las empresas.'}
json.dump(c, open(PR + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok', {pg: len(l) for pg, l in porpag.items()})
