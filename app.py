import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Gráfico de Desplazamiento y Precipitación")

# Subir archivo
archivo = st.file_uploader("Sube tu archivo CSV o Excel", type=['csv', 'xlsx', 'xls'])

if archivo is not None:
    try:
        # Leer el archivo
        if archivo.name.endswith('.csv'):
            # Probar diferentes separadores y configuraciones
            try:
                df = pd.read_csv(archivo, sep=',')
            except:
                try:
                    df = pd.read_csv(archivo, sep=';')
                except:
                    try:
                        df = pd.read_csv(archivo, sep='\t')
                    except:
                        df = pd.read_csv(archivo, sep=',', error_bad_lines=False, warn_bad_lines=False)
        else:
            df = pd.read_excel(archivo)
    except Exception as e:
        st.error(f"Error al leer el archivo: {str(e)}")
        st.write("Intenta con estas soluciones:")
        st.write("1. Verifica que el archivo no esté dañado")
        st.write("2. Guarda el archivo como CSV con separador de comas")
        st.write("3. Verifica que no haya caracteres especiales")
        st.stop()
        
    # Mostrar los datos
    st.write("Datos cargados:")
    st.dataframe(df.head())
                 
    # Detectar automáticamente las columnas
    columnas = df.columns.tolist()
    fecha_col = columnas[0]  # Primera columna es fecha
    precip_col = columnas[-1]  # Última columna es precipitación
        
    # Las columnas del medio son desplazamiento
    desplazamiento_cols = columnas[1:-1]
        
    # Convertir la fecha
    try:
        df[fecha_col] = pd.to_datetime(df[fecha_col])
    except:
        st.error("Error al convertir las fechas. Verifica el formato de la primera columna.")
        st.stop()
        
    # Verificar que hay datos numéricos
    for col in desplazamiento_cols + [precip_col]:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    # Eliminar filas con valores vacíos
    df = df.dropna()
        
    # Crear el gráfico principal
    fig, ax1 = plt.subplots(figsize=(12, 6))
        
    # Graficar todos los desplazamientos como puntos
    for i, col in enumerate(desplazamiento_cols):
        ax1.scatter(df[fecha_col], df[col], label=f'Desplazamiento {col}', alpha=0.7, s=20)
        
    # Configurar el primer eje (desplazamiento)
    ax1.set_xlabel('Fecha')
    ax1.set_ylabel('Desplazamiento')
    ax1.tick_params(axis='y')
    ax1.legend(loc='upper left')
        
    # Crear segundo eje para precipitación
    ax2 = ax1.twinx()
    ax2.plot(df[fecha_col], df[precip_col], color='blue', linewidth=2, label='Precipitación')
    ax2.set_ylabel('Precipitación (mm)', color='blue')
    ax2.tick_params(axis='y', labelcolor='blue')
    ax2.legend(loc='upper right')
        
    # Título del gráfico
    plt.title('Desplazamiento y Precipitación vs Tiempo')
        
    # Rotar las fechas para que se vean mejor
    plt.xticks(rotation=45)
        
    # Ajustar el diseño
    plt.tight_layout()
        
    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)
    
    # NUEVO: Crear histograma de precipitaciones mensuales
    st.write("---")
    st.subheader("Histograma de Precipitaciones Mensuales")
    
    # Crear una copia del dataframe para el análisis mensual
    df_mensual = df.copy()
    
    # Extraer año y mes
    df_mensual['año'] = df_mensual[fecha_col].dt.year
    df_mensual['mes'] = df_mensual[fecha_col].dt.month
    df_mensual['año_mes'] = df_mensual[fecha_col].dt.to_period('M')
    
    # Agrupar por mes y sumar precipitaciones
    precipitacion_mensual = df_mensual.groupby('año_mes')[precip_col].sum().reset_index()
    
    # Crear el histograma
    fig2, ax3 = plt.subplots(figsize=(12, 6))
    
    # Graficar barras
    bars = ax3.bar(range(len(precipitacion_mensual)), 
                   precipitacion_mensual[precip_col], 
                   color='skyblue', 
                   alpha=0.7,
                   edgecolor='blue',
                   linewidth=0.5)
    
    # Configurar el gráfico
    ax3.set_xlabel('Mes/Año')
    ax3.set_ylabel('Precipitación Total (mm)')
    ax3.set_title('Precipitaciones Mensuales')
    
    # Configurar etiquetas del eje X
    ax3.set_xticks(range(len(precipitacion_mensual)))
    ax3.set_xticklabels([str(periodo) for periodo in precipitacion_mensual['año_mes']], 
                        rotation=45, ha='right')
    
    # Agregar valores en las barras
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                f'{height:.1f}', ha='center', va='bottom', fontsize=8)
    
    # Agregar línea de promedio
    promedio = precipitacion_mensual[precip_col].mean()
    ax3.axhline(y=promedio, color='red', linestyle='--', alpha=0.7, 
                label=f'Promedio: {promedio:.1f} mm')
    ax3.legend()
    
    # Ajustar el diseño
    plt.tight_layout()
    
    # Mostrar el histograma
    st.pyplot(fig2)
    
    # Estadísticas adicionales
    st.write("### Estadísticas de Precipitación Mensual:")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Promedio mensual", f"{promedio:.1f} mm")
    with col2:
        st.metric("Máximo mensual", f"{precipitacion_mensual[precip_col].max():.1f} mm")
    with col3:
        st.metric("Mínimo mensual", f"{precipitacion_mensual[precip_col].min():.1f} mm")
    with col4:
        st.metric("Desviación estándar", f"{precipitacion_mensual[precip_col].std():.1f} mm")
    
    # Mostrar tabla de datos mensuales
    st.write("### Datos Mensuales:")
    st.dataframe(precipitacion_mensual.rename(columns={
        'año_mes': 'Año-Mes',
        precip_col: 'Precipitación Total (mm)'
    }))
        
    # Mostrar información básica
    st.write("---")
    st.write("### Información del archivo:")
    st.write(f"- Total de registros: {len(df)}")
    st.write(f"- Columnas de desplazamiento: {len(desplazamiento_cols)}")
    st.write(f"- Rango de fechas: {df[fecha_col].min()} a {df[fecha_col].max()}")
    st.write(f"- Total de meses analizados: {len(precipitacion_mensual)}")

else:
    st.write("Por favor, sube un archivo CSV o Excel para comenzar.")
    st.write("El archivo debe tener:")
    st.write("- Primera columna: Fechas")
    st.write("- Columnas del medio: Datos de desplazamiento")
    st.write("- Última columna: Datos de precipitación")