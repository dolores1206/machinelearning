# -*- coding: utf-8 -*-
"""M6_02_SparkSession_Teoría.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TbRcGgPjtTo2o_jTRHZNc1_Sku3_p9jL

# SparkSession vs SparkContext

## Importamos SparkContext y SparkSession
"""

!pip install pyspark --quiet
from pyspark import SparkContext
from pyspark.sql import SparkSession

"""## Creamos nuestra primera sesion

En Apache Spark, una **sesión es una conexión de un cliente con el cluster Spark**. La sesión se utiliza para enviar trabajos al cluster y obtener resultados de ellos. Una sesión se puede iniciar de forma interactiva desde la línea de comandos o programáticamente desde una aplicación de Spark.

Un **contexto de Spark** es un objeto que representa una conexión a un cluster Spark y proporciona un punto de acceso a todas las funcionalidades de Spark. En una aplicación de Spark, normalmente se crea un contexto al principio del programa y se utiliza para realizar todas las operaciones de Spark en esa aplicación. Por ejemplo, podrías utilizar un contexto para crear un conjunto de datos (RDD), aplicar transformaciones y acciones sobre él y obtener resultados.

Es importante mencionar que **una sesión puede tener múltiples contextos**, y que cada contexto se puede utilizar para realizar operaciones de Spark de forma independiente. Por ejemplo, podrías tener un contexto para procesar datos en tiempo real y otro contexto para realizar análisis en lote.
"""

#Convenio
#Sesión --> spark
#Contexto --> sc

spark = SparkSession.builder \
        .master("local") \
        .appName("miPrimerApplicacion") \
        .getOrCreate()

"""## Terminamos la sesión actual

No podemos tener mas de una sesión a la vez en nuestro notebook, por lo cual con el método 'stop' terminaremos la applicación.

De la misma forma, al terminar una applicación, debemos de indicar explicitamente que termine. De otra forma no liberará los recursos asignados.
"""

spark.stop()

"""## Creamos una sesión heredando los atributos de un contexto"""

sc = SparkContext(master="local",appName = "miPrimerContexto")
spark2 = SparkSession(sc)

spark2

"""## Creamos una sesión múltiple"""

sparkSession2 = spark2.newSession()

"""## Revisamos que los tres objetos apuntan a la misma aplicación

Aprovechando la salida que nos ofrece, conocemos SparkUI, el monitor por excelencia para Spark
"""

spark2

print(spark)

sparkSession2

spark2.stop()