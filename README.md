# Sistema de Análisis de Sentimiento de Comentarios en Twitter

## Descripción del Proyecto

En este proyecto se ha diseñado e implementado un sistema de análisis de sentimiento de comentarios en Twitter utilizando Kafka y otros servicios del ecosistema de Big Data. Dado que la API de Twitter no está abierta, la captura de datos se ha realizado desde un archivo a un topic de Kafka, utilizando el dataset [sentiment140](https://www.kaggle.com/datasets/kazanova/sentiment140). Posteriormente, se ha llevado a cabo un análisis de sentimientos en tiempo real utilizando el [analizador de sentimientos](https://huggingface.co/blog/sentiment-analysis-python) de Python proporcionado por Hugging Face. Finalmente, los resultados han sido transferidos a otro topic de Kafka, desde el cual se han implementado mecanismos de consumo de la información para obtener los resultados agregados utilizando KSQLDB, MongoDB y Jupyter Notebook.

El proyecto ha sido realizado como parte del Máster Experto Big Data Architecture & Engineering en Datahack. 

**Tecnologías utilizadas:**
- Kafka
- MongoDB
- Jupyter Notebook
- Docker
- Python


## Documentación


### Manual de Operación

El manual de operación proporciona instrucciones para desplegar y operar el sistema y se encuentra en [Manual de Operacion.md](./doc/Manual%20de%20Operacion.md). Apartados:
  - [Prerrequisitos para el Despliegue](./doc/Manual%20de%20Operacion.md#prerrequisitos-para-el-despliegue)
  - [Instrucciones de Despliegue del Sistema](./doc/Manual%20de%20Operacion.md#instrucciones-de-despliegue-del-sistema)
  - [Configuración y Detalle Técnico del sistema](./doc/Manual%20de%20Operacion.md#configuración-y-detalle-técnico-del-sistema)
  - [Otras Operaciones](./doc/Manual%20de%20Operacion.md#otras-operaciones)
    - [Consumir Mensajes desde Topics](./doc/Manual%20de%20Operacion.md#consumir-mensajes-desde-topics)
    - [Ver documentos en MongoDB](./doc/Manual%20de%20Operacion.md#ver-documentos-en-mongodb)


### Manual de Uso

### Arquitectura y Diseño
El documento de Arquitectura y Diseño.md describe el Diagrama de Arquitectura de los componentes de la solución. Contiene la siguiente información:
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







## Referencias
https://docs.confluent.io/kafka-connectors/spooldir/current/connectors/csv_source_connector.html#spooldir-csv-source-connector

https://github.com/sergiokhayyat/kafka-exercises/blob/main/1.Environment/docker-compose.yml

https://docs.conda.io/projects/conda/en/stable/user-guide/getting-started.html

https://huggingface.co/blog/sentiment-analysis-python

https://pypi.org/project/transformers/#history

https://www.kaggle.com/datasets/kazanova/sentiment140

https://python.land/deployment/containerize-your-project#Dockerize_yournbspPython_project


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).

