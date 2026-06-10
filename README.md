# Quantum Machine Learning with Python - Companion Repository

Repositorio abierto de acompanamiento para estudiar, reproducir y extender ejercicios inspirados en el libro _Quantum Machine Learning with Python_ de Santanu Pattanayak.

Este proyecto no es oficial ni sustituye al libro. La intencion es construir, paso a paso, implementaciones propias, notas tecnicas, experimentos reproducibles y pequenas variaciones pedagogicas que ayuden a entender los conceptos de computacion cuantica y aprendizaje automatico cuantico.

## Objetivos

- Acompanar la lectura del libro con codigo Python claro, verificable y comentado cuando sea necesario.
- Separar notas, notebooks, scripts reutilizables y experimentos para que el repositorio crezca de forma ordenada.
- Documentar decisiones tecnicas, diferencias entre versiones de librerias y posibles adaptaciones modernas.
- Facilitar el trabajo colaborativo con IA, manteniendo trazabilidad sobre que se implementa y por que.
- Reproducir y adaptar el codigo del libro como base de estudio, indicando la referencia del capitulo o seccion cuando corresponda.
- Evitar copiar texto explicativo extenso, figuras o material editorial del libro; las notas y explicaciones del repositorio deben escribirse con palabras propias.

## Estado

Infraestructura inicial lista. Entorno Anaconda definido (`environment.yml`), estructura de carpetas creada y convenciones de trabajo documentadas. Pendiente: publicar en GitHub y comenzar la lectura del capitulo 1.

**Entorno:** Python 3.11 · Cirq >=1.3 · Qiskit >=1.0 / qiskit-aer >=0.14 · JupyterLab >=4

Ver progreso por capitulos en `ROADMAP.md`.

## Instalacion Local con Anaconda

Requisitos sugeridos:

- Anaconda o Miniconda.
- Git.

El entorno principal del proyecto se llama `qml-santanu`. Desde Anaconda Prompt:

```bat
cd /d D:\QUANTUM_COMPUTING\QML_santanu
conda env create -f environment.yml
conda activate qml-santanu
python -m pip install -e .
```

Registrar el kernel para Jupyter:

```bat
python -m ipykernel install --user --name qml-santanu --display-name "Python (qml-santanu)"
```

Ejecutar checks siempre con el entorno activo:

```bat
conda activate qml-santanu
python -m ruff check .
python -m pytest
```

Ver mas detalles en `docs/environment.md`.

## Crear el Repositorio en GitHub

Este proyecto ya esta inicializado como repositorio git local. Para publicarlo:

```bash
git add .
git commit -m "chore: initialize companion repository"
gh repo create qml-santanu-companion --public --source . --remote origin --push
```

Si no usas GitHub CLI, crea un repositorio vacio en GitHub y luego ejecuta:

```bash
git remote add origin https://github.com/<usuario>/qml-santanu-companion.git
git push -u origin main
```

## Estructura Propuesta

```text
.
|-- .github/              # CI, plantillas de issues y pull requests
|-- docs/                 # Guias, notas de lectura y decisiones tecnicas
|-- notebooks/
|   |-- cirq/             # Notebooks con ejemplos basados en Cirq
|   |-- qiskit/           # Notebooks con ejemplos basados en Qiskit
|-- src/
|   |-- qml_santanu/
|       |-- cirq/         # Codigo reutilizable para ejemplos Cirq
|       |-- qiskit/       # Codigo reutilizable para ejemplos Qiskit
|       |-- common/       # Utilidades compartidas
|-- tests/                # Pruebas unitarias y de reproducibilidad
|-- experiments/          # Experimentos puntuales, benchmarks y variantes
|-- data/                 # Datos pequenos o instrucciones para obtener datos
|-- environment.yml       # Entorno Anaconda principal
|-- requirements.txt      # Dependencias pip equivalentes
|-- README.md             # Proposito general del repositorio
|-- ROADMAP.md            # Plan de trabajo por etapas
|-- AI_GUIDE.md           # Guia para acompanamiento con IA
|-- CONTRIBUTING.md       # Normas para contribuir
|-- LICENSE               # Licencia del codigo propio del repositorio
```

## Principios

- El libro es la referencia de estudio; el repositorio es un cuaderno de trabajo abierto.
- Cada capitulo debe tener una carpeta o seccion con contexto, objetivos y resultados esperados.
- Los ejemplos se organizaran por framework cuando corresponda: Cirq y Qiskit.
- El codigo del libro puede transcribirse como punto de partida, y luego ajustarse, comentarse o extenderse segun el aprendizaje del proyecto.
- El codigo debe ser ejecutable con instrucciones claras.
- Cuando una API moderna difiera de la usada en el libro, se documentara la diferencia.
- Las respuestas generadas por IA deben revisarse, probarse y atribuirse como asistencia, no como autoridad final.

## Referencia

- Santanu Pattanayak, _Quantum Machine Learning with Python_.
- Enlace compartido por el usuario para consulta externa: https://indico.cern.ch/event/1288913/attachments/2650941/4589882/Quantum%20machine%20learning%20with%20python.pdf

## Aviso Legal

Este repositorio no esta afiliado con el autor, la editorial ni los distribuidores del libro. Puede incluir codigo trabajado a partir de los ejemplos del libro con fines de estudio, pero no debe incluir reproducciones extensas del texto, figuras, tablas o material editorial protegido. Las notas, explicaciones y extensiones deben ser propias.
