"""Móvil · Home y menú. Genera MobTabBar (componente) y los tableros Mob*.
Uso: python3 tools/movil.py  (escribe en project/ y actualiza project/canvas.json)"""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/'

G, LIME, INK, MUT, BOR, BG = '#0E5A3A', '#B5D334', '#17231D', '#56615B', '#E6EBE7', '#F6F8F6'

I = {
 'home': 'M3 10.5 12 3l9 7.5V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z',
 'compass': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM15.5 8.5l-2 5-5 2 2-5z',
 'search': 'M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zM20 20l-3.5-3.5',
 'brief': 'M5 7h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2zM8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M3 13h18',
 'grid': 'M4 4h7v7H4zM13 4h7v7h-7zM4 13h7v7H4zM13 13h7v7h-7z',
 'menu': 'M4 6h16M4 12h16M4 18h16',
 'bell': 'M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10 21a2 2 0 0 0 4 0',
 'msg': 'M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z',
 'chev': 'm9 6 6 6-6 6', 'down': 'm6 9 6 6 6-6',
 'back': 'M19 12H5M12 19l-7-7 7-7', 'x': 'M6 6l12 12M18 6 6 18',
 'clock': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM12 7v5l3 2',
 'trend': 'M3 17l6-6 4 4 8-8M15 7h6v6',
 'pin': 'M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11zM12 7.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z',
 'plus': 'M12 5v14M5 12h14', 'check': 'm5 12 5 5 9-10',
 'building': 'M5 3h14v18H5zM9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1',
 'user': 'M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM4 21a8 8 0 0 1 16 0',
 'book': 'M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5zM4 19.5A2.5 2.5 0 0 0 6.5 22H20v-5',
 'cal': 'M5 5h14a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2zM16 3v4M8 3v4M3 10h18',
 'gear': 'M12 9a3 3 0 1 0 0 6 3 3 0 0 0 0-6zM12 2v3M12 19v3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M2 12h3M19 12h3M4.9 19.1 7 17M17 7l2.1-2.1',
 'help': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.6.3-1 .8-1 1.5V14M12 17h.01',
 'logout': 'M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9',
 'scale': 'M12 3v18M5 7h14M5 7l-3 7a3 3 0 0 0 6 0zM19 7l-3 7a3 3 0 0 0 6 0z',
 'inbox': 'M22 12h-6l-2 3h-4l-2-3H2M5.5 5h13L22 12v6a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-6z',
 'globe': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18',
 'star': 'm12 3 2.8 5.7 6.2.9-4.5 4.4 1 6.2L12 17.3 6.5 20.2l1-6.2L3 9.6l6.2-.9z',
 'sliders': 'M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0M14 4v4M8 10v4M16 16v4',
 'tool': 'M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z',
 'ext': 'M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5',
 'bookmark': 'M6 3h12v18l-6-4-6 4z', 'mic': 'M12 3a3 3 0 0 0-3 3v6a3 3 0 0 0 6 0V6a3 3 0 0 0-3-3zM5 11a7 7 0 0 0 14 0M12 18v3',
 # familias
 'nutricion': 'M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.5 19 2c1 2 2 4.2 2 8 0 5.5-4.8 10-10 10zM2 21c0-3 1.9-5.4 5.1-6',
 'materias_primas': 'M7 21h10M12 21V11M12 11c0-3 2-5 6-5 0 3-2 5-6 5zM12 14c0-3-2-5-6-5 0 3 2 5 6 5z',
 'salud': 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10zM12 8v6M9 11h6',
 'genetica': 'M5 3c0 6 14 6 14 12M19 3c0 6-14 6-14 12M5 21c0-2 1-3 2-4M19 21c0-2-1-3-2-4M8 7h8M8 13h8',
 'equipamiento': 'M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z',
 'avicola': 'M12 3c-4 0-7 6-7 11a7 7 0 0 0 14 0c0-5-3-11-7-11z',
 'porcino': 'M3 21V9l9-6 9 6v12M8 21v-7h8v7',
 'rumiantes': 'M12 3s6 7 6 11a6 6 0 0 1-12 0c0-4 6-11 6-11z',
 'sostenibilidad': 'M13 2 4 14h7l-1 8 9-12h-7z',
 'tecnologia': 'M8 6h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2zM9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4',
}

def ic(n, s=20, c='currentColor', w=1.8):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="%s"/></svg>') % (s, s, c, w, I[n])

FAM = [('nutricion', 'Nutrición y aditivos', 'Nutrición', 1860, 17), ('salud', 'Salud animal y bioseguridad', 'Salud', 1240, 10),
       ('genetica', 'Genética y reproducción', 'Genética', 410, 7), ('equipamiento', 'Equipamiento e instalaciones', 'Equipos', 2310, 15),
       ('tecnologia', 'Tecnología, sensores y software', 'Tecnología', 680, 9), ('materias_primas', 'Materias primas', 'Materias primas', 520, 7),
       ('sostenibilidad', 'Sostenibilidad y energía', 'Sostenibilidad', 390, 8), ('avicola', 'Equipamiento avícola', 'Avícola', 740, 8),
       ('porcino', 'Equipamiento porcino', 'Porcino', 460, 5), ('rumiantes', 'Equipamiento para rumiantes', 'Rumiantes', 380, 7)]
ESP = [('Avicultura', '🐔', '#FFF4DE', 4120, 640), ('Porcino', '🐖', '#FDE9EC', 3870, 590), ('Bovino', '🐄', '#EEF2E6', 3150, 520),
       ('Ovino', '🐑', '#F1EFEA', 1290, 260), ('Caprino', '🐐', '#F3EEE6', 980, 210), ('Acuicultura', '🐟', '#E5F1F7', 760, 150),
       ('Cunicultura', '🐇', '#F2EDF6', 410, 95)]

CSS = """
body{margin:0;font-family:'Poppins',sans-serif;color:#17231D;background:#FFFFFF}
*{box-sizing:border-box}
a{color:#0E5A3A;text-decoration:none;font-weight:500}
.ph{width:390px;position:relative;background:#F6F8F6;overflow:hidden;display:flex;flex-direction:column}
.sb{height:44px;flex:none;display:flex;align-items:center;justify-content:space-between;padding:0 26px 0 30px;font-size:15px;font-weight:600}
.sbi{display:flex;gap:6px;align-items:center}
.top{height:52px;flex:none;display:flex;align-items:center;gap:10px;padding:0 16px}
.ib{width:40px;height:40px;border-radius:12px;display:inline-flex;align-items:center;justify-content:center;color:#17231D;position:relative;flex:none}
.dot{position:absolute;top:8px;right:8px;width:8px;height:8px;border-radius:50%;background:#D64545;border:2px solid #F6F8F6}
.bdg{position:absolute;top:4px;right:2px;min-width:17px;height:17px;padding:0 4px;border-radius:9px;background:#D64545;color:#FFF;font-size:10px;font-weight:600;display:flex;align-items:center;justify-content:center;border:2px solid #F6F8F6}
.av{width:36px;height:36px;border-radius:50%;background:#0E5A3A;color:#FFFFFF;font-size:13px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;flex:none}
.logo{display:flex;align-items:center;gap:8px;font-size:19px;font-weight:700;letter-spacing:-.3px;color:#0E5A3A}
.logo b{width:30px;height:30px;border-radius:9px;background:#0E5A3A;display:inline-flex;align-items:center;justify-content:center}
.logo i{font-style:normal;color:#17231D}
.pad{padding:0 16px}
.srch{height:48px;border-radius:14px;background:#FFFFFF;border:1px solid #DCE4DE;display:flex;align-items:center;gap:10px;padding:0 6px 0 14px;color:#8A948F;font-size:13.5px;box-shadow:0 1px 2px rgba(16,40,28,.04)}
.srch span{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.go{width:36px;height:36px;border-radius:10px;background:#0E5A3A;color:#FFF;display:inline-flex;align-items:center;justify-content:center;flex:none}
.sec{display:flex;align-items:baseline;justify-content:space-between;margin:0 0 10px}
.sec h2{font-size:16px;font-weight:600;margin:0}
.sec a{font-size:12.5px}
.chip{display:inline-flex;align-items:center;gap:6px;height:34px;padding:0 13px;border-radius:999px;background:#FFFFFF;border:1px solid #DCE4DE;font-size:12.5px;font-weight:500;white-space:nowrap;color:#17231D;flex:none}
.chip.on{background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF}
.chip.soft{background:#EEF6EE;border-color:#EEF6EE;color:#0E5A3A}
.row{display:flex;gap:8px}
.hs{display:flex;gap:10px;overflow:hidden}
.card{background:#FFFFFF;border:1px solid #E6EBE7;border-radius:16px;box-shadow:0 1px 2px rgba(16,40,28,.04)}
.li{display:flex;align-items:center;gap:12px;padding:0 14px;min-height:54px;border-bottom:1px solid #EEF1EE;font-size:14px;color:#17231D}
.li:last-child{border-bottom:0}
.li .t{flex:1;min-width:0}
.li small{display:block;font-size:11.5px;color:#56615B;font-weight:400;margin-top:1px}
.li .n{font-size:12px;color:#56615B}
.ico{width:36px;height:36px;border-radius:11px;background:#EEF6EE;color:#0E5A3A;display:inline-flex;align-items:center;justify-content:center;flex:none}
.emo{width:44px;height:44px;border-radius:13px;display:inline-flex;align-items:center;justify-content:center;font-size:23px;flex:none}
.cap{font-size:11px;font-weight:600;letter-spacing:.6px;color:#56615B;text-transform:uppercase;margin:0 0 8px 2px}
.btn{height:50px;border-radius:14px;background:#0E5A3A;color:#FFFFFF;font-size:14.5px;font-weight:600;display:flex;align-items:center;justify-content:center;gap:8px}
.btn2{height:44px;border-radius:12px;background:#FFFFFF;border:1px solid #CFD8D2;color:#17231D;font-size:13.5px;font-weight:500;display:flex;align-items:center;justify-content:center;gap:8px}
.seg{display:flex;background:#E9EEEA;border-radius:12px;padding:3px}
.seg span{flex:1;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:13.5px;font-weight:500;color:#56615B}
.seg span.on{background:#FFFFFF;color:#17231D;font-weight:600;box-shadow:0 1px 3px rgba(16,40,28,.12)}
.tabw{position:absolute;left:0;right:0;bottom:0}
.sticky{position:absolute;left:0;right:0;bottom:84px;padding:12px 16px;background:linear-gradient(rgba(246,248,246,0),#F6F8F6 30%)}
.h1{font-size:24px;font-weight:600;letter-spacing:-.3px;margin:0}
.sub{font-size:13px;color:#56615B;margin:4px 0 0;line-height:1.45}
.prod{width:156px;flex:none;overflow:hidden}
.pimg{height:104px;display:flex;align-items:center;justify-content:center;border-bottom:1px solid #EEF1EE}
.tag{display:inline-flex;height:22px;padding:0 8px;border-radius:6px;background:#F1F4F1;font-size:10.5px;color:#4A5650;align-items:center;white-space:nowrap}
"""

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>%s</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&amp;display=swap" rel="stylesheet">
<style>%s</style>
</helmet>
"""
TAIL = """</x-dc>
<script type="text/x-dc" data-dc-script data-props='%s'>
class Component extends DCLogic {
  renderVals() { return %s; }
}
</script>
</body>
</html>
"""

SB = ('<div class="sb"><span>9:41</span><span class="sbi">'
      '<svg width="18" height="12" viewBox="0 0 18 12" aria-hidden="true"><rect x="0" y="8" width="3" height="4" rx="1" fill="#17231D"/><rect x="5" y="5" width="3" height="7" rx="1" fill="#17231D"/><rect x="10" y="2.5" width="3" height="9.5" rx="1" fill="#17231D"/><rect x="15" y="0" width="3" height="12" rx="1" fill="#17231D"/></svg>'
      '<svg width="16" height="12" viewBox="0 0 24 18" fill="none" stroke="#17231D" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M2 6a15 15 0 0 1 20 0M5.5 9.5a10 10 0 0 1 13 0M9 13a5 5 0 0 1 6 0"/></svg>'
      '<svg width="26" height="12" viewBox="0 0 26 12" aria-hidden="true"><rect x=".5" y=".5" width="22" height="11" rx="3.5" fill="none" stroke="#17231D" opacity=".4"/><rect x="2" y="2" width="17" height="8" rx="2" fill="#17231D"/><rect x="23.5" y="4" width="2" height="4" rx="1" fill="#17231D" opacity=".4"/></svg>'
      '</span></div>')
LOGO = ('<span class="logo"><b>' + ic('nutricion', 17, LIME, 2.2) + '</b><span>agroo<i>link</i></span></span>')

def tab(n):
    return ('<div class="tabw"><dc-import name="MobTabBar" activo="{{ tab }}" hint-size="390px,84px"></dc-import></div>', n)

def board(fn, title, h, body, tabn=None):
    t = HEAD % (title, CSS)
    t += '<div class="ph" style="height: %dpx;">\n' % h + SB + '\n' + body + '\n'
    vals = '{}'
    if tabn:
        t += tab(tabn)[0] + '\n'
        vals = '{ tab: %d }' % tabn
    t += '</div>\n'
    t += TAIL % (json.dumps({'$preview': {'width': 390, 'height': h}}), vals)
    open(P + fn, 'w').write(t)
    return fn, title, h

def topback(title='', right=''):
    return ('<div class="top"><span class="ib" style="margin-left:-8px;">' + ic('back', 22) + '</span>'
            '<span style="flex:1;font-size:16px;font-weight:600;text-align:center;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' + title + '</span>'
            '<span style="width:40px;display:flex;justify-content:flex-end;">' + right + '</span></div>')

def chev(c='#8A948F'):
    return ic('chev', 16, c, 2)

# ---------------- componente barra inferior ----------------
TABS = [('home', 'Inicio'), ('compass', 'Explorar'), ('brief', 'Proyectos'), ('grid', 'Tableros'), ('menu', 'Menú')]
def tabbar():
    t = HEAD % ('Componente · Barra inferior móvil', CSS + """
.tb{width:390px;height:84px;background:#FFFFFF;border-top:1px solid #E6EBE7;display:flex;flex-direction:column}
.tbr{display:flex;height:58px;padding:0 6px}
.tbi{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;font-size:10.5px;font-weight:500;position:relative}
.tbp{width:52px;height:30px;border-radius:15px;display:flex;align-items:center;justify-content:center}
.hi{height:26px;display:flex;align-items:center;justify-content:center}
.hi span{width:134px;height:5px;border-radius:3px;background:#17231D}
.nb{position:absolute;top:4px;left:50%;margin-left:8px;min-width:16px;height:16px;padding:0 4px;border-radius:8px;background:#D64545;color:#FFF;font-size:9.5px;font-weight:600;display:flex;align-items:center;justify-content:center;border:2px solid #FFF}
""")
    t += '<nav class="tb" aria-label="Navegación principal"><div class="tbr">\n'
    t += '<sc-for list="{{ items }}" as="t" hint-placeholder-count="5">\n'
    t += ('<a href="#" class="tbi" aria-current="{{ t.cur }}" style="color: {{ t.tinta }}; font-weight: {{ t.peso }};">'
          '<span class="tbp" style="background: {{ t.fondo }};"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="{{ t.grosor }}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{{ t.d }}"/></svg></span>'
          '<span>{{ t.label }}</span>'
          '<sc-if value="{{ t.badge }}" hint-placeholder-val="{{ false }}"><span class="nb">{{ t.badge }}</span></sc-if></a>\n')
    t += '</sc-for>\n</div><div class="hi"><span></span></div></nav>\n'
    items = json.dumps([[I[k], l] for k, l in TABS], ensure_ascii=False)
    t += """</x-dc>
<script type="text/x-dc" data-dc-script data-props='{"activo":{"editor":"int","default":1,"min":1,"max":5},"proyectos":{"editor":"text","default":"3"},"$preview":{"width":390,"height":84}}'>
class Component extends DCLogic {
  renderVals() {
    const a = this.props.activo ?? 1;
    const T = %s;
    const items = T.map(([d, label], i) => {
      const on = i + 1 === a;
      return { d: d, label: label, cur: on ? 'page' : 'false', tinta: on ? '#0E5A3A' : '#56615B', peso: on ? '600' : '500',
        fondo: on ? '#E4F0D0' : 'transparent', grosor: on ? '2.1' : '1.8', badge: i === 2 ? (this.props.proyectos ?? '3') : '' };
    });
    return { items: items };
  }
}
</script>
</body>
</html>
""" % items
    open(P + 'MobTabBar.dc.html', 'w').write(t)

# ---------------- piezas ----------------
def famgrid(n=7):
    out = '<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px 6px;">'
    for k, _, short, _, _ in FAM[:n]:
        out += ('<a href="#" style="display:flex;flex-direction:column;align-items:center;gap:6px;color:#17231D;font-size:11.5px;font-weight:500;text-align:center;line-height:1.25;">'
                '<span class="ico" style="width:52px;height:52px;border-radius:16px;background:#FFFFFF;border:1px solid #E6EBE7;">' + ic(k, 24, G) + '</span>' + short + '</a>')
    out += ('<a href="#" style="display:flex;flex-direction:column;align-items:center;gap:6px;color:#0E5A3A;font-size:11.5px;font-weight:600;text-align:center;">'
            '<span class="ico" style="width:52px;height:52px;border-radius:16px;background:#EEF6EE;">' + ic('grid', 22, G) + '</span>Ver todas</a>')
    return out + '</div>'

def explore_cards():
    return ('<div class="row">'
            '<a href="#" class="card" style="flex:1;padding:14px;background:#0E5A3A;border-color:#0E5A3A;color:#FFFFFF;display:flex;flex-direction:column;gap:10px;">'
            '<span style="font-size:20px;letter-spacing:3px;">🐔🐖🐄</span><span style="font-size:14px;font-weight:600;line-height:1.25;">Explorar por<br>especie</span>'
            '<span style="font-size:11px;opacity:.8;font-weight:400;">7 especies · sus producciones</span></a>'
            '<a href="#" class="card" style="flex:1;padding:14px;color:#17231D;display:flex;flex-direction:column;gap:10px;">'
            '<span class="ico" style="width:30px;height:30px;border-radius:9px;">' + ic('grid', 17, G) + '</span><span style="font-size:14px;font-weight:600;line-height:1.25;">Explorar por<br>categoría</span>'
            '<span style="font-size:11px;color:#56615B;font-weight:400;">10 familias de producto</span></a></div>')

def pcard(name, by, tint, glyph, tags, verified=True):
    return ('<div class="card prod"><div class="pimg" style="background:' + tint + ';">' + ic(glyph, 38, G, 1.5) + '</div>'
            '<div style="padding:10px 11px 12px;display:flex;flex-direction:column;gap:6px;">'
            '<span style="font-size:13px;font-weight:600;line-height:1.25;">' + name + '</span>'
            '<span style="font-size:11px;color:#56615B;display:flex;align-items:center;gap:4px;">' + by +
            (ic('check', 11, G, 3) if verified else '') + '</span>'
            '<span style="display:flex;gap:4px;flex-wrap:wrap;">' + ''.join('<span class="tag">%s</span>' % t for t in tags) + '</span></div></div>')

def comp(name, ini, color, sub):
    return ('<div class="card" style="width:112px;flex:none;padding:12px 8px;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center;">'
            '<span style="width:46px;height:46px;border-radius:12px;background:' + color + ';color:#FFF;font-size:14px;font-weight:700;display:flex;align-items:center;justify-content:center;">' + ini + '</span>'
            '<span style="font-size:12px;font-weight:600;line-height:1.2;">' + name + '</span><span style="font-size:10.5px;color:#56615B;">' + sub + '</span></div>')

# ---------------- tableros ----------------
B = []

# M1 Home logueado
body = ('<div class="top"><span style="flex:1;">' + LOGO + '</span>'
        '<span class="ib">' + ic('msg', 22) + '<span class="bdg">2</span></span>'
        '<span class="ib">' + ic('bell', 22) + '<span class="dot"></span></span>'
        '<span class="av">SM</span></div>'
        '<div class="pad" style="display:flex;flex-direction:column;gap:22px;padding-top:6px;">'
        '<div><div style="display:flex;align-items:center;justify-content:space-between;">'
        '<p style="margin:0;font-size:22px;font-weight:600;letter-spacing:-.3px;">Hola, Samuel</p>'
        '<a href="#" class="chip" style="height:30px;padding:0 10px;font-size:12px;">' + ic('pin', 14, G) + 'España' + ic('down', 13, '#56615B', 2) + '</a></div>'
        '<p class="sub" style="margin-top:2px;">Esto es lo nuevo para tus especies.</p></div>'
        '<div class="srch">' + ic('search', 19, '#56615B') + '<span>Productos, empresas, expertos…</span><span class="ib" style="width:36px;height:36px;color:#56615B;">' + ic('mic', 19) + '</span></div>'
        '<div><div class="sec"><h2 style="font-size:13px;color:#56615B;font-weight:500;">Tus intereses</h2><a href="#">Editar</a></div>'
        '<div class="row" style="overflow:hidden;margin-right:-16px;"><span class="chip on">🐔 Avicultura</span><span class="chip on">🐖 Porcino</span><span class="chip soft">Bienestar animal</span><span class="chip soft">Huevo campero</span><span class="chip soft">Conversión alimenticia</span></div></div>'
        + explore_cards() +
        # proyecto
        '<div><div class="sec"><h2>Tus proyectos</h2><a href="#">Ver todos</a></div>'
        '<div class="card" style="padding:14px;display:flex;flex-direction:column;gap:12px;">'
        '<div style="display:flex;gap:12px;align-items:flex-start;"><span class="ico">' + ic('brief', 19, G) + '</span>'
        '<div style="flex:1;min-width:0;"><span style="font-size:14px;font-weight:600;display:block;">Nave 2 · broilers</span>'
        '<span style="font-size:12px;color:#56615B;">Ventilación y cooling · Lleida</span></div>'
        '<span style="height:24px;padding:0 9px;border-radius:999px;background:#FCEFD9;color:#8A5A00;font-size:11px;font-weight:600;display:inline-flex;align-items:center;white-space:nowrap;">3 propuestas nuevas</span></div>'
        '<div class="row"><a href="#" class="btn" style="flex:1;height:42px;font-size:13.5px;">Ver propuestas</a>'
        '<a href="#" class="btn2" style="flex:1;color:#0E5A3A;">' + ic('plus', 16, G, 2.2) + 'Nuevo proyecto</a></div></div></div>'
        # categorias
        '<div><div class="sec"><h2>Categorías</h2></div>' + famgrid() + '</div>'
        # productos
        '<div><div class="sec"><h2>Novedades en avicultura</h2><a href="#">Ver más</a></div><div class="hs" style="margin-right:-16px;">'
        + pcard('Aviary Pro · aviario para ponedoras', 'Zucami', '#EEF2E6', 'avicola', ['Avicultura', 'Equipos'])
        + pcard('Ronozyme® ProAct', 'DSM-Firmenich', '#FFF4DE', 'nutricion', ['Enzimas', 'Broilers'])
        + pcard('Sensor de ambiente NH₃', 'AgroNova', '#E5F1F7', 'tecnologia', ['Sensores']) +
        '</div></div>'
        # empresas
        '<div><div class="sec"><h2>Empresas destacadas</h2><a href="#">Ver todas</a></div><div class="hs" style="margin-right:-16px;">'
        + comp('DSM-Firmenich', 'dsm', '#1E4FA0', 'Nutrición') + comp('Zucami', 'Z', '#C8102E', 'Equipos avícolas')
        + comp('AgroNova', 'AN', '#0E5A3A', 'Sensores') + '</div></div>'
        # tableros
        '<div><div class="sec"><h2>Tus tableros</h2><a href="#">Ver todos</a></div><div class="row">'
        '<a href="#" class="card" style="flex:1;padding:12px;color:#17231D;"><span style="display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-bottom:10px;">'
        '<span style="height:34px;border-radius:7px;background:#FFF4DE;"></span><span style="height:34px;border-radius:7px;background:#EEF2E6;"></span><span style="height:34px;border-radius:7px;background:#E5F1F7;"></span><span style="height:34px;border-radius:7px;background:#F2EDF6;"></span></span>'
        '<span style="font-size:13px;font-weight:600;display:block;">Nutrición avícola</span><span style="font-size:11px;color:#56615B;font-weight:400;">12 productos</span></a>'
        '<a href="#" class="card" style="flex:1;padding:12px;color:#17231D;"><span style="display:grid;grid-template-columns:1fr 1fr;gap:4px;margin-bottom:10px;">'
        '<span style="height:34px;border-radius:7px;background:#E5F1F7;"></span><span style="height:34px;border-radius:7px;background:#EEF2E6;"></span><span style="height:34px;border-radius:7px;background:#FDE9EC;"></span><span style="height:34px;border-radius:7px;background:#F1EFEA;"></span></span>'
        '<span style="font-size:13px;font-weight:600;display:block;">Nave 2 · broilers</span><span style="font-size:11px;color:#56615B;font-weight:400;">8 productos · 3 propuestas</span></a></div></div>'
        # contenido
        '<div><div class="sec"><h2>Para estar al día</h2><a href="#">Agrinews ' + ic('ext', 12, G, 2) + '</a></div>'
        '<div class="card" style="overflow:hidden;">'
        '<a href="#" class="li" style="padding:12px 14px;"><span class="emo" style="background:#F2EDF6;border-radius:12px;">' + ic('book', 20, '#4B3BA6') + '</span><span class="t" style="font-weight:500;line-height:1.3;">Cómo reducir el estrés térmico en broilers<small>Guía técnica · 8 min</small></span></a>'
        '<a href="#" class="li" style="padding:12px 14px;"><span class="emo" style="background:#EEF6EE;border-radius:12px;">' + ic('cal', 20, G) + '</span><span class="t" style="font-weight:500;line-height:1.3;">AviForum 2026<small>Evento · 12–13 nov · Madrid</small></span></a>'
        '</div></div>'
        '<div style="height:96px;"></div></div>')
B.append(board('MobHome.dc.html', 'Móvil · Home con sesión', 2010, body, 1))

# M2 Home sin sesión
body = ('<div class="top"><span style="flex:1;">' + LOGO + '</span><a href="#" class="chip" style="height:36px;">Entrar</a></div>'
        '<div style="margin:6px 16px 0;border-radius:22px;padding:22px 18px 18px;background:linear-gradient(160deg,#0E5A3A 0%,#13714A 60%,#2E8A4F 100%);color:#FFFFFF;display:flex;flex-direction:column;gap:12px;">'
        '<span style="font-size:10.5px;font-weight:600;letter-spacing:1.2px;color:' + LIME + ';">PRODUCTOS · CONOCIMIENTO · OPORTUNIDADES</span>'
        '<p style="margin:0;font-size:25px;font-weight:600;line-height:1.18;letter-spacing:-.4px;">El marketplace B2B de la ganadería</p>'
        '<p style="margin:0;font-size:13px;line-height:1.45;opacity:.85;">Encuentra productos, empresas y expertos para tu especie y tu zona.</p>'
        '<div class="srch" style="border:0;margin-top:4px;">' + ic('search', 19, '#56615B') + '<span>Productos, empresas, expertos…</span><span class="go">' + ic('back', 18, '#FFF', 2.2).replace('M19 12H5M12 19l-7-7 7-7', 'M5 12h14M12 5l7 7-7 7') + '</span></div></div>'
        '<div class="pad" style="display:flex;flex-direction:column;gap:24px;padding-top:22px;">'
        + explore_cards() +
        '<div><div class="sec"><h2>Especies</h2><a href="#">Ver todas</a></div><div class="hs" style="margin-right:-16px;">'
        + ''.join('<a href="#" style="display:flex;flex-direction:column;align-items:center;gap:6px;width:64px;flex:none;color:#17231D;font-size:11.5px;font-weight:500;"><span class="emo" style="width:56px;height:56px;border-radius:18px;font-size:27px;background:%s;">%s</span>%s</a>' % (c, e, n) for n, e, c, _, _ in ESP[:6]) +
        '</div></div>'
        '<div><div class="sec"><h2>Categorías</h2></div>' + famgrid() + '</div>'
        '<div><div class="sec"><h2>Empresas destacadas</h2><a href="#">Ver todas</a></div><div class="hs" style="margin-right:-16px;">'
        + comp('DSM-Firmenich', 'dsm', '#1E4FA0', 'Nutrición') + comp('Zucami', 'Z', '#C8102E', 'Equipos avícolas')
        + comp('AgroNova', 'AN', '#0E5A3A', 'Sensores') + '</div></div>'
        '<div class="card" style="padding:16px;display:flex;flex-direction:column;gap:10px;background:#F7FBEA;border-color:#E2EDB8;">'
        '<span style="font-size:15px;font-weight:600;">¿Vendes, distribuyes o asesoras?</span>'
        '<span style="font-size:12.5px;color:#4A5650;line-height:1.45;">Crea gratis la ficha de tu empresa o tu perfil de experto y recibe proyectos de tu zona.</span>'
        '<a href="#" class="btn" style="height:44px;font-size:13.5px;">Empezar gratis</a>'
        '<span style="font-size:11.5px;color:#56615B;text-align:center;">Entras con tu cuenta Agrinews: una sola cuenta para las dos.</span></div>'
        '<div style="height:96px;"></div></div>')
B.append(board('MobHomeVisitante.dc.html', 'Móvil · Home sin sesión', 1500, body, 1))

# M3 Menú
def mrow(icn, label, extra='', col=G, bg='#EEF6EE'):
    return ('<a href="#" class="li" style="min-height:50px;"><span class="ico" style="width:32px;height:32px;border-radius:10px;background:' + bg + ';color:' + col + ';">' + ic(icn, 17) + '</span>'
            '<span class="t" style="font-weight:500;">' + label + '</span>' + extra + chev() + '</a>')
def badge(n): return '<span style="min-width:22px;height:20px;padding:0 6px;border-radius:10px;background:#D64545;color:#FFF;font-size:11px;font-weight:600;display:inline-flex;align-items:center;justify-content:center;">%s</span>' % n
def val(t): return '<span class="n">%s</span>' % t
body = ('<div class="top"><span style="flex:1;font-size:22px;font-weight:600;letter-spacing:-.3px;">Menú</span><span class="ib">' + ic('gear', 21) + '</span></div>'
        '<div class="pad" style="display:flex;flex-direction:column;gap:18px;padding-top:4px;">'
        '<div class="card" style="padding:14px;display:flex;flex-direction:column;gap:12px;">'
        '<div style="display:flex;gap:12px;align-items:center;"><span class="av" style="width:48px;height:48px;font-size:16px;">SM</span>'
        '<div style="flex:1;min-width:0;"><span style="font-size:15px;font-weight:600;display:block;">Samuel Martín</span><span style="font-size:12px;color:#56615B;">Granjero · Granja El Pinar</span></div>'
        '<a href="#" style="font-size:12.5px;">Ver perfil</a></div>'
        '<div style="height:1px;background:#EEF1EE;"></div>'
        '<span class="cap" style="margin:0;">Estás en</span>'
        '<div style="display:flex;flex-direction:column;gap:6px;">'
        '<a href="#" style="display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:12px;background:#EEF6EE;color:#17231D;font-size:13.5px;font-weight:600;">' + ic('user', 17, G) + '<span style="flex:1;">Espacio personal</span>' + ic('check', 17, G, 2.4) + '</a>'
        '<a href="#" style="display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:12px;color:#17231D;font-size:13.5px;font-weight:500;">' + ic('building', 17, '#56615B') + '<span style="flex:1;">Granja El Pinar</span><span class="n" style="font-size:11px;">Empresa</span></a>'
        '<a href="#" style="display:flex;align-items:center;gap:10px;padding:9px 10px;border-radius:12px;color:#0E5A3A;font-size:13px;font-weight:500;">' + ic('plus', 17, G, 2.2) + '<span style="flex:1;">Crear ficha de empresa o de experto</span></a>'
        '</div></div>'
        '<div><p class="cap">Tu actividad</p><div class="card" style="overflow:hidden;">'
        + mrow('brief', 'Proyectos', badge(3)) + mrow('grid', 'Tableros', val('4')) + mrow('scale', 'Comparador', val('2 listas'))
        + mrow('msg', 'Mensajes', badge(2)) + mrow('inbox', 'Solicitudes enviadas', val('5')) + '</div></div>'
        '<div><p class="cap">Explorar</p><div class="card" style="overflow:hidden;">'
        + mrow('compass', 'Productos') + mrow('building', 'Empresas') + mrow('user', 'Expertos', '', '#4B3BA6', '#F1EEFB')
        + mrow('tool', 'Servicios') + mrow('book', 'Contenido técnico') + mrow('cal', 'Eventos') + '</div></div>'
        '<div><p class="cap">Cuenta</p><div class="card" style="overflow:hidden;">'
        + mrow('user', 'Mi perfil', val('Cuenta global')) + mrow('sliders', 'Mis intereses', val('9')) + mrow('star', 'Compras y facturación', val('Comprador Gratis'), '#8A5A00', '#FCEFD9') + mrow('globe', 'Región e idioma', val('España · ES'))
        + mrow('bell', 'Notificaciones') + mrow('help', 'Ayuda') +
        '<a href="#" class="li" style="min-height:50px;color:#B42318;"><span class="ico" style="width:32px;height:32px;border-radius:10px;background:#FDECEA;color:#B42318;">' + ic('logout', 17) + '</span><span class="t" style="font-weight:500;">Cerrar sesión</span></a>'
        '</div></div>'
        '<p style="margin:0;font-size:11.5px;color:#56615B;text-align:center;line-height:1.5;">Tu cuenta es la misma que en Agrinews.<br><a href="#">Ir a Agrinews ' + ic('ext', 11, G, 2) + '</a></p>'
        '<div style="height:96px;"></div></div>')
B.append(board('MobMenu.dc.html', 'Móvil · Menú', 1570, body, 5))

# M4 Búsqueda
body = ('<div class="top" style="gap:6px;"><span class="ib" style="margin-left:-8px;">' + ic('back', 22) + '</span>'
        '<div class="srch" style="flex:1;height:44px;border:1.5px solid #0E5A3A;color:#17231D;padding-right:4px;">' + ic('search', 18, '#56615B') + '<span>micotox<span style="display:inline-block;width:1.5px;height:17px;background:#0E5A3A;vertical-align:middle;"></span></span><span class="ib" style="width:32px;height:32px;">' + ic('x', 16, '#8A948F', 2) + '</span></div></div>'
        '<div class="pad" style="display:flex;flex-direction:column;gap:20px;padding-top:6px;">'
        '<div class="row" style="overflow:hidden;margin-right:-16px;"><span class="chip on">Todo</span><span class="chip">Productos</span><span class="chip">Empresas</span><span class="chip">Expertos</span><span class="chip">Contenido</span></div>'
        '<div class="card" style="overflow:hidden;">'
        + ''.join('<a href="#" class="li" style="min-height:50px;"><span class="ico" style="width:32px;height:32px;border-radius:10px;">' + ic(i, 16, G) + '</span><span class="t">%s<small>%s</small></span>' % (t, s) + chev() + '</a>'
                  for i, t, s in [('nutricion', '<b style="font-weight:600;">Micotox</b>inas · adsorbentes', 'Tipo de producto · 86 productos'),
                                  ('salud', 'Control de <b style="font-weight:600;">micotox</b>inas en porcino', 'Búsqueda · 124 resultados'),
                                  ('building', '<b style="font-weight:600;">Micotox</b>Lab Ibérica', 'Empresa · Laboratorio'),
                                  ('user', 'Dra. Ana Ruiz · <b style="font-weight:600;">micotox</b>inas', 'Experta · Nutrición animal')]) +
        '</div>'
        '<div><div class="sec"><h2>Recientes</h2><a href="#">Borrar</a></div><div class="card" style="overflow:hidden;">'
        + ''.join('<a href="#" class="li" style="min-height:46px;color:#17231D;font-weight:400;">' + ic('clock', 17, '#8A948F') + '<span class="t">%s</span>' % t + ic('x', 14, '#8A948F', 2) + '</a>'
                  for t in ['aditivo porcino', 'vacuna PRRS', 'calidad de agua', 'ventilación túnel']) + '</div></div>'
        '<div><div class="sec"><h2 style="display:flex;align-items:center;gap:6px;">' + ic('trend', 17, G, 2) + 'Tendencias del sector</h2><a href="#">Tus intereses</a></div>'
        '<div style="display:flex;flex-wrap:wrap;gap:8px;">' + ''.join('<span class="chip">%s</span>' % t for t in ['Bienestar animal', 'Reducción antibióticos', 'Huevo campero', 'One Health', 'Salud intestinal', 'Inteligencia Artificial']) + '</div></div>'
        '</div>')
B.append(board('MobBuscar.dc.html', 'Móvil · Búsqueda', 844, body, 2))

# M10 Tus intereses
TEND = json.load(open(W + '/tools/intereses.json'))['tendencias']
def chips(lst, on):
    return '<div style="display:flex;flex-wrap:wrap;gap:8px;">' + ''.join('<span class="chip%s">%s%s</span>' % (' on' if x in on else '', ic('check', 13, '#FFF', 2.6) if x in on else '', x) for x in lst) + '</div>'
import sys as _s; _s.path.insert(0, W + '/tools')
from intsel import SUBESP, SUBCAT, OFF as SOFF
def msubs(main, lst, mx=6):
    h = '<div style="display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin-top:8px;padding:8px 10px;border-radius:12px;background:#F3F8F2;"><span style="font-size:11px;font-weight:700;color:#0E5A3A;margin-right:3px;">' + main + ' ›</span>'
    for x in lst[:mx]:
        off = x in SOFF
        h += '<span style="display:inline-flex;align-items:center;gap:4px;height:26px;padding:0 9px;border-radius:999px;font-size:11.5px;font-weight:500;white-space:nowrap;border:1px solid %s;background:%s;color:%s;">%s%s</span>' % (('#D5DED8', '#FFFFFF', '#56615B') if off else ('#C9E3C3', '#DDF0D8', '#0E5A3A')) + ('' if off else ic('check', 10, G, 3.2)) + x + '</span>' if False else ('<span style="display:inline-flex;align-items:center;gap:4px;height:26px;padding:0 9px;border-radius:999px;font-size:11.5px;font-weight:500;white-space:nowrap;border:1px solid %s;background:%s;color:%s;">' % (('#D5DED8', '#FFFFFF', '#56615B') if off else ('#C9E3C3', '#DDF0D8', '#0E5A3A')) + ('' if off else ic('check', 10, G, 3.2)) + x + '</span>')
    if len(lst) > mx:
        h += '<span style="font-size:11.5px;font-weight:600;color:#0E5A3A;padding:0 4px;">+%d incluidos</span>' % (len(lst) - mx)
    return h + '</div>'
def blk(t, s, inner):
    return '<div><p style="margin:0 0 2px;font-size:15px;font-weight:600;">' + t + '</p><p style="margin:0 0 10px;font-size:12px;color:#56615B;">' + s + '</p>' + inner + '</div>'
body = (topback('Tus intereses', '<a href="#" style="font-size:13px;white-space:nowrap;">Saltar</a>') +
        '<div class="pad" style="display:flex;flex-direction:column;gap:22px;padding-top:4px;">'
        '<p class="sub" style="margin:0;">Elige lo que quieras. Lo usamos para recomendarte productos, contenidos y proyectos. Puedes cambiarlo en Menú › Mis intereses.</p>'
        + blk('Especies', 'Se incluyen sus producciones; quita las que no quieras', chips([e[0] for e in ESP], ['Avicultura', 'Porcino']) + msubs('Avicultura', SUBESP['Avicultura']) + msubs('Porcino', SUBESP['Porcino']))
        + blk('Categorías principales', 'Se incluyen todos sus tipos; quita los que no quieras', chips([f[2] for f in FAM], ['Nutrición', 'Avícola']) + msubs('Nutrición', SUBCAT['Nutrición y aditivos']) + msubs('Avícola', SUBCAT['Equipamiento avícola']))
        + blk('Objetivos y tendencias', 'Se actualiza con lo que se mueve en el sector', chips(TEND, ['Bienestar animal', 'Conversión alimenticia', 'Huevo campero', 'Reducción de costes', 'Sostenibilidad'])) +
        '<div style="height:150px;"></div></div>'
        '<div class="sticky"><a href="#" class="btn">Guardar intereses (9)</a></div>')
B.append(board('MobIntereses.dc.html', 'Móvil · Tus intereses', 1700, body, 5))

# M5 Explorar · especies
def esp_row(n, e, c, p, emp):
    return ('<a href="#" class="li" style="min-height:68px;"><span class="emo" style="background:' + c + ';">' + e + '</span>'
            '<span class="t" style="font-size:15px;font-weight:600;">' + n + '<small>%s productos · %s empresas</small></span>' % (format(p, ',').replace(',', '.'), emp) + chev() + '</a>')
def explore_head(sel):
    return ('<div class="top"><span style="flex:1;font-size:22px;font-weight:600;letter-spacing:-.3px;">Explorar</span><span class="ib">' + ic('search', 22) + '</span></div>'
            '<div class="pad" style="display:flex;flex-direction:column;gap:14px;padding-top:4px;">'
            '<div class="seg"><span class="%s">Por especie</span><span class="%s">Por categoría</span></div>' % (('on', '') if sel == 1 else ('', 'on')))
body = (explore_head(1) +
        '<div class="card" style="overflow:hidden;">' + ''.join(esp_row(*x) for x in ESP) + '</div>'
        '<p style="margin:0;font-size:12px;color:#56615B;text-align:center;">¿Falta tu especie? <a href="#">Sugiérela</a></p>'
        '</div>')
B.append(board('MobExplorarEspecies.dc.html', 'Móvil · Explorar por especie', 844, body, 2))

# M6 Especie Avicultura
AV = [('Pollos de engorde', 'Broilers · crecimiento lento', 1460), ('Gallinas ponedoras', 'Producción de huevo', 1180),
      ('Reproductoras', 'Genética e incubación', 520), ('Pavos', '', 340), ('Patos', '', 160), ('Ocas', '', 70),
      ('Perdices', '', 90), ('Aves ornamentales', '', 40)]
body = (topback('', '<span class="ib">' + ic('bookmark', 20) + '</span>') +
        '<div class="pad" style="display:flex;flex-direction:column;gap:14px;">'
        '<div style="display:flex;gap:12px;align-items:center;"><span class="emo" style="width:52px;height:52px;font-size:28px;background:#FFF4DE;">🐔</span>'
        '<div><p class="h1">Avicultura</p><p class="sub" style="margin:0;">4.120 productos · 640 empresas</p></div></div>'
        '<div class="srch" style="height:44px;">' + ic('search', 18, '#56615B') + '<span>Buscar en avicultura…</span></div>'
        '<div><div class="sec" style="margin-bottom:8px;"><h2 style="font-size:14px;">Afina por producción <span style="font-weight:400;color:#56615B;">(opcional)</span></h2></div>'
        '<div class="card" style="overflow:hidden;">'
        '<a href="#" class="li" style="min-height:52px;background:#EEF6EE;"><span class="t" style="font-weight:600;color:#0E5A3A;">Toda la avicultura</span>' + ic('check', 18, G, 2.4) + '</a>'
        + ''.join('<a href="#" class="li" style="min-height:%dpx;"><span class="t" style="font-weight:500;">%s%s</span><span class="n">%s</span>' % (56 if s else 48, n, ('<small>%s</small>' % s) if s else '', format(c, ',').replace(',', '.')) + chev() + '</a>' for n, s, c in AV) +
        '</div></div></div>'
        '<div class="sticky"><a href="#" class="btn">Ver todo avicultura (4.120)</a></div>')
B.append(board('MobEspecie.dc.html', 'Móvil · Especie → producción', 900, body, 2))

# M7 Resultados del recorrido
def rcard(name, by, desc, tint, glyph, tags, kind=''):
    return ('<div class="card" style="padding:12px;display:flex;gap:12px;">'
            '<span style="width:76px;height:76px;border-radius:12px;background:' + tint + ';display:flex;align-items:center;justify-content:center;flex:none;">' + ic(glyph, 30, G, 1.5) + '</span>'
            '<div style="flex:1;min-width:0;display:flex;flex-direction:column;gap:4px;">'
            '<div style="display:flex;gap:6px;align-items:flex-start;"><span style="flex:1;font-size:14px;font-weight:600;line-height:1.25;">' + name + '</span>' + ic('bookmark', 18, '#8A948F') + '</div>'
            '<span style="font-size:12px;color:#4A5650;line-height:1.35;">' + desc + '</span>'
            '<span style="display:flex;gap:4px;flex-wrap:wrap;margin-top:2px;">' + ''.join('<span class="tag">%s</span>' % t for t in tags) + '</span>'
            '<span style="font-size:11.5px;color:#56615B;display:flex;align-items:center;gap:4px;margin-top:2px;">' + by + ic('check', 11, G, 3) + kind + '</span></div></div>')
body = (topback('Pollos de engorde', '<span class="ib">' + ic('search', 21) + '</span>') +
        '<div class="pad" style="display:flex;flex-direction:column;gap:12px;">'
        '<p style="margin:-4px 0 0;font-size:12px;color:#56615B;text-align:center;">Avicultura › Pollos de engorde</p>'
        '<div class="row" style="overflow:hidden;margin-right:-16px;"><span class="chip on">Productos 1.460</span><span class="chip">Empresas 312</span><span class="chip">Expertos 48</span><span class="chip">Contenido</span></div>'
        '<div class="row" style="overflow:hidden;margin-right:-16px;">'
        '<span class="chip soft" style="height:30px;font-size:12px;">Todas las categorías</span>'
        + ''.join('<span class="chip" style="height:30px;font-size:12px;">%s</span>' % s for s in ['Nutrición', 'Salud', 'Equipos', 'Tecnología', 'Genética']) + '</div>'
        '<div style="display:flex;align-items:center;justify-content:space-between;font-size:12.5px;color:#56615B;">'
        '<span style="display:flex;align-items:center;gap:4px;">' + ic('pin', 14, G) + 'Disponible en España</span>'
        '<a href="#" class="chip" style="height:32px;font-size:12px;">' + ic('sliders', 15, INK) + 'Filtros</a></div>'
        + rcard('Ronozyme® ProAct', 'DSM-Firmenich', 'Proteasa que mejora la digestibilidad de la proteína.', '#FFF4DE', 'nutricion', ['Enzimas', 'Broilers'])
        + rcard('Sistema de cooling Evap 150', 'Zucami', 'Refrigeración evaporativa para naves de broilers.', '#E5F1F7', 'equipamiento', ['Cooling', 'Naves'])
        + rcard('Sensor de ambiente NH₃ / CO₂', 'AgroNova', 'Mide gases y temperatura y avisa en el móvil.', '#EEF2E6', 'tecnologia', ['Sensores', 'Ambiente'])
        + rcard('Vacuna Gumboro viva', 'Lab. Ibérico', 'Prevención de la bursitis infecciosa en broilers.', '#FDE9EC', 'salud', ['Vacunas'], ' · Información del distribuidor') +
        '</div>')
B.append(board('MobResultados.dc.html', 'Móvil · Resultados del recorrido', 920, body, 2))

# M8 Explorar · categorías
body = (explore_head(2) +
        '<div class="card" style="overflow:hidden;">'
        + ''.join('<a href="#" class="li" style="min-height:58px;"><span class="ico">' + ic(k, 19, G) + '</span><span class="t" style="font-weight:500;">%s<small>%s productos · %d tipos</small></span>' % (l, format(p, ',').replace(',', '.'), t) + chev() + '</a>' for k, l, _, p, t in FAM) +
        '</div><div style="height:96px;"></div></div>')
B.append(board('MobExplorarCategorias.dc.html', 'Móvil · Explorar por categoría', 940, body, 2))

# M9 Categoría Nutrición
NUT = [('Adsorbentes de micotoxinas', 142), ('Enzimas', 128), ('Aminoácidos', 96), ('Probióticos', 88), ('Prebióticos', 54), ('Acidificantes', 77),
       ('Fitogénicos', 69), ('Vitaminas', 81), ('Minerales y oligoelementos', 73), ('Premezclas', 110), ('Piensos completos', 260)]
body = (topback('', '<span class="ib">' + ic('bookmark', 20) + '</span>') +
        '<div class="pad" style="display:flex;flex-direction:column;gap:14px;">'
        '<div style="display:flex;gap:12px;align-items:center;"><span class="ico" style="width:52px;height:52px;border-radius:16px;">' + ic('nutricion', 26, G) + '</span>'
        '<div style="min-width:0;"><p class="h1" style="font-size:21px;">Nutrición y aditivos</p><p class="sub" style="margin:0;">1.860 productos · 17 tipos</p></div></div>'
        '<div class="srch" style="height:44px;">' + ic('search', 18, '#56615B') + '<span>Buscar en nutrición…</span></div>'
        '<div class="row" style="overflow:hidden;margin-right:-16px;"><span class="chip" style="height:30px;font-size:12px;">Todas las especies</span><span class="chip on" style="height:30px;font-size:12px;">🐔 Avicultura</span><span class="chip on" style="height:30px;font-size:12px;">🐖 Porcino</span><span class="chip" style="height:30px;font-size:12px;">🐄 Bovino</span></div>'
        '<p style="margin:-6px 0 0 2px;font-size:11.5px;color:#56615B;">Filtrado por tus especies. Puedes cambiarlo.</p>'
        '<div class="card" style="overflow:hidden;">'
        + ''.join('<a href="#" class="li" style="min-height:48px;"><span class="t" style="font-weight:500;">%s</span><span class="n">%d</span>' % (n, c) + chev() + '</a>' for n, c in NUT) +
        '<a href="#" class="li" style="min-height:48px;color:#0E5A3A;font-weight:500;justify-content:center;">Ver los 17 tipos</a>'
        '</div></div>'
        '<div class="sticky"><a href="#" class="btn">Ver toda la categoría (1.120)</a></div>')
B.append(board('MobCategoria.dc.html', 'Móvil · Categoría → tipo de producto', 1030, body, 2))

tabbar()

# ---------------- índice ----------------
c = json.load(open(P + 'canvas.json'))
for k in [k for k, b in c['boards'].items() if b.get('page') == 'movil']: del c['boards'][k]
for k in [k for k, b in c['notes'].items() if b.get('page') == 'movil']: del c['notes'][k]
if not any(p['id'] == 'movil' for p in c['pages']):
    i = next(i for i, p in enumerate(c['pages']) if p['id'] == 'figma')
    c['pages'].insert(i, {'id': 'movil', 'name': 'Móvil · Home y menú'})
names = [b[0] for b in B] + ['MobTabBar.dc.html']
c['order'] = [o for o in c['order'] if o not in names] + names
T = {'MobHome.dc.html': 'M1 · Home con sesión', 'MobHomeVisitante.dc.html': 'M2 · Home sin sesión', 'MobMenu.dc.html': 'M3 · Menú (pestaña 5)',
     'MobBuscar.dc.html': 'M4 · Búsqueda', 'MobIntereses.dc.html': 'M10 · Tus intereses (alta y Menú › Mis intereses)', 'MobExplorarEspecies.dc.html': 'M5 · Explorar · por especie', 'MobEspecie.dc.html': 'M6 · Especie → producción (opcional)',
     'MobResultados.dc.html': 'M7 · Resultados · categoría en chips', 'MobExplorarCategorias.dc.html': 'M8 · Explorar · por categoría',
     'MobCategoria.dc.html': 'M9 · Categoría → tipo de producto'}
rows = [['MobHome.dc.html', 'MobHomeVisitante.dc.html', 'MobMenu.dc.html', 'MobBuscar.dc.html', 'MobIntereses.dc.html'],
        ['MobExplorarEspecies.dc.html', 'MobEspecie.dc.html', 'MobResultados.dc.html', 'MobExplorarCategorias.dc.html', 'MobCategoria.dc.html']]
H = {b[0]: b[2] for b in B}
heads = ['Home y menú · una sola barra inferior: Inicio · Explorar · Proyectos · Tableros · Menú',
         'Explorar · especie → producción (opcional) → resultados, o categoría → tipo']
y = 0
for r, row in enumerate(rows):
    c['notes']['movT%d' % r] = {'kind': 'title1', 'maxW': 2600, 'page': 'movil', 'text': heads[r], 'w': 240, 'x': 0, 'y': y - 300}
    x = 0
    for fn in row:
        c['boards'][fn] = {'h': H[fn], 'page': 'movil', 'title': T[fn], 'w': 390, 'x': x, 'y': y}
        x += 390 + 140
    y += max(H[fn] for fn in row) + 500
c['notes']['movT2'] = {'kind': 'title1', 'maxW': 2600, 'page': 'movil', 'text': 'Componente · barra inferior (prop activo 1–5)', 'w': 240, 'x': 0, 'y': y - 300}
c['boards']['MobTabBar.dc.html'] = {'h': 84, 'page': 'movil', 'title': 'MobTabBar · componente', 'w': 390, 'x': 0, 'y': y}
json.dump(c, open(P + 'canvas.json', 'w'), ensure_ascii=False, indent=1)
print('ok', names)
