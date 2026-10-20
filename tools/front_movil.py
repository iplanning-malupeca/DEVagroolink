"""Front de Agroolink en móvil (390 px): versión móvil de las páginas de «Agroolink Frontend» (comunes, home, categoría, especie,
producto, empresa, expertos, eventos y ventanas). Reglas móviles del proyecto: logo oficial; arriba logo, Buscar y Mensajes; abajo
Explorar · Proyectos · Tableros · Tú (sin sesión: «Entrar»); buscador «¿Qué buscas?» que abre la búsqueda combinada; filtros con el
botón «Filtros» con contador y un botón por filtro; las ventanas son hojas inferiores. Sin teléfonos, emails ni webs.
Uso: python3 tools/front_movil.py <carpeta>/project   → escribe Mv*.dc.html y movil.json"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from front_piezas import DEST, IMG, CAT, ESP, PROD
import front_paginas, front_fichas  # imágenes de páginas y fichas
from front_paginas import LISTA
from front_fichas import EXP

V = '#0E5A3A'
LOGO = '<img src="' + IMG['logo'] + '" alt="Agroolink" style="height:24px;width:auto;display:block">'
CSS = """*{box-sizing:border-box}body{margin:0}.m{font-family:'Poppins',system-ui,sans-serif;color:#17231D;font-size:14px;line-height:1.38}
a{color:#0E5A3A;text-decoration:none;font-weight:600}
.sb{height:44px;display:flex;align-items:center;justify-content:space-between;padding:0 26px 0 30px;font-size:15px;font-weight:600;background:#FFFFFF}
.top{height:56px;display:flex;align-items:center;gap:4px;padding:0 6px 0 16px;background:#FFFFFF;border-bottom:1px solid #E3E8E4}
.ib{width:44px;height:44px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;color:#17231D;position:relative;flex:none;background:none;border:0}
.bdg{position:absolute;top:5px;right:3px;min-width:18px;height:18px;padding:0 5px;border-radius:9px;background:#D93A3A;color:#FFFFFF;font-size:10.5px;font-weight:600;display:flex;align-items:center;justify-content:center;border:2px solid #FFFFFF}
.card{background:#FFFFFF;border:1px solid #E6EBE7;border-radius:16px;overflow:hidden}
.pad{padding:12px 14px}
.hint{font-size:12px;color:#56615B}
.h2{margin:0;font-size:19px;font-weight:700}
.kick{font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.btn{height:44px;border-radius:12px;background:#0E5A3A;color:#FFFFFF;font:600 14.5px 'Poppins',sans-serif;border:0;display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:0 16px;white-space:nowrap;text-decoration:none}
.btn2{height:44px;border-radius:12px;background:#FFFFFF;color:#0E5A3A;border:1.5px solid #0E5A3A;font:600 14.5px 'Poppins',sans-serif;display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:0 16px;white-space:nowrap;text-decoration:none}
.chip{display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 14px;border-radius:999px;border:1px solid #DCE4DE;background:#FFFFFF;font-size:13px;font-weight:500;white-space:nowrap;flex:none;color:#17231D}
.chip.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}
.fil{background:#EEF6EE;border:1.5px solid #0E5A3A;color:#0E5A3A;font-weight:600}
.row{display:flex;gap:8px;overflow:hidden}
.tag{font-size:11.5px;padding:2px 8px;border-radius:999px;background:#F1F4F2;white-space:nowrap}
.tbi{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:10.5px;font-weight:500;color:#56615B;min-height:56px}
.tbp{width:54px;height:30px;border-radius:15px;display:flex;align-items:center;justify-content:center}
.ov{position:absolute;inset:0;background:rgba(7,43,30,.45)}
.sheet{position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-radius:22px 22px 0 0;padding:8px 16px 30px;display:flex;flex-direction:column;gap:12px}
.campo{min-height:46px;border:1px solid #D5DED8;border-radius:12px;padding:11px 12px;font-size:14px;color:#8A948F;background:#FFFFFF}
.lbl{font-size:13px;font-weight:600}"""

def svg(d, s=22, w=1.8):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex:none">%s</svg>' % (s, s, w, ''.join('<path d="%s"/>' % p for p in d.split('|')))
I = {'lupa': 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5', 'proy': 'M3 21V10l9-6 9 6v11M2 21h20M9 21v-6h6v6M9 11h6', 'tab': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z',
     'mail': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6', 'back': 'M15 6l-6 6 6 6', 'der': 'm9 6 6 6-6 6', 'flecha': 'M5 12h14M13 6l6 6-6 6',
     'filtro': 'M4 6h16M7 12h10M10 18h4', 'pata': 'M8 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM16 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM5 15a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM19 15a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM12 13c-3 0-5 3-5 5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2c0-2-2-5-5-5z',
     'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z', 'virus': 'M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM12 2v4M12 18v4M2 12h4M18 12h4M5 5l2.8 2.8M16.2 16.2 19 19M5 19l2.8-2.8M16.2 7.8 19 5',
     'pais': 'M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z', 'marca': 'M3 12V4h8l9 9-8 8zM7.5 7.5h.01', 'ok': 'M5 12l5 5 9-10', 'x': 'M6 6l12 12M18 6 6 18',
     'guardar': 'M6 3h12v18l-6-4-6 4z', 'comp': 'M4 5h7v14H4zM13 5h7v14h-7z', 'compartir': 'M18 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM18 22a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM8.6 13.5l6.8 4M15.4 6.5l-6.8 4',
     'msg': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6', 'descarga': 'M12 4v12M6 10l6 6 6-6M4 20h16', 'video': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM10 8.5v7l6-3.5z',
     'carro': 'M3 4h2l2.4 11h11L21 7H6.2M10 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM17 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2z', 'manos': 'M8 13l3 3 6-6M3 12l4-4 3 2 4-3 3 2 4 4-4 5-3-1',
     'persona': 'M12 4a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM4 21a8 8 0 0 1 16 0', 'cal': 'M4 6h16v14H4zM4 10h16M8 3v4M16 3v4', 'play': 'M8 5v14l11-7z', 'candado': 'M6 11h12v10H6zM9 11V7a3 3 0 0 1 6 0v4',
     'mapa': 'M9 4 3 6v14l6-2 6 2 6-2V4l-6 2zM9 4v14M15 6v14', 'info': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 8v5M12 16h.01', 'campana': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4',
     'hoja': 'M5 19c0-8 5-13 14-14-1 9-6 14-14 14zM5 19l7-7', 'escudo': 'M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6zM9 12l2 2 4-4', 'mas': 'M12 5v14M5 12h14', 'globo': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18',
     'nutri': 'M4 20c0-8 6-14 16-16-2 10-8 16-16 16zM4 20 14 10', 'salud': 'M12 5v14M5 12h14', 'gen': 'M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3',
     'equipo': 'M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1', 'inst': 'M5 21V4h14v17M9 8h2M13 8h2M9 12h2M13 12h2M9 16h2M13 16h2M3 21h18',
     'tec': 'M7 7h10v10H7zM10 10h4v4h-4zM9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4', 'serv': 'M9 4a3 3 0 1 1 0 6 3 3 0 0 1 0-6zM3 20a6 6 0 0 1 12 0M17 11l2 2 4-4', 'sost': 'M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5'}
SB = ('<div class="sb"><span>9:41</span><span style="display:flex;gap:6px;align-items:center"><svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="1" fill="#17231D"/><rect x="5" y="5" width="3" height="7" rx="1" fill="#17231D"/><rect x="10" y="2.5" width="3" height="9.5" rx="1" fill="#17231D"/><rect x="15" y="0" width="3" height="12" rx="1" fill="#17231D"/></svg>'
      '<svg width="26" height="12" viewBox="0 0 26 12" aria-hidden="true"><rect x=".5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="#17231D" opacity=".4"/><rect x="2" y="2" width="17" height="8" rx="2" fill="#17231D"/></svg></span></div>')

def top(sesion=True):
    der = ('<button type="button" class="ib" aria-label="Mensajes, 3 sin leer">' + svg(I['mail']) + '<span class="bdg">3</span></button>') if sesion else ''
    return '<div class="top"><span style="flex:1;display:flex;align-items:center">' + LOGO + '</span><button type="button" class="ib" aria-label="Buscar">' + svg(I['lupa']) + '</button>' + der + '</div>'
def atras(t, sub=''):
    return ('<div class="top" style="padding-left:4px"><button type="button" class="ib" aria-label="Volver">' + svg(I['back'], 22, 2) + '</button><span style="flex:1;min-width:0;display:flex;flex-direction:column;line-height:1.2"><strong style="font-size:15.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + t + '</strong>' +
            ('<span class="hint" style="white-space:nowrap;overflow:hidden;text-overflow:ellipsis">' + sub + '</span>' if sub else '') + '</span><button type="button" class="ib" aria-label="Compartir">' + svg(I['compartir'], 20) + '</button><button type="button" class="ib" aria-label="Guardar">' + svg(I['guardar'], 20) + '</button></div>')
def buscador():
    return ('<button type="button" style="width:100%;height:56px;border-radius:999px;border:1px solid #DCE3DE;background:#FFFFFF;box-shadow:0 2px 10px rgba(16,40,28,.08);display:flex;align-items:center;gap:12px;padding:0 6px 0 18px;text-align:left;font-family:inherit">'
            '<span style="color:#0E5A3A">' + svg(I['lupa'], 20, 2) + '</span><span style="flex:1;display:flex;flex-direction:column;line-height:1.25"><strong style="font-size:14px;color:#17231D">¿Qué buscas?</strong><span style="font-size:12px;color:#56615B">Cualquier especie · categoría · enfermedad</span></span>'
            '<span style="width:44px;height:44px;border-radius:50%;background:#0E5A3A;color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg(I['filtro'], 18, 2.2) + '</span></button>')
def tabbar(activo='Explorar', sesion=True):
    items = [('lupa', 'Explorar'), ('proy', 'Proyectos'), ('tab', 'Tableros'), (None, 'Tú' if sesion else 'Entrar')]
    h = '<nav aria-label="Menú" style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;z-index:6"><div style="display:flex;padding:2px 6px 0">'
    for ic, t in items:
        on = t == activo
        if ic: icon = svg(I[ic], 22, 2.1 if on else 1.8)
        elif sesion: icon = '<span style="width:26px;height:26px;border-radius:50%;background:#0E5A3A;color:#FFFFFF;font-size:10.5px;font-weight:600;display:flex;align-items:center;justify-content:center">SE</span>'
        else: icon = svg(I['persona'], 22)
        h += '<span class="tbi" style="' + ('color:#0E5A3A;font-weight:600' if on else '') + '"><span class="tbp" style="background:' + ('#E4F0D0' if on else 'transparent') + '">' + icon + '</span>' + t + '</span>'
    return h + '</div><div style="height:26px;display:flex;align-items:center;justify-content:center"><span style="width:134px;height:5px;border-radius:3px;background:#17231D"></span></div></nav>'
def wrap(title, h, body):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + title + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n<div class="m" style="width: 390px; height: ' + str(h) + 'px; position: relative; overflow: hidden; background: #F6F8F6;">' + body + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":390,"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')
def pagina(cuerpo, cab=None, activo='Explorar', sesion=True, fondo_pie=True):
    return SB + (cab if cab is not None else top(sesion)) + '<div style="display:flex;flex-direction:column">' + cuerpo + (pie() if fondo_pie else '') + '<div style="height:84px"></div></div>' + tabbar(activo, sesion)
def sec(t, ver=''):
    return '<div style="display:flex;align-items:baseline;justify-content:space-between;padding:0 16px 10px"><h2 class="h2">' + t + '</h2>' + ('<a href="#" style="font-size:13px">' + ver + '</a>' if ver else '') + '</div>'
def bloque(cont, pad='22px 0 0'):
    return '<section style="padding:' + pad + '">' + cont + '</section>'
def scroll(items, gap=10):
    return '<div style="display:flex;gap:' + str(gap) + 'px;overflow:hidden;padding:0 16px">' + items + '</div>'
def migas(*ls):
    return '<div class="hint" style="padding:12px 16px 0;display:flex;gap:4px;flex-wrap:wrap">' + ' › '.join(ls[:-1]) + ' › <strong style="color:#17231D;font-weight:500">' + ls[-1] + '</strong></div>'
def tag(t, f='#F1F4F2', c='#17231D'):
    return '<span class="tag" style="background:' + f + ';color:' + c + '">' + t + '</span>'
VERIF = '<span style="color:#0E5A3A;display:inline-flex">' + svg(I['escudo'], 14, 2) + '</span>'

# ---------- comunes ----------
def pie():
    col = lambda t, ls: '<div style="display:flex;flex-direction:column;gap:8px"><span class="kick" style="color:#FFFFFF">' + t + '</span>' + ''.join('<a href="#" style="font-weight:400;color:#B9CFC2;font-size:13.5px">' + l + '</a>' for l in ls) + '</div>'
    return ('<footer style="margin-top:32px;background:#072B1E;color:#FFFFFF;padding:28px 20px 24px;display:flex;flex-direction:column;gap:20px"><img src="' + IMG['logo_b'] + '" alt="Agroolink" style="height:28px;width:auto;align-self:flex-start">'
            '<p style="margin:0;color:#B9CFC2;font-size:13.5px">La plataforma B2B para encontrar, comparar y pedir productos y servicios para la producción animal.</p>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px">' + col('Explorar', ['Categorías', 'Especies', 'Empresas', 'Expertos']) + col('Para empresas', ['Publicar catálogo', 'Planes y precios']) + col('Ayuda', ['Centro de ayuda', 'Términos de uso', 'Privacidad']) + '</div>'
            '<span style="display:flex;gap:8px"><span class="chip" style="background:transparent;color:#FFFFFF;border-color:#2E5A47">' + svg(I['globo'], 16) + 'Español</span><span class="chip" style="background:transparent;color:#FFFFFF;border-color:#2E5A47">' + svg(I['pais'], 16) + 'España</span></span>'
            '<span style="font-size:12px;color:#8FAE9D;border-top:1px solid #1E4A38;padding-top:14px">© 2026 Agroolink</span></footer>')
def mv_cabecera(sesion):
    return SB + top(sesion) + '<div style="padding:14px 16px">' + buscador() + '</div>' + tabbar('Explorar', sesion)
def mv_pie():
    return SB + top() + pie() + tabbar()

# ---------- home ----------
def tarjeta_prod(k, cat, n, m, ok, esp, w=None):
    return ('<article class="card" style="' + ('width:' + str(w) + 'px;flex:none;' if w else '') + 'display:flex;flex-direction:column"><img src="' + IMG[k] + '" alt="' + n + '" style="width:100%;height:118px;object-fit:cover;display:block">'
            '<div style="padding:10px 12px 12px;display:flex;flex-direction:column;gap:3px;flex:1"><span class="hint" style="font-size:11px">' + cat + '</span><strong style="font-size:14px;line-height:1.25">' + n + '</strong>'
            '<span style="font-size:12px;color:#4A5650;display:flex;gap:4px;align-items:center">' + m + (VERIF if ok else '') + '</span><span style="flex:1"></span>'
            '<span style="display:flex;gap:6px;padding-top:8px"><a href="#" class="btn2" style="flex:1;height:36px;font-size:12.5px;padding:0">Comparar</a><a href="#" class="btn" style="flex:1;height:36px;font-size:12.5px;padding:0">Ver ficha</a></span></div></article>')
def mv_home():
    esp = ''.join('<a href="#" class="card" style="width:112px;flex:none;color:#17231D"><img src="' + IMG[k] + '" alt="" style="width:100%;height:80px;object-fit:cover;display:block"><span style="display:block;padding:8px 10px;font-size:13px;font-weight:600">' + t + '</span></a>' for t, k, n in ESP)
    cats = ''.join('<a href="#" class="card pad" style="display:flex;flex-direction:column;gap:6px;color:#17231D"><span style="width:36px;height:36px;border-radius:10px;background:#EEF6EE;color:#0E5A3A;display:flex;align-items:center;justify-content:center">' + svg(I[ic], 19) + '</span><strong style="font-size:13.5px;font-weight:600">' + n + '</strong></a>' for n, ic, d in CAT)
    prods = ''.join(tarjeta_prod(*p, w=176) for p in LISTA[:4])
    cuerpo = ('<div style="padding:16px 16px 0;display:flex;flex-direction:column;gap:14px"><div style="border-radius:20px;background:#0A3D28;color:#FFFFFF;padding:22px 18px;display:flex;flex-direction:column;gap:10px;position:relative;overflow:hidden">'
              '<img src="' + IMG['hero'] + '" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.25">'
              '<h1 style="margin:0;font-size:28px;line-height:1.1;font-weight:700;position:relative">Hola Samuel,<br><span style="color:#A8E6BC">¿qué necesitas hoy?</span></h1>'
              '<p style="margin:0;font-size:14px;color:#DCEDE2;position:relative">Compara productos, proveedores y propuestas para tu granja en un solo lugar.</p><div style="position:relative">' + buscador() + '</div></div></div>' +
              bloque(sec('Explora por especie', 'Ver todas') + scroll(esp)) + bloque(sec('Explora por categoría', 'Ver todas') + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:0 16px">' + cats + '</div>') +
              bloque('<div style="margin:0 16px;padding:20px 18px;border-radius:20px;background:#FFFFFF;border:1px solid #E6EBE7;display:flex;flex-direction:column;gap:10px"><span class="kick" style="color:#0E5A3A">Proyectos</span>'
                     '<h2 style="margin:0;font-size:24px;line-height:1.15">De la idea a la realidad, juntos.</h2><p style="margin:0;color:#4A5650;font-size:14px">Organiza tus proyectos y recibe propuestas de los proveedores del sector.</p>'
                     '<img src="' + IMG['gallo'] + '" alt="" style="width:100%;height:150px;object-fit:cover;border-radius:14px"><a href="#" class="btn">Crear un proyecto ' + svg(I['flecha'], 16, 2) + '</a></div>') +
              bloque(sec('Productos destacados', 'Ver todos') + '<div style="padding:0 16px 10px" class="row">' + ''.join('<span class="chip' + (' on' if i == 0 else '') + '">' + t + '</span>' for i, t in enumerate(['Todos', 'Nutrición', 'Salud animal', 'Equipos'])) + '</div>' + scroll(prods)) +
              bloque('<div style="margin:0 16px;display:flex;flex-direction:column;gap:12px"><div style="border-radius:20px;padding:20px 18px;background:#EEF8F1;border:1px solid #CDE9D6;display:flex;flex-direction:column;gap:8px"><span class="kick" style="color:#0E5A3A">Tableros y comparador</span>'
                     '<strong style="font-size:21px">Compara. Decide. Avanza.</strong><span style="font-size:14px;color:#4A5650">Guarda productos y compáralos lado a lado.</span><a href="#" class="btn" style="align-self:flex-start">Descubre el comparador</a></div>'
                     '<div style="border-radius:20px;padding:20px 18px;background:#072B1E;color:#FFFFFF;display:flex;flex-direction:column;gap:8px"><span class="kick" style="color:#A8E6BC">Proyectos y presupuestos</span><strong style="font-size:21px;line-height:1.2">¿Buscas un proveedor o un equipo concreto?</strong>'
                     '<span style="font-size:14px;color:#CFE5D7">Publica tu proyecto y recibe propuestas, todo por Agroolink.</span><a href="#" class="btn" style="align-self:flex-start;background:#B5D334;color:#072B1E">Publicar un proyecto</a></div></div>') +
              bloque('<div style="margin:0 16px;display:flex;flex-direction:column;gap:10px">' + ''.join('<div class="card pad" style="display:flex;gap:12px;align-items:center"><span style="width:40px;height:40px;border-radius:10px;background:#EEF6EE;color:#0E5A3A;display:flex;align-items:center;justify-content:center">' + svg(I[ic], 20) + '</span><span style="display:flex;flex-direction:column"><strong style="font-size:14px">' + t + '</strong><span class="hint">' + d + '</span></span></div>'
                                                                                         for ic, t, d in [('escudo', 'Proveedores verificados', 'Empresas comprobadas por Agroolink'), ('msg', 'Compras más seguras', 'Todo queda en tus mensajes y proyectos'), ('hoja', 'Un sector más sostenible', 'Soluciones para el futuro')]) + '</div>'))
    return pagina(cuerpo)

# ---------- listados (categoría) ----------
def filtros(botones, activos, total, tabs):
    b = ''.join('<button type="button" class="chip' + (' fil' if v else '') + '">' + svg(I[ic], 16, 2) + t + (': ' + v if v else '') + '</button>' for ic, t, v in botones)
    return ('<div style="padding:12px 0 0;display:flex;flex-direction:column;gap:8px"><div class="row" style="padding:0 16px"><button type="button" class="chip on" style="font-weight:600">' + svg(I['filtro'], 16, 2.2) + 'Filtros' +
            ('<span style="min-width:20px;height:20px;border-radius:999px;background:#B5D334;color:#072B1E;font-size:11.5px;font-weight:700;display:flex;align-items:center;justify-content:center">' + str(activos) + '</span>' if activos else '') + '</button>' + b + '</div>'
            '<div style="padding:0 16px;display:flex;gap:10px;align-items:baseline"><strong style="font-size:13px">Filtros activos (' + str(activos) + ')</strong>' + ('<a href="#" style="font-size:12.5px">Limpiar todo</a>' if activos else '') + '</div>'
            '<span class="hint" style="padding:0 16px">Se cumplen todos a la vez; dentro de un filtro, basta una opción.</span>'
            '<div style="display:flex;align-items:center;border-bottom:1px solid #E3E8E4;margin:2px 16px 0">' + ''.join('<a href="#" style="padding:10px 0;margin-right:22px;font-size:14px;' + ('box-shadow:inset 0 -3px 0 #0E5A3A' if i == 0 else 'font-weight:500;color:#4A5650') + '">' + t + '</a>' for i, t in enumerate(tabs)) +
            '<span style="flex:1"></span><span class="hint">' + total + '</span></div></div>')
def mv_categoria():
    subs = ''.join('<span class="chip' + (' on' if i == 0 else '') + '">' + t + '</span>' for i, t in enumerate(['Piensos 124', 'Aditivos 98', 'Ingredientes 76', 'Enzimas 64']))
    cuerpo = (migas('Inicio', 'Aves', 'Broilers', 'Nutrición', 'Piensos') + '<div style="margin:10px 16px 0;padding:18px;border-radius:18px;background:linear-gradient(110deg,#F6EFE6,#FBF8F3);border:1px solid #EADFCF;display:flex;flex-direction:column;gap:6px">'
              '<span class="kick" style="color:#7A5A2E">Aves › Broilers · Nutrición</span><h1 style="margin:0;font-size:26px">Piensos</h1><p style="margin:0;color:#4A5650;font-size:13.5px">Soluciones en piensos para una producción avícola más eficiente y rentable.</p></div>'
              '<div class="row" style="padding:12px 16px 0">' + subs + '</div>' +
              filtros([('pata', 'Especie', 'Aves › Broilers'), ('grid', 'Categoría', 'Piensos'), ('virus', 'Enfermedad', ''), ('pais', 'País', '')], 2, '124 productos', ['Productos', 'Empresas']) +
              '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px 16px 0">' + ''.join(tarjeta_prod(*p) for p in LISTA[:6]) + '</div>'
              '<div style="padding:16px"><a href="#" class="btn2" style="width:100%">Ver más productos (118)</a></div>'
              '<div style="margin:0 16px;padding:16px;border-radius:16px;background:#EEF6EE;border:1px solid #CDE9D6;display:flex;flex-direction:column;gap:8px"><strong>¿No encuentras lo que buscas?</strong><span style="font-size:13.5px;color:#4A5650">Publica tu proyecto y te llegan propuestas.</span><a href="#" class="btn">Publicar un proyecto</a></div>')
    return pagina(cuerpo)

# ---------- especie ----------
def mv_especie():
    chips = ''.join('<span class="chip" style="' + ('background:#B5D334;border-color:#B5D334;color:#072B1E;font-weight:600' if i == 0 else 'border-color:transparent') + '">' + t + '</span>' for i, t in enumerate(['Todas', 'Broilers', 'Ponedoras', 'Reproductoras', 'Pavos']))
    cats = ''.join('<a href="#" class="card pad" style="display:flex;gap:10px;align-items:center;color:#17231D"><span style="color:#0E5A3A">' + svg(I[ic], 19) + '</span><strong style="font-size:13px;font-weight:600">' + n + '</strong></a>' for n, ic, d in CAT)
    nec = [('nec_rendimiento', 'Mejorar el rendimiento'), ('nec_salud', 'Mejorar la salud animal'), ('nec_produccion', 'Optimizar la producción'), ('nec_instalaciones', 'Mejorar las instalaciones'), ('nec_genetica', 'Genética'), ('nec_sostenible', 'Ser más sostenible')]
    necs = ''.join('<a href="#" class="card" style="color:#17231D;display:flex;flex-direction:column"><img src="' + IMG[k] + '" alt="" style="width:100%;height:96px;object-fit:cover;display:block"><span style="padding:10px 12px;font-size:13.5px;font-weight:600;color:#0A3D28">' + t + '</span></a>' for k, t in nec)
    cuerpo = (migas('Inicio', 'Aves') + '<div style="margin:10px 16px 0;border-radius:20px;padding:20px 18px;background:linear-gradient(160deg,#0A3D28 55%,#3E6B4A);color:#FFFFFF;display:flex;flex-direction:column;gap:12px">'
              '<h1 style="margin:0;font-size:30px">Aves</h1><p style="margin:0;color:#DCEDE2;font-size:13.5px">3.240 productos, 410 empresas y 95 expertos.</p><div class="row">' + chips + '</div>'
              '<a href="#" class="btn" style="background:#FFFFFF;color:#0A3D28">Ver todos los resultados ' + svg(I['flecha'], 16, 2) + '</a></div>' +
              bloque(sec('Categorías en Aves') + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:0 16px">' + cats + '</div>') +
              bloque(sec('¿Qué necesitas?') + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:0 16px">' + necs + '</div>') +
              bloque(sec('Productos destacados', 'Ver todos') + scroll(''.join(tarjeta_prod(*p, w=176) for p in LISTA[:4]))) +
              bloque('<div style="margin:0 16px;display:flex;flex-direction:column;gap:12px"><div class="card" style="display:flex;gap:12px;padding:12px;align-items:center;background:#FBF7F0;border-color:#EFE4D2"><img src="' + IMG['editorial'] + '" alt="" style="width:84px;height:84px;object-fit:cover;border-radius:12px">'
                     '<span style="display:flex;flex-direction:column;gap:4px"><span class="kick" style="color:#7A5A00">Contenidos</span><strong style="font-size:15px;line-height:1.25">Conocimiento que impulsa la avicultura</strong><a href="#" style="font-size:13px">Ver contenidos</a></span></div>'
                     '<div class="card pad" style="display:flex;flex-direction:column;gap:8px"><span class="kick" style="color:#0E5A3A">Evento destacado</span><div style="display:flex;gap:12px;align-items:center"><span style="width:56px;height:56px;border-radius:12px;background:#0A3D28;color:#FFFFFF;display:flex;flex-direction:column;align-items:center;justify-content:center;line-height:1.1"><span style="font-size:10px;color:#A8E6BC">FEB</span><strong>24–25</strong></span>'
                     '<span style="display:flex;flex-direction:column"><strong>AviForum Puesta 2026</strong><span class="hint">Madrid · congreso</span></span></div><img src="' + IMG['evento'] + '" alt="" style="width:100%;height:96px;object-fit:cover;border-radius:12px"></div></div>'))
    return pagina(cuerpo)

# ---------- producto ----------
def barra_accion(pri, sec_ic='guardar'):
    return ('<div style="position:absolute;left:0;right:0;bottom:0;background:#FFFFFF;border-top:1px solid #E3E8E4;padding:10px 16px 30px;display:flex;gap:8px;z-index:7"><button type="button" class="btn2" style="width:48px;padding:0" aria-label="Guardar">' + svg(I[sec_ic], 20) + '</button>'
            '<button type="button" class="btn2" style="width:48px;padding:0" aria-label="Comparar">' + svg(I['comp'], 20) + '</button><a href="#" class="btn" style="flex:1">' + svg(I['msg'], 18) + pri + '</a></div>')
def ficha_cuerpo(k, galeria, titulo, sub, desc, verif, chips_, acciones, empresa):
    return ('<div style="position:relative;background:#F1F4F2"><img src="' + IMG[k] + '" alt="" style="width:100%;height:300px;object-fit:' + ('contain' if k == 'of_bolsa' else 'cover') + ';display:block">'
            '<span style="position:absolute;right:12px;bottom:12px;font-size:12px;font-weight:600;padding:3px 10px;border-radius:999px;background:rgba(23,35,29,.7);color:#FFFFFF">1 / 6</span></div>'
            '<div style="display:flex;gap:8px;padding:10px 16px 0">' + ''.join('<img src="' + IMG[g] + '" alt="" style="width:56px;height:56px;border-radius:10px;object-fit:cover;border:' + ('2px solid #0E5A3A' if i == 0 else '1px solid #E3E8E4') + '">' for i, g in enumerate(galeria)) + '</div>'
            '<div style="padding:14px 16px 0;display:flex;flex-direction:column;gap:8px">' + (tag('✓ ' + verif, '#EEF6EE', '#0E5A3A').replace('class="tag" style="', 'class="tag" style="align-self:flex-start;font-weight:600;') if verif else '') +
            '<h1 style="margin:0;font-size:26px">' + titulo + '</h1><strong style="font-size:15px;color:#33424C">' + sub + '</strong><p style="margin:0;color:#4A5650;font-size:14px;line-height:1.5">' + desc + '</p>'
            '<div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join(tag(c) for c in chips_) + '</div></div>'
            '<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:12px 16px 0"><a href="#" class="btn2" style="height:40px;font-size:13px;border-color:#D5DED8;color:#17231D">' + svg(I['video'], 16) + 'Ver vídeo</a><a href="#" class="btn2" style="height:40px;font-size:13px;border-color:#D5DED8;color:#17231D">' + svg(I['descarga'], 16) + 'Ficha técnica</a></div>'
            '<div style="padding:12px 16px 0;display:flex;flex-direction:column;gap:8px">' + acciones + empresa + '</div>')
def accion(ic, t, d):
    return ('<a href="#" class="card pad" style="display:flex;gap:12px;align-items:center;color:#17231D"><span style="width:38px;height:38px;border-radius:10px;background:#F1F4F2;display:flex;align-items:center;justify-content:center">' + svg(I[ic], 19) + '</span>'
            '<span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px;font-weight:600">' + t + '</strong><span class="hint" style="font-weight:400">' + d + '</span></span>' + svg(I['der'], 16, 2) + '</a>')
def detalle_acordeon():
    kv = lambda k, v: '<div style="display:flex;justify-content:space-between;padding:9px 0;border-top:1px solid #EEF1EE;font-size:13.5px"><span style="color:#4A5650">' + k + '</span><strong style="font-weight:600">' + v + '</strong></div>'
    fila = lambda t, abierto=False, cont='': ('<div style="border-top:1px solid #E3E8E4"><div style="display:flex;align-items:center;padding:14px 16px"><strong style="flex:1;font-size:15px">' + t + '</strong>' + svg('m6 15 6-6 6 6' if abierto else 'm6 9 6 6 6-6', 18, 2) + '</div>' + (('<div style="padding:0 16px 14px">' + cont + '</div>') if abierto else '') + '</div>')
    return ('<div style="margin-top:18px;background:#FFFFFF">' + fila('Información clave', True, kv('Categoría', 'Nutrición › Aditivos') + kv('Formato', 'Polvo') + kv('Presentación', 'Sacos de 25 kg') + kv('Registro', 'Según el país')) +
            fila('Descripción') + fila('Especificaciones') + fila('Beneficios y resultados') + fila('Documentación') + fila('Dónde comprar') + '</div>')
def mv_producto():
    acciones = accion('carro', '¿Dónde comprar?', 'Distribuidores en tu zona') + accion('manos', 'Quiero distribuir este producto', 'Hazte distribuidor')
    empresa = ('<div class="card pad" style="display:flex;gap:12px;align-items:center"><span style="width:48px;height:48px;border-radius:12px;border:1px solid #E3E8E4;display:flex;align-items:center;justify-content:center;font-weight:700;font-style:italic;color:#1D4E89;font-size:12px">Cargill</span>'
               '<span style="flex:1;display:flex;flex-direction:column"><strong>Cargill</strong><span style="font-size:12px;font-weight:600;color:#0E5A3A">Empresa verificada</span></span><a href="#" style="font-size:13px">Ver ficha</a></div>')
    cuerpo = (ficha_cuerpo('of_bolsa', ['of_bolsa', 'of_pellets', 'of_pienso', 'of_granja'], 'OptiFeed®', 'Aditivo para mejorar la conversión alimentaria', 'Solución nutricional que mejora la eficiencia alimentaria en aves de engorde, con enzimas y compuestos funcionales.', 'Producto verificado', ['Aditivos', 'Polvo', 'Sacos de 25 kg', 'Aves', 'Broilers'], acciones, empresa) +
              detalle_acordeon() + bloque(sec('Productos relacionados', 'Ver todos') + scroll(''.join(tarjeta_prod(*p, w=176) for p in LISTA[2:6]))))
    return SB + atras('OptiFeed®', 'Cargill · Aditivos') + '<div style="display:flex;flex-direction:column">' + cuerpo + '<div style="height:110px"></div></div>' + barra_accion('Pedir información')
def mv_disproducto():
    acciones = ('<div class="card pad" style="display:flex;flex-direction:column;gap:8px"><span class="kick" style="color:#56615B">Lo vende en tu zona</span><div style="display:flex;gap:10px;align-items:center"><span style="width:42px;height:42px;border-radius:10px;border:1px solid #E3E8E4;color:#0E5A3A;display:flex;align-items:center;justify-content:center">' + svg(I['hoja'], 20) + '</span>'
                '<span style="display:flex;flex-direction:column"><strong>AgroNova</strong><span style="font-size:12px;font-weight:600;color:#0E5A3A">Distribuidor autorizado de Zucami</span><span class="hint">España · Portugal</span></span></div><a href="#" class="btn2">Ver el catálogo de AgroNova</a></div>')
    cuerpo = ('<div style="padding:10px 16px 0;display:flex;justify-content:space-between"><a href="#" class="chip" style="height:32px;background:#EEF6EE;border-color:#EEF6EE;color:#0E5A3A;font-weight:600">' + svg(I['back'], 15, 2) + 'Catálogo de AgroNova</a><span class="hint" style="align-self:center">2 de 18</span></div><div style="height:10px"></div>' +
              ficha_cuerpo('aviario', ['aviario', 'zuc1', 'zuc2', 'zuc4'], 'Zucami Aviary Pro', 'Aviario modular para ponedoras · de Zucami', 'Alojamiento modular pensado para el bienestar animal, la eficiencia y la rentabilidad.', 'Producto verificado', ['Aviarios', 'Ponedoras', 'Sistema modular'], acciones, '') + detalle_acordeon())
    return SB + atras('Zucami Aviary Pro', 'En el catálogo de AgroNova') + '<div style="display:flex;flex-direction:column">' + cuerpo + '<div style="height:110px"></div></div>' + barra_accion('Pedir información a AgroNova')

# ---------- empresa ----------
def pestanas(ls, on):
    return '<div style="display:flex;border-bottom:1px solid #E3E8E4;margin:16px 16px 0;overflow:hidden">' + ''.join('<a href="#" style="padding:10px 0;margin-right:20px;font-size:14px;white-space:nowrap;' + ('box-shadow:inset 0 -3px 0 #0E5A3A' if t == on else 'font-weight:500;color:#4A5650') + '">' + t + '</a>' for t in ls) + '</div>'
def mv_empresa():
    cab = ('<div style="margin:10px 16px 0;padding:18px;border-radius:18px;background:#FFFFFF;border:1px solid #E6EBE7;display:flex;flex-direction:column;gap:8px"><div style="display:flex;gap:8px;align-items:center">' + tag('✓ Empresa verificada', '#EEF6EE', '#0E5A3A') + '<span class="hint">Fabricante</span></div>'
           '<h1 style="margin:0;font-size:26px">DSM-Firmenich</h1><strong style="color:#0E5A3A;font-size:14.5px">Ciencia, innovación y soluciones en nutrición animal</strong><p style="margin:0;color:#4A5650;font-size:13.5px">Soluciones en nutrición, salud y bienestar animal para un sistema alimentario más sostenible.</p>'
           '<div style="display:flex;gap:18px;font-size:12.5px;color:#33424C"><span><strong style="font-size:16px">48</strong> productos</span><span><strong style="font-size:16px">60</strong> países</span><span class="hint">Sede: Suiza</span></div>'
           '<a href="#" class="btn">' + svg(I['pais'], 16) + 'Encontrar distribuidor</a><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px"><a href="#" class="btn2" style="font-size:13px">' + svg(I['msg'], 16) + 'Pedir información</a><a href="#" class="btn2" style="font-size:13px">' + svg(I['manos'], 16) + 'Ser distribuidor</a></div></div>')
    cuerpo = (migas('Inicio', 'Empresas', 'DSM-Firmenich') + cab + pestanas(['Productos', 'Sobre la empresa', 'Distribuidores', 'Servicios'], 'Productos') +
              filtros([('pata', 'Especie', 'Aves'), ('grid', 'Categoría', ''), ('pais', 'Disponible en', '')], 1, '48 productos', ['Todos', 'Novedades']) +
              '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px 16px 0">' + ''.join(tarjeta_prod(*p) for p in LISTA[:4]) + '</div>'
              '<div style="padding:16px"><a href="#" class="btn2" style="width:100%">Ver los 48 productos</a></div>' +
              bloque(sec('Distribuidores en tu zona', 'Ver todos') + '<div style="padding:0 16px;display:flex;flex-direction:column;gap:8px">' +
                     ''.join('<div class="card pad" style="display:flex;gap:10px;align-items:center"><span style="width:40px;height:40px;border-radius:10px;background:' + c + ';color:#FFFFFF;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center">' + i + '</span><span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px">' + n + '</strong><span class="hint">' + z + '</span></span><a href="#" class="btn" style="height:36px;font-size:12.5px;padding:0 12px">Escribir</a></div>'
                             for i, c, n, z in [('AS', '#2E8B57', 'Agropecuària del Segre', 'Lleida, Huesca y Zaragoza'), ('NF', '#6B7A2E', 'NutriFeed Distribuciones', 'Madrid y Castilla-La Mancha')]) + '</div>', '8px 0 0'))
    return pagina(cuerpo)
def mv_distribuidor():
    marcas = ''.join('<div class="card pad" style="display:flex;flex-direction:column;align-items:center;gap:4px;text-align:center"><strong style="font-size:15px;color:' + c + '">' + n + '</strong><span class="hint">' + d + '</span></div>' for n, c, d in [('AgroNova', '#0E5A3A', 'Marca propia'), ('NovaFeed', '#2E8B57', 'Marca propia'), ('Cargill', '#1D4E89', '24 productos'), ('dsm-firmenich', '#17231D', '16 productos'), ('Elanco', '#1D6FD9', '9 productos'), ('HIPRA', '#2E6FB7', '14 productos')])
    cuerpo = (migas('Inicio', 'Empresas', 'AgroNova') + '<div style="margin:10px 16px 0;padding:18px;border-radius:18px;background:#FFFFFF;border:1px solid #E6EBE7;display:flex;flex-direction:column;gap:8px"><div style="display:flex;gap:12px;align-items:center"><span style="width:56px;height:56px;border-radius:14px;border:1px solid #E3E8E4;color:#0E5A3A;display:flex;align-items:center;justify-content:center">' + svg(I['hoja'], 26) + '</span>'
              '<span style="display:flex;flex-direction:column;gap:4px"><h1 style="margin:0;font-size:24px">AgroNova</h1><span style="display:flex;gap:6px">' + tag('✓ Verificada', '#EEF6EE', '#0E5A3A') + tag('Distribuidor') + '</span></span></div>'
              '<strong style="color:#0E5A3A;font-size:14px">Tu socio para una producción más rentable</strong><span class="hint" style="font-size:12.5px">Vende en España, Portugal y Latinoamérica</span><a href="#" class="btn">' + svg(I['msg'], 16) + 'Pedir información</a></div>' +
              pestanas(['Productos', 'Sobre la empresa', 'Marcas', 'Servicios'], 'Marcas') + '<div style="padding:12px 16px 0" class="row">' + ''.join('<span class="chip' + (' on' if i == 0 else '') + '">' + t + '</span>' for i, t in enumerate(['Todas 14', 'Propias 2', 'Distribuidas 12'])) + '</div>'
              '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:12px 16px 0">' + marcas + '</div>' + bloque('<div style="margin:0 16px;border-radius:16px;overflow:hidden"><img src="' + IMG['planta'] + '" alt="" style="width:100%;height:180px;object-fit:cover;display:block"></div>'))
    return pagina(cuerpo)
def mv_sucursal():
    prods = ''.join('<article class="card" style="width:150px;flex:none"><img src="' + IMG[k] + '" alt="" style="width:100%;height:100px;object-fit:cover;display:block"><span style="display:block;padding:8px 10px;font-size:13px;font-weight:600">' + n + '</span></article>' for k, n in [('zuc1', 'Aviary Pro'), ('zuc2', 'Nest Pro'), ('zuc3', 'EggFlow'), ('zuc4', 'FeedLine')])
    sedes = ''.join('<a href="#" class="card pad" style="display:flex;gap:10px;align-items:center;color:#17231D"><span style="width:38px;height:38px;border-radius:10px;background:#E9F0F9;color:#1D4E89;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center">' + i + '</span><span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px">' + n + '</strong><span class="hint" style="font-weight:400">' + d + '</span></span>' + svg(I['der'], 16, 2) + '</a>'
                    for i, n, d in [('ES', 'Zucami España · sede', 'Segovia'), ('MX', 'Zucami México', 'Querétaro'), ('IT', 'Zucami Italia', 'Bérgamo')])
    cuerpo = (migas('Inicio', 'Zucami', 'Sucursales', 'LATAM · Brasil') + '<div style="margin:10px 16px 0;padding:18px;border-radius:18px;background:#FFFFFF;border:1px solid #E6EBE7;display:flex;flex-direction:column;gap:8px"><span class="hint">Sucursal de Zucami Poultry Equipment</span><h1 style="margin:0;font-size:24px">Zucami LATAM · Brasil</h1>'
              '<p style="margin:0;color:#4A5650;font-size:13.5px">Desde São Paulo atendemos a toda América Latina con soporte técnico, comercial y postventa.</p><strong style="font-size:13.5px">Zonas de venta</strong><div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join(tag(p) for p in ['Brasil', 'México', 'Colombia', 'Perú', 'Chile', 'Argentina']) + '</div>'
              '<a href="#" class="btn">' + svg(I['msg'], 16) + 'Escribir a esta sucursal</a></div>' + bloque(sec('Productos en esta región', 'Ver todos') + scroll(prods)) + bloque(sec('Otras sucursales') + '<div style="padding:0 16px;display:flex;flex-direction:column;gap:8px">' + sedes + '</div>'))
    return pagina(cuerpo)

# ---------- expertos ----------
def tarjeta_exp(k, n, t, org, tags_):
    return ('<article class="card" style="display:flex;gap:12px;padding:12px"><img src="' + IMG[k] + '" alt="' + n + '" style="width:84px;height:96px;border-radius:12px;object-fit:cover"><div style="flex:1;display:flex;flex-direction:column;gap:3px;min-width:0">'
            '<strong style="font-size:14.5px;display:flex;gap:4px;align-items:center">' + n + VERIF + '</strong><span style="font-size:13px;color:#33424C">' + t + '</span><span class="hint">' + org + '</span>'
            '<div style="display:flex;gap:6px;padding-top:4px"><a href="#" class="btn2" style="height:34px;font-size:12.5px;padding:0 10px">Ver perfil</a><a href="#" class="btn" style="height:34px;font-size:12.5px;padding:0 10px">Asesoramiento</a></div></div></article>')
def mv_expertos():
    cuerpo = (migas('Inicio', 'Expertos') + '<div style="padding:8px 16px 0"><h1 style="margin:0;font-size:24px">Expertos en producción animal</h1><p style="margin:2px 0 0;color:#4A5650;font-size:13.5px">Les escribes o pides asesoramiento por Agroolink.</p></div>' +
              filtros([('grid', 'Especialidad', ''), ('pata', 'Especie', 'Aves'), ('persona', 'Tipo', ''), ('pais', 'País', '')], 1, '312 expertos', ['Todos', 'Consultores', 'Veterinarios']) +
              '<div style="padding:12px 16px 0;display:flex;flex-direction:column;gap:10px">' + ''.join(tarjeta_exp(*e) for e in EXP[:5]) + '</div><div style="padding:16px"><a href="#" class="btn2" style="width:100%">Ver más expertos</a></div>')
    return pagina(cuerpo)
def mv_experto():
    cuerpo = ('<div style="padding:16px;display:flex;flex-direction:column;gap:10px;align-items:center;text-align:center;background:#FFFFFF"><img src="' + IMG['exp1'] + '" alt="Dr. Carlos Martínez" style="width:112px;height:112px;border-radius:50%;object-fit:cover">'
              '<h1 style="margin:0;font-size:22px;display:flex;gap:6px;align-items:center">Dr. Carlos Martínez' + VERIF + '</h1><strong style="color:#0A3D28;font-size:14px">Consultor especialista en nutrición avícola</strong>'
              '<span class="hint" style="font-size:12.5px">Consultor independiente · España · ES · EN · PT</span><div style="display:flex;flex-wrap:wrap;gap:6px;justify-content:center">' + ''.join(tag(t) for t in ['Nutrición avícola', 'Salud intestinal', 'Aditivos', 'Sostenibilidad']) + '</div>'
              '<span class="hint">Responde en menos de 24 h</span></div>' + pestanas(['Perfil', 'Experiencia', 'Servicios', 'Actividad'], 'Perfil') +
              '<div style="padding:14px 16px 0;display:flex;flex-direction:column;gap:12px"><h2 class="h2">Sobre mí</h2><p style="margin:0;color:#4A5650;font-size:14px;line-height:1.55">Veterinario y consultor en nutrición avícola con más de 15 años asesorando a productores, integradoras y empresas del sector.</p>'
              '<h2 class="h2">Trabaja con</h2><div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join(tag(t) for t in ['Ponedoras', 'Broilers', 'Reproductoras', 'Pavos']) + '</div>'
              '<h2 class="h2">Servicios</h2>' + ''.join('<div class="card pad" style="display:flex;flex-direction:column;gap:4px"><strong style="font-size:14.5px">' + t + '</strong><span style="font-size:13px;color:#4A5650">' + d + '</span><a href="#" style="font-size:13px">Pedir información</a></div>'
                                                         for t, d in [('Auditoría y diagnóstico técnico', 'Presencial o a distancia · según proyecto'), ('Diseño de programas nutricionales', 'A distancia · 2–4 semanas')]) +
              '<div class="card pad" style="display:flex;gap:10px;align-items:center"><span style="font-weight:700;font-style:italic;color:#1D4E89;font-size:13px">Cargill</span><span style="flex:1;font-size:13px">Colabora con Cargill Animal Nutrition</span><a href="#" style="font-size:13px">Ver</a></div></div>')
    return SB + atras('Dr. Carlos Martínez', 'Experto verificado') + '<div style="display:flex;flex-direction:column">' + cuerpo + '<div style="height:110px"></div></div>' + barra_accion('Pedir asesoramiento')

# ---------- eventos ----------
def mv_eventos():
    ev = lambda k, t, f, l, tags_: ('<article class="card"><img src="' + IMG[k] + '" alt="" style="width:100%;height:140px;object-fit:cover;display:block"><div class="pad" style="display:flex;flex-direction:column;gap:6px"><div style="display:flex;gap:6px">' + ''.join(tag(x) for x in tags_) + '</div>'
                                    '<strong style="font-size:16px">' + t + '</strong><span style="display:flex;gap:14px;font-size:13px;color:#33424C"><span style="display:flex;gap:4px;align-items:center;font-weight:600">' + svg(I['cal'], 15) + f + '</span><span style="display:flex;gap:4px;align-items:center">' + svg(I['pais'], 15) + l + '</span></span></div></article>')
    dias = ''.join('<span style="flex:none;width:52px;height:64px;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;' + ('background:#0E5A3A;color:#FFFFFF;' if d == 24 else 'background:#FFFFFF;border:1px solid #E6EBE7;') + '"><span style="font-size:10.5px;opacity:.8">' + w + '</span><strong style="font-size:17px">' + str(d) + '</strong></span>' for d, w in zip(range(22, 28), ['DOM', 'LUN', 'MAR', 'MIÉ', 'JUE', 'VIE']))
    cuerpo = (migas('Inicio', 'Eventos') + '<div style="padding:8px 16px 0;display:flex;align-items:flex-end"><h1 style="margin:0;font-size:24px;flex:1">Eventos</h1><span style="display:flex;gap:2px;padding:3px;border-radius:12px;background:#E9EEEA"><span class="chip on" style="height:32px">Lista</span><span class="chip" style="height:32px;border-color:transparent;background:transparent">Calendario</span></span></div>'
              '<div style="padding:12px 16px 0;display:flex;justify-content:space-between"><strong>Febrero 2026</strong><span class="hint">‹ ›</span></div>' + scroll(dias, 8).replace('padding:0 16px', 'padding:8px 16px 0') +
              filtros([('pata', 'Especie', 'Aves'), ('cal', 'Tipo', ''), ('pais', 'País', '')], 1, '24 eventos', ['Próximos', 'Pasados']) +
              '<div style="padding:12px 16px 0;display:flex;flex-direction:column;gap:12px">' + ev('evento1', 'AviForum Puesta 2026', '24–25 feb', 'Madrid', ['Aves', 'Congreso']) + ev('evento2', 'porciForum España 2026', '3–4 mar', 'Madrid', ['Porcino', 'Congreso']) + ev('evento3', 'NutriForum 2026', '22–23 abr', 'Madrid', ['Monogástricos']) + '</div>')
    return pagina(cuerpo)
def mv_evento():
    prog = ''.join('<div style="display:flex;gap:14px;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13.5px"><strong style="width:44px">' + h + '</strong><span style="display:flex;flex-direction:column"><strong style="font-weight:600">' + t + '</strong>' + ('<span class="hint">' + p + '</span>' if p else '') + '</span></div>'
                   for h, t, p in [('09:00', 'Apertura institucional', ''), ('10:00', 'Estrategias nutricionales en ponedoras', 'Dr. Carlos Martínez'), ('11:30', 'Pausa café y expositores', ''), ('12:00', 'Mesa redonda: retos del sector', '')])
    cuerpo = ('<img src="' + IMG['evento1'] + '" alt="" style="width:100%;height:200px;object-fit:cover;display:block"><div style="padding:14px 16px 0;display:flex;flex-direction:column;gap:8px">' + tag('Congreso').replace('class="tag" style="', 'class="tag" style="align-self:flex-start;') +
              '<h1 style="margin:0;font-size:24px">AviForum Puesta 2026</h1><p style="margin:0;color:#4A5650;font-size:14px">Innovación y conocimiento para una producción de huevos más eficiente y sostenible.</p>'
              '<div class="card pad" style="display:flex;flex-direction:column;gap:6px;font-size:13.5px"><span style="display:flex;gap:8px;align-items:center">' + svg(I['cal'], 16) + '<strong>24–25 febrero 2026</strong></span><span style="display:flex;gap:8px;align-items:center">' + svg(I['pais'], 16) + 'IFEMA Madrid</span><span style="display:flex;gap:8px;align-items:center">' + svg(I['descarga'], 16) + 'Folleto (PDF)</span></div>'
              '<h2 class="h2" style="padding-top:6px">Programa</h2><div class="row"><span class="chip on">Día 1 · 24 feb</span><span class="chip">Día 2 · 25 feb</span></div><div>' + prog + '</div>'
              '<div class="card pad" style="display:flex;gap:10px;align-items:center"><span class="hint">Organiza</span><strong>Agrinews</strong></div></div>')
    return SB + atras('AviForum Puesta 2026', '24–25 feb · Madrid') + '<div style="display:flex;flex-direction:column">' + cuerpo + '<div style="height:110px"></div></div>' + barra_accion('Inscribirme', 'cal').replace(svg(I['msg'], 18), '')

# ---------- ventanas (hojas inferiores) ----------
def hoja(titulo, sub, cuerpo, sesion=True):
    fondo_ = SB + top(sesion) + '<div style="padding:16px;display:flex;flex-direction:column;gap:12px"><div style="height:220px;border-radius:16px;background:#E9EEEA"></div><div style="height:22px;width:70%;border-radius:6px;background:#E9EEEA"></div><div style="height:14px;width:90%;border-radius:6px;background:#EEF2EF"></div></div>'
    return (fondo_ + tabbar('Explorar', sesion) + '<div class="ov"></div><div role="dialog" aria-modal="true" class="sheet" style="z-index:8"><span style="align-self:center;width:40px;height:5px;border-radius:3px;background:#D5DED8"></span>'
            + (('<div style="display:flex;gap:10px;align-items:flex-start"><div style="flex:1"><strong style="font-size:18px">' + titulo + '</strong>' + ('<div style="font-size:13px;color:#4A5650;margin-top:2px">' + sub + '</div>' if sub else '') + '</div><button type="button" class="ib" style="width:36px;height:36px;background:#F1F4F2;border-radius:50%" aria-label="Cerrar">' + svg(I['x'], 16, 2) + '</button></div>') if titulo else '') + cuerpo + '</div>')
def campo(l, v, alto=46, ph=True):
    return '<label style="display:flex;flex-direction:column;gap:5px"><span class="lbl">' + l + '</span><span class="campo" style="min-height:' + str(alto) + 'px;' + ('' if ph else 'color:#17231D;') + '">' + v + '</span></label>'
def aviso(t):
    return '<div style="display:flex;gap:8px;padding:10px 12px;border-radius:12px;background:#F2F7F3;border:1px solid #E1ECE4;font-size:12px;color:#33424C"><span style="color:#0E5A3A">' + svg(I['candado'], 15) + '</span><span>' + t + '</span></div>'
def mini(k, n, d):
    return '<div style="display:flex;gap:10px;align-items:center;padding:8px;border-radius:12px;background:#F6F8F6"><img src="' + IMG[k] + '" alt="" style="width:44px;height:44px;border-radius:10px;object-fit:cover"><span style="display:flex;flex-direction:column"><strong style="font-size:14px">' + n + '</strong><span class="hint">' + d + '</span></span></div>'
def chips_(ls, on=0):
    return '<div style="display:flex;flex-wrap:wrap;gap:6px">' + ''.join('<span class="chip' + (' on' if i == on else '') + '" style="height:34px;font-size:12.5px">' + t + '</span>' for i, t in enumerate(ls)) + '</div>'
def radio(t, d, on=False):
    return ('<div style="display:flex;gap:12px;align-items:center;padding:11px 12px;border-radius:12px;border:' + ('1.5px solid #0E5A3A;background:#F2F7F3' if on else '1px solid #E3E8E4') + '"><span style="width:20px;height:20px;border-radius:50%;border:2px solid ' + ('#0E5A3A' if on else '#B9C6BE') + ';display:flex;align-items:center;justify-content:center">' + ('<span style="width:9px;height:9px;border-radius:50%;background:#0E5A3A"></span>' if on else '') + '</span>'
            '<span style="display:flex;flex-direction:column"><strong style="font-size:14px;font-weight:600">' + t + '</strong><span class="hint">' + d + '</span></span></div>')
REGLA = 'Va por Mensajes de Agroolink desde tu cuenta. Sin teléfonos, emails ni webs: no se enviaría.'
def mv_info():
    return hoja('Pedir información', 'A Cargill, sobre este producto', mini('of_bolsa', 'OptiFeed®', 'Cargill · Aditivos') + '<span class="lbl">¿Qué necesitas?</span>' + chips_(['Precio y plazo', 'Disponibilidad', 'Ficha técnica', 'Una muestra']) +
                campo('Tu mensaje', 'Tengo dos naves de broilers en Lleida. ¿Qué dosis recomendáis?', 90, False) + aviso(REGLA) + '<a href="#" class="btn">Enviar ' + svg(I['flecha'], 16, 2) + '</a>')
def mv_asesoramiento():
    return hoja('Pedir asesoramiento', 'Al Dr. Carlos Martínez', '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + campo('Tipo de consulta', 'Nutrición ▾', 46, False) + campo('Cómo prefieres', 'A distancia ▾', 46, False) + '</div>' +
                campo('Tu consulta', 'Cuéntale tu caso, tus objetivos y el apoyo que necesitas…', 110) + aviso(REGLA) + '<a href="#" class="btn">Enviar consulta</a>')
def mv_guardar():
    return hoja('Guardar en un tablero', 'OptiFeed®', radio('Nutrición avícola', '8 productos', True) + radio('Proveedores posibles', '5 productos') + radio('Nueva granja 2027', '12 productos') +
                '<a href="#" style="font-size:14px;display:flex;gap:6px;align-items:center">' + svg(I['mas'], 16, 2) + 'Crear un tablero</a><span class="hint">Plan Gratis: 4 de 5 tableros.</span><a href="#" class="btn">Guardar</a>')
def mv_guardado():
    return hoja('', '', '<div style="display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;padding:8px 0"><span style="width:56px;height:56px;border-radius:50%;background:#0E5A3A;color:#FFFFFF;display:flex;align-items:center;justify-content:center">' + svg(I['ok'], 28, 2.6) + '</span>'
                '<strong style="font-size:18px">Guardado</strong><span style="color:#4A5650;font-size:14px">OptiFeed® está en «Nutrición avícola».</span></div><a href="#" class="btn">Ver el tablero</a><a href="#" style="text-align:center;font-size:14px">Seguir navegando</a>')
def mv_ficha():
    return hoja('Descargar la ficha técnica', 'Una por idioma', '<div style="display:flex;gap:12px;align-items:center;padding:12px;border-radius:14px;background:#F6F8F6"><span style="width:52px;height:66px;border-radius:8px;background:#FFFFFF;border:1px solid #E3E8E4;display:flex;align-items:center;justify-content:center;color:#C0392B;font-weight:700;font-size:12px">PDF</span>'
                '<span style="display:flex;flex-direction:column;font-size:12.5px;color:#4A5650"><strong style="font-size:14px;color:#17231D">OptiFeed® · Ficha técnica</strong>PDF · 2,4 MB · sep. 2026</span></div><span class="lbl">Idioma</span>' + chips_(['Español', 'English', 'Português', 'Français']) +
                '<a href="#" class="btn">' + svg(I['descarga'], 16, 2) + 'Descargar</a>')
def mv_disponible():
    it = lambda ic, t: '<span style="display:flex;gap:8px;align-items:center;font-size:13.5px"><span style="color:#0E5A3A">' + svg(I[ic], 16) + '</span>' + t + '</span>'
    return hoja('Disponible en Lleida', '<a href="#">Cambiar zona</a>', '<span class="kick" style="color:#56615B">Distribuidor oficial en tu zona</span><div class="card pad" style="display:flex;flex-direction:column;gap:8px"><div style="display:flex;gap:10px;align-items:center"><span style="width:42px;height:42px;border-radius:10px;background:#2E8B57;color:#FFFFFF;font-weight:700;display:flex;align-items:center;justify-content:center">AS</span>'
                '<span style="display:flex;flex-direction:column"><strong>Agropecuària del Segre</strong><span style="font-size:12px;font-weight:600;color:#0E5A3A">Distribuidor autorizado</span></span></div>' + it('mapa', 'Lleida, Huesca y Zaragoza') + it('ok', 'Entrega en 48–72 h') + '</div>'
                '<a href="#" class="btn">' + svg(I['msg'], 16) + 'Escribir al distribuidor</a><a href="#" style="text-align:center;font-size:14px">Ver su ficha</a>')
def mv_nodisponible():
    op = lambda ic, t, d: '<a href="#" class="card pad" style="display:flex;gap:10px;align-items:center;color:#17231D"><span style="color:#17231D">' + svg(I[ic], 19) + '</span><span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px;font-weight:600">' + t + '</strong><span class="hint" style="font-weight:400">' + d + '</span></span>' + svg(I['der'], 16, 2) + '</a>'
    return hoja('No disponible en Lleida', '<a href="#">Cambiar zona</a>', '<div style="padding:10px 12px;border-radius:12px;background:#FFF8EC;border:1px solid #F3DFB8;font-size:13.5px">Aún no hay distribuidor de OptiFeed® en tu zona.</div>' +
                op('mapa', 'Ver en otro país', 'Dónde se vende ahora') + op('msg', 'Escribir a Cargill', 'Por Mensajes') + op('manos', 'Quiero distribuirlo', 'Si eres distribuidor') + op('campana', 'Avisarme cuando llegue', 'En Avisos y por email'))
def mv_zona():
    provs = ''.join('<span style="padding:11px 12px;border-radius:10px;font-size:14px;' + ('background:#EEF6EE;color:#0E5A3A;font-weight:600' if p == 'Lleida' else '') + '">' + p + '</span>' for p in ['Huesca', 'Lleida', 'Madrid', 'Murcia', 'Navarra'])
    return hoja('Cambiar zona', 'Para ver quién lo vende cerca de ti', campo('País', 'España ▾', 46, False) + '<span class="campo">Buscar provincia…</span><div style="display:flex;flex-direction:column;border:1px solid #E3E8E4;border-radius:12px;padding:4px">' + provs + '</div><a href="#" class="btn">Usar esta zona</a>')
def mv_distribuidorm():
    return hoja('Quiero distribuir este producto', 'Tu solicitud llega a Cargill', mini('of_bolsa', 'OptiFeed®', 'Cargill · Aditivos') + campo('Tu empresa', 'AgroExport SRL (tu cuenta)', 46, False) + '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + campo('Actividad', 'Distribuidor ▾', 46, False) + campo('Dónde vendes', 'España ▾', 46, False) + '</div>' +
                campo('Cuéntanos', 'A qué clientes vendes y qué marcas distribuyes…', 80) + aviso(REGLA) + '<a href="#" class="btn">Enviar solicitud</a>')
def mv_comercial():
    s = lambda i, n, d: '<div style="display:flex;gap:10px;align-items:center;padding:10px 0;border-top:1px solid #EEF1EE"><span style="width:38px;height:38px;border-radius:50%;background:#E9F0F9;color:#1D4E89;font-weight:600;font-size:12px;display:flex;align-items:center;justify-content:center">' + i + '</span><span style="flex:1;display:flex;flex-direction:column"><strong style="font-size:14px">' + n + '</strong><span class="hint">' + d + '</span></span><a href="#" class="btn" style="height:34px;font-size:12.5px;padding:0 12px">Escribir</a></div>'
    return hoja('Encuentra tu comercial', 'Zucami · un comercial por zona', '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">' + campo('País', 'España ▾', 46, False) + campo('Provincia', 'Segovia ▾', 46, False) + '</div><span class="kick" style="color:#56615B">Tu comercial</span>' + s('JP', 'Jorge Pérez', 'Castilla y León') +
                '<span class="kick" style="color:#56615B">Otras sedes</span>' + s('ZM', 'Zucami México', 'Querétaro') + s('ZI', 'Zucami Italia', 'Bérgamo'))
def mv_video():
    caps = ''.join('<span style="display:flex;gap:12px;font-size:13.5px;padding:8px 0;border-top:1px solid #EEF1EE"><span style="color:#56615B;width:40px">' + t + '</span>' + n + '</span>' for t, n in [('00:00', 'Introducción'), ('00:28', 'Bienestar animal'), ('00:56', 'Diseño modular'), ('01:40', 'Recogida de huevos')])
    return hoja('Vídeo del producto', 'Zucami Aviary Pro · 2:36', '<div style="position:relative;border-radius:14px;overflow:hidden"><img src="' + IMG['aviario'] + '" alt="" style="width:100%;height:200px;object-fit:cover;display:block;filter:brightness(.8)"><span style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:56px;height:56px;border-radius:50%;background:#FFFFFF;color:#0E5A3A;display:flex;align-items:center;justify-content:center">' + svg(I['play'], 24, 2) + '</span></div><strong>Capítulos</strong><div>' + caps + '</div>')
def acceso(cuerpo):
    return hoja('', '', '<div style="display:flex;justify-content:space-between;align-items:center">' + LOGO + '<button type="button" class="ib" style="width:36px;height:36px;background:#F1F4F2;border-radius:50%" aria-label="Cerrar">' + svg(I['x'], 16, 2) + '</button></div>' + cuerpo, sesion=False)
def gran(ic, f='#EEF6EE', c='#0E5A3A'):
    return '<span style="align-self:center;width:56px;height:56px;border-radius:50%;background:' + f + ';color:' + c + ';display:flex;align-items:center;justify-content:center">' + svg(I[ic], 26, 2) + '</span>'
def mv_acceso():
    return acceso(gran('mail') + '<div style="text-align:center"><strong style="font-size:19px">Accede para continuar</strong><p style="margin:4px 0 0;font-size:13.5px;color:#4A5650">Te enviaremos un código si ya tienes una cuenta.</p></div>' + campo('Email', 'nombre@empresa.com') + '<a href="#" class="btn">Continuar</a>' + aviso('Tus datos están seguros. Solo los usamos para identificar tu cuenta.'))
def mv_codigo():
    cajas = ''.join('<span style="width:44px;height:52px;border-radius:10px;border:' + ('2px solid #0E5A3A' if i == 4 else '1px solid #D5DED8') + ';display:flex;align-items:center;justify-content:center;font-size:21px;font-weight:600">' + d + '</span>' for i, d in enumerate(['4', '8', '2', '9', '', '']))
    return acceso(gran('mail') + '<div style="text-align:center"><strong style="font-size:19px">Introduce tu código</strong><p style="margin:4px 0 0;font-size:13.5px;color:#4A5650">Enviado a <strong>s•••@granjalosolmos.es</strong></p></div><div style="display:flex;gap:7px;justify-content:center">' + cajas + '</div><a href="#" class="btn">Entrar</a><span class="hint" style="text-align:center">¿No te ha llegado? Reenviar en 0:42</span>')
def mv_sincuenta():
    return acceso(gran('persona') + '<div style="text-align:center"><strong style="font-size:19px">Todavía no tienes cuenta</strong><p style="margin:4px 0 0;font-size:13.5px;color:#4A5650">Es gratis y te lleva un minuto.</p></div><a href="#" class="btn">Crear cuenta</a><a href="#" class="btn2">Ya tengo una cuenta</a><span class="hint" style="text-align:center">Se crea con el registro de Agrinews y vuelves aquí.</span>')
def mv_creada():
    return acceso(gran('ok', '#0E5A3A', '#FFFFFF') + '<div style="text-align:center"><strong style="font-size:19px">¡Cuenta creada!</strong><p style="margin:4px 0 0;font-size:13.5px;color:#4A5650">Vuelves a donde estabas.</p></div><a href="#" class="btn">Continuar</a>')

PIEZAS = [  # (clave, título, función, alto, página)
    ('MvCabecera', 'Móvil · Cabecera con sesión y buscador', lambda: mv_cabecera(True), 844, 'mcomunes'), ('MvCabeceraSinSesion', 'Móvil · Cabecera sin sesión («Entrar»)', lambda: mv_cabecera(False), 844, 'mcomunes'),
    ('MvPie', 'Móvil · Pie', mv_pie, 844, 'mcomunes'),
    ('MvHome', 'Móvil · Home con sesión', mv_home, 3020, 'mhome'),
    ('MvCategoria', 'Móvil · Categoría (Piensos para broilers)', mv_categoria, 2110, 'mcategoria'), ('MvEspecie', 'Móvil · Especie (Aves)', mv_especie, 2460, 'mespecie'),
    ('MvProducto', 'Móvil · Ficha de producto (OptiFeed®)', mv_producto, 1870, 'mproducto'), ('MvDisProducto', 'Móvil · Producto en el catálogo de AgroNova', mv_disproducto, 1512, 'mproducto'),
    ('MvEmpresa', 'Móvil · Ficha de empresa (DSM-Firmenich)', mv_empresa, 2122, 'mempresa'), ('MvDistribuidor', 'Móvil · Ficha de distribuidor (AgroNova)', mv_distribuidor, 1515, 'mempresa'), ('MvSucursal', 'Móvil · Sucursal (Zucami LATAM)', mv_sucursal, 1528, 'mempresa'),
    ('MvExpertos', 'Móvil · Directorio de expertos', mv_expertos, 1790, 'mexpertos'), ('MvExperto', 'Móvil · Perfil de experto', mv_experto, 1094, 'mexpertos'),
    ('MvEventos', 'Móvil · Eventos', mv_eventos, 1830, 'meventos'), ('MvEvento', 'Móvil · Ficha de un evento', mv_evento, 955, 'meventos'),
    ('MvModInfo', 'Móvil · Pedir información', mv_info, 844, 'mventanas'), ('MvModAsesoramiento', 'Móvil · Pedir asesoramiento', mv_asesoramiento, 844, 'mventanas'), ('MvModGuardar', 'Móvil · Guardar en un tablero', mv_guardar, 844, 'mventanas'),
    ('MvModGuardado', 'Móvil · Guardado', mv_guardado, 844, 'mventanas'), ('MvModFicha', 'Móvil · Ficha técnica', mv_ficha, 844, 'mventanas'), ('MvModDisponible', 'Móvil · Disponible en tu zona', mv_disponible, 844, 'mventanas'),
    ('MvModNoDisponible', 'Móvil · No disponible en tu zona', mv_nodisponible, 844, 'mventanas'), ('MvModZona', 'Móvil · Cambiar zona', mv_zona, 844, 'mventanas'), ('MvModDistribuidor', 'Móvil · Quiero distribuir', mv_distribuidorm, 844, 'mventanas'),
    ('MvModComercial', 'Móvil · Encuentra tu comercial', mv_comercial, 844, 'mventanas'), ('MvModVideo', 'Móvil · Vídeo del producto', mv_video, 844, 'mventanas'),
    ('MvModAcceso', 'Móvil · Acceso · email', mv_acceso, 844, 'mventanas'), ('MvModCodigo', 'Móvil · Acceso · código', mv_codigo, 844, 'mventanas'), ('MvModSinCuenta', 'Móvil · Acceso · sin cuenta', mv_sincuenta, 844, 'mventanas'), ('MvModCreada', 'Móvil · Acceso · cuenta creada', mv_creada, 844, 'mventanas')]
PAGINAS = [('mcomunes', '10 · Móvil · Componentes comunes'), ('mhome', '11 · Móvil · Home'), ('mcategoria', '12 · Móvil · Categoría'), ('mespecie', '13 · Móvil · Especie'), ('mproducto', '14 · Móvil · Ficha de producto'),
           ('mempresa', '15 · Móvil · Ficha de empresa'), ('mexpertos', '16 · Móvil · Expertos'), ('meventos', '17 · Móvil · Eventos'), ('mventanas', '18 · Móvil · Ventanas y acceso')]
if __name__ == '__main__':
    alto = {k: h for k, t, f, h, p in PIEZAS}
    alto.update({k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    for k, t, f, h, p in PIEZAS:
        open(DEST + k + '.dc.html', 'w').write(wrap(t, alto[k], f()))
    json.dump({'alto': alto, 'piezas': [(k, t, p) for k, t, f, h, p in PIEZAS], 'paginas': PAGINAS}, open(DEST + '../movil.json', 'w'), ensure_ascii=False)
    print('ok', len(PIEZAS))
