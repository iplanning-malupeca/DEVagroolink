"""Subniveles por defecto en el selector de intereses: principal elegido en verde oscuro,
sus subcategorías incluidas en verde claro (se pueden quitar)."""
import json, os, sys
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, W + '/tools')
from especies import TREE
FAM = json.load(open('/Volumes/DEV/GIT/DEVagroolink/docs/modelo-producto/familias.json'))['familias']
CAT = ['Nutrición y aditivos', 'Materias primas', 'Salud y bioseguridad', 'Genética y reproducción', 'Equipamiento e instalaciones',
       'Equipamiento avícola', 'Equipamiento porcino', 'Equipamiento rumiantes', 'Sostenibilidad y energía', 'Tecnología y software']
SUBESP = {e: [c for c, _ in cats] for e, cats in TREE}
SUBCAT = {CAT[i]: [t if isinstance(t, str) else t.get('label') for t in f['tipos']] for i, f in enumerate(FAM)}
OFF = {'Aves ornamentales', 'Equipos de procesamiento avícola'}
SEL_ESP = ['Avicultura', 'Porcino']
SEL_CAT = ['Nutrición y aditivos', 'Equipamiento avícola']
MAXSUB = 8
CSS = ('.sbx{display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin-top:7px;padding:7px 9px;border-radius:10px;background:#F3F8F2}'
       '.sbl{font-size:11px;font-weight:700;color:#0E5A3A;margin-right:3px;white-space:nowrap}'
       '.sc{display:inline-flex;align-items:center;gap:4px;height:24px;padding:0 9px;border-radius:999px;font-size:11.5px;font-weight:500;white-space:nowrap;border:1px solid #C9E3C3;background:#DDF0D8;color:#0E5A3A;box-sizing:border-box}'
       '.sc.off{background:#FFFFFF;border-color:#D5DED8;color:#56615B}'
       '.sc.more{background:none;border:0;color:#0E5A3A;font-weight:600}')
CK = '<svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5 9-10"/></svg>'

def subs(main, lst):
    shown = lst[:MAXSUB]
    h = '<div class="sbx" role="group" aria-label="Incluido en %s"><span class="sbl">%s ›</span>' % (main, main)
    for s in shown:
        off = s in OFF
        h += '<span class="sc%s" aria-pressed="%s">%s%s</span>' % (' off' if off else '', 'false' if off else 'true', '' if off else CK, s)
    if len(lst) > MAXSUB:
        h += '<span class="sc more">+%d incluidos</span>' % (len(lst) - MAXSUB)
    return h + '</div>'

def bloque_esp():
    return ''.join(subs(e, SUBESP[e]) for e in SEL_ESP)

def bloque_cat():
    return ''.join(subs(c, SUBCAT[c]) for c in SEL_CAT)

def aplicar(path, mobile=False):
    s = open(path).read()
    if '.sbx{' not in s:
        s = s.replace('</style>', CSS + '\n</style>', 1)
    for leg, blk in [('>Especies <span>', bloque_esp()), ('>Categorías principales <span>', bloque_cat())]:
        i = s.index(leg)
        j = s.index('<div class="wr">', i); k = s.index('</div>', j) + len('</div>')
        if s[k:k + 17] == '<div class="sbx" ':
            k = s.index('</fieldset>', k) if '</fieldset>' in s[k:k + 4000] else k
        s = s[:k] + blk + s[k:] if 'class="sbx"' not in s[k:k + 30] else s
    s = s.replace('Incluye todas sus producciones</span>', 'Al elegirla se incluyen sus producciones; quita las que no quieras</span>')
    s = s.replace('Qué tipo de soluciones buscas</span>', 'Se incluyen todos sus tipos; quita los que no quieras</span>')
    open(path, 'w').write(s)

if __name__ == '__main__':
    for f in ['LoginIntereses', 'AltaMiEspacioIntereses']:
        aplicar(W + '/project/%s.dc.html' % f)
    print(SUBCAT['Nutrición y aditivos'][:3], SUBESP['Avicultura'][:2])
