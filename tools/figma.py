import json,os
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ids="""69f6843989ce349fa90ff356df5b8d2d debad870080fb9cf0f0fca63b473bf11 e5e9b2ec169d3aafef52b1a8ffc9ad02 8f5ce825e8bfe80bdddc7237d1de6791 1645c70ccb00fad2b5bfd5179f38d70a 532a978da67c8871e354f02c2a5d019c 9267e5b2a8cafd5dacd955621c107e08 964c4ca4f75abe879f4e7b6598ee8ff2 84a48475c14ce9c82eeb2587fd7dabd4 1de6c74d8b96d5d4a9106be987a4d047 e046110eb332768284917fdc1f96968f 02b7b15f8150a7e961dcacdce4d935f5 d2728fba98006f990919abea0487ef55 d2f197aba57e0b801a2e21628d1af195 1e5267f40856c193e9d6f00c126c879b 34b9d471aaef60d49122afb8a1d5324c 5678b56eefc4d927a44a6ea7354acc82 bedb629985fe5e6fac162201689c6339 39c596432f354edcb0cdcc761ffa6620 eb5fc22227b9520e588260728c340368 c18d7986068d8e32c4d5c9c9f77b84b0 002290f906a9e0c5e5f1f64cb65e431c 29ddf6f7adc6b11571cb8f8b0a462a71 d5f3f1e4d441a6f4995da1da36497f0e 94c4214881ff19362e6b5614bf2429f3 5da7eb6404cb912335f19c4d8861595d eb9616e167211cdb9fad9e280ecf2ad1 94416b603d8b8f11e0d4b45814b20b59 b6154a2b0100954b24f957f8001e7b4b 8235eb93d4b67b5810402fccb6083c56 6b1cbac4564ee8650259e308c5080c4e 725385ff68312ea736eba746836d1e8e 8d6f10f58af1b0875af363552bdf6490 66e63d75de72ac911034879bb110e184 a1925a95261ab3c182d139471d5c36ad d45b6ebcb31797e6943954ceded0cdf3 373932a6d942d72e261b833d54b72bcd 5f92f4956f13f8c68e274d6fe8ac7528 8dfcda7d9094b8957a981886f9bb4360 aa115c6ed244d59b2b5080d1893940fd 682a4e00096109e296e1892ccfb33d14 892743ed8368ffbaf4ffc04992f44507 1b2f83064a511cbf7f4cc07f9ac0d2ea af665256a2dbc5e69357b6af1af34fd0 a5f86da2a94e1227c45ef79e57576843 800e56376c1b1dd1525df6a31f1b16b1 5071fca492f8ecea984c6254edc90b6f 8f78ad9729250bf3311ff10e65294421 6657dd1ec4148e00defb3a90a1dc9029 9d27871979eafb8804c3b3c7c1cbcc50 cb9a22065f0c02de3d509f3424c94040 86a8db84a7221c712414e81c4978ba2b 00ece495f7ff694c8d14e7f588b2261c f018735b41d4b2eac1a96514b6992cd6 70c76b3cf2703bf2edbbf80ae7228c28 c38f6e912ab4d16a22b1ef283b809c14 69b7370da5a60b75665a377a03966f70 81f97f02373b1ff0f52137398d7006fc 6a9979949efc6e1ecb88242a3f5f208e e1c1df3f3ea14e87f29224f56d9680f9 2aa03fad0c9896d19ee71ec6184b9c17 54e4839091bd6992c49cd1ea17b25cad 54449d9b0ec760824da475a1fc692fc0 31d6b65aa8fddeec6967f78406cd8d4a 9159b9f3303e9c8c27715ba95268674a 5dcff1a0fe2b7e4d08f2b3f2dc96a043 d8a10bf51139ca417c10c16ec656473e af059ee6d8d71e2082435e5f28925827""".split()
dims={int(k):v for k,v in json.load(open(W+'/figma-full/dims.json')).items()}
F='(nombre antiguo: Farm4You)'
T={1:'Header · usuario logueado',2:'Header · con selector de región',3:'Home logueado «Hola Samuel»',4:'Mega-menú de categorías',5:'Home logueado · variante',
6:'Categoría · Aves › Broilers › Nutrición',7:'Categoría · variante',8:'Resultados «micotoxinas porcino»',9:'Resultados · variante',10:'Página de especie · Aves',
11:'Producto OptiFeed · modal',12:'Contactar con la empresa',19:'Ficha de producto OptiFeed',20:'Pantalla '+F,21:'Pantalla '+F,22:'Pantalla '+F,23:'Pantalla '+F,24:'Pantalla '+F,
28:'Producto Zucami Aviary Pro',29:'Guardar en tablero',30:'Pantalla '+F,31:'Pantalla '+F,32:'Pantalla '+F,36:'Producto en catálogo de AgroNova',45:'Producto en catálogo de AgroNova · variante',
47:'Modal · guardar en tablero',48:'Modal · guardado en tablero',51:'Modal · descargar vademécum',52:'Modal · visitar la web',56:'Modal · únete como distribuidor',57:'Modal · solicitar información',60:'Producto OptiFeed · modal',62:'Producto OptiFeed · modal',
13:'Directorio de expertos',14:'Perfil · Dr. Carlos Martínez',15:'Perfil experto · variante',16:'Perfil experto · variante',
17:'Modal · menú de categorías',18:'Modal · menú de categorías (variante)',25:'Login',26:'Login · código',27:'Login · paso',33:'Login · paso',34:'Cuenta creada',35:'Login · paso',
37:'Listado de empresas / expertos / eventos',38:'Listado · variante',39:'Evento · AviForum',
40:'Ficha empresa AgroNova',41:'AgroNova · sección',42:'AgroNova · sección',43:'AgroNova · sección',44:'AgroNova · sección',
46:'Ficha empresa DSM',49:'DSM · sección',50:'DSM · sección',53:'DSM · sección',54:'DSM · sección',55:'DSM · sección',
58:'Ficha empresa Zucami',59:'Zucami · sección',61:'Encontrar mi comercial',63:'Contactar con Laura García',64:'Zucami · catálogo',65:'Zucami · catálogo',66:'Zucami · catálogo',67:'Zucami · catálogo',68:'Zucami LATAM'}
G=[('Header y home',[1,2,3,4,5]),('Listados, búsqueda y especie',[6,7,8,9,10]),
('Producto y modales',[19,11,12,47,48,51,52,56,57,60,62,28,29,36,45]),('Pantallas con el nombre antiguo (Farm4You)',[20,21,22,23,24,30,31,32]),
('Expertos',[13,14,15,16]),('Login y menús',[25,26,27,33,34,35,17,18]),('Listados y eventos',[37,38,39]),
('Empresa · AgroNova',[40,41,42,43,44]),('Empresa · DSM',[46,49,50,53,54,55]),('Empresa · Zucami',[58,59,64,65,66,67,68,61,63])]
assert sorted(n for _,l in G for n in l)==list(range(1,69))
c=json.load(open(W+'/project/canvas.json'))
for k in [k for k,b in c['boards'].items() if b.get('page')=='figma']: del c['boards'][k]
for k in [k for k,b in c['notes'].items() if b.get('page')=='figma']: del c['notes'][k]
c['pages']=[p for p in c['pages'] if p['id']!='figma']+[{'id':'figma','name':'Front · Figma (referencia escritorio)'}]
c['order']=[o for o in c['order'] if not o.startswith('Fig')]
y=0
for gi,(name,lst) in enumerate(G):
    c['notes']['figT%d'%gi]={'kind':'title1','maxW':6000,'page':'figma','text':name,'w':240,'x':0,'y':y-300}
    x=0;rowh=0
    for n in lst:
        w,h=dims[n];w=round(w);h=round(h);fn='Fig%02d.dc.html'%n
        open(W+'/project/'+fn,'w').write(f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Figma {n:02d} · {T[n]}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>body{{margin:0;background:#FFFFFF}}img{{display:block}}</style>
</helmet>
<img src="/_blob/{ids[n-1]}" width="{w}" height="{h}" alt="Figma página {n} · {T[n]}">
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
''')
        c['boards'][fn]={'h':h,'page':'figma','title':'F%02d · %s'%(n,T[n]),'w':w,'x':x,'y':y}
        c['order'].append(fn);x+=w+120;rowh=max(rowh,h)
    y+=rowh+500
json.dump(c,open(W+'/project/canvas.json','w'),ensure_ascii=False,indent=1)
print('ok',y)
