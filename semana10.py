# Importar pandas
import pandas as pd

# Crear el DataFrame con los datos de estudiantes
data = {
    'Nombre': ['Ana', 'Juan', 'Pedro', 'Sofía', 'Carlos', 'María', 'Luis'],
    'Edad': [18, 19, 18, 17, 20, 18, 19],
    'Género': ['Mujer', 'Hombre', 'Hombre', 'Mujer', 'Hombre', 'Mujer', 'Hombre'],
    'Calificación': [8.5, 7.0, 9.2, 9.8, 6.5, 8.0, 7.8]
}
df = pd.DataFrame(data)
print("Paso 1: DataFrame de Estudiantes\n", df, "\n")

# Agrupación por Género
grouped = df.groupby('Género')
print("Paso 2: DataFrame Agrupado por Género\n", grouped.size(), "\n")

# Resumen de Edad - Calcular la edad promedio por género
age_summary = grouped['Edad'].mean()
print("Paso 3: Edad Promedio por Género\n", age_summary, "\n")

# Resumen de Calificaciones - Calcular calificación promedio y máxima por género
calif_summary = grouped['Calificación'].agg(['mean', 'max'])
print("Paso 4: Calificación Promedio y Máxima por Género\n", calif_summary, "\n")

# Crear la tabla de resumen que combine ambos resúmenes
summary_table = pd.DataFrame({
    'Edad Promedio': age_summary,
    'Calificación Promedio': calif_summary['mean'],
    'Calificación Máxima': calif_summary['max']
})
print("Paso 5: Tabla de Resumen (Edad Promedio, Calificación Promedio y Máxima)\n", summary_table, "\n")

# Pregunta 1: Cantidad de estudiantes por género
count_by_gender = grouped.size()
print("Pregunta 1: Cantidad de Estudiantes por Género\n", count_by_gender, "\n")

# Pregunta 2: Ordenar la tabla de resumen por calificación promedio de forma descendente
sorted_summary = summary_table.sort_values(by='Calificación Promedio', ascending=False)
print("Pregunta 2: Tabla de Resumen Ordenada por Calificación Promedio Descendente\n", sorted_summary, "\n")

# Pregunta 3: Agregar columna de categoría de edad al DataFrame
df['Categoría Edad'] = df['Edad'].apply(lambda x: 'Joven' if x < 19 else 'Adulto')
print("Pregunta 3: DataFrame con Categoría de Edad\n", df, "\n")