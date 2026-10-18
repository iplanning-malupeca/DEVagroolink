"""Construye el prototipo navegable de la búsqueda con el modelo (categorías, especies, enfermedades, plantillas, pertinencia)."""
import json, os, shutil
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m = json.load(open(W + '/data/producto.json'))
sub = {k: m[k] for k in ('categorias', 'especies', 'enfermedades', 'plantillas', 'pertinencia', 'transversales', 'paises')}
src = open(W + '/tools/buscar.src.html').read()
logo = open('/Volumes/DEV/GIT/DEVagroolink/design/assets/agroolink-logo.svg').read().strip().replace('<svg ', '<svg role="img" aria-label="Agroolink" ', 1)
src = src.replace('/*LOGO*/', logo)
out = src.replace('/*MODELO*/', json.dumps(sub, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
os.makedirs(W + '/out', exist_ok=True); open(W + '/out/buscar.html', 'w').write(out)
R = '/Volumes/DEV/GIT/DEVagroolink/design/prototipos/'
if os.path.isdir(R): open(R + 'buscar.html', 'w').write(out); shutil.copy(W + '/tools/buscar.src.html', R + 'buscar.src.html')
print('ok', len(out))
