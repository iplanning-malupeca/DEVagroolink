"""Ordena el alta de empresa (18/10/2026): quita las páginas antiguas «Alta empresa» (E1–E7) y
«Alta empresa · configuraciones» (F1–F9), superadas por 006–010, 011a–e y 012; mueve el tipo de
empresa del consultor a 012 y unifica nombres y códigos."""
import json, os
W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = W + '/project/canvas.json'
c = json.load(open(P))
B = c['boards']
quitar = [k for k, b in B.items() if b.get('page') in ('altaempresa', 'configempresa') and k != 'EmpConsultor.dc.html']
for k in quitar:
    del B[k]
c['order'] = [k for k in c['order'] if k not in quitar]
c['notes'] = {k: n for k, n in c['notes'].items() if n.get('page') not in ('altaempresa', 'configempresa')}
c['pages'] = [p for p in c['pages'] if p['id'] not in ('altaempresa', 'configempresa')]
# consultor → 012, escenario E
B['EmpConsultor.dc.html'].update(page='altaserv', x=0, y=5360, title='SE0 · Tipo de empresa solo de servicios (Asvet Veterinaris): atiende con su equipo de expertos')
B['SrvAsvLista.dc.html']['x'] = 1360; B['SrvAsvEditor.dc.html']['x'] = 2720
# nombres de página
nombres = {'fabdist': '006_Alta empresa · Fabricante con distribuidores (DSM-Firmenich)',
           'comerciales': '007_Alta empresa · Fabricante con comerciales (Zucami)',
           'sucursales': '008_Alta empresa · Fabricante con sucursales (Big Dutchman)',
           'sucursal': '009_Alta empresa · Sucursal de un grupo (Aviagen Ibérica)',
           'distmulti': '010_Alta empresa · Distribuidor multimarca (NewFarms)'}
for p in c['pages']:
    if p['id'] in nombres: p['name'] = nombres[p['id']]
# códigos: especies 1b-1 / 1b-2 / 1b-3 en las cuatro páginas
def titulo(k, viejo, nuevo):
    t = B[k]['title']; assert t.startswith(viejo), (k, t); B[k]['title'] = nuevo + t[len(viejo):]
for k, l in [('FabTipoEspecies', 'D'), ('ComTipoEspecies', 'K'), ('SucTipoEspecies', 'S'), ('DisTipoEspecies', 'X')]:
    titulo(k + '.dc.html', l + '1b ·', l + '1b-2 ·')
# 010: avisos al unirse como X0c / X0d (antes chocaban con X1b)
titulo('DisAvisoEmpresa.dc.html', 'X1b ·', 'X0c ·'); titulo('DisAvisoAdmin.dc.html', 'X1c ·', 'X0d ·')
c['notes']['disT1']['text'] = c['notes']['disT1']['text'].replace('X1b/X1c avisos', 'X0c/X0d avisos')
# 009: U en vez de S3 (chocaba con S3 · Países de 008)
for k, v, n in [('SucAltaCRM', 'S3a', 'U0a'), ('SucAltaVerifica', 'S3b', 'U0b'), ('SucAltaSede', 'S3c', 'U0c'), ('SucEsSucursal', 'S3', 'U1')]:
    titulo(k + '.dc.html', v + ' ·', n + ' ·')
c['notes']['sucT3']['text'] = '3 · Alta de una sucursal — Aviagen Ibérica SL (sucursal de Aviagen): U0a empresa del CRM · U0b verificar email · U0c aviso a la Sede y al superadmin · U1 tipo de empresa'
# 007: K2 seguido de K2b, K2c, K2d y después K3
for k, x in [('ComEquipoCrear', 5440), ('ComEmailSolicitud', 6800), ('ComAltaComercial', 8160), ('ComZonas', 9520)]:
    B[k + '.dc.html']['x'] = x
# 001: a dónde lleva «Represento una empresa»
c['notes']['altaTitulo2']['text'] = '7 · Solo para mí → Mi espacio. «Represento una empresa» sigue en 006–010 (según cómo vende la empresa); experto y «más tarde», en sus páginas'
json.dump(c, open(P, 'w'), ensure_ascii=False, indent=1)
print(len(quitar), 'quitados:', ' '.join(sorted(quitar)))
