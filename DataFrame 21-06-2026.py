# Databricks notebook source
from pyspark.sql  import SparkSession

spark = SparkSession.builder.appName('FirstLearning').getOrCreate()


# COMMAND ----------


# employees_details = spark.read.csv('/Volumes/workspace/default/volume/Data_Engineering/employees.csv',header=True, schema='id integer, name string, department string, salary long') #

# COMMAND ----------

employees_details = spark.read.csv('/Volumes/workspace/default/volume/Data_Engineering/employees.csv',header=True, inferSchema=True)

# COMMAND ----------

employees_details.display()

# COMMAND ----------

employees_details.display()

# COMMAND ----------

employees_details.display()

# COMMAND ----------

employees_details.display()

# COMMAND ----------

# MAGIC %md 
# MAGIC # how to the multiline JSON and CSV 

# COMMAND ----------

 emp_multi = spark.read.option('multiline','True').json('/Volumes/workspace/default/volume/Data_Engineering/employees.json')

# COMMAND ----------

 emp_multi = spark.read.option('multiline','True').csv('/Volumes/workspace/default/volume/Data_Engineering/employees.json')

# COMMAND ----------

# MAGIC %md
# MAGIC # how to read the entire dictionaries or folder

# COMMAND ----------


complete_dictionaries_json = spark.read.option('multiline','True').json('/Volumes/workspace/default/volume/Data_Engineering/student_Json_file.json')


# COMMAND ----------


 complete_dictionaries_json = spark.read.option('multiline','True').csv('/Volumes/workspace/default/volume/Data_Engineering/employees.csv')

# COMMAND ----------

# complete_dictionaries_json = spark.read.option('multiline','True').csv(['Data_Engineering.json2','Data_Engineering.json1','Data_Engineering.json3'])

# COMMAND ----------

# MAGIC %md
# MAGIC # how to read text file #

# COMMAND ----------

 text_file = spark.read.text('Data_Engineering.text')

# COMMAND ----------

# MAGIC %md 
# MAGIC # how to read the parquet file #

# COMMAND ----------

 parquet_file_read = spark.read.parquet('/Volumes/workspace/default/volume/Data_Engineering/parquet_fil')

# COMMAND ----------

# MAGIC %md 
# MAGIC # how to read the XML File 

# COMMAND ----------

 xml_file = spark.read.xml('/Volumes/workspace/default/volume/Data_Engineering/student_xml_file.xlsx')

# COMMAND ----------

# MAGIC %md 
# MAGIC # How th read the ORC file 

# COMMAND ----------

 orc_file = spark.read.orc('/Volumes/workspace/default/volume/Data_Engineering/xml_file')

# COMMAND ----------

# MAGIC %md
# MAGIC # How to create dataframe from table 

# COMMAND ----------

table_dataframe = spark.sql("""SELECT * FROM  workspace.default.employees""")

# COMMAND ----------

table_dataframe.display()

# COMMAND ----------

