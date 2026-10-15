"""Ejecuta las celdas del único notebook y guarda sus figuras y un registro textual.

Uso desde la raíz: python src/ejecutar_eda.py
Las transformaciones permanecen en notebooks/01_limpieza_datos.ipynb.
"""
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path
import json
import traceback
import matplotlib

matplotlib.use('Agg')

def display(*objects, **kwargs):
    for obj in objects:
        print(obj.to_string() if hasattr(obj, 'to_string') else obj)

def main():
    root = Path(__file__).resolve().parents[1]
    path = root / 'notebooks' / '01_limpieza_datos.ipynb'
    notebook = json.loads(path.read_text(encoding='utf-8'))
    log_path = root / 'reports' / 'ejecucion_eda.txt'
    log_path.parent.mkdir(parents=True, exist_ok=True)
    namespace = {'__name__': '__main__', 'display': display}
    try:
        with log_path.open('w', encoding='utf-8') as log:
            for index, cell in enumerate(notebook['cells']):
                if cell['cell_type'] != 'code':
                    continue
                print(f'Ejecutando celda {index + 1}... ', flush=True)
                source = ''.join(cell['source'])
                with redirect_stdout(log), redirect_stderr(log):
                    print(f'\n--- Celda {index + 1} ---')
                    exec(compile(source, f'{path.name}:celda-{index + 1}', 'exec'), namespace)
    except Exception:
        with log_path.open('a', encoding='utf-8') as log:
            traceback.print_exc(file=log)
        raise
    print('EDA completado. CSV en data/, figuras en images/eda/.')
    print(f'Registro: {log_path}')

if __name__ == '__main__':
    main()
