# StreamView Analytics

Proyecto académico de **Visualización de Datos, Duoc UC, sede Plaza Norte**.
Equipo: **Abraham Abanto, Bastián Soto y Andrés Silva**. Docente: Alicia Ramos de Peraza.

## Problema y objetivo

Identificar las características de los títulos mejor evaluados y populares para ayudar a la
**Gerencia de Adquisición y Gestión de Contenidos** a priorizar su revisión. El dashboard
ofrece también una página ejecutiva para el **Directorio**.
El trabajo continúa la primera entrega, centrada en películas, e integra películas y series
con estrenos entre **2010 y 2025**. El foco es el problema 6, apoyado por el análisis de
popularidad por género del problema 2.

## Productos finales

- [Dashboard exportado: dos páginas](dashboard/dashboard_ep2.pdf).
- [Acceso al dashboard interactivo](dashboard/enlace_dashboard.md): https://datastudio.google.com/reporting/5b6f98f7-9a1c-49e3-aab5-77f96458c8d4
- [Único notebook: limpieza, EDA y exportación](notebooks/01_limpieza_datos.ipynb).

## Estructura del repositorio

```text
streamview-analytics/
├── README.md
├── requirements.txt
├── requirements-notebook.txt
├── .gitignore
├── .gitattributes
├── data/
│   ├── README.md
│   ├── raw/
│   │   ├── netflix_movies_detailed_up_to_2025.csv
│   │   └── netflix_tv_shows_detailed_up_to_2025.csv
│   ├── content_clean.csv
│   ├── content_financials.csv
│   └── origenes.json
├── notebooks/
│   └── 01_limpieza_datos.ipynb
├── src/
│   └── ejecutar_eda.py
├── dashboard/
│   ├── dashboard_ep2.pdf
│   ├── configuracion_looker.md
│   └── enlace_dashboard.md
├── images/
│   ├── README.md
│   ├── eda/                  # 13 figuras PNG
│   └── dashboard/            # Las dos páginas en PNG
```

## Requisitos

Python **3.11 o 3.12**. Dependencias del análisis en `requirements.txt`.
JupyterLab es opcional y figura en `requirements-notebook.txt`.
Los CSV finales y documentos ya están incluidos: su consulta no requiere ejecutar Python.

### Windows, PowerShell

Abrir una terminal dentro de `streamview-analytics`:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/ejecutar_eda.py
```

Si se usa Python 3.11, cambiar únicamente `py -3.12` por `py -3.11`.
No es necesario activar el entorno virtual para estos comandos.

### macOS o Linux

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python src/ejecutar_eda.py
```

### Ejecución interactiva en un solo notebook

En Windows:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements-notebook.txt
.\.venv\Scripts\python.exe -m jupyterlab
```

En macOS/Linux usar `.venv/bin/python` en esos mismos comandos.
Abrir `notebooks/01_limpieza_datos.ipynb` y seleccionar **Ejecutar todo**.
Las rutas detectan la raíz del proyecto, incluso si el kernel se inicia desde `notebooks/`.

### Google Colab

Abrir `notebooks/01_limpieza_datos.ipynb` en Colab. Si solo se abre ese archivo, ejecutar
todo y subir los dos CSV de `data/raw/` cuando se soliciten. Si el repositorio completo
está disponible en el entorno, situarse en su raíz antes de ejecutar. No se requieren
claves API, Google Drive ni rutas personales para reproducir el análisis.

### Resultados de la ejecución

1. Lectura de los originales, diagnóstico e integración.
2. Limpieza y generación de variables analíticas.
3. EDA, gráficos y conclusiones, dentro del único notebook.
4. Validaciones de integridad, escalas, clasificaciones y finanzas.
5. Exportación final de `data/content_clean.csv` y `data/content_financials.csv`.

Las 13 figuras se guardan en `images/eda/`. La ejecución por consola también produce
`reports/ejecucion_eda.txt`, que `.gitignore` excluye por ser un registro regenerable.
`src/ejecutar_eda.py` lee las celdas del notebook: no mantiene una segunda implementación del EDA.

## Valores de control, sin filtros

| Indicador | Resultado de referencia |
| --- | ---: |
| Títulos | 31.991 |
| Películas / series | 16.000 / 15.991 |
| Títulos evaluables: mínimo 50 votos | 15.397 (48,1%) |
| Valoración promedio entre evaluables | 6,63 / 10 |
| Títulos con nota ≥7 entre evaluables | 38,1% |
| Popularidad promedio / mediana, todos los títulos | 42,63 / 22,07 |
| Títulos de alto potencial | 4.662 |
| Alto potencial entre evaluables | 30,3% |
| Países con producciones de un solo país | 100 |
| Películas con presupuesto e ingresos positivos | 3.540 |
| Ingresos/presupuesto individual mediano | 1,70 veces |

**Alto potencial:** al menos 50 votos y valoración y popularidad iguales o superiores
a las medianas de su propio tipo. Los umbrales permanecen fijos al aplicar filtros.
Películas: nota 6,400 y popularidad 11,4400. Series: nota 7,599 y popularidad 47,6225.
Esta clasificación prioriza candidatos para revisar y no predice su éxito comercial.

## Dashboard en Looker Studio

- **Página 1, Directorio:** composición del catálogo, países, idiomas y valoración por año.
- **Página 2, Gerencia:** alto potencial, tabla de títulos y popularidad mediana por año.
- Fuentes: `data/content_clean.csv` y `data/content_financials.csv`.
- Filtros: tipo, género, país, idioma y año de estreno. Navegación entre páginas.
- Fórmulas, tipos y alcance: [configuracion_looker.md](dashboard/configuracion_looker.md).

Al cargar una actualización completa, evitar agregarla sobre la anterior si eso duplica las filas.
Probar los filtros entre fuentes: al seleccionar Serie, el indicador financiero debe quedar sin datos.
El PDF no sustituye la publicación interactiva. El enlace del reporte no estaba presente en los
archivos recibidos y debe incorporarse en `dashboard/enlace_dashboard.md` antes de entregar.

## Fuentes y límites de interpretación

Los dos originales son **Netflix Movies Detailed up to 2025** y **Netflix TV Shows Detailed up to 2025**,
proporcionados para el caso académico. El registro de fuentes y sus huellas SHA-256 está en
[data/origenes.json](data/origenes.json). El [diccionario](data/diccionario_datos.csv) describe los campos.

- El extracto tiene selección fija de registros por año y tipo. No representa todo el catálogo real.
- Popularidad es un índice externo, no reproducciones, usuarios, demanda ni retención de StreamView.
- El mínimo de 50 votos es una regla operativa, no una garantía estadística.
- Los gráficos por año comparan grupos según su estreno, no la evolución histórica de los mismos títulos.
- Ingresos/presupuesto corresponde a producciones cinematográficas, no a rentabilidad de la plataforma.
- La fuente no acredita costos de licencias ni permite recomendar compras automáticamente.


