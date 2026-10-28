import sys
from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder \
    .appName("Analisis_Lotes_UMV") \
    .getOrCreate()

ruta = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "/home/vboxuser/Modelo_de_Priorizaci_n_UMV.csv"
)

df = spark.read \
    .option("header", "true") \
    .option("encoding", "UTF-8") \
    .option("inferSchema", "true") \
    .csv(ruta)

# Limpiar y convertir las columnas numéricas
df_limpio = (
    df
    .withColumn(
        "AREA_NUM",
        F.regexp_replace(F.col("AREACALZAD"), ",", "").cast("double")
    )
    .withColumn(
        "LONGITUD_NUM",
        F.regexp_replace(F.col("LONGITUDHO"), ",", "").cast("double")
    )
)

print("\n===== 1. RESUMEN GENERAL =====")
print("Registros:", df_limpio.count())
print("Columnas originales:", len(df.columns))

print("\n===== 2. ESTADÍSTICAS DESCRIPTIVAS =====")
df_limpio.select(
    "ANCHOCALZA",
    "AREA_NUM",
    "LONGITUD_NUM",
    "PUNTAJE_IP",
    "IP_RELATIV"
).describe().show(truncate=False)

print("\n===== 3. REGISTROS POR TIPO DE SUPERFICIE =====")
df_limpio.groupBy("TIPOSUPERF") \
    .count() \
    .orderBy(F.desc("count")) \
    .show(20, truncate=False)

print("\n===== 4. REGISTROS POR RANGO DE IP =====")
df_limpio.groupBy("RANGOS_IP") \
    .count() \
    .orderBy("RANGOS_IP") \
    .show(30, truncate=False)

print("\n===== 5. DIEZ REGISTROS CON MAYOR IP RELATIVO =====")
df_limpio.select(
    "OBJECTID",
    "CIV",
    "TIPOSUPERF",
    "AREA_NUM",
    "LONGITUD_NUM",
    "IP_RELATIV",
    "RANGOS_IP"
).orderBy(F.desc("IP_RELATIV")) \
 .show(10, truncate=False)

print("\n===== 6. VALORES NULOS =====")
expresiones = [
    F.sum(
        F.when(F.col(c).isNull(), 1).otherwise(0)
    ).alias(c)
    for c in df.columns
]

df.select(*expresiones).show(truncate=False)

# Guardar resultados para usarlos en el informe
salida = "/home/vboxuser/resultados_umv"
(
    df_limpio.select(
        "OBJECTID",
        "CIV",
        "TIPOSUPERF",
        "AREA_NUM",
        "LONGITUD_NUM",
        "PUNTAJE_IP",
        "IP_RELATIV",
        "RANGOS_IP"
    )
    .write
    .mode("overwrite")
    .option("header", "true")
    .csv(salida)
)

print("\nResultados guardados en:", salida)

spark.stop()
