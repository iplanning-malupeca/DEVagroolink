"""Ficha de producto en móvil (versión de S4 · IntS4Ficha), como la ve el comprador. Escribe BuscaMovFicha; busqueda_canvas.py la pone en «002_MB_Búsqueda y filtros».
Sin precios ni contactos: «Pedir precio» abre la consulta (MB_Alta7) y la respuesta llega por Mensajes.
Uso: python3 tools/ficha_movil.py"""
import os, sys
sys.argv = sys.argv[:1] + [os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/project/canvas.json']
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from proyectos_movil import SB, svg, I, wrap, tabbar, backbar, W, VE

I.update({'heart': 'M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z', 'comp': 'M4 6h7v12H4zM13 6h7v12h-7z', 'pin': 'M12 21s7-6.5 7-12a7 7 0 0 0-14 0c0 5.5 7 12 7 12zM12 11a2 2 0 1 0 0-4 2 2 0 0 0 0 4z',
          'pdf': 'M6 3h9l4 4v14H6zM14 3v5h5M9 14h6M9 17h4', 'share': 'M4 12v7h16v-7M12 3v12M7 8l5-5 5 5'})

def fila(k, v):
    return '<div style="display:flex;justify-content:space-between;gap:12px;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13.5px"><span style="color:#4A5650">' + k + '</span><span style="text-align:right;font-weight:500">' + v + '</span></div>'

def ficha():
    tag = lambda t: '<span style="font-size:12px;font-weight:500;background:#EEF6EE;color:' + VE + ';border-radius:999px;padding:4px 10px">' + t + '</span>'
    b = ('<div style="position:relative;height:280px;background:#EAF0EB;display:flex;align-items:center;justify-content:center;color:#56615B;font-size:13px">[Foto de producto]'
         '<span style="position:absolute;right:12px;top:12px;width:40px;height:40px;border-radius:50%;background:#FFFFFF;color:' + VE + ';display:flex;align-items:center;justify-content:center;box-shadow:0 1px 4px rgba(0,0,0,.12)">' + svg(I['share'], 18) + '</span>'
         '<span style="position:absolute;bottom:12px;left:0;right:0;display:flex;gap:6px;justify-content:center">' + ''.join('<span style="width:%dpx;height:6px;border-radius:3px;background:%s"></span>' % ((18, VE) if i == 0 else (6, '#B9C6BE')) for i in range(4)) + '</span></div>'
         '<div style="padding:16px 16px 190px;display:flex;flex-direction:column;gap:12px;background:#FFFFFF">'
         '<span class="hint">Nutrición › Correctores y premezclas › Avicultura</span>'
         '<h1 style="margin:0;font-size:22px;font-weight:700;line-height:1.2">Corrector vitamínico CV-20</h1>'
         '<span style="display:flex;align-items:center;gap:8px;font-size:14px;color:' + VE + ';font-weight:500"><span style="width:26px;height:26px;border-radius:7px;background:#1F3A5F;color:#FFFFFF;font-size:10px;font-weight:600;display:flex;align-items:center;justify-content:center">AE</span>AgroExport SRL'
         '<svg width="15" height="15" viewBox="0 0 24 24" role="img" aria-label="Empresa verificada"><circle cx="12" cy="12" r="10" fill="' + VE + '"/><path d="m8 12 3 3 5-6" fill="none" stroke="#FFFFFF" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg></span>'
         '<div style="display:flex;flex-wrap:wrap;gap:6px">' + tag('Avicultura') + tag('Broilers') + tag('Fase de arranque') + '</div>'
         '<p style="margin:0;font-size:14px;color:#2F3D36;line-height:1.45">[Descripción del producto según su ficha técnica: composición, dosis recomendada y presentación.]</p>'
         '<div style="display:flex;gap:8px"><span class="btn" style="flex:1;height:44px;gap:6px;background:#EEF6EE;border:1.5px solid ' + VE + ';color:' + VE + '">' + svg(I['heart'], 18) + 'Guardado</span>'
         '<span class="btn" style="flex:1;height:44px;gap:6px">' + svg(I['comp'], 18) + 'Comparar</span></div>'
         '<div style="display:flex;gap:10px;align-items:flex-start;padding:12px;border-radius:12px;background:#F2F7F3;border:1px solid #DCE9DF;font-size:13px">' + '<span style="color:' + VE + '">' + svg(I['pin'], 18) + '</span>'
         '<span><strong>En Lleida lo sirve Agropecuària del Segre</strong>, distribuidor oficial de AgroExport. Al pedir precio, tu solicitud le llega a él.</span></div>'
         '<div><strong style="font-size:15px">Datos</strong>' + fila('Especie', 'Broilers') + fila('Presentación', 'Saco de 25 kg') + fila('Disponible en', 'España y Portugal') +
         '<div style="display:flex;justify-content:space-between;align-items:center;padding:10px 0;border-top:1px solid #EEF1EE;font-size:13.5px"><span style="color:#4A5650">Ficha técnica</span><span style="display:flex;gap:6px;align-items:center;color:' + VE + ';font-weight:600">' + svg(I['pdf'], 16) + 'Descargar PDF</span></div></div>'
         '<span class="hint">Sin precios en la ficha: pide precio y te responden por Mensajes. Tus datos de contacto no se comparten.</span></div>')
    foot = ('<div class="foot" style="bottom:84px;padding-bottom:10px"><span class="btn" style="height:48px;width:52px;padding:0;color:' + VE + ';border-color:' + VE + '">' + svg(I['tab'], 20) + '</span>'
            '<span class="btnp" style="flex:1;height:48px;background:' + VE + ';font-size:14px">Pedir precio</span></div>')
    return SB + backbar('Corrector vitamínico CV-20', 'AgroExport SRL') + b + foot + tabbar('Explorar')

if __name__ == '__main__':
    h = int(os.environ.get('ALTO', 1150))
    html = wrap('Móvil · Ficha de producto', h, ficha())
    open(W + '/project/BuscaMovFicha.dc.html', 'w').write(html)
    print('ok')
