"""Front por piezas (2): categoría, especie y producto, rehechos desde la referencia de Figma (F06, F10, F19) para el canvas «Agroolink · Figma (referencia)».
Mismas reglas que front_piezas.py: 1440 / 1320, cabecera IntHeader, Poppins, verde #0E5A3A, sin contactos.
El listado sigue los resultados de búsqueda ya trabajados (B1): botón «Filtros» con contador, un botón por filtro con su icono,
«Filtros activos (n)» con la frase de cómo se combinan siempre visible, pestañas Productos · Empresas y tarjetas con Comparar · Ver ficha.
Uso: python3 tools/front_paginas.py <carpeta>/project   → escribe FrCat*, FrEsp*, FrProd*, FrPag* y paginas.json"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from front_piezas import DEST, B, IMG, CSS, svg, I, doc, sec, cabecera, pie, productos, CAT

IMG.update({k: B(v) for k, v in {
    'editorial': 'a951699dfb7fa8a66c31f3d1d0523007', 'evento': 'fb920aebb9be968b58f3b06cdcb2b4d9', 'nec_genetica': '59562230118d920172aadb5b886c765e',
    'nec_instalaciones': '2a5d2be5c87328769ec78fe418be748b', 'nec_produccion': '822620462b751acaefbf9378810167e2', 'nec_rendimiento': '52909c9b99eb3b9c20ec334affbfce45',
    'nec_salud': '0a69be701bb8144adf077409697ad0ff', 'nec_sostenible': 'eb7775c01fcaca5ba1925ac7770309b7', 'of_bolsa': '3e288fc50ad71f68b1c8d1005d1b1f47',
    'of_granja': '40f55526846b6139ae82bc48782e2ee4', 'of_pellets': '397fbce6ae2c3dd17a45f4817abaf6eb', 'of_pienso': '39d26bc61b12f1f922fbd3a64bc02197'}.items()})
I.update({'filtro': 'M4 6h16M7 12h10M10 18h4', 'marca': 'M3 12V4h8l9 9-8 8zM7.5 7.5h.01', 'comp': 'M4 5h7v14H4zM13 5h7v14h-7z', 'compartir': 'M18 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM18 22a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM8.6 13.5l6.8 4M15.4 6.5l-6.8 4',
          'guardar': 'M6 3h12v18l-6-4-6 4z', 'descarga': 'M12 4v12M6 10l6 6 6-6M4 20h16', 'video': 'M12 3a9 9 0 1 1 0 18 9 9 0 0 1 0-18zM10 8.5v7l6-3.5z', 'carro': 'M3 4h2l2.4 11h11L21 7H6.2M10 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2zM17 20a1 1 0 1 0 0-2 1 1 0 0 0 0 2z',
          'manos': 'M8 13l3 3 6-6M3 12l4-4 3 2 4-3 3 2 4 4-4 5-3-1', 'tend': 'M3 17l6-6 4 4 8-8M15 7h6v6', 'caja': 'M21 8 12 3 3 8v8l9 5 9-5zM3 8l9 5 9-5M12 13v8', 'euro': 'M17 6a7 7 0 1 0 0 12M4 10h9M4 14h9',
          'doc': 'M6 3h9l4 4v14H6zM14 3v5h5', 'calendario': 'M4 6h16v14H4zM4 10h16M8 3v4M16 3v4', 'pais': 'M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z'})
V = '#0E5A3A'

def migas(*ls):
    return ('<nav aria-label="Migas" class="wrap" style="display: flex; align-items: center; gap: 6px; padding-top: 18px; font-size: 13px; color: #56615B;">' +
            ''.join(('<a href="#" style="font-weight: 400; color: #56615B;">' + t + '</a>' + svg(I['der'], 13, 2)) if i < len(ls) - 1 else '<span style="color: #17231D; font-weight: 500;">' + t + '</span>' for i, t in enumerate(ls)) + '</nav>')

# ---------- Tarjeta de producto (la de los resultados de búsqueda, a 210 px) ----------
LISTA = [('econase', 'Enzimas', 'Econase® XT', 'DSM-Firmenich', True, ['Aves', 'Porcino']), ('of_bolsa', 'Aditivos', 'OptiFeed®', 'Cargill', True, ['Aves', 'Broilers']),
         ('rovabio', 'Enzimas', 'Rovabio® Advance', 'Adisseo', True, ['Aves', 'Porcino']), ('natuphos', 'Enzimas', 'Natuphos® E', 'BASF', True, ['Aves', 'Porcino', 'Rumiantes']),
         ('aviplus', 'Aditivos', 'AviPlus®', 'Huvepharma', False, ['Aves']), ('opticell', 'Aditivos', 'OptiCell®', 'Cargill', True, ['Aves', 'Porcino']),
         ('of_pellets', 'Piensos de arranque', 'NuStart Broiler', 'Nuscience', False, ['Broilers']), ('broilermax', 'Piensos completos', 'Broiler Max', 'Alltech', True, ['Broilers']),
         ('nutricion', 'Premezclas', 'Sangrovit® Extra', 'Phibro', False, ['Aves', 'Porcino']), ('of_pienso', 'Piensos de arranque', 'Inicio Pollitos 1', 'NutriAves', False, ['Broilers']),
         ('piensos', 'Piensos completos', 'Crecimiento B-2', 'Agropecuària del Segre', True, ['Broilers']), ('promo', 'Piensos complementarios', 'Selko® IntelliBond', 'Trouw Nutrition', True, ['Aves', 'Porcino'])]
def tarjeta(k, cat, n, m, ok, esp, ancho=210):
    return ('<article class="card" style="width: ' + str(ancho) + 'px; display: flex; flex-direction: column; overflow: hidden;"><div style="position: relative;"><img src="' + IMG[k] + '" alt="' + n + '" style="width: 100%; height: 150px; object-fit: cover; display: block;">'
            '<button type="button" aria-label="Guardar en un tablero" style="position: absolute; top: 8px; right: 8px; width: 32px; height: 32px; border-radius: 50%; border: 0; background: #FFFFFF; color: #4A5650; display: flex; align-items: center; justify-content: center; box-shadow: 0 1px 4px rgba(0,0,0,.12);">' + svg(I['guardar'], 16) + '</button></div>'
            '<div style="padding: 12px 14px 14px; display: flex; flex-direction: column; gap: 4px; flex: 1;"><span style="font-size: 12px; color: #56615B;">' + cat + '</span><strong style="font-size: 15px; font-weight: 600; line-height: 1.25;">' + n + '</strong>'
            '<span style="font-size: 13px; color: #4A5650; display: flex; align-items: center; gap: 4px;">' + m + ('<span style="color: #0E5A3A;" title="Empresa verificada">' + svg(I['ok'], 14, 2.4) + '</span>' if ok else '') + '</span>'
            '<span style="display: flex; flex-wrap: wrap; gap: 4px; padding-top: 4px;">' + ''.join('<span style="font-size: 11.5px; padding: 2px 8px; border-radius: 999px; background: #F1F4F2;">' + e + '</span>' for e in esp) + '</span><span style="flex: 1;"></span>'
            '<span style="display: flex; gap: 6px; padding-top: 10px;"><a href="#" class="btn2" style="flex: 1; height: 36px; padding: 0 8px; font-size: 13.5px; justify-content: center;">Comparar</a><a href="#" class="btn" style="flex: 1; height: 36px; padding: 0 8px; font-size: 13.5px; justify-content: center;">Ver ficha</a></span></div></article>')

# ---------- Categoría ----------
def cat_cabecera():
    sub = ''.join('<a href="#" class="chip" style="font-weight: 500;' + (' background: #0E5A3A; border-color: #0E5A3A; color: #FFFFFF;' if i == 0 else '') + '">' + t + ' <span style="opacity: .7; font-weight: 400;">' + n + '</span></a>'
                  for i, (t, n) in enumerate([('Piensos', '124'), ('Aditivos', '98'), ('Ingredientes', '76'), ('Enzimas', '64'), ('Micotoxinas', '48'), ('Vitaminas y minerales', '41'), ('Premezclas', '37')]))
    return (migas('Inicio', 'Aves', 'Broilers', 'Nutrición', 'Piensos') +
            '<section class="wrap" style="margin-top: 14px; box-sizing: border-box; padding: 28px 32px; border-radius: 20px; background: linear-gradient(110deg, #F6EFE6, #FBF8F3); border: 1px solid #EADFCF; display: flex; flex-direction: column; gap: 12px;">'
            '<span class="kick" style="color: #7A5A2E;">Aves › Broilers · Nutrición</span><h1 style="margin: 0; font-size: 32px; font-weight: 700; letter-spacing: -.02em;">Piensos</h1>'
            '<p style="margin: 0; color: #4A5650; max-width: 760px;">Soluciones en piensos para una producción avícola más eficiente, saludable y rentable.</p>'
            '<div style="display: flex; flex-wrap: wrap; gap: 8px; align-items: center;"><span style="font-size: 13px; color: #56615B; margin-right: 4px;">Dentro de Nutrición:</span>' + sub + '</div></section>')

def boton_filtro(ic, t, valor=''):
    if valor:
        return '<button type="button" class="chip" style="height: 40px; padding: 0 14px; background: #EEF6EE; border: 1.5px solid #0E5A3A; color: #0E5A3A; font-weight: 600;">' + svg(I[ic], 16, 2) + t + ': ' + valor + svg(I['abajo'], 15, 2) + '</button>'
    return '<button type="button" class="chip" style="height: 40px; padding: 0 14px; font-size: 14px;">' + svg(I[ic], 16, 2) + t + '</button>'

def cat_filtros():
    return ('<section class="wrap" style="padding-top: 22px; display: flex; flex-direction: column; gap: 10px;">'
            '<div style="display: flex; gap: 8px; align-items: center; flex-wrap: wrap;"><button type="button" class="btn" style="height: 40px; border-radius: 999px; padding: 0 16px;">' + svg(I['filtro'], 17, 2.2) + 'Filtros'
            '<span style="min-width: 22px; height: 22px; border-radius: 999px; background: #B5D334; color: #072B1E; font-size: 12px; font-weight: 700; display: flex; align-items: center; justify-content: center;">2</span></button>' +
            boton_filtro('pata', 'Especie', 'Aves › Broilers') + boton_filtro('grid', 'Categoría', 'Nutrición › Piensos') + boton_filtro('virus', 'Enfermedad') + boton_filtro('pais', 'País') + boton_filtro('marca', 'Marca') +
            '<label style="display: flex; align-items: center; gap: 8px; font-size: 14px; margin-left: 6px;"><span style="width: 18px; height: 18px; border: 1.5px solid #B9C6BE; border-radius: 4px; background: #FFFFFF;"></span>Solo verificadas</label></div>'
            '<div style="display: flex; gap: 12px; align-items: baseline;"><strong style="font-size: 14px;">Filtros activos (2)</strong><a href="#" style="font-size: 13px;">Limpiar todo</a></div>'
            '<p style="margin: 0; font-size: 13px; color: #4A5650;">Los filtros se combinan: ves lo que cumple <strong>todos</strong>. Dentro de un mismo filtro basta con <strong>una</strong> opción. Lo que no depende de especie (equipos, bioseguridad…) sale con cualquier especie.</p>'
            '<div style="display: flex; align-items: center; border-bottom: 1px solid #E3E8E4; margin-top: 4px;"><a href="#" style="padding: 10px 0; margin-right: 26px; font-size: 15px; box-shadow: inset 0 -3px 0 #0E5A3A;">Productos 124</a>'
            '<a href="#" style="padding: 10px 0; font-size: 15px; font-weight: 500; color: #4A5650;">Empresas 42</a><span style="flex: 1;"></span>'
            '<span style="font-size: 13px; color: #56615B; margin-right: 8px;">Ordenar por</span><button type="button" class="chip" style="height: 36px; border-radius: 10px; font-weight: 600;">Más relevantes' + svg(I['abajo'], 15, 2) + '</button></div></section>')

def cat_listado():
    pag = ''.join('<a href="#" style="width: 36px; height: 36px; border-radius: 10px; display: flex; align-items: center; justify-content: center; font-size: 14px; ' + ('background: #0E5A3A; color: #FFFFFF;' if t == '1' else 'color: #17231D; font-weight: 500;') + '">' + t + '</a>' for t in ['1', '2', '3', '4', '5', '…', '11'])
    return ('<section class="wrap" style="padding-top: 20px;"><div style="display: grid; grid-template-columns: repeat(6, 210px); gap: 12px;">' + ''.join(tarjeta(*p) for p in LISTA) + '</div>'
            '<div style="display: flex; align-items: center; justify-content: space-between; padding: 22px 0 0; margin-top: 22px; border-top: 1px solid #E3E8E4; font-size: 14px; color: #4A5650;"><span>Mostrando 1–12 de 124 productos</span>'
            '<span style="display: flex; gap: 4px; align-items: center;">' + pag + '</span><span style="display: flex; gap: 8px; align-items: center;">Por página <span class="chip" style="height: 34px; border-radius: 10px;">12' + svg(I['abajo'], 14, 2) + '</span></span></div></section>')

def cat_ayuda():
    return ('<section class="wrap" style="padding: 32px 0 48px;"><div style="border-radius: 18px; background: #EEF6EE; border: 1px solid #CDE9D6; padding: 22px 26px; display: flex; gap: 18px; align-items: center;">'
            '<span style="width: 48px; height: 48px; border-radius: 12px; background: #0E5A3A; color: #FFFFFF; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I['proy'], 22) + '</span>'
            '<span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 17px;">¿No encuentras lo que buscas?</strong><span style="color: #4A5650;">Publica tu proyecto y te llegan propuestas de fabricantes y distribuidores, todo por Agroolink.</span></span>'
            '<a href="#" class="btn">Publicar un proyecto ' + svg(I['flecha'], 17, 2) + '</a><a href="#" class="btn2" style="background: transparent;">Crear una alerta</a></div></section>')

# ---------- Especie ----------
def esp_hero():
    chips = ''.join('<a href="#" class="chip" style="height: 40px; padding: 0 18px; font-size: 14.5px; ' + ('background: #B5D334; border-color: #B5D334; color: #072B1E; font-weight: 600;' if i == 0 else 'background: rgba(255,255,255,.95); border-color: transparent;') + '">' + t + '</a>'
                    for i, t in enumerate(['Todas', 'Broilers', 'Ponedoras', 'Reproductoras', 'Pavos', 'Aves cinegéticas', 'Otras aves']))
    cards = ''.join('<a href="#" class="card" style="padding: 14px; display: flex; flex-direction: column; gap: 6px; color: #17231D;"><span style="width: 36px; height: 36px; border-radius: 10px; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center;">' + svg(I[ic], 19) + '</span>'
                    '<strong style="font-size: 14px; font-weight: 600;">' + n + '</strong><span style="font-size: 12px; font-weight: 400; color: #56615B; line-height: 1.3;">' + d + '</span></a>' for n, ic, d in CAT)
    return (migas('Inicio', 'Aves') + '<section class="wrap" style="margin-top: 14px; box-sizing: border-box; border-radius: 22px; padding: 36px 36px 30px; background: linear-gradient(100deg, #0A3D28 45%, #3E6B4A 80%, #8FA77A); color: #FFFFFF; display: flex; flex-direction: column; gap: 18px;">'
            '<div style="display: flex; align-items: flex-start; gap: 20px;"><div style="flex: 1; display: flex; flex-direction: column; gap: 6px;"><h1 style="margin: 0; font-size: 40px; font-weight: 700; letter-spacing: -.02em;">Aves</h1>'
            '<p style="margin: 0; color: #DCEDE2;">3.240 productos, 410 empresas y 95 expertos en avicultura. Elige la producción o entra por categoría.</p></div>'
            '<a href="#" class="btn" style="background: #FFFFFF; color: #0A3D28;">Ver todos los resultados ' + svg(I['flecha'], 17, 2) + '</a></div>'
            '<div style="display: flex; flex-wrap: wrap; gap: 8px;">' + chips + '</div>'
            '<div style="display: grid; grid-template-columns: repeat(8, minmax(0, 1fr)); gap: 10px; padding-top: 6px;">' + cards + '</div></section>')

def esp_necesitas():
    n = [('nec_rendimiento', 'tend', 'Mejorar el rendimiento', 'Conversión, crecimiento y eficiencia productiva.'), ('nec_salud', 'cor', 'Mejorar la salud animal', 'Prevenir enfermedades y cuidar el bienestar de tus aves.'),
         ('nec_produccion', 'caja', 'Optimizar la producción', 'Soluciones para una producción más eficiente y rentable.'), ('nec_instalaciones', 'equipo', 'Mejorar las instalaciones', 'Equipos y tecnología para un manejo más seguro.'),
         ('nec_genetica', 'gen', 'Genética', 'Mejora el potencial genético de tus aves.'), ('nec_sostenible', 'hoja', 'Ser más sostenible', 'Soluciones más responsables con el medio ambiente.')]
    cards = ''.join('<a href="#" class="card" style="display: flex; flex-direction: column; overflow: hidden; color: #17231D;"><span style="position: relative; display: block;"><img src="' + IMG[k] + '" alt="" style="width: 100%; height: 150px; object-fit: cover; display: block;">'
                    '<span style="position: absolute; left: 14px; bottom: -18px; width: 40px; height: 40px; border-radius: 50%; background: #FFFFFF; color: #0E5A3A; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 8px rgba(0,0,0,.12);">' + svg(I[ic], 19) + '</span></span>'
                    '<span style="padding: 26px 14px 14px; display: flex; flex-direction: column; gap: 6px; flex: 1;"><strong style="font-size: 16px; font-weight: 600; color: #0A3D28;">' + t + '</strong><span style="font-size: 13px; font-weight: 400; color: #4A5650; line-height: 1.4;">' + d + '</span>'
                    '<span style="flex: 1;"></span><span style="align-self: flex-end; width: 34px; height: 34px; border-radius: 50%; background: #EEF6EE; color: #0E5A3A; display: flex; align-items: center; justify-content: center;">' + svg(I['flecha'], 17, 2) + '</span></span></a>' for k, ic, t, d in n)
    return '<section class="wrap" style="padding-top: 40px;">' + sec('¿Qué necesitas?', 'Empieza por tu objetivo y te enseñamos productos, empresas y expertos.') + '<div style="display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 12px;">' + cards + '</div></section>'

def esp_contenido():
    return ('<section class="wrap" style="padding: 48px 0 56px; display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(0, 1fr); gap: 20px;">'
            '<div style="border-radius: 20px; background: #FBF7F0; border: 1px solid #EFE4D2; padding: 28px; display: flex; gap: 24px; align-items: center;"><img src="' + IMG['editorial'] + '" alt="Pollito en una incubadora" style="width: 200px; height: 200px; object-fit: cover; border-radius: 16px;">'
            '<div style="display: flex; flex-direction: column; gap: 10px; align-items: flex-start;"><span style="font-size: 11px; font-weight: 700; letter-spacing: .08em; padding: 4px 10px; border-radius: 999px; background: #FFF0C9; color: #7A5A00;">CONTENIDOS</span>'
            '<h2 style="margin: 0; font-size: 24px; font-weight: 700; line-height: 1.2;">Conocimiento que impulsa la avicultura</h2><p style="margin: 0; color: #4A5650;">Artículos técnicos, guías y webinars de investigadores y expertos del sector.</p>'
            '<a href="#" class="btn2" style="background: #FFFFFF;">Ver contenidos de Aves ' + svg(I['flecha'], 16, 2) + '</a></div></div>'
            '<div class="card" style="border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 12px;"><div style="display: flex; justify-content: space-between; align-items: center;"><span class="kick" style="font-size: 11px; padding: 4px 10px; border-radius: 999px; background: #EEF6EE; color: #0E5A3A;">Evento destacado</span><span style="font-size: 13px; color: #0E5A3A; display: flex; align-items: center; gap: 6px;"><span style="width: 8px; height: 8px; border-radius: 50%; background: #2E9E5B;"></span>Inscripciones abiertas</span></div>'
            '<div style="display: flex; gap: 14px; align-items: center;"><span style="width: 64px; height: 64px; border-radius: 14px; background: #0A3D28; color: #FFFFFF; display: flex; flex-direction: column; align-items: center; justify-content: center; line-height: 1.1;"><span style="font-size: 11px; color: #A8E6BC;">FEB 2026</span><strong style="font-size: 20px;">24–25</strong></span>'
            '<span style="display: flex; flex-direction: column;"><strong style="font-size: 18px;">AviForum Puesta 2026</strong><span style="font-size: 13px; color: #56615B;">Madrid · Congreso internacional</span></span></div>'
            '<img src="' + IMG['evento'] + '" alt="Auditorio lleno en un congreso" style="width: 100%; height: 110px; object-fit: cover; border-radius: 12px;">'
            '<a href="#" class="ver" style="padding-top: 8px; border-top: 1px solid #EEF1EE;">Ver agenda y ponentes ' + svg(I['flecha'], 17, 2) + '</a></div></section>')

# ---------- Producto ----------
def prod_cabecera():
    thumbs = ''.join('<span style="width: 84px; height: 84px; border-radius: 12px; overflow: hidden; border: ' + ('2px solid #0E5A3A' if i == 0 else '1px solid #E3E8E4') + '; display: block;"><img src="' + IMG[k] + '" alt="" style="width: 100%; height: 100%; object-fit: cover;"></span>' for i, k in enumerate(['of_bolsa', 'of_pellets', 'of_pienso', 'of_granja']))
    accion = lambda ic, t, d: ('<a href="#" class="card" style="display: flex; gap: 12px; align-items: center; padding: 14px 16px; color: #17231D;"><span style="width: 40px; height: 40px; border-radius: 10px; background: #F1F4F2; color: #17231D; display: flex; align-items: center; justify-content: center; flex: none;">' + svg(I[ic], 20) + '</span>'
                               '<span style="flex: 1; display: flex; flex-direction: column;"><strong style="font-size: 14.5px; font-weight: 600;">' + t + '</strong>' + ('<span style="font-size: 12.5px; font-weight: 400; color: #56615B;">' + d + '</span>' if d else '') + '</span>' + svg(I['der'], 16, 2) + '</a>')
    benef = ''.join('<span style="display: flex; flex-direction: column; align-items: center; gap: 6px; text-align: center; font-size: 12.5px; color: #33424C;"><span style="color: #0E5A3A;">' + svg(I[ic], 24) + '</span>' + t + '</span>' for ic, t in [('tend', 'Mejora la conversión'), ('cor', 'Favorece la salud intestinal'), ('equipo', 'Optimiza el crecimiento'), ('euro', 'Reduce costes')])
    return ('<div class="wrap" style="display: flex; align-items: center; padding-top: 18px;"><div style="flex: 1;">' + migas('Inicio', 'Productos', 'Nutrición', 'Aditivos', 'OptiFeed®').replace('class="wrap" style="', 'style="width: auto; ').replace('padding-top: 18px;', '') + '</div>'
            '<a href="#" style="display: flex; gap: 6px; align-items: center; font-size: 14px; font-weight: 500; color: #33424C; margin-left: 18px;">' + svg(I['compartir'], 17) + 'Compartir</a>'
            '<a href="#" style="display: flex; gap: 6px; align-items: center; font-size: 14px; font-weight: 500; color: #33424C; margin-left: 18px;">' + svg(I['comp'], 17) + 'Comparar</a></div>'
            '<section class="wrap" style="padding-top: 18px; display: grid; grid-template-columns: 84px 420px minmax(0, 1fr) 320px; gap: 20px; align-items: start;">'
            '<div style="display: flex; flex-direction: column; gap: 10px;">' + thumbs + '<span style="width: 84px; height: 60px; border-radius: 12px; border: 1px solid #E3E8E4; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 12px; color: #4A5650;"><strong style="font-size: 15px; color: #17231D;">+2</strong>Ver más</span></div>'
            '<div style="display: flex; flex-direction: column; gap: 12px;"><div style="position: relative; height: 420px; border-radius: 18px; background: #F1F4F2; display: flex; align-items: center; justify-content: center; overflow: hidden;"><img src="' + IMG['of_bolsa'] + '" alt="Saco de OptiFeed de 25 kg" style="height: 380px; width: auto; border-radius: 10px;">'
            '<span style="position: absolute; right: 14px; bottom: 14px; font-size: 12px; font-weight: 600; padding: 4px 10px; border-radius: 999px; background: rgba(23,35,29,.7); color: #FFFFFF;">1 / 6</span></div>'
            '<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;"><a href="#" class="btn2" style="justify-content: center; border-color: #D5DED8; color: #17231D;">' + svg(I['video'], 17) + 'Ver vídeo</a><a href="#" class="btn2" style="justify-content: center; border-color: #D5DED8; color: #17231D;">' + svg(I['descarga'], 17) + 'Ficha técnica (PDF)</a></div></div>'
            '<div style="display: flex; flex-direction: column; gap: 12px;"><span style="align-self: flex-start; display: flex; gap: 6px; align-items: center; font-size: 13px; font-weight: 600; padding: 4px 12px; border-radius: 999px; background: #EEF6EE; color: #0E5A3A;">' + svg(I['ok'], 14, 2.4) + 'Producto verificado</span>'
            '<h1 style="margin: 0; font-size: 34px; font-weight: 700; letter-spacing: -.02em;">OptiFeed®</h1><p style="margin: 0; font-size: 17px; font-weight: 600; color: #33424C;">Aditivo nutricional para mejorar la conversión alimentaria</p>'
            '<p style="margin: 0; color: #4A5650; line-height: 1.55;">Solución nutricional para mejorar la eficiencia alimentaria en aves de engorde. Combina enzimas y compuestos funcionales que mejoran la digestibilidad y el rendimiento, respaldada por estudios y ensayos de campo.</p>'
            '<div style="display: flex; gap: 8px; flex-wrap: wrap;">' + ''.join('<span class="chip" style="cursor: default;">' + svg(I[ic], 15) + t + '</span>' for ic, t in [('grid', 'Aditivos'), ('caja', 'Polvo'), ('caja', 'Sacos de 25 kg')]) + '</div>'
            '<div style="display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; padding: 14px 0; border-top: 1px solid #E3E8E4; border-bottom: 1px solid #E3E8E4;">' + benef + '</div>'
            '<div style="display: flex; gap: 8px; flex-wrap: wrap; align-items: center;"><span style="font-size: 14px; color: #4A5650;">Para:</span>' + ''.join('<span class="chip" style="cursor: default; background: #F1F4F2; border-color: transparent;">' + t + '</span>' for t in ['Aves', 'Broilers', 'Ponedoras', 'Reproductoras']) + '</div></div>'
            '<aside style="display: flex; flex-direction: column; gap: 10px;"><a href="#" class="btn" style="height: 50px; border-radius: 14px; justify-content: space-between; padding: 0 20px; font-size: 16px;"><span style="display: flex; gap: 10px; align-items: center;">' + svg(I['msg'], 19) + 'Pedir información</span>' + svg(I['flecha'], 19, 2) + '</a>' +
            accion('carro', '¿Dónde comprar?', 'Distribuidores en tu zona') + accion('manos', 'Quiero distribuir este producto', 'Hazte distribuidor') + accion('guardar', 'Guardar en un tablero', '') +
            '<div class="card" style="padding: 16px; display: flex; flex-direction: column; gap: 10px;"><div style="display: flex; gap: 12px; align-items: center;"><span style="width: 56px; height: 56px; border-radius: 12px; border: 1px solid #E3E8E4; display: flex; align-items: center; justify-content: center; font-weight: 700; font-style: italic; color: #1D4E89;">Cargill</span>'
            '<span style="display: flex; flex-direction: column; gap: 4px;"><strong style="font-size: 16px;">Cargill</strong><span style="align-self: flex-start; font-size: 12px; font-weight: 600; padding: 2px 9px; border-radius: 999px; background: #EEF6EE; color: #0E5A3A;">Empresa verificada</span></span></div>'
            '<a href="#" class="ver" style="padding-top: 10px; border-top: 1px solid #EEF1EE; font-size: 14px;">Ver la ficha de la empresa ' + svg(I['flecha'], 16, 2) + '</a></div>'
            '<span class="hint" style="line-height: 1.4;">Todo va por Mensajes de Agroolink: la empresa te responde sin que tengas que dar tu teléfono ni tu email.</span></aside></section>')

def prod_detalle():
    tabs = ''.join('<a href="#" style="padding: 12px 0; margin-right: 30px; font-size: 15px; ' + ('box-shadow: inset 0 -3px 0 #0E5A3A;' if i == 0 else 'font-weight: 500; color: #4A5650;') + '">' + t + '</a>' for i, t in enumerate(['Información', 'Especificaciones', 'Beneficios', 'Resultados', 'Documentación', 'Certificaciones', 'Dónde comprar']))
    kv = lambda ic, k, v: '<div style="display: flex; align-items: center; gap: 10px; padding: 11px 0; border-top: 1px solid #EEF1EE; font-size: 14px;"><span style="color: #0E5A3A;">' + svg(I[ic], 17) + '</span><span style="flex: 1; color: #4A5650;">' + k + '</span><strong style="font-weight: 600;">' + v + '</strong></div>'
    obj = ''.join('<span style="font-size: 13px; padding: 4px 12px; border-radius: 999px; background: #F1F4F2;">' + t + '</span>' for t in ['Conversión alimentaria', 'Crecimiento', 'Salud intestinal', 'Rendimiento', 'Reducción de costes'])
    return ('<section class="wrap" style="padding-top: 40px;"><nav style="display: flex; border-bottom: 1px solid #E3E8E4;">' + tabs + '</nav>'
            '<div style="padding-top: 20px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; align-items: start;">'
            '<div class="card" style="padding: 20px 22px;"><h2 class="h2" style="font-size: 18px; padding-bottom: 8px;">Información clave</h2>' + kv('marca', 'Categoría', 'Nutrición › Aditivos') + kv('caja', 'Formato', 'Polvo') + kv('caja', 'Presentación', 'Sacos de 25 kg') + kv('doc', 'Registro', 'Según el país') + '</div>'
            '<div class="card" style="padding: 20px 22px; display: flex; flex-direction: column; gap: 10px;"><h2 class="h2" style="font-size: 18px;">Descripción del producto</h2><p style="margin: 0; color: #4A5650; line-height: 1.55; font-size: 14px;">OptiFeed® es un aditivo nutricional formulado para mejorar la eficiencia alimentaria y el rendimiento. Su fórmula combina enzimas y compuestos funcionales que actúan en el tracto digestivo, mejoran la digestibilidad de los nutrientes y ayudan a reducir los costes de producción.</p><a href="#" class="ver" style="font-size: 14px;">Leer más ' + svg(I['flecha'], 16, 2) + '</a></div>'
            '<div class="card" style="padding: 20px 22px; display: flex; flex-direction: column; gap: 12px;"><h2 class="h2" style="font-size: 18px;">Aplicación</h2><span style="display: flex; gap: 8px; align-items: center; font-weight: 600;"><span style="color: #0E5A3A;">' + svg(I['pata'], 18) + '</span>Aves › Broilers</span>'
            '<strong style="font-size: 14px;">Objetivos</strong><div style="display: flex; flex-wrap: wrap; gap: 6px;">' + obj + '</div>'
            '<strong style="font-size: 14px;">Disponible en</strong><div style="display: grid; grid-template-columns: 1fr 1fr; gap: 6px; font-size: 14px;">' + ''.join('<span style="display: flex; gap: 6px; align-items: center;"><span style="font-size: 11px; font-weight: 700; padding: 1px 5px; border: 1px solid #C9D2CC; border-radius: 4px;">' + c + '</span>' + p + '</span>' for c, p in [('ES', 'España'), ('PT', 'Portugal'), ('FR', 'Francia'), ('MX', 'México')]) + '</div></div></div></section>')

def prod_relacionados():
    rel = [p for p in LISTA if p[2] != 'OptiFeed®'][:6]
    return ('<section class="wrap" style="padding: 44px 0 56px;"><div class="sec"><div><h2 class="h2">Productos relacionados</h2><p class="sub">Otros productos de Nutrición para broilers</p></div>'
            '<a href="#" class="ver">Ver todos ' + svg(I['flecha'], 18, 2) + '</a></div><div style="display: grid; grid-template-columns: repeat(6, 210px); gap: 12px;">' + ''.join(tarjeta(*p) for p in rel) + '</div></section>')

PIEZAS = [('FrCatCabecera', 'C01 · Categoría · migas y cabecera (Aves › Broilers › Nutrición › Piensos)', cat_cabecera, 260),
          ('FrCatFiltros', 'C02 · Filtros como en los resultados: «Filtros» con contador, un botón por filtro, activos y cómo se combinan', cat_filtros, 178),
          ('FrCatListado', 'C03 · Listado: tarjetas de 210 (Comparar · Ver ficha) y paginación', cat_listado, 784),
          ('FrCatAyuda', 'C04 · ¿No encuentras lo que buscas? · Publicar un proyecto', cat_ayuda, 222),
          ('FrEspHero', 'E01 · Especie · Aves: producción y categorías', esp_hero, 426),
          ('FrEspNecesitas', 'E02 · Especie · ¿Qué necesitas?', esp_necesitas, 452),
          ('FrEspContenido', 'E03 · Especie · Contenidos y evento', esp_contenido, 468),
          ('FrProdCabecera', 'R01 · Producto · galería, datos y acciones (sin contactos)', prod_cabecera, 572),
          ('FrProdDetalle', 'R02 · Producto · pestañas e información', prod_detalle, 428),
          ('FrProdRelacionados', 'R03 · Producto · relacionados', prod_relacionados, 568)]
PAGINAS = [('FrPagCategoria', 'Página · Categoría (Piensos para broilers)', ['FrCatCabecera', 'FrCatFiltros', 'FrCatListado', 'FrCatAyuda']),
           ('FrPagEspecie', 'Página · Especie (Aves)', ['FrEspHero', 'FrEspNecesitas', 'FrProductos', 'FrEspContenido']),
           ('FrPagProducto', 'Página · Producto (OptiFeed®)', ['FrProdCabecera', 'FrProdDetalle', 'FrProdRelacionados'])]
if __name__ == '__main__':
    alto = {k: h for k, t, f, h in PIEZAS}
    otros = json.load(open(DEST + '../piezas.json'))['alto'] if os.path.exists(DEST + '../piezas.json') else {}
    alto.update({k: otros[k] for k in ('FrCabecera', 'FrProductos', 'FrPie') if k in otros})
    alto.update({k: int(v) for k, v in (a.split('=') for a in sys.argv[2:] if '=' in a)})
    for k, t, f, h in PIEZAS:
        open(DEST + k + '.dc.html', 'w').write(doc('Front · ' + t, 1440, alto[k], f()))
    tot = {}
    for k, t, ls in PAGINAS:
        ls = ['FrCabecera'] + ls + ['FrPie']
        H = sum(alto[x] for x in ls); tot[k] = H
        cuerpo = ''.join('<dc-import name="' + x + '" hint-size="1440px,' + str(alto[x]) + 'px"></dc-import>' for x in ls)
        open(DEST + k + '.dc.html', 'w').write(doc('Front · ' + t, 1440, H, '<div style="display: flex; flex-direction: column;">' + cuerpo + '</div>'))
    json.dump({'alto': alto, 'paginas': tot, 'piezas': [(k, t) for k, t, f, h in PIEZAS], 'titulos': {k: t for k, t, ls in PAGINAS}}, open(DEST + '../paginas.json', 'w'), ensure_ascii=False)
    print('ok', len(PIEZAS) + len(PAGINAS), tot)
