# Diagrama de Arquitectura de Componentes

## Modelo C4
La arquitectura del sistema se representa mediante el [diagrama C4](https://c4model.com/).

Nivel 1: Diagrama de contexto del sistema:

![](./img/arquitectura/01.png)

Nivel 2: Diagrama de contenedores:

![](./img/arquitectura/02.png)

Nivel 3: Diagrama de componentes.
- Detalla los componentes internos de cada contenedor, mostrando cómo están estructurados y cómo interactúan entre sí para realizar las funciones del sistema.
- En este caso se omite el nivel 3, dado que no se considera necesario.

Nivel 4: Diagrama de código
- Se adentra en los detalles de implementación a nivel de código fuente, proporcionando una vista detallada de los módulos, clases y relaciones dentro del sistema.
- En este caso se omite este diagrama por simplicidad.


## Descripción de componentes

Se ha empleado una arquitectura basada en Kafka y otros servicios del ecosistema de Big Data para gestionar la captura, análisis y almacenamiento de datos.

**1. Captura de Datos:**
Se utiliza un File System como fuente de datos, donde se almacenan archivos CSV con información de los Tweets. Estos datos se procesan mediante el CSV Spool Dir Source Connector, que los lee y los publica en el topic de Kafka "tweets-input".

**2. Schema Registry - Gestión de Esquemas:**
Para garantizar la consistencia en la lectura de los tweets desde archivo, se emplea el Schema Registry, que gestiona el esquema de los datos.

**3. Analyzer - Análisis de Sentimientos:**
Los tweets son analizados en tiempo real utilizando el *Analyzer* de tweets, un contenedor de Docker que implementa el analizador de sentimientos de Hugging Face en Python. Los resultados se publican en el topic "analyzed-tweets" de Kafka.

**4. KSQLDB server y KSQLDB Cli - Procesamiento en Tiempo Real:**
KSQLDB server y KSQLDB Cli posibilitan la ejecución de consultas SQL en tiempo real sobre los streams de Kafka, permitiendo análisis adicional sobre los datos en movimiento.

**5. Almacenamiento en MongoDB:**
Los tweets procesados se transfieren desde el topic "analyzed-tweets" de Kafka a MongoDB mediante el MongoDB Sink Connector. En MongoDB, los datos se almacenan de forma orientada a documentos.

**6. Mongo Express - Interfaz de Usuario Web para Visualización:**
Para visualizar y manipular los datos almacenados en MongoDB, se utiliza Mongo Express, una interfaz de usuario web que permite acceder y gestionar los datos de forma intuitiva.

**7. Jupyter Notebook - Análisis Avanzado:**
Jupyter Notebook se emplea como una herramienta para conectar a MongoDB y realizar análisis avanzados de los datos. Utilizando las librerías pymongo, pandas y matplotlib, se pueden realizar exploraciones detalladas y generar visualizaciones interactivas.


## Justificación de la elección de tecnología

Explicación del por qué de los distintos componentes que conforman la solución, justificación de la elección de tecnología (si procede), tareas que realizan, interdependencias…