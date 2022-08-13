from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType
from pyspark.sql.functions import lit
import os
import configparser

config = configparser.RawConfigParser()
path = os.path.join(os.path.expanduser('~'), '.aws/credentials')
config.read(path)

conf = SparkConf()
conf.set('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.4')
conf.set("spark.hadoop.fs.s3a.endpoint", "s3.amazonaws.com")
conf.set('spark.hadoop.fs.s3a.access.key', config.get('datasouls', 'aws_access_key_id'))
conf.set('spark.hadoop.fs.s3a.secret.key', config.get('datasouls', 'aws_secret_access_key'))
conf.set('spark.executor.memory', '8g')
conf.set('spark.driver.memory', '8g')
conf.set('spark.executor.cores', '4')
conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

spark = SparkSession.builder.appName("eda").config(conf=conf).getOrCreate()

microdados_bronze_read_path = 's3a://enem-pyspark-athena-bronze/2020/microdados/MICRODADOS_ENEM_2020.csv'
microdados_silver_write_path = 's3a://enem-pyspark-athena-silver/2020/microdados/'

itens_prova_bronze_read_path = 's3a://enem-pyspark-athena-bronze/2020/itens_prova/ITENS_PROVA_2020.csv'
itens_prova_silver_write_path = 's3a://enem-pyspark-athena-silver/2020/itens_prova/'

itens_prova_gold_write_path = 's3a://enem-pyspark-athena-gold/itens_prova/'
microdados_gold_write_path = 's3a://enem-pyspark-athena-gold/microdados/'


schema_microdados = StructType([
    StructField("NU_INSCRICAO", IntegerType(), True),
    StructField("NU_ANO", IntegerType(), True),
    StructField("TP_FAIXA_ETARIA", IntegerType(), True),
    StructField("TP_SEXO", StringType(), True),
    StructField("TP_ESTADO_CIVIL", IntegerType(), True),
    StructField("TP_COR_RACA", IntegerType(), True),
    StructField("TP_NACIONALIDADE", IntegerType(), True),
    StructField("TP_ST_CONCLUSAO", IntegerType(), True),
    StructField("TP_ANO_CONCLUIU", IntegerType(), True),
    StructField("TP_ESCOLA", IntegerType(), True),
    StructField("TP_ENSINO", IntegerType(), True),
    StructField("IN_TREINEIRO", IntegerType(), True),
    StructField("CO_MUNICIPIO_ESC", IntegerType(), True),
    StructField("NO_MUNICIPIO_ESC", StringType(), True),
    StructField("CO_UF_ESC", IntegerType(), True),
    StructField("SG_UF_ESC", StringType(), True),
    StructField("TP_DEPENDENCIA_ADM_ESC", IntegerType(), True),
    StructField("TP_LOCALIZACAO_ESC", IntegerType(), True),
    StructField("TP_SIT_FUNC_ESC", IntegerType(), True),
    StructField("CO_MUNICIPIO_PROVA", IntegerType(), True),
    StructField("NO_MUNICIPIO_PROVA", StringType(), True),
    StructField("CO_UF_PROVA", StringType(), True),
    StructField("SG_UF_PROVA", StringType(), True),
    StructField("TP_PRESENCA_CN", IntegerType(), True),
    StructField("TP_PRESENCA_CH", IntegerType(), True),
    StructField("TP_PRESENCA_LC", IntegerType(), True),
    StructField("TP_PRESENCA_MT", IntegerType(), True),
    StructField("CO_PROVA_CN", IntegerType(), True),
    StructField("CO_PROVA_CH", IntegerType(), True),
    StructField("CO_PROVA_LC", IntegerType(), True),
    StructField("CO_PROVA_MT", IntegerType(), True),
    StructField("NU_NOTA_CN", IntegerType(), True),
    StructField("NU_NOTA_CH", IntegerType(), True),
    StructField("NU_NOTA_LC", IntegerType(), True),
    StructField("NU_NOTA_MT", IntegerType(), True),
    StructField("TX_RESPOSTAS_CN", StringType(), True),
    StructField("TX_RESPOSTAS_CH", StringType(), True),
    StructField("TX_RESPOSTAS_LC", StringType(), True),
    StructField("TX_RESPOSTAS_MT", StringType(), True),
    StructField("TP_LINGUA", IntegerType(), True),
    StructField("TX_GABARITO_CN", StringType(), True),
    StructField("TX_GABARITO_CH", StringType(), True),
    StructField("TX_GABARITO_LC", StringType(), True),
    StructField("TX_GABARITO_MT", StringType(), True),
    StructField("TP_STATUS_REDACAO", IntegerType(), True),
    StructField("NU_NOTA_COMP1", IntegerType(), True),
    StructField("NU_NOTA_COMP2", IntegerType(), True),
    StructField("NU_NOTA_COMP3", IntegerType(), True),
    StructField("NU_NOTA_COMP4", IntegerType(), True),
    StructField("NU_NOTA_COMP5", IntegerType(), True),
    StructField("NU_NOTA_REDACAO", IntegerType(), True),
    StructField("Q001", StringType(), True),
    StructField("Q002", StringType(), True),
    StructField("Q003", StringType(), True),
    StructField("Q004", StringType(), True),
    StructField("Q005", StringType(), True),
    StructField("Q006", StringType(), True),
    StructField("Q007", StringType(), True),
    StructField("Q008", StringType(), True),
    StructField("Q009", StringType(), True),
    StructField("Q010", StringType(), True),
    StructField("Q011", StringType(), True),
    StructField("Q012", StringType(), True),
    StructField("Q013", StringType(), True),
    StructField("Q014", StringType(), True),
    StructField("Q015", StringType(), True),
    StructField("Q016", StringType(), True),
    StructField("Q017", StringType(), True),
    StructField("Q018", StringType(), True),
    StructField("Q019", StringType(), True),
    StructField("Q020", StringType(), True),
    StructField("Q021", StringType(), True),
    StructField("Q022", StringType(), True),
    StructField("Q023", StringType(), True),
    StructField("Q024", StringType(), True),
    StructField("Q025", StringType(), True), 
])




df_microdados = spark.read \
        .options(delimiter=';', 
                 header='True',
                 encoding='latin1') \
        .schema(schema_microdados) \
        .csv(microdados_bronze_read_path)
        
        
schema_itens_prova = StructType([
    StructField("CO_POSICAO", IntegerType(), True),
    StructField("SG_AREA", StringType(), True),
    StructField("CO_ITEM", IntegerType(), True),
    StructField("TX_GABARITO", StringType(), True),
    StructField("CO_HABILIDADE", IntegerType(), True),
    StructField("IN_ITEM_ABAN", IntegerType(), True),
    StructField("TX_MOTIVO_ABAN", StringType(), True),
    StructField("NU_PARAM_A", DoubleType(), True),
    StructField("NU_PARAM_B", DoubleType(), True),
    StructField("NU_PARAM_C", DoubleType(), True),
    StructField("TX_COR", StringType(), True),
    StructField("CO_PROVA", IntegerType(), True),
    StructField("TP_LINGUA", IntegerType(), True),
    StructField("IN_ITEM_ADAPTADO", IntegerType(), True),
    StructField("TP_VERSAO_DIGITAL", IntegerType(), True),
])



df_itens_prova = spark.read \
        .options(delimiter=';', 
                 header='True',
                 encoding='latin1') \
        .schema(schema_itens_prova) \
        .csv(itens_prova_bronze_read_path)
        
df_itens_prova.write.mode('overwrite').parquet(itens_prova_silver_write_path)

df_microdados.write.mode('overwrite').parquet(microdados_silver_write_path)

df_itens_prova = df_itens_prova.withColumn('NU_ANO', lit(2020))

df_itens_prova.write.partitionBy('NU_ANO').mode('overwrite').parquet(itens_prova_gold_write_path)

df_microdados.write.partitionBy('NU_ANO').mode('overwrite').parquet(microdados_gold_write_path)