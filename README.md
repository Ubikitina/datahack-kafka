# Sistema de Análisis de Sentimiento de Comentarios en Twitter

## Descripción del Proyecto

En este proyecto se ha diseñado e implementado un sistema de análisis de sentimiento de comentarios en Twitter utilizando Kafka y otros servicios del ecosistema de Big Data. 
- La captura de datos se ha realizado desde un archivo a un topic de Kafka, utilizando el dataset [sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140), dado que la API de Twitter no está abierta.
- Posteriormente, se ha llevado a cabo un análisis de sentimientos en tiempo real utilizando el [analizador de sentimientos](https://huggingface.co/blog/sentiment-analysis-python) de Python proporcionado por Hugging Face. 
- Finalmente, los resultados han sido transferidos a otro topic de Kafka, desde el cual se han implementado mecanismos de consumo de la información para obtener los resultados agregados utilizando KSQLDB, MongoDB y Jupyter.

El proyecto ha sido realizado como parte del Máster Experto Big Data Architecture & Engineering en Datahack. 

**Tecnologías utilizadas:**
- Kafka
- MongoDB
- Jupyter
- Docker
- Python


## Documentación

### Manual de Operación [[Link](./doc/Manual%20de%20Operacion.md)]

Proporciona instrucciones para desplegar y operar el sistema. Apartados:
- [Prerrequisitos para el Despliegue](./doc/Manual%20de%20Operacion.md#prerrequisitos-para-el-despliegue)
- [Instrucciones de Despliegue del Sistema](./doc/Manual%20de%20Operacion.md#instrucciones-de-despliegue-del-sistema)
- [Configuración y Detalle Técnico del sistema](./doc/Manual%20de%20Operacion.md#configuración-y-detalle-técnico-del-sistema)
- [Otras Operaciones](./doc/Manual%20de%20Operacion.md#otras-operaciones)
  - [Consumir Mensajes desde Topics](./doc/Manual%20de%20Operacion.md#consumir-mensajes-desde-topics)
  - [Ver documentos en MongoDB](./doc/Manual%20de%20Operacion.md#ver-documentos-en-mongodb)


### Manual de Uso [[Link](./doc/Manual%20de%20Uso.md)]

Proporciona instrucciones para la carga de datos y su posterior consulta. Apartados:

- [Carga de datos](./doc/Manual%20de%20Uso.md#carga-de-datos)
- [Consultas agregadas con KSQLDB en Tiempo Real](./doc/Manual%20de%20Uso.md#consultas-agregadas-con-ksqldb-en-tiempo-real)
- [Consultas con Mongo Express](./doc/Manual%20de%20Uso.md#consultas-con-mongo-express)
- [Análisis de datos en Jupyter Notebook](./doc/Manual%20de%20Uso.md#análisis-de-datos-en-jupyter-notebook)

### Arquitectura y Diseño [[Link](./doc/Arquitectura%20y%20Diseño.md)]
Describe el Diagrama de Arquitectura de los componentes, además de justificar su elección. Contiene:
- [Modelo C4](./doc/Arquitectura%20y%20Diseño.md#modelo-c4)
- [Descripción de componentes](./doc/Arquitectura%20y%20Diseño.md#descripción-de-componentes)
- [Justificación de la elección de tecnología](./doc/Arquitectura%20y%20Diseño.md#justificación-de-la-elección-de-tecnología)
  - [Captura de datos mediante CSV Spool Dir Source Connector](./doc/Arquitectura%20y%20Diseño.md#captura-de-datos-mediante-csv-spool-dir-source-connector)
  - [Topic 'tweets-input'](./doc/Arquitectura%20y%20Diseño.md#topic-tweets-input)
  - [Analyzer: Programa en Python en contenedor de Docker](./doc/Arquitectura%20y%20Diseño.md#analyzer-programa-en-python-en-contenedor-de-docker)
  - [Topic 'analyzed-tweets'](./doc/Arquitectura%20y%20Diseño.md#topic-analyzed-tweets)
  - [Análisis de datos y almacenamiento](./doc/Arquitectura%20y%20Diseño.md#análisis-de-datos-y-almacenamiento)
    - [KSQLDB Server y Cli](./doc/Arquitectura%20y%20Diseño.md#ksqldb-server-y-cli)
    - [MongoDB y Jupyter Notebook](./doc/Arquitectura%20y%20Diseño.md#mongodb-y-jupyter-notebook)
- [Futuras Líneas de Trabajo](./doc/Arquitectura%20y%20Diseño.md#futuras-líneas-de-trabajo)


## Referencias
- CSV Source Connector for Confluent Platform - [[Link](https://docs.confluent.io/kafka-connectors/spooldir/current/connectors/csv_source_connector.html#spooldir-csv-source-connector)]
- sergiokhayyat/kafka-exercises: Exercises to master Kafka from the very beggining (github.com) - [[Link](https://github.com/sergiokhayyat/kafka-exercises/blob/main/1.Environment/docker-compose.yml)]
- Getting Started with Sentiment Analysis using Python - [[Link](https://huggingface.co/blog/sentiment-analysis-python)]
- transformers · PyPI - [[Link](https://pypi.org/project/transformers/#history)]
- Sentiment140 dataset with 1.6 million tweets | Kaggle - [[Link](https://www.kaggle.com/datasets/kazanova/sentiment140)]
- How To Use Docker To Containerize Your Python Project - [[Link](https://python.land/deployment/containerize-your-project#Dockerize_yournbspPython_project)]



## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

