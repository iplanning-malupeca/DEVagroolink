"""Alta empresa (18/10/2026, comentario en D0a): el nombre de la organización se escribe al empezar
y, si ninguna del CRM es la tuya, se crea en una pantalla nueva (D0a-2, K0a-2, S0a-2, U0a-2, X0a-2)."""
import json, os, re
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PR = W + '/project/'
# pagina, prefijo, pantalla CRM, verificar, código, nombre, dominio, atributos del shell, nota, sucursal
ESC = [
 ('fabdist', 'Fab', 'FabCRMVarias', 'FabVerifica', 'D', 'DSM-Firmenich', 'dsm-firmenich.com', '', 'fabT1', None),
 ('comerciales', 'Com', 'ComCRM', 'ComVerifica', 'K', 'Zucami', 'zucami.com', ' empresa="Zucami" persona="Javier Ortega" iniciales="JO" paso4="Equipo comercial"', 'comT1', None),
 ('sucursales', 'Suc', 'SucCRM', 'SucVerifica', 'S', 'Big Dutchman', 'bigdutchman.com', ' empresa="Big Dutchman" persona="Anna Becker" iniciales="AB" paso4="Sucursales"', 'sucT1', None),
 ('sucursal', 'SucAlta', 'SucAltaCRM', 'SucAltaVerifica', 'U', 'Aviagen Ibérica', 'aviagen.com', ' empresa="Aviagen Ibérica" persona="Pablo Ruiz" iniciales="PR" paso4="Equipo y contacto"', 'sucT3', 'Aviagen'),
 ('distmulti', 'Dis', 'DisCRM', 'DisVerifica', 'X', 'NewFarms', 'newfarms.es', ' empresa="NewFarms" persona="Laura García" iniciales="LG" paso4="Marcas"', 'disT1', None),
]
LUPA = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#56615B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5"/></svg>'
MAS = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;"><path d="M12 5v14M5 12h14"/></svg>'
INFO = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#1D4E89" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none; margin-top: 1px;"><path d="M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM12 11v5M12 8h.01"/></svg>'

def campo_nombre(nombre):
    return ('<label style="display: flex; align-items: center; gap: 10px; height: 44px; box-sizing: border-box; border: 1.5px solid #1D4E89; border-radius: 12px; background: #FFFFFF; padding: 0 14px;">' + LUPA +
            '<span style="font-size: 12px; font-weight: 600; color: #56615B; white-space: nowrap;">Nombre de tu organización</span>'
            f'<input type="search" value="{nombre}" aria-label="Nombre de tu organización" style="flex: 1; min-width: 0; border: 0; outline: none; font: 600 15px \'Poppins\', sans-serif; color: #17231D; background: none;">'
            '<span style="font-size: 12px; color: #8A948F; white-space: nowrap;">o razón social, marca, CIF/VAT</span></label>')

def crear_link(pref, nombre):
    return (f'<a href="{pref}Crear.dc.html" style="display: flex; align-items: center; gap: 10px; height: 42px; box-sizing: border-box; padding: 0 14px; border: 1.5px dashed #1D4E89; border-radius: 12px; color: #1D4E89; font-size: 13.5px; font-weight: 600; background: #FFFFFF;">'
            f'{MAS}Ninguna es la mía: crear «{nombre}»<span style="margin-left: auto; font-size: 12px; font-weight: 400; color: #56615B;">Empiezas con una ficha en blanco</span></a>')

def f(l, v='', ph='', ayuda=''):
    val = f' value="{v}"' if v else ''
    return (f'<label style="display: flex; flex-direction: column; gap: 5px; font-size: 13px; font-weight: 500; min-width: 0;">{l}'
            f'<input{val} placeholder="{ph}" style="height: 38px; border: 1px solid #D5DED8; border-radius: 10px; padding: 0 12px; font: 400 14px \'Poppins\', sans-serif; color: #17231D; background: #FFFFFF; width: 100%; box-sizing: border-box;">'
            + (f'<span style="font-size: 12px; font-weight: 400; color: #56615B;">{ayuda}</span>' if ayuda else '') + '</label>')

def pantalla_crear(pref, crm, verif, cod, nombre, dom, shell, grupo):
    extra = ''
    if grupo:
        extra = (f'<div style="grid-column: 1 / -1; display: flex; align-items: center; gap: 12px; padding: 10px 14px; border-radius: 12px; background: #F3F7FC; border: 1px solid #C8D8EE; font-size: 13px;">'
                 f'<span style="width: 34px; height: 34px; border-radius: 9px; background: #8A1020; color: #FFF; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center; flex: none;">AV</span>'
                 f'<span style="flex: 1;"><strong style="font-weight: 600;">Sucursal de {grupo}</strong> · la marca, el catálogo y las especies vienen de la Sede</span><a href="#" style="font-size: 12.5px;">Cambiar</a></div>')
    nota = ('Entra directamente: avisamos a la Sede de ' + grupo + ' y al superadmin, que la añade al CRM.') if grupo else \
           'Entra directamente y tú serás su primera persona administradora. El equipo de Agroolink la revisa y la añade al CRM; si ya existía, las une.'
    cuerpo = (
      '<div><span style="font-size: 11.5px; font-weight: 600; letter-spacing: .09em; color: #56615B;">ANTES DE EMPEZAR</span>'
      f'<h1 style="margin: 4px 0 0; font-size: 27px; font-weight: 700;">Crear {"tu sucursal" if grupo else "tu organización"}</h1>'
      f'<p style="margin: 4px 0 0; font-size: 13.5px; color: #4A5650;">«{nombre}» no está en Agroolink. Con el nombre basta para empezar; lo demás puedes completarlo ahora o más tarde.</p></div>'
      '<div style="background: #FFFFFF; border: 1px solid #E6EBE7; border-radius: 16px; padding: 18px 20px; display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 14px 18px;">'
      + extra
      + f('Nombre de la organización', nombre, '', 'Es el nombre que verán los compradores')
      + f('Razón social', '', 'Por ejemplo: ' + nombre + ', S.L.')
      + f('CIF / VAT', '', 'Para no duplicar empresas')
      + f('País de la sede', 'España' if grupo or pref in ('Com', 'Dis') else '', 'Elige el país')
      + f('Web', dom, '')
      + f('Email de empresa', 'tu email @' + dom, '', 'Te enviaremos un código para confirmarlo')
      + '</div>'
      f'<div style="display: flex; gap: 10px; align-items: flex-start; padding: 10px 14px; border-radius: 12px; background: #F6F8F6; font-size: 12.5px; color: #33424C; line-height: 1.4;">{INFO}<span>{nota}</span></div>'
      f'<div style="display: flex; gap: 10px; align-items: center; margin-top: auto;"><a href="{crm}.dc.html" style="height: 44px; padding: 0 18px; border-radius: 10px; border: 1px solid #D5DED8; color: #17231D; font-size: 14px; display: flex; align-items: center;">Volver a buscar</a>'
      f'<a href="{verif}.dc.html" style="height: 44px; padding: 0 22px; border-radius: 10px; background: #1D4E89; color: #FFF; font-size: 14px; display: flex; align-items: center;">Crear y continuar</a>'
      '<span style="font-size: 12px; color: #56615B;">Después confirmaremos tu email de empresa con un código.</span></div>')
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + ('Sucursal' if grupo else 'Empresa') + ' · Crear ' + ('tu sucursal' if grupo else 'tu organización') + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\nbody{margin:0;line-height:1.3;font-family:\'Poppins\',sans-serif;color:#17231D}\na{color:#1D4E89;text-decoration:none;font-weight:500}\n</style>\n</helmet>\n'
            '<div style="width: 1280px; height: 940px; position: relative; overflow: hidden;">\n'
            f'  <div style="position: absolute; inset: 0;"><dc-import name="FabShell" activo="{{{{ n }}}}"{shell} hint-size="1280px,940px"></dc-import></div>\n'
            f'  <div style="position: absolute; top: 64px; left: 260px; right: 0; bottom: 72px; padding: 24px 32px 20px; display: flex; flex-direction: column; gap: 14px;">{cuerpo}</div>\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":1280,"height":940}}\'>\nclass Component extends DCLogic {\n  renderVals() { return { n: 1 }; }\n}\n</script>\n</body>\n</html>\n')

c = json.load(open(PR + 'canvas.json')); B = c['boards']
for page, pref, crm, verif, cod, nombre, dom, shell, nota, grupo in ESC:
    p = PR + crm + '.dc.html'; s = open(p).read()
    if 'Nombre de tu organización' not in s:
        a = 'Con tu email <strong>@'
        assert s.count(a) == 1, crm
        s = s.replace(a, 'Escribe el nombre de tu organización. Con él y tu email <strong>@', 1)
        s = s.replace('</p></div>', '</p></div>' + campo_nombre(nombre), 1)
        s, k = re.subn(r'<div style="display: flex; align-items: center; gap: 10px;"><span style="flex: 1; display: flex; align-items: center; gap: 8px; height: 40px;.*?</div>', lambda m: crear_link(pref, nombre), s, count=1, flags=re.S)
        assert k == 1, crm
        s = s.replace('gap: 12px;"><div><span style="font-size: 11.5px; font-weight: 600; letter-spacing: .09em', 'gap: 10px;"><div><span style="font-size: 11.5px; font-weight: 600; letter-spacing: .09em', 1)
        open(p, 'w').write(s)
    nuevo = pref + 'Crear.dc.html'
    open(PR + nuevo, 'w').write(pantalla_crear(pref, crm, verif, cod, nombre, dom, shell, grupo))
    t = B[crm + '.dc.html']['title']; cod0 = t.split(' ·')[0]
    B[crm + '.dc.html']['title'] = cod0 + ' · ¿Cuál es tu empresa? Escribes el nombre y eliges entre las del CRM'
    if nuevo not in B:
        y0 = B[crm + '.dc.html']['y']; x0 = B[crm + '.dc.html']['x']
        for k, b in B.items():
            if b.get('page') == page and b['y'] == y0 and b['x'] > x0: b['x'] += 1360
        B[nuevo] = {'w': 1280, 'h': 940, 'page': page, 'x': x0 + 1360, 'y': y0,
                    'title': cod0 + '-2 · Ninguna es la mía: crear ' + ('la sucursal' if grupo else 'la organización') + ' (basta con el nombre)'}
        c['order'].insert(c['order'].index(crm + '.dc.html') + 1, nuevo)
        n = c['notes'][nota]; n['text'] = n['text'].replace(cod0 + ' ', cod0 + ' nombre y empresa del CRM · ' + cod0 + '-2 crear si no está · ', 1) if 'crear si no está' not in n['text'] else n['text']
        n['maxW'] = max(n.get('maxW', 4000), 16000)
json.dump(c, open(PR + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
