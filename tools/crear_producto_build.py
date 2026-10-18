"""Construye el prototipo navegable del alta de producto con el modelo dentro (un solo archivo)."""
import json, os, shutil
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m = json.load(open(W + '/data/producto.json'))
src = open(W + '/tools/crear-producto.src.html').read()
logo = open('/Volumes/DEV/GIT/DEVagroolink/design/assets/agroolink-logo.svg').read().strip().replace('<svg ', '<svg role="img" aria-label="Agroolink" ', 1)
src = src.replace('/*LOGO*/', logo)
out = src.replace('/*MODELO*/', json.dumps(m, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
os.makedirs(W + '/out', exist_ok=True)
open(W + '/out/crear-producto.html', 'w').write(out)
R = '/Volumes/DEV/GIT/DEVagroolink/design/prototipos/'
open(R + 'crear-producto.html', 'w').write(out); shutil.copy(W + '/tools/crear-producto.src.html', R + 'crear-producto.src.html')
print('ok', len(out))
