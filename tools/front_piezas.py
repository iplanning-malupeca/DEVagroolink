"""Front de Agroolink por piezas, rehecho desde la referencia de Figma (F01–F05) para el canvas «Agroolink · Figma (referencia)».
Ancho tipo vevor.es: tablero de 1440 px con contenido de 1320 px (márgenes de 60), cabecera 56 + 44, texto 15, títulos de sección 22/700,
botones de 38, tarjeta de producto de 216 px. Poppins, verde de usuario #0E5A3A y logo oficial. Sin contactos (ni web, ni email, ni teléfono).
Cada pieza es un tablero; FrHome las junta con <dc-import>.
Uso: python3 tools/front_piezas.py <carpeta>/project   → escribe Fr*.dc.html y piezas.json (tamaños)"""
import os, sys, json
DEST = sys.argv[1].rstrip('/') + '/'
B = lambda i: '/_blob/' + i
IMG = {k: B(v) for k, v in {
    'logo': 'd59fcac1179ae49cf668ad7038b0e202', 'logo_b': 'd8958c15fd8ffe7c8ae791dec448c50d', 'hero': 'ca53707297d7d6488bef79e787d1e1fc',
    'aves': 'c6db52325cef5dd75d3c61c695a00de1', 'porcino': 'e12695e818b073142ffc882ad80d371b', 'vacuno': 'ac0884b813ad4faf1c140a862d00560d', 'ovino': 'd8d7e9a45c84edfbc4ccc377c49f7443',
    'nutricion': '4f88820db270f70c68fa5cb0f7fc7d53', 'conejos': '68c6d3d383466035b88a5956202f3c8e', 'acuicultura': 'f47818b5a73794b46bd8e816c678a8ae',
    'aves_prod': '154c4c989f00720ee35c6399af5babc0', 'gallo': 'f5f960c75583e85cde66e4991479de1f', 'promo': '5363f249110778ae646fc7c6cb2c8c74',
    'piensos': '01416d51cd87a4a9fe62a9c6f21195ca', 'aditivos': '892463497042d7223723b0b82b1abc74', 'ingredientes': 'f401bcf96430bf44a4cda15eba11df3c', 'micotoxinas': 'b1dad6710cdb892f23e006007702de27',
    'vitaminas': '0d8b3a1a6b5f376eac5c4642893a021d', 'otros': 'd6bc9ef65b877b8d81c61fdc70552f94',
    'p_vent': 'bdd273ec51f56ec9e387cb8e782d8e39', 'p_comed': '676fd233123de8b27e7d375c1edbca96', 'p_solar': '7933fe5b809ad5be32c93bc6fa7de543', 'p_granja': '475aec76cacf8ae1cd6377f7fc084e60',
    'econase': 'aaefd069f7021352d99e95642007216c', 'rovabio': '9cbbdf210d3077e61c6d774738c10faf', 'aviplus': '1282745c906afa9400eaf89ec1285ff5', 'natuphos': '6b654d081286d3b019ba167273dadb3e',
    'opticell': 'cdaa4a86548bd3bc88cdaae1a9de2ad0', 'broilermax': 'bed4862dfd09c6d833ea9ee59c6cba9a', 'licit': 'da9d9401495fb24b2f342ed64a62c49e'}.items()}
V, VO, VD, VS, LIMA = '#0E5A3A', '#0A3D28', '#072B1E', '#EEF6EE', '#B5D334'
CSS = """body{margin:0;line-height:1.35;font-family:'Poppins',sans-serif;color:#17231D;font-size:15px}
a{color:#0E5A3A;text-decoration:none;font-weight:600}a:hover{color:#0A3D28}
.wrap{width:1320px;margin:0 auto}
.h2{margin:0;font-size:22px;font-weight:700;letter-spacing:-.01em}
.sub{margin:2px 0 0;font-size:15px;color:#4A5650}
.hint{font-size:12px;color:#56615B}
.kick{font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.card{background:#FFFFFF;border:1px solid #E3E8E4;border-radius:14px;box-sizing:border-box}
.btn{height:38px;padding:0 18px;border-radius:10px;background:#0E5A3A;color:#FFFFFF;font:600 15px 'Poppins',sans-serif;border:0;display:inline-flex;align-items:center;gap:8px;white-space:nowrap;cursor:pointer;text-decoration:none}
.btn2{height:36px;padding:0 16px;border-radius:10px;background:#FFFFFF;color:#0E5A3A;border:1.5px solid #0E5A3A;font:600 15px 'Poppins',sans-serif;display:inline-flex;align-items:center;gap:8px;white-space:nowrap;cursor:pointer;text-decoration:none;box-sizing:border-box}
.chip{height:32px;padding:0 14px;border-radius:999px;border:1px solid #D5DED8;background:#FFFFFF;font:500 13.5px 'Poppins',sans-serif;color:#17231D;display:inline-flex;align-items:center;gap:6px;white-space:nowrap;cursor:pointer}
.chip.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}
.ib{width:38px;height:38px;border-radius:10px;border:0;background:none;color:#17231D;display:inline-flex;align-items:center;justify-content:center;cursor:pointer;position:relative}
.ver{display:inline-flex;align-items:center;gap:6px;font-size:15px}
.sec{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:16px}"""

def svg(d, s=18, w=1.9, extra=''):
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none;%s"><path d="%s"/></svg>' % (s, s, w, extra, d)
I = {'lupa': 'M11 4a7 7 0 1 1 0 14 7 7 0 0 1 0-14zM20 20l-3.5-3.5', 'abajo': 'm6 9 6 6 6-6', 'der': 'm9 6 6 6-6 6', 'flecha': 'M5 12h14M13 6l6 6-6 6', 'izq': 'm15 6-6 6 6 6',
     'globo': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18', 'pin': 'M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
     'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z', 'msg': 'M4 5h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V6a1 1 0 0 1 1-1zM3.5 6.5l8.5 6 8.5-6',
     'campana': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21h4', 'cor': 'M12 20s-7-4.4-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.6-7 10-7 10z',
     'nutri': 'M4 20c0-8 6-14 16-16-2 10-8 16-16 16zM4 20 14 10', 'salud': 'M12 5v14M5 12h14', 'gen': 'M9 3h6M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3',
     'equipo': 'M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1',
     'inst': 'M5 21V4h14v17M9 8h2M13 8h2M9 12h2M13 12h2M9 16h2M13 16h2M3 21h18', 'tec': 'M7 7h10v10H7zM10 10h4v4h-4zM9 3v4M15 3v4M9 17v4M15 17v4M3 9h4M3 15h4M17 9h4M17 15h4',
     'serv': 'M9 4a3 3 0 1 1 0 6 3 3 0 0 1 0-6zM3 20a6 6 0 0 1 12 0M17 11l2 2 4-4', 'sost': 'M3 12a9 9 0 0 1 15-6.7L21 8M21 3v5h-5M21 12a9 9 0 0 1-15 6.7L3 16M3 21v-5h5',
     'ok': 'M5 12l5 5 9-10', 'escudo': 'M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6zM9 12l2 2 4-4', 'hoja': 'M5 19c0-8 5-13 14-14-1 9-6 14-14 14zM5 19l7-7',
     'reloj': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM12 7v5l3 2', 'estrella': 'M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z',
     'casa': 'M3 11 12 4l9 7v9H3z', 'proy': 'M4 4h16v16H4zM8 9h8M8 13h8M8 17h5', 'play': 'M8 5v14l11-7z', 'x': 'M6 6l12 12M18 6 6 18'}

def doc(titulo, w, h, cuerpo, fondo='#F6F8F6'):
    return ('<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<title>' + titulo + '</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">\n'
            '<style>\n' + CSS + '\n</style>\n</helmet>\n<div style="width: ' + str(w) + 'px; height: ' + str(h) + 'px; background: ' + fondo + '; position: relative; overflow: hidden; font-family: \'Poppins\', sans-serif; color: #17231D;">' + cuerpo + '</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":' + str(w) + ',"height":' + str(h) + '}}\'>\nclass Component extends DCLogic {\n  renderVals() { return {}; }\n}\n</script>\n</body>\n</html>\n')

def sec(t, sub='', ver=''):
    return ('<div class="sec"><div><h2 class="h2">' + t + '</h2>' + ('<p class="sub">' + sub + '</p>' if sub else '') + '</div>' +
            ('<a href="#" class="ver">' + ver + ' ' + svg(I['flecha'], 18, 2) + '</a>' if ver else '') + '</div>')


# Buscador combinado (el mismo de IntHeader y del prototipo de búsqueda): Qué buscas · Especie · Categoría · Enfermedad
SEG = [('lupa', 'Qué buscas', 'Producto, empresa, marca…'), ('pata', 'Especie', 'Cualquier especie'), ('grid', 'Categoría', 'Cualquier categoría'), ('virus', 'Enfermedad', 'Cualquier enfermedad')]
I.update({'pata': 'M8 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM16 10a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM5 15a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM19 15a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM12 13c-3 0-5 3-5 5a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2c0-2-2-5-5-5z',
          'virus': 'M12 8a4 4 0 1 1 0 8 4 4 0 0 1 0-8zM12 2v4M12 18v4M2 12h4M18 12h4M5 5l2.8 2.8M16.2 16.2 19 19M5 19l2.8-2.8M16.2 7.8 19 5'})
def barra_compacta():
    segs = ''.join('<button type="button" style="flex: ' + ('1.4' if i == 0 else '1') + '; min-width: 0; height: 26px; padding: 0 14px; display: flex; align-items: center; gap: 7px; border: 0; background: none; border-left: ' + ('0' if i == 0 else '1px solid #DCE3DE') + '; font: 400 14px \'Poppins\', sans-serif; color: #56615B; white-space: nowrap; overflow: hidden; cursor: pointer;"><span style="color: #0E5A3A; display: flex;">' + svg(I[ic], 15, 2) + '</span><span style="overflow: hidden; text-overflow: ellipsis;">' + ('Buscar…' if i == 0 else l) + '</span></button>' for i, (ic, l, v) in enumerate(SEG))
    return ('<div role="search" aria-label="Búsqueda combinada: qué buscas, especie, categoría y enfermedad" style="flex: 1; min-width: 0; height: 44px; box-sizing: border-box; display: flex; align-items: center; border-radius: 999px; border: 1px solid #DCE3DE; background: #FFFFFF; box-shadow: 0 2px 8px rgba(16, 40, 28, .08);">' + segs +
            '<button type="button" aria-label="Buscar" style="width: 34px; height: 34px; margin-right: 4px; border-radius: 50%; background: #0E5A3A; color: #FFFFFF; border: 0; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I['lupa'], 16, 2.2) + '</button></div>')
def barra_grande():
    segs = ''.join('<button type="button" style="flex: ' + ('1.3' if i == 0 else '1') + '; min-width: 0; padding: 12px 22px; border: 0; background: none; text-align: left; display: flex; flex-direction: column; gap: 1px; position: relative; cursor: pointer; font-family: \'Poppins\', sans-serif;' + ('' if i == 0 else ' box-shadow: inset 1px 0 0 #E3E8E4;') + '">'
                   '<span style="font-size: 12px; font-weight: 600; color: #17231D; display: flex; align-items: center; gap: 6px;"><span style="color: #0E5A3A; display: flex;">' + svg(I[ic], 14, 2.2) + '</span>' + l + '</span>'
                   '<span style="font-size: 14px; color: #56615B; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">' + v + '</span></button>' for i, (ic, l, v) in enumerate(SEG))
    return ('<div role="search" aria-label="Búsqueda combinada" style="margin-top: 18px; width: 880px; display: flex; align-items: center; border-radius: 999px; background: #FFFFFF; box-shadow: 0 10px 30px rgba(0, 0, 0, .18); color: #17231D;">' + segs +
            '<button type="button" aria-label="Buscar" style="width: 52px; height: 52px; margin: 6px 8px 6px 4px; border-radius: 50%; border: 0; background: #0E5A3A; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I['lupa'], 20, 2.2) + '</button></div>')

# ---------- Cabecera: 56 + 44 ----------
def cabecera(activo=None):
    menu = ''.join('<a href="#" style="display: inline-flex; align-items: center; gap: 4px; height: 44px; padding: 0 14px; font-size: 15px; font-weight: 600; color: ' + ('#0E5A3A' if i == activo else '#17231D') + ';' + (' box-shadow: inset 0 -3px 0 #0E5A3A;' if i == activo else '') + '">' + t + (svg(I['abajo'], 16, 2) if i < 2 else '') + '</a>'
                   for i, t in enumerate(['Categorías', 'Especies', 'Empresas', 'Expertos', 'Proyectos', 'Tableros y comparador', 'Contenidos']))
    barra = ('<div class="wrap" style="height: 56px; display: flex; align-items: center; gap: 12px;">'
             '<a href="#" aria-label="Agroolink, inicio" style="flex: none; display: flex;"><img src="' + IMG['logo'] + '" alt="Agroolink" style="height: 30px; width: auto; display: block;"></a>'
             + barra_compacta() +
             '<button type="button" class="ib" style="width: auto; padding: 0 8px; gap: 6px; font: 600 14px \'Poppins\', sans-serif; white-space: nowrap;" aria-label="Idioma y región: español, España">' + svg(I['globo']) + 'ES · España</button>'
             '<button type="button" class="ib" aria-label="Avisos, 3 sin leer">' + svg(I['campana'], 21) + '<span style="position: absolute; top: 2px; right: 2px; min-width: 17px; height: 17px; border-radius: 999px; background: #D93A3A; color: #FFFFFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; border: 2px solid #FFFFFF;">3</span></button>'
             '<button type="button" class="ib" aria-label="Mensajes, 2 sin leer">' + svg(I['msg'], 21) + '<span style="position: absolute; top: 2px; right: 2px; min-width: 17px; height: 17px; border-radius: 999px; background: #D93A3A; color: #FFFFFF; font-size: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; border: 2px solid #FFFFFF;">2</span></button>'
             '<button type="button" class="ib" aria-label="Mis tableros">' + svg(I['grid'], 21) + '</button>'
             '<button type="button" aria-label="Tu cuenta: Samuel" style="display: flex; align-items: center; gap: 8px; border: 0; background: none; font: 600 14px \'Poppins\', sans-serif; color: #17231D; cursor: pointer;"><span style="width: 34px; height: 34px; border-radius: 50%; background: #0E5A3A; color: #FFFFFF; font-size: 13px; display: flex; align-items: center; justify-content: center;">SE</span>Samuel' + svg(I['abajo'], 16, 2) + '</button></div>')
    menu_bar = ('<div style="border-top: 1px solid #EEF1EE;"><nav aria-label="Menú principal" class="wrap" style="height: 44px; display: flex; align-items: center; margin-left: auto; margin-right: auto;"><div style="display: flex; margin-left: -14px;">' + menu + '</div>'
                '<span style="flex: 1;"></span><a href="#" style="font-size: 14px; display: inline-flex; align-items: center; gap: 6px;">' + svg(I['proy'], 17) + 'Publica tu proyecto</a>'
                '<span style="width: 1px; height: 20px; background: #E3E8E4; margin: 0 14px;"></span><a href="#" style="font-size: 14px; color: #17231D;">Para empresas</a></nav></div>')
    return '<header style="background: #FFFFFF; border-bottom: 1px solid #E3E8E4;">' + barra + menu_bar + '</header>'

# ---------- Mega-menús ----------
def fondo_mega(panel, izq, activo):
    return (cabecera(activo) +
            '<div style="position: absolute; top: 102px; left: 0; right: 0; bottom: 0; background: rgba(7, 43, 30, .35);"></div>'
            '<div style="position: absolute; top: 102px; left: ' + str(izq) + 'px;">' + panel + '</div>')

def mega_categorias():
    cats = [('Nutrición', 'nutri'), ('Salud animal', 'salud'), ('Genética', 'gen'), ('Equipamientos', 'equipo'), ('Instalaciones', 'inst'), ('Tecnología', 'tec'), ('Servicios', 'serv'), ('Sostenibilidad', 'sost')]
    lista = ''.join('<a href="#" style="display: flex; align-items: center; gap: 12px; height: 42px; padding: 0 12px; border-radius: 10px; font-size: 15px; font-weight: ' + ('600; background: #EEF6EE; color: #0E5A3A;' if i == 0 else '500; color: #17231D;') + '">' + svg(I[ic], 19) + '<span style="flex: 1;">' + t + '</span>' + (svg(I['der'], 16, 2) if i == 0 else '') + '</a>' for i, (t, ic) in enumerate(cats))
    subs = ''.join('<a href="#" style="font-size: 15px; font-weight: 400; color: #17231D; padding: 6px 0;">' + t + '</a>' for t in ['Piensos', 'Micotoxinas', 'Aditivos', 'Vitaminas y minerales', 'Ingredientes', 'Probióticos', 'Enzimas', 'Premezclas'])
    panel = ('<div class="card" style="width: 900px; display: flex; border-radius: 0 0 16px 16px; border-top: 0; box-shadow: 0 18px 40px rgba(7, 43, 30, .18); overflow: hidden;">'
             '<div style="width: 280px; padding: 14px; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #EEF1EE;">' + lista + '</div>'
             '<div style="flex: 1; padding: 22px 26px; display: flex; flex-direction: column; gap: 12px; background: #FBFCFB;"><div><strong style="font-size: 18px;">Nutrición</strong><p class="sub" style="font-size: 14px;">Soluciones para mejorar la salud, el rendimiento y la eficiencia en la producción animal.</p></div>'
             '<div style="display: grid; grid-template-columns: 1fr 1fr; column-gap: 24px;">' + subs + '</div>'
             '<div class="card" style="display: flex; gap: 14px; align-items: center; padding: 12px;"><img src="' + IMG['promo'] + '" alt="" style="width: 72px; height: 72px; border-radius: 10px; object-fit: cover;"><span style="display: flex; flex-direction: column; gap: 4px;"><span style="font-size: 13.5px; color: #33424C;">Una nutrición más eficiente para un sector más competitivo.</span><a href="#" class="ver" style="font-size: 14px;">Ver productos de Nutrición ' + svg(I['flecha'], 16, 2) + '</a></span></div>'
             '<a href="#" class="ver" style="padding-top: 6px; border-top: 1px solid #EEF1EE;">Ver todas las subcategorías ' + svg(I['flecha'], 18, 2) + '</a></div></div>')
    return fondo_mega(panel, 60, 0)

def mega_especies():
    esp = ['Aves', 'Porcino', 'Vacuno', 'Ovino', 'Caprino', 'Cunicultura', 'Acuicultura']
    lista = ''.join('<a href="#" style="display: flex; align-items: center; gap: 12px; height: 42px; padding: 0 12px; border-radius: 10px; font-size: 15px; font-weight: ' + ('600; background: #EEF6EE; color: #0E5A3A;' if i == 0 else '500; color: #17231D;') + '"><span style="flex: 1;">' + t + '</span>' + (svg(I['der'], 16, 2) if i == 0 else '') + '</a>' for i, t in enumerate(esp))
    chips = ''.join('<span class="chip' + (' on' if i == 0 else '') + '">' + t + '</span>' for i, t in enumerate(['Todas', 'Broilers', 'Ponedoras', 'Reproductoras', 'Pavos', 'Aves cinegéticas', 'Otras aves']))
    panel = ('<div class="card" style="width: 760px; display: flex; border-radius: 0 0 16px 16px; border-top: 0; box-shadow: 0 18px 40px rgba(7, 43, 30, .18); overflow: hidden;">'
             '<div style="width: 240px; padding: 14px; display: flex; flex-direction: column; gap: 2px; border-right: 1px solid #EEF1EE;">' + lista + '</div>'
             '<div style="flex: 1; padding: 22px 26px; display: flex; flex-direction: column; gap: 12px; background: #FBFCFB;"><div><strong style="font-size: 18px;">Aves</strong><p class="sub" style="font-size: 14px;">Productos, proveedores y soluciones para una avicultura más eficiente.</p></div>'
             '<img src="' + IMG['gallo'] + '" alt="Gallo y gallinas en una granja" style="width: 100%; height: 150px; object-fit: cover; border-radius: 12px;">'
             '<strong style="font-size: 14px;">Tipo de producción</strong><div style="display: flex; flex-wrap: wrap; gap: 8px;">' + chips + '</div>'
             '<a href="#" class="ver" style="padding-top: 8px; border-top: 1px solid #EEF1EE;">Ver todos los productos de Aves ' + svg(I['flecha'], 18, 2) + '</a></div></div>')
    return fondo_mega(panel, 190, 1)

# ---------- Hero ----------
def hero():
    return ('<div class="wrap" style="padding-top: 24px;"><section style="position: relative; height: 360px; border-radius: 22px; overflow: hidden; background: #0A3D28;">'
            '<img src="' + IMG['hero'] + '" alt="" style="position: absolute; right: 0; top: 0; width: 760px; height: 100%; object-fit: cover; opacity: .55;">'
            '<div style="position: absolute; inset: 0; background: linear-gradient(90deg, #0A3D28 38%, rgba(10, 61, 40, .55) 70%, rgba(10, 61, 40, .2));"></div>'
            '<div style="position: relative; padding: 52px 64px; display: flex; flex-direction: column; gap: 14px; color: #FFFFFF;">'
            '<h1 style="margin: 0; font-size: 42px; line-height: 1.08; font-weight: 700; letter-spacing: -.02em;">Hola Samuel,<br><span style="color: #A8E6BC;">¿qué necesitas hoy?</span></h1>'
            '<p style="margin: 0; font-size: 17px; max-width: 620px; color: #DCEDE2;">Compara productos, proveedores y propuestas técnicas para granjas, plantas e instalaciones en un solo lugar.</p>'
            + barra_grande() +
            '<span style="font-size: 13px; color: #CFE5D7;">Más buscado: <u>micotoxinas porcino</u> · <u>ventilación naves</u> · <u>bebederos broilers</u></span></div></section></div>')

# ---------- Especies ----------
ESP = [('Aves', 'aves', '3.240'), ('Porcino', 'porcino', '2.180'), ('Vacuno', 'vacuno', '1.950'), ('Ovino y caprino', 'ovino', '860'), ('Nutrición animal', 'nutricion', '4.100'), ('Cunicultura', 'conejos', '310'), ('Acuicultura', 'acuicultura', '540')]
def especies(abierta=False):
    tarjetas = ''.join('<a href="#" class="card" style="display: flex; flex-direction: column; overflow: hidden; color: #17231D;' + (' border: 2px solid #0E5A3A;' if abierta and i == 0 else '') + '"><img src="' + IMG[k] + '" alt="' + t + '" style="width: 100%; height: 128px; object-fit: cover; display: block;">'
                       '<span style="display: flex; align-items: center; gap: 8px; padding: 10px 12px;"><span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 15px; font-weight: 600;">' + t + '</strong><span class="hint">' + n + ' productos</span></span>' + svg(I['der'], 16, 2) + '</span></a>'
                       for i, (t, k, n) in enumerate(ESP))
    abre = ''
    if abierta:
        chips = ''.join('<span class="chip' + (' on' if i == 0 else '') + '" style="height: 38px; padding: 0 18px; font-size: 14px;">' + t + '</span>' for i, t in enumerate(['Broilers', 'Ponedoras', 'Reproductoras', 'Pavos', 'Aves cinegéticas', 'Otras aves']))
        abre = ('<div class="card" style="margin-top: 14px; display: flex; gap: 22px; align-items: center; padding: 16px;"><img src="' + IMG['aves'] + '" alt="" style="width: 150px; height: 112px; object-fit: cover; border-radius: 10px;">'
                '<div style="flex: 1; display: flex; flex-direction: column; gap: 10px;"><strong style="font-size: 18px;">Aves · ¿qué producción te interesa?</strong><div style="display: flex; flex-wrap: wrap; gap: 8px;">' + chips + '</div></div>'
                '<div style="width: 260px; padding-left: 22px; border-left: 1px solid #EEF1EE; display: flex; flex-direction: column; gap: 8px;"><span style="font-size: 14px; color: #4A5650;">¿Prefieres verlo todo?</span><a href="#" class="btn">Ver todo Aves ' + svg(I['flecha'], 17, 2) + '</a></div></div>')
    return '<section class="wrap" style="padding-top: 36px;">' + sec('Explora por especie', '', 'Ver todas las especies') + '<div style="display: grid; grid-template-columns: repeat(7, minmax(0, 1fr)); gap: 12px;">' + tarjetas + '</div>' + abre + '</section>'

# ---------- Categorías ----------
CAT = [('Nutrición', 'nutri', 'Piensos, aditivos, ingredientes'), ('Salud animal', 'salud', 'Vacunas, diagnóstico, bioseguridad'), ('Genética', 'gen', 'Reproducción, incubación'), ('Equipamientos', 'equipo', 'Alimentación, climatización'),
       ('Instalaciones', 'inst', 'Naves, ventilación, energía'), ('Tecnología', 'tec', 'Sensores, software, automatización'), ('Servicios', 'serv', 'Consultoría, formación'), ('Sostenibilidad', 'sost', 'Gestión ambiental, economía circular')]
def categorias():
    t = ''.join('<a href="#" class="card" style="display: flex; flex-direction: column; gap: 10px; padding: 16px; color: #17231D;"><span style="width: 42px; height: 42px; border-radius: 12px; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center;">' + svg(I[ic], 21) + '</span>'
                '<strong style="font-size: 15px; font-weight: 600;">' + n + '</strong><span class="hint" style="font-size: 12.5px; font-weight: 400; line-height: 1.35;">' + d + '</span></a>' for n, ic, d in CAT)
    return '<section class="wrap" style="padding-top: 36px;">' + sec('Explora por categoría', '', 'Ver todas las categorías') + '<div style="display: grid; grid-template-columns: repeat(8, minmax(0, 1fr)); gap: 12px;">' + t + '</div></section>'

def categoria_panel():
    lista = ''.join('<a href="#" style="display: flex; align-items: center; gap: 12px; height: 44px; padding: 0 14px; border-radius: 10px; font-size: 15px; ' + ('font-weight: 600; background: #0E5A3A; color: #FFFFFF;' if i == 0 else 'font-weight: 500; color: #17231D;') + '">' + svg(I[ic], 19) + '<span style="flex: 1;">' + n + '</span>' + svg(I['der'], 16, 2) + '</a>' for i, (n, ic, d) in enumerate(CAT))
    sub = lambda k, t, d: ('<a href="#" class="card" style="display: flex; gap: 14px; align-items: center; padding: 12px; color: #17231D;"><img src="' + IMG[k] + '" alt="" style="width: 56px; height: 56px; border-radius: 10px; object-fit: cover;">'
                           '<span style="flex: 1; display: flex; flex-direction: column; gap: 2px;"><strong style="font-size: 15px; font-weight: 600;">' + t + '</strong><span class="hint" style="font-size: 12.5px; font-weight: 400;">' + d + '</span></span>' + svg(I['der'], 16, 2) + '</a>')
    marca = lambda n, color: '<a href="#" style="display: flex; align-items: center; justify-content: space-between; padding: 10px 0; border-top: 1px solid #EEF1EE; font-size: 15px; font-weight: 700; color: ' + color + ';">' + n + '<span style="color: #8A948F;">' + svg(I['der'], 15, 2) + '</span></a>'
    return ('<section class="wrap" style="padding-top: 40px;">' + sec('Explorar por categoría', 'Descubre productos y soluciones según lo que necesitas', 'Ver todas las categorías') +
            '<div style="display: grid; grid-template-columns: 290px minmax(0, 1fr) 300px; gap: 20px; align-items: start;">'
            '<nav aria-label="Categorías" class="card" style="padding: 10px; display: flex; flex-direction: column; gap: 2px;">' + lista + '</nav>'
            '<div style="display: flex; flex-direction: column; gap: 16px;"><div style="padding: 26px 28px; border-radius: 16px; background: #F6EFE6; border: 1px solid #EADFCF; display: flex; flex-direction: column; gap: 12px; align-items: flex-start;">'
            '<h3 style="margin: 0; font-size: 26px; font-weight: 700;">Nutrición</h3><p style="margin: 0; color: #4A5650; max-width: 560px;">Soluciones nutricionales para mejorar la salud, el rendimiento y la eficiencia de la producción animal.</p>'
            '<a href="#" class="btn">Ver los productos de Nutrición ' + svg(I['flecha'], 17, 2) + '</a></div>'
            '<span class="kick" style="color: #33424C;">Subcategorías destacadas</span><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">' +
            sub('piensos', 'Piensos', 'Completos, complementarios y específicos') + sub('aditivos', 'Aditivos', 'Enzimas, probióticos, acidificantes') + sub('ingredientes', 'Ingredientes', 'Materias primas e ingredientes funcionales') +
            sub('micotoxinas', 'Micotoxinas', 'Detección y control de micotoxinas') + sub('vitaminas', 'Vitaminas y minerales', 'Vitaminas, minerales y oligoelementos') + sub('otros', 'Otros', 'Otras soluciones nutricionales') + '</div></div>'
            '<div style="display: flex; flex-direction: column; gap: 16px;"><div class="card" style="padding: 16px 18px;"><div style="display: flex; justify-content: space-between; align-items: baseline; padding-bottom: 6px;"><strong style="font-size: 15px;">Marcas destacadas</strong><a href="#" style="font-size: 13px;">Ver todas</a></div>' +
            marca('Cargill', '#17231D') + marca('DSM-Firmenich', '#1D4E89') + marca('Adisseo', '#C0392B') + marca('Alltech', '#D9822B') + marca('EW Nutrition', '#17231D') + '</div>'
            '<div class="card" style="padding: 16px 18px; display: flex; flex-direction: column; gap: 10px;"><strong style="font-size: 15px;">Contenido relacionado</strong>'
            '<div style="display: flex; gap: 12px; align-items: center;"><span style="position: relative; flex: none;"><img src="' + IMG['p_granja'] + '" alt="" style="width: 96px; height: 72px; border-radius: 10px; object-fit: cover; display: block;"><span style="position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; color: #FFFFFF;">' + svg(I['play'], 22, 2) + '</span></span>'
            '<span style="display: flex; flex-direction: column; gap: 2px;"><span class="kick" style="color: #56615B; font-size: 11px;">Guía</span><strong style="font-size: 14px; line-height: 1.3;">Claves para una nutrición más eficiente</strong><a href="#" style="font-size: 13px;">Ver guía</a></span></div></div></div></div></section>')

# ---------- Proyectos ----------
def proyectos():
    item = lambda k, t, p, est, bg, fg: ('<div class="card" style="display: flex; gap: 12px; align-items: center; padding: 10px 12px;"><img src="' + IMG[k] + '" alt="" style="width: 44px; height: 44px; border-radius: 8px; object-fit: cover;">'
                                         '<span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 14px; font-weight: 600;">' + t + '</strong><span class="hint">' + p + '</span></span><span style="font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 999px; background: ' + bg + '; color: ' + fg + ';">' + est + '</span></div>')
    ok = lambda t: '<span style="display: flex; gap: 10px; align-items: flex-start; font-size: 15px;"><span style="color: #0E5A3A; margin-top: 2px;">' + svg(I['ok'], 18, 2.4) + '</span>' + t + '</span>'
    return ('<section class="wrap" style="padding-top: 48px;"><div class="card" style="border-radius: 22px; padding: 40px 44px; display: grid; grid-template-columns: minmax(0, 1.05fr) 430px 330px; gap: 34px; align-items: center;">'
            '<div style="display: flex; flex-direction: column; gap: 14px;"><span class="kick" style="color: #0E5A3A; display: flex; align-items: center; gap: 8px;">' + svg(I['hoja'], 18) + 'Proyectos</span>'
            '<h2 style="margin: 0; font-size: 34px; line-height: 1.12; font-weight: 700; letter-spacing: -.02em;">De la idea a la realidad, juntos.</h2>'
            '<p style="margin: 0; color: #4A5650; font-size: 16px;">Planifica, organiza y centraliza tus proyectos con los proveedores del sector ganadero.</p>'
            '<a href="#" class="btn" style="align-self: flex-start;">Crear un proyecto ' + svg(I['flecha'], 17, 2) + '</a>'
            '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px 20px; padding-top: 6px;">' + ok('Guarda productos y proveedores') + ok('Documentación y presupuestos en un sitio') + ok('Compara opciones y pide propuestas') + ok('Trabaja en equipo') + '</div></div>'
            '<div class="card" style="padding: 18px; background: #FBFCFB; display: flex; flex-direction: column; gap: 10px;"><div style="display: flex; justify-content: space-between; align-items: center;"><strong style="font-size: 15px;">Nueva granja avícola</strong><strong style="color: #0E5A3A;">65 %</strong></div>'
            '<span style="height: 6px; border-radius: 3px; background: #E3E8E4; display: block;"><span style="width: 65%; height: 100%; border-radius: 3px; background: #0E5A3A; display: block;"></span></span>' +
            item('p_vent', 'Sistema de ventilación', '3 propuestas', 'Propuesta recibida', '#EEF6EE', '#0E5A3A') + item('p_comed', 'Comedero automático', '2 propuestas', 'En evaluación', '#FFF4E0', '#7A4B00') +
            item('p_solar', 'Paneles solares', 'Guardado de un tablero', 'Añadido', '#E9F0F9', '#1D4E89') + '</div>'
            '<div style="position: relative; height: 380px; border-radius: 18px; overflow: hidden;"><img src="' + IMG['gallo'] + '" alt="Gallo en una granja" style="width: 100%; height: 100%; object-fit: cover;">'
            '<div style="position: absolute; left: 16px; right: 16px; top: 16px; background: #FFFFFF; border-radius: 14px; padding: 14px 16px; display: flex; flex-direction: column; gap: 8px; font-size: 14px;"><strong>Ejemplos de proyectos</strong>' +
            ''.join('<span style="display: flex; gap: 8px; align-items: center;"><span style="color: #0E5A3A;">' + svg(I[ic], 16) + '</span>' + t + '</span>' for ic, t in [('casa', 'Nueva granja'), ('sost', 'Renovación de equipamiento'), ('nutri', 'Mejora de la alimentación'), ('hoja', 'Proyecto de sostenibilidad')]) +
            '</div></div></div></section>')

# ---------- Productos destacados: tarjetas de 216 ----------
PROD = [('econase', 'Econase® XT', 'Mejora la digestibilidad en broilers', 'DSM-Firmenich', '#1D4E89'), ('rovabio', 'Rovabio® Advance', 'Complejo enzimático', 'Adisseo', '#C0392B'),
        ('aviplus', 'AviPlus®', 'Salud intestinal', 'Huvepharma', '#0E5A3A'), ('natuphos', 'Natuphos® E', 'Fitasa de alto rendimiento', 'BASF', '#1D4E89'),
        ('opticell', 'OptiCell®', 'Soporte digestivo natural', 'Cargill', '#17231D'), ('broilermax', 'Broiler Max', 'Solución nutricional avanzada', 'Alltech', '#D9822B')]
def productos():
    tabs = ''.join('<span class="chip' + (' on' if i == 0 else '') + '">' + t + '</span>' for i, t in enumerate(['Todos', 'Nutrición', 'Salud animal', 'Equipamientos', 'Instalaciones', 'Tecnología']))
    card = lambda k, n, d, m, c: ('<a href="#" class="card" style="width: 210px; height: 324px; display: flex; flex-direction: column; overflow: hidden; color: #17231D; position: relative;">'
                                  '<span style="position: absolute; top: 8px; right: 8px; width: 32px; height: 32px; border-radius: 50%; background: #FFFFFF; color: #4A5650; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 4px rgba(0,0,0,.12);">' + svg(I['cor'], 17) + '</span>'
                                  '<img src="' + IMG[k] + '" alt="' + n + '" style="width: 100%; height: 178px; object-fit: cover;"><span style="padding: 12px 14px; display: flex; flex-direction: column; gap: 4px; flex: 1;">'
                                  '<strong style="font-size: 15px; font-weight: 600;">' + n + '</strong><span style="font-size: 13px; font-weight: 400; color: #4A5650; line-height: 1.35;">' + d + '</span><span style="flex: 1;"></span>'
                                  '<span style="font-size: 12.5px; font-weight: 700; color: ' + c + '; padding-top: 8px; border-top: 1px solid #EEF1EE;">' + m + '</span></span></a>')
    flecha = lambda d, lado: '<button type="button" aria-label="' + ('Anteriores' if lado == 'left' else 'Siguientes') + '" style="position: absolute; top: 140px; ' + lado + ': -20px; width: 40px; height: 40px; border-radius: 50%; border: 1px solid #E3E8E4; background: #FFFFFF; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(0,0,0,.1); color: #17231D;">' + svg(I[d], 18, 2) + '</button>'
    return ('<section class="wrap" style="padding-top: 48px;"><div class="sec"><h2 class="h2">Productos destacados</h2><div style="display: flex; gap: 8px; align-items: center;">' + tabs + '<a href="#" class="ver" style="margin-left: 12px;">Ver todos ' + svg(I['flecha'], 18, 2) + '</a></div></div>'
            '<div style="position: relative;"><div style="display: flex; gap: 12px;">' + ''.join(card(*p) for p in PROD) + '</div>' + flecha('izq', 'left') + flecha('der', 'right') + '</div></section>')

# ---------- Comparador + proyectos ----------
def comparador():
    fila = lambda t: '<div style="display: flex; justify-content: space-between; padding: 8px 0; border-top: 1px solid #EEF1EE; font-size: 14px;">' + t + '<span style="color: #0E5A3A;">' + svg(I['ok'], 17, 2.4) + '</span></div>'
    return ('<section class="wrap" style="padding-top: 48px; display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">'
            '<div style="border-radius: 22px; padding: 36px 40px; background: linear-gradient(135deg, #EEF8F1, #F8FCF9); border: 1px solid #CDE9D6; display: flex; gap: 24px; align-items: center;">'
            '<div style="flex: 1; display: flex; flex-direction: column; gap: 12px;"><span class="kick" style="color: #0E5A3A;">Tableros y comparador</span><h2 style="margin: 0; font-size: 28px; font-weight: 700; letter-spacing: -.02em;">Compara. Decide. Avanza.</h2>'
            '<p style="margin: 0; color: #4A5650;">Guarda productos en tus tableros y compáralos en una tabla técnica, lado a lado.</p><a href="#" class="btn" style="align-self: flex-start;">Descubre el comparador ' + svg(I['flecha'], 17, 2) + '</a></div>'
            '<div class="card" style="width: 230px; padding: 12px 16px; box-shadow: 0 8px 24px rgba(14, 90, 58, .1);"><div style="display: flex; justify-content: space-between; font-size: 12px; color: #8A948F; padding-bottom: 6px;"><span>Especificación</span><span>Cumple</span></div>' +
            fila('Rendimiento') + fila('Certificación UE') + fila('Disponible en tu zona') + '</div></div>'
            '<div style="border-radius: 22px; padding: 36px 40px; background: #072B1E; color: #FFFFFF; display: flex; gap: 24px; align-items: center;">'
            '<div style="flex: 1; display: flex; flex-direction: column; gap: 12px;"><span class="kick" style="color: #A8E6BC;">Proyectos y presupuestos</span><h2 style="margin: 0; font-size: 28px; font-weight: 700; letter-spacing: -.02em; line-height: 1.15;">¿Buscas un proveedor o un equipo concreto?</h2>'
            '<p style="margin: 0; color: #CFE5D7;">Publica tu proyecto y recibe propuestas de fabricantes y distribuidores, todo por Agroolink.</p>'
            '<a href="#" class="btn" style="align-self: flex-start; background: #B5D334; color: #072B1E;">Publicar un proyecto ' + svg(I['flecha'], 17, 2) + '</a></div>'
            '<img src="' + IMG['licit'] + '" alt="Técnica revisando un lote de broilers" style="width: 200px; height: 200px; border-radius: 16px; object-fit: cover;"></div></section>')

# ---------- Confianza ----------
def confianza():
    it = lambda ic, t, d: ('<div style="flex: 1; display: flex; gap: 14px; align-items: center;"><span style="width: 48px; height: 48px; border-radius: 12px; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I[ic], 22) + '</span>'
                           '<span style="display: flex; flex-direction: column;"><strong style="font-size: 15px;">' + t + '</strong><span style="font-size: 13px; color: #4A5650;">' + d + '</span></span></div>')
    return ('<section class="wrap" style="padding-top: 48px; padding-bottom: 56px; display: grid; grid-template-columns: minmax(0, 1fr) 420px; gap: 20px;">'
            '<div class="card" style="border-radius: 18px; padding: 24px 28px; display: flex; gap: 20px;">' + it('escudo', 'Proveedores verificados', 'Empresas comprobadas por Agroolink') +
            it('reloj', 'Compras más seguras', 'Todo queda en tus mensajes y proyectos') + it('cor', 'Un sector más sostenible', 'Soluciones para el futuro de la ganadería') + '</div>'
            '<div style="border-radius: 18px; padding: 24px 28px; background: #0A3D28; color: #FFFFFF; display: flex; gap: 16px; align-items: center;"><span style="width: 48px; height: 48px; border-radius: 50%; background: rgba(255,255,255,.12); color: #B5D334; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I['estrella'], 22) + '</span>'
            '<strong style="flex: 1; font-size: 17px; line-height: 1.3;">Hagamos crecer juntos el sector ganadero.</strong><span style="width: 42px; height: 42px; border-radius: 50%; background: #FFFFFF; color: #0A3D28; display: flex; align-items: center; justify-content: center;">' + svg(I['flecha'], 20, 2.2) + '</span></div></section>')

# ---------- Pie ----------
def pie():
    col = lambda t, ls: '<div style="display: flex; flex-direction: column; gap: 12px;"><span class="kick" style="color: #FFFFFF;">' + t + '</span>' + ''.join('<a href="#" style="font-size: 14px; font-weight: 400; color: #B9CFC2;">' + l + '</a>' for l in ls) + '</div>'
    return ('<footer style="background: #072B1E; color: #FFFFFF;"><div class="wrap" style="padding: 52px 0 28px; display: grid; grid-template-columns: minmax(0, 1.3fr) repeat(3, minmax(0, 1fr)); gap: 40px;">'
            '<div style="display: flex; flex-direction: column; gap: 16px;"><img src="' + IMG['logo_b'] + '" alt="Agroolink" style="height: 34px; width: auto; align-self: flex-start;">'
            '<p style="margin: 0; color: #B9CFC2; max-width: 420px;">La plataforma B2B para encontrar, comparar y pedir productos y servicios para la producción animal.</p>'
            '<span style="display: flex; gap: 8px;"><span class="chip" style="background: transparent; color: #FFFFFF; border-color: #2E5A47;">' + svg(I['globo'], 16) + 'Español</span><span class="chip" style="background: transparent; color: #FFFFFF; border-color: #2E5A47;">' + svg(I['pin'], 16) + 'España</span></span></div>' +
            col('Explorar', ['Categorías', 'Especies', 'Empresas', 'Expertos', 'Contenidos']) + col('Para empresas', ['Publicar catálogo', 'Panel de empresa', 'Proyectos abiertos', 'Planes y precios']) +
            col('Ayuda', ['Centro de ayuda', 'Cómo funciona', 'Términos de uso', 'Privacidad y cookies']) + '</div>'
            '<div class="wrap" style="border-top: 1px solid #1E4A38; padding: 18px 0 24px; display: flex; justify-content: space-between; font-size: 13px; color: #8FAE9D;"><span>© 2026 Agroolink. Todos los derechos reservados.</span><span>Hecho para profesionales de la producción animal</span></div></footer>')

PIEZAS = [  # nombre, título, cuerpo, alto, fondo
    ('FrCabecera', 'P01 · Cabecera · 56 + 44 (con sesión)', cabecera, 102, '#FFFFFF'),
    ('FrMegaCategorias', 'P02 · Mega-menú de categorías (abierto)', mega_categorias, 560, '#F6F8F6'),
    ('FrMegaEspecies', 'P03 · Mega-menú de especies (abierto)', mega_especies, 560, '#F6F8F6'),
    ('FrHero', 'P04 · Hero «Hola Samuel» con buscador', hero, 402, '#F6F8F6'),
    ('FrEspecies', 'P05 · Explora por especie', especies, 268, '#F6F8F6'),
    ('FrEspeciesAbierta', 'P05b · Explora por especie · Aves abierta', lambda: especies(True), 430, '#F6F8F6'),
    ('FrCategorias', 'P06 · Explora por categoría', categorias, 249, '#F6F8F6'),
    ('FrCategoriaPanel', 'P07 · Explorar una categoría (Nutrición)', categoria_panel, 618, '#F6F8F6'),
    ('FrProyectos', 'P08 · Proyectos: de la idea a la realidad', proyectos, 510, '#F6F8F6'),
    ('FrProductos', 'P09 · Productos destacados (tarjetas de 216)', productos, 422, '#F6F8F6'),
    ('FrComparador', 'P10 · Comparador y proyectos', comparador, 349, '#F6F8F6'),
    ('FrConfianza', 'P11 · Confianza', confianza, 209, '#F6F8F6'),
    ('FrPie', 'P12 · Pie', pie, 311, '#072B1E')]
HOME = ['FrCabecera', 'FrHero', 'FrEspecies', 'FrCategorias', 'FrCategoriaPanel', 'FrProyectos', 'FrProductos', 'FrComparador', 'FrConfianza', 'FrPie']
if __name__ == '__main__':
    alto = {k: h for k, t, f, h, fo in PIEZAS}
    alto.update({k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    for k, t, f, h, fo in PIEZAS:
        open(DEST + k + '.dc.html', 'w').write(doc('Front · ' + t, 1440, alto[k], f(), fo))
    H = sum(alto[k] for k in HOME)
    cuerpo = ''.join('<dc-import name="' + k + '" hint-size="1440px,' + str(alto[k]) + 'px"></dc-import>' for k in HOME)
    open(DEST + 'FrHome.dc.html', 'w').write(doc('Front · Home con sesión (piezas juntas)', 1440, H, '<div style="display: flex; flex-direction: column;">' + cuerpo + '</div>'))
    json.dump({'alto': alto, 'home': H, 'piezas': [(k, t) for k, t, f, h, fo in PIEZAS]}, open(DEST + '../piezas.json', 'w'), ensure_ascii=False)
    print('ok', len(PIEZAS) + 1, H)
