import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

def analyze_data(file_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Cargar los datos
    df = pd.read_csv(file_path, thousands=',')  # Maneja comas en números

    # Convertir columnas de texto que parecen numéricas
    for column in df.select_dtypes(include='object').columns:
        if df[column].str.contains(',').any():
            df[column] = df[column].str.replace(',', '.').astype(float, errors='ignore')

    # Análisis Estadístico Descriptivo
    def generate_descriptive_stats(df, output_file):
        stats = df.describe(include='all').transpose()
        stats.to_csv(output_file)
        print(f"Descriptive statistics saved to {output_file}")

    generate_descriptive_stats(df, os.path.join(output_folder, 'descriptive_stats.csv'))

    # Visualización de Distribuciones de Datos
    def plot_distributions(df, output_folder):
        def plot_column(column):
            plt.figure(figsize=(10, 5))
            sns.histplot(df[column], kde=True)
            plt.title(f'Distribution of {column}')
            plt.savefig(os.path.join(output_folder, f'{column}_distribution.png'))
            plt.close()

        numeric_columns = df.select_dtypes(include='number').columns
        with ThreadPoolExecutor() as executor:
            executor.map(plot_column, numeric_columns)
        print(f"Distributions saved to {output_folder}")

    plot_distributions(df, output_folder)

    # Detección y Manejo de Valores Faltantes
    def missing_values_summary(df, output_file):
        missing = df.isnull().sum()
        missing_percentage = (missing / len(df)) * 100
        summary = pd.DataFrame({'Missing Values': missing, 'Percentage': missing_percentage})
        summary = summary[summary['Missing Values'] > 0]
        summary.to_csv(output_file)
        print(f"Missing values summary saved to {output_file}")

    missing_values_summary(df, os.path.join(output_folder, 'missing_values_summary.csv'))

    # Análisis de Correlación
    def correlation_heatmap(df, output_file):
        try:
            corr = df.corr()
            plt.figure(figsize=(12, 10))
            sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
            plt.title('Correlation Heatmap')
            plt.savefig(output_file)
            plt.close()
            print(f"Correlation heatmap saved to {output_file}")
        except Exception as e:
            print(f"Error generating correlation heatmap: {e}")

    correlation_heatmap(df, os.path.join(output_folder, 'correlation_heatmap.png'))

    # Detección de Valores Atípicos (Outliers)
    def detect_outliers(df):
        def process_column(column):
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            outliers = df[(df[column] < (Q1 - 1.5 * IQR)) | (df[column] > (Q3 + 1.5 * IQR))]
            if not outliers.empty:
                outliers.to_csv(os.path.join(output_folder, f'{column}_outliers.csv'), index=False)
                print(f"Outliers in {column}: {len(outliers)} - Saved to {column}_outliers.csv")

        numeric_columns = df.select_dtypes(include='number').columns
        with ThreadPoolExecutor() as executor:
            executor.map(process_column, numeric_columns)

    detect_outliers(df)

    # Análisis de Datos Categóricos
    def categorical_analysis(df, output_file):
        categorical_columns = df.select_dtypes(include='object').columns
        if categorical_columns.empty:
            print("No categorical columns found for analysis.")
            return
        
        summary = {}
        for column in categorical_columns:
            summary[column] = df[column].value_counts()
        
        with pd.ExcelWriter(output_file) as writer:
            for column, counts in summary.items():
                counts.to_frame().to_excel(writer, sheet_name=column[:31])
        print(f"Categorical analysis saved to {output_file}")

    categorical_analysis(df, os.path.join(output_folder, 'categorical_analysis.xlsx'))

    # Análisis de Tendencias Temporales (si hay columnas de fecha)
    def time_series_analysis(df, output_folder):
        date_columns = df.select_dtypes(include='object').apply(pd.to_datetime, errors='ignore').columns
        if not date_columns.empty:
            for column in date_columns:
                if pd.api.types.is_datetime64_any_dtype(df[column]):
                    df.set_index(column, inplace=True)
                    plt.figure(figsize=(12, 6))
                    df.resample('M').size().plot()
                    plt.title(f'Time Series Analysis for {column}')
                    plt.xlabel('Date')
                    plt.ylabel('Count')
                    plt.savefig(os.path.join(output_folder, f'{column}_time_series.png'))
                    plt.close()
                    df.reset_index(inplace=True)
            print(f"Time series analysis saved to {output_folder}")
        else:
            print("No date columns found for time series analysis.")

    time_series_analysis(df, output_folder)

# Ajusta la ruta del archivo y la carpeta de salida
file_path = r'Ruta de tu archivo csv'
output_folder = r'ruta donde quieres que se almacene todo'

analyze_data(file_path, output_folder)