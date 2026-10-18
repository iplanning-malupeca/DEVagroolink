"""Construye el prototipo navegable del alta de servicios del experto (un solo archivo con el modelo y el logo)."""
import json, os, shutil
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
R = '/Volumes/DEV/GIT/DEVagroolink/'
m = json.load(open(W + '/data/producto.json'))
sub = {k: m[k] for k in ('categorias', 'especies', 'plantillas', 'paises', 'regiones')}
sub['ramas'] = json.load(open(R + 'docs/modelo-producto/ramas_y_cargos.json'))
logo = open(R + 'design/assets/agroolink-logo.svg').read().strip().replace('<svg ', '<svg role="img" aria-label="Agroolink" ', 1)
src = open(W + '/tools/crear-servicio.src.html').read().replace('/*LOGO*/', logo)
out = src.replace('/*MODELO*/', json.dumps(sub, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/'))
open(W + '/out/crear-servicio.html', 'w').write(out)
open(R + 'design/prototipos/crear-servicio.html', 'w').write(out); shutil.copy(W + '/tools/crear-servicio.src.html', R + 'design/prototipos/crear-servicio.src.html')
print('ok', len(out))
