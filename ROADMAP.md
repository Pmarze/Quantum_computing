# Roadmap del Repositorio

Este roadmap propone una forma ordenada de construir el repositorio mientras avanzamos por _Quantum Machine Learning with Python_.

## Fase 0 - Preparacion

- Definir proposito publico del repositorio.
- Crear guias de uso, contribucion y acompanamiento con IA.
- Elegir licencia para el codigo propio.
- Decidir entorno base: Python, gestor de dependencias, notebooks y pruebas.
- Definir convenciones de nombres para capitulos y ejercicios.

## Fase 1 - Infraestructura

- Inicializar estructura de carpetas.
- Crear `pyproject.toml` o archivo equivalente de dependencias.
- Configurar formateo y pruebas.
- Crear primer notebook de verificacion del entorno.
- Documentar como ejecutar notebooks y scripts desde cero.
- Crear caminos separados para ejemplos en Cirq y Qiskit.

## Capitulos del Libro

_Quantum Machine Learning with Python_ — Santanu Pattanayak (Apress, 2021). 7 capitulos:

- [ ] Ch01 — Introduction to Quantum Computing
- [ ] Ch02 — Mathematical Foundations and Postulates of Quantum Computing
- [ ] Ch03 — Introduction to Quantum Algorithms
- [ ] Ch04 — Quantum Fourier Transform and Related Algorithms
- [ ] Ch05 — Quantum Machine Learning
- [ ] Ch06 — Quantum Deep Learning
- [ ] Ch07 — Quantum Variational Optimization and Adiabatic Methods

## Fase 2 - Lectura Guiada por Capitulos

Para cada capitulo:

- Crear una nota corta con objetivos conceptuales.
- Implementar ejemplos propios basados en las ideas del capitulo, separando versiones Cirq y Qiskit cuando ambas existan.
- Separar codigo reutilizable en `src/`.
- Agregar pruebas cuando haya funciones deterministas.
- Registrar diferencias con librerias actuales.
- Cerrar con resultados, dudas y siguientes pasos.

## Fase 3 - Reproducibilidad

- Fijar versiones de dependencias por bloque de capitulos si hace falta.
- Anadir scripts de ejecucion para notebooks importantes.
- Guardar resultados ligeros y regenerables.
- Documentar limitaciones de simulacion local.

## Fase 4 - Extension

- Comparar enfoques clasicos y cuanticos en datasets pequenos.
- Agregar variantes modernas de los algoritmos.
- Crear visualizaciones propias.
- Explorar ejecucion en simuladores y, si procede, backends cuanticos reales.

## Propuesta de Convencion por Capitulo

```text
notebooks/
|-- cirq/
|   |-- ch01_intro/
|   |   |-- 01_environment_check.ipynb
|   |   |-- 02_concepts_walkthrough.ipynb
|-- qiskit/
|   |-- ch01_intro/
|   |   |-- 01_environment_check.ipynb
|   |   |-- 02_concepts_walkthrough.ipynb

docs/
|-- ch01_intro.md
|-- ch02_linear_algebra.md

src/
|-- qml_santanu/
|   |-- __init__.py
|   |-- common/
|   |-- cirq/
|   |-- qiskit/

tests/
|-- cirq/
|-- qiskit/
|-- common/
```

## Decisiones Tomadas

- Python 3.11.
- Cirq >=1.3 y Qiskit >=1.0 / qiskit-aer >=0.14 (instalados via pip; conda-forge no incluye Cirq).
- Licencia MIT.
- Orden del libro como eje principal; adaptaciones modernas documentadas cuando la API difiera.

## Decisiones Pendientes

- Nombre final del repositorio en GitHub.
- Si se agregaran otras librerias cuanticas mas adelante (PennyLane, Qiskit extensions, etc.).
- Idioma principal de notas y comentarios: espanol, ingles o mixto.
