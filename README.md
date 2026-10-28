# Análisis de priorización vial con Apache Spark

## 1. Descripción del proyecto

Este proyecto implementa un proceso de análisis batch utilizando Python y Apache Spark para explorar y analizar datos relacionados con la priorización de vías en Bogotá, Colombia. El objetivo es procesar un conjunto de datos de tamaño considerable, realizar tareas de limpieza y transformación, obtener estadísticas descriptivas e identificar patrones relevantes para el análisis de la infraestructura vial.

## 2. Fuente de los datos

Se utiliza el conjunto de datos **Modelo de Priorización de Vías Unidad de Mantenimiento Vial 2020**, publicado en el portal de Datos Abiertos de Bogotá.

Fuente: https://datosabiertos.bogota.gov.co/dataset/modelo-de-priorizacion-umv-2020

El archivo CSV debe descargarse desde la fuente oficial y guardarse en la ubicación configurada en el código fuente.

## 3. Tecnologías utilizadas

- Python.
- Apache Spark y PySpark.
- Pandas o Matplotlib, cuando corresponda a las visualizaciones del proyecto.
- Git y GitHub para el control de versiones y la publicación del código.

## 4. Procesamiento realizado

El programa `analisis_umv.py` desarrolla las siguientes actividades:

1. Lectura del archivo CSV mediante Apache Spark.
2. Inspección de la estructura y los tipos de datos.
3. Limpieza y transformación de variables seleccionadas.
4. Cálculo de estadísticas descriptivas.
5. Análisis de frecuencias de categorías de superficie.
6. Identificación de registros con valores nulos.
7. Consulta de los registros con mayores valores de priorización relativa.
8. Exportación de resultados para su posterior revisión.

## 5. Resultados del procesamiento

En la ejecución realizada se procesaron 93.684 registros y 28 columnas.

Entre los resultados obtenidos se encuentran estadísticas descriptivas de variables relacionadas con el ancho de calzada, el área, la longitud y los puntajes de priorización, además de distribuciones de categorías y rangos de priorización.

Los resultados corresponden a la ejecución realizada con el archivo de datos disponible y pueden variar si cambia la fuente o su contenido.

## 6. Requisitos

- Python 3.
- Java compatible con la versión instalada de Apache Spark.
- Apache Spark.
- PySpark.
- Las dependencias adicionales indicadas en `requirements.txt`.

## 7. Ejecución

### Paso 1. Descargar los datos

Descargue el archivo CSV desde el portal de Datos Abiertos de Bogotá indicado anteriormente.

### Paso 2. Configurar la ruta

Revise la variable que define la ruta del archivo CSV en `analisis_umv.py` y ajústela a la ubicación del archivo en su equipo.

### Paso 3. Ejecutar el programa

Con Apache Spark instalado y configurado, ejecute:

```bash
spark-submit analisis_umv.py
```

El programa generará los resultados definidos en el código. Verifique las rutas de salida configuradas antes de ejecutar el análisis.

## 8. Estructura del repositorio

- `analisis_umv.py`: código fuente del procesamiento batch.
- `requirements.txt`: dependencias de Python.
- `.gitignore`: archivos y directorios excluidos del control de versiones.
- `README.md`: documentación del proyecto.

## 9. Autoría

Proyecto académico desarrollado como ejercicio de procesamiento y análisis de datos con Apache Spark y Python.
