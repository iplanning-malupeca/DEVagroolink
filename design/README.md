# Agroolink · Diseño (canvas)

Copia en git del canvas de diseño de Agroolink:
https://claude.ai/artifact/6Q2317uagG93v21oXLyi7t

## Contenido

- `canvas/canvas.json` — índice del canvas: páginas, posición y título de cada pantalla.
- `canvas/*.dc.html` — una pantalla (artboard) por archivo, en el formato del editor de diseño.
- `assets/` — logo de Agroolink en versión color y blanca.

## Páginas del canvas

| Página | Prefijo de archivos |
|---|---|
| Componentes · especies, mercados, ramas y cargos | `SelEspecies`, `SelMercados`, `SelRamasCargos` |
| Proyectos (módulo central) | `Proy*` |
| Header | `Main`, `Personal`, `Experto`, `ConEmpresa`, `Empresa`, `AvatarMenu` |
| Alta (login Agrinews) | `Login*`, `Alta4MiEspacio`, `AltaEmpresa`, `AltaExperto`, `AltaConsulta` |
| Alta empresa | `EmpE*` |
| Alta solo para mí | `MiM*` |
| Alta experto | `ExpX*` |
| Intranet | `Int*` |
| Planes | `Precios*`, `Checkout` |
| Alta empresa · configuraciones | `Cfg*`, `WizTop` |
| Alta · Fabricante con distribuidores | `Fab*` |
| Alta · Fabricante con comerciales | `ComTipo`, `ComEquipo`, `ComZonas`, `ComContacto`, `ComPublicar`, `ComBandeja` |
| Alta · Fabricante con sucursales | `Suc*` |
| Alta · Distribuidor multimarca | `Dis*` |
| Productos (módulo) | `Prod*` |
| Servicios (módulo) | `ServLista`, `ServEditor` |
| Tableros y comparador | `Tab*`, `Comp*` |

## Flujo de trabajo

El canvas no se sincroniza solo con git:

1. **Canvas → git:** se descargan las pantallas del canvas a `canvas/` y se hace commit.
2. **git → canvas:** se publican en el canvas los archivos cambiados de `canvas/`.

Estos archivos son prototipos de diseño, no código de producción.
