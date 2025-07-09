# traductor_sdh

Librería para la detección automática de determinantes sociales de la salud (SDH) en textos médicos.

## Instalación

Descarga el `.whl` desde la sección *Releases* o clona el repositorio y construye con:

```bash
pip install .

### Ejemplo de uso

from traductor_sdh import TraductorSDH

traductor = TraductorSDH('SDOH_Zcodes_traducciones.xlsx')
textos, archivos = traductor.cargar_corpus_desde_carpeta('corpus')
resultados = traductor.analizar_corpus(textos, archivos, umbral=0.5)
traductor.exportar_csv(resultados)
