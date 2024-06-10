# Sistema de Análisis de Sentimiento de Comentarios en Twitter

## Descripción del Proyecto

El objetivo de este proyecto es diseñar e implementar un sistema de análisis de sentimiento de comentarios en Twitter utilizando Kafka y otros servicios del ecosistema de Big Data. Dado que la API de Twitter no está abierta, la captura de datos se realizará desde un archivo a un topic de Kafka. Posteriormente, se llevará a cabo un análisis de sentimientos en tiempo real utilizando el [analizador de sentimientos](https://huggingface.co/blog/sentiment-analysis-python) de Python proporcionado por Hugging Face. Finalmente, los resultados serán transferidos a otro topic de Kafka, desde el cual se implementará un mecanismo de consumo de la información para obtener los resultados agregados.

El proyecto ha sido realizado como parte del Máster Experto Big Data Architecture & Engineering en Datahack. Tecnologías utilizadas:
- Kafka
- MongoDB
- Jupyter Notebook
- Docker
- Python



## Requisitos del Sistema

Para ejecutar este proyecto, necesitarás:

- Python 3.7 o superior
- Apache Kafka
- Librerías de Python: `pandas`, `kafka-python`, `transformers`, `torch`
- Archivo de comentarios de Twitter en formato CSV

## Instalación
TBD

## Configuración

1. **Configurar Kafka:**


2. **Crear topics en Kafka:**


3. **Modificar las configuraciones del proyecto (si es necesario):**


## Uso

1. **Carga de datos a Kafka:**


2. **Análisis de Sentimientos en Tiempo Real:**


3. **Consumo de Resultados Agregados:**


## Arquitectura del Sistema


2. **Análisis de Sentimientos:**

3. **Consumo y Agregación de Resultados:**



## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

