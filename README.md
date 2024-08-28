# Data Analysis Pipeline

Este script permite realizar un análisis exhaustivo de un conjunto de datos almacenado en un archivo CSV. Genera estadísticas descriptivas, distribuciones de datos, mapas de calor de correlación, y más. Además, guarda todos los resultados en una carpeta específica para una fácil consulta.

## Requisitos

- Python 3.7 o superior
- Librerías necesarias: `pandas`, `seaborn`, `matplotlib`, `concurrent.futures`

### Instalación de dependencias


pip install pandas seaborn matplotlib
Coloca tu archivo CSV en la ubicación deseada.
Ajusta las variables file_path y output_folder en el script para que apunten a tu archivo CSV y a la carpeta donde deseas guardar los resultados.
Ejecuta el script:


python analyze_data.py

Funcionalidades
Análisis Estadístico Descriptivo
Genera estadísticas descriptivas de todas las columnas y las guarda en descriptive_stats.csv.

Visualización de Distribuciones de Datos
Genera gráficos de distribución (histogramas con curvas KDE) para todas las columnas numéricas y los guarda como imágenes PNG.

Detección y Manejo de Valores Faltantes
Genera un resumen de valores faltantes por columna, incluyendo el porcentaje de valores faltantes, y lo guarda en missing_values_summary.csv.

Análisis de Correlación
Genera un mapa de calor de correlaciones entre las columnas numéricas y lo guarda en correlation_heatmap.png.

Detección de Valores Atípicos (Outliers)
Identifica y guarda los valores atípicos para cada columna numérica en archivos CSV separados.

Análisis de Datos Categóricos
Genera un análisis de columnas categóricas, guardando la frecuencia de cada categoría en un archivo Excel categorical_analysis.xlsx.

Análisis de Tendencias Temporales
Si el conjunto de datos contiene columnas de fechas, realiza un análisis de series temporales y guarda los gráficos de tendencia en formato PNG.

Personalización
Manejo de Fechas: El script intentará convertir automáticamente las columnas de texto en fechas si es posible.
Detección de Outliers: Utiliza el rango intercuartílico (IQR) para identificar valores atípicos.
Análisis Categórico: El análisis categórico se guarda en un archivo Excel con una hoja por cada columna categórica.
Ejemplo de Ejecución
python

file_path = r'C:\ruta\a\tu\archivo.csv'
output_folder = r'C:\ruta\de\salida'

analyze_data(file_path, output_folder)
Notas
Asegúrate de que el archivo CSV esté correctamente formateado con delimitadores de coma.
Para columnas numéricas con comas como separadores de miles, el script maneja esto automáticamente.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.



Este archivo README en formato `.md` es profesional, claro y conciso, facilitando su lectura y entendimiento por parte de cualquier usuario que necesite utilizar el script.
