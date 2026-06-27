# Databricks notebook source
print('Hello')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create Spark Session ###
# MAGIC ## Create Spark Session ##
# MAGIC # Create Spark Session #
# MAGIC

# COMMAND ----------

from pyspark.sql  import SparkSession

spark = SparkSession.builder.appName('FirstLearning').getOrCreate()


# COMMAND ----------

help(SparkSession)

# COMMAND ----------

help(spark.createDataFrame)

# COMMAND ----------

# MAGIC %md
# MAGIC # How to Create Dataframe using list of Tuple #

# COMMAND ----------

data =[(1,'Chetan'),(2,'Pratik')]
student_details_dataframe=spark.createDataFrame(data,['id','name'])
student_details_dataframe.show()

# COMMAND ----------

student_details_dataframe.display()

# COMMAND ----------

type(data)

# COMMAND ----------

# MAGIC %md
# MAGIC # how to create dataframe using list of lists #

# COMMAND ----------

mydata = [[1,'Anil'],['2','Sunil']]
collage_data_df = spark.createDataFrame(mydata,['roll_no','student_name'])

# COMMAND ----------

collage_data_df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # how to create dataframe using list of dictionaries #

# COMMAND ----------

mydictonaries = [
                {'id': 1 , 'name':'chetan'},
                {'id': 2 , 'name':'pratik'},
                {'id': 3 , 'name':'pranav'},
                {'id': 4 , 'name':'dhruv'},
                {'id': 5 , 'name':'Aniket'}
]

players_name_dataframe = spark.createDataFrame(mydictonaries,['id','name'])
players_name_dataframe.display()

# COMMAND ----------

players_name_dataframe.printSchema()

# COMMAND ----------

# MAGIC %md 
# MAGIC # How to Define the schema manually structType #

# COMMAND ----------

from pyspark.sql.types import *

# COMMAND ----------

help(StructType)

# COMMAND ----------

from pyspark.sql.types import *

schema = StructType([
    StructField('id', LongType(), True),
    StructField('name', StringType(), True)
])

df = spark.createDataFrame(data, schema)


# COMMAND ----------

df.display()

# COMMAND ----------

df.printSchema()