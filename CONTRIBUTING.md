# Contribuir

Gracias por querer contribuir. Este repositorio es un proyecto de estudio abierto, asi que priorizamos claridad, reproducibilidad y respeto por los derechos de autor.

## Que Aceptamos

- Implementaciones originales de conceptos estudiados.
- Transcripciones o adaptaciones de codigo del libro cuando sirvan como base de estudio y se indique el capitulo o seccion de referencia.
- Notebooks pedagogicos.
- Pruebas para codigo reutilizable.
- Correcciones de compatibilidad con librerias actuales.
- Mejoras de documentacion.
- Visualizaciones propias.

## Que No Aceptamos

- Copias extensas de texto del libro.
- Figuras, tablas o material editorial protegido del libro.
- Archivos grandes de datos que puedan descargarse o generarse.

## Estilo de Trabajo

- Mantener los cambios pequenos y enfocados.
- Indicar cuando un ejemplo parte del codigo del libro y que ajustes se hicieron.
- Documentar dependencias nuevas.
- Preferir funciones reutilizables cuando un fragmento se repita.
- Agregar pruebas cuando una funcion tenga comportamiento claro.
- Explicar diferencias si se actualiza una API usada por el libro.

## Convencion de Commits

Formato sugerido:

```text
tipo: descripcion breve
```

Ejemplos:

```text
docs: add chapter 1 reading notes
feat: implement basic qubit state utilities
test: add normalization checks
fix: update qiskit circuit import path
```

## Uso de IA

Se permite usar IA como apoyo siempre que el resultado sea revisado y probado. La IA no debe usarse para copiar texto explicativo, figuras ni material editorial protegido del libro.

Flujo sugerido: definir el concepto o ejercicio → decidir si se parte del codigo del libro o de una implementacion propia → ejecutar y revisar → documentar diferencias con APIs modernas.

Prompt base sugerido para iniciar una sesion:

```text
Estamos trabajando en un repositorio de acompanamiento para el libro
"Quantum Machine Learning with Python" de Santanu Pattanayak.
Ayudame a trabajar el siguiente concepto: [describe aqui capitulo y ejercicio].
Revisa la estructura del repo, propone o edita los archivos necesarios,
explica decisiones importantes, agrega pruebas cuando tenga sentido,
y documenta diferencias con APIs modernas.
```
