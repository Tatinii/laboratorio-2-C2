# --------------------------------------------------------
#Uso del dataset "Students Performance in Exams" con Pandas
# --------------------------------------------------------

import pandas as pd

# 1️ Cargar el dataset
df = pd.read_csv("StudentsPerformance.csv")

# 2 Resumen estadístico general
print("----- Resumen estadístico -----")
print(df.describe())

# 3 Tipos de datos por columna
print("\n----- Tipos de datos -----")
print(df.dtypes)

# 4 Primeros y últimos registros
print("\n----- Primeros registros -----")
print(df.head())

print("\n----- Últimos registros -----")
print(df.tail())

# 5 Ordenar resultados: promedio más alto en matemáticas
print("\n----- Estudiantes ordenados por puntaje en matemáticas -----")
print(df.sort_values(by="math score", ascending=False).head(10))

# 6 Calcular medidas estadísticas para una columna numérica

# Ejemplo: puntaje de lectura ("reading score")
media = df["reading score"].mean()
mediana = df["reading score"].median()
desv_std = df["reading score"].std()

print("\n----- Medidas estadísticas de 'reading score' -----")
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Desviación estándar: {desv_std:.2f}")
