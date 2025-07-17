Documentación y Resumen del Informe de Investigación
Aplicación Interactiva para Análisis de Desplazamientos del Terreno mediante DInSAR

📋 Información General del Proyecto
Título: Aplicación Interactiva para Análisis de Desplazamientos del Terreno mediante DInSAR
Autores: Luis Cumbicus, Kattia Guartan, Jose Isaac Patiño, Leiver Morocho
Fecha: 16 de julio de 2025
Materia: Lenguaje de Programación
Docente: Ing. Santiago Quiñones Cuenca
Carrera: Geología
Semestre: Cuarto

🎯 Resumen Ejecutivo
Este informe presenta el desarrollo de una aplicación interactiva construida con Streamlit para el análisis de desplazamientos del terreno en Ciudad Victoria utilizando datos DInSAR (Interferometría Diferencial de Radar de Apertura Sintética). La aplicación permite visualizar y analizar la correlación entre desplazamientos acumulados del terreno y precipitación promedio, proporcionando una herramienta clave para la gestión del riesgo geológico.
Hallazgos Principales:

Correlación directa entre precipitaciones intensas y desplazamientos del terreno
Picos críticos de desplazamiento superiores a 20,000 mm en 2016 y 2018
Comportamiento heterogéneo entre diferentes puntos de monitoreo
Períodos de estabilidad seguidos por deformaciones severas


🔧 Metodología Técnica
Tecnologías Utilizadas:

Lenguaje: Python
Entorno de Desarrollo: Visual Studio Code
Framework Web: Streamlit
Librerías Principales:

pandas - Manipulación de datos
matplotlib - Visualización gráfica
openpyxl - Lectura de archivos Excel



Proceso de Desarrollo:
1. Configuración del Entorno
bashpip install streamlit pandas matplotlib openpyxl
2. Preparación de Datos

Datos DInSAR organizados en formato Excel
Ajuste de encabezados (header=2) para correcta interpretación
Selección de columnas relevantes: temporal, desplazamiento acumulado, precipitación

3. Sistema de Visualización

Doble eje Y con matplotlib
Eje izquierdo (Y1): Desplazamiento acumulado (mm) - línea azul
Eje derecho (Y2): Precipitación promedio (mm) - línea/barra verde
Eje X: Escala temporal común
Actualización dinámica según selecciones del usuario

4. Interfaz de Usuario

Carga de archivos Excel/CSV
Menús desplegables para selección de variables
Visualización en tiempo real
Diseño modular y amigable


📊 Resultados Obtenidos
Período de Análisis: Enero 2015 - Julio 2019
Observaciones Críticas:

Desplazamientos máximos: >20,000 mm en puntos específicos
Años críticos: 2016 y 2018 con mayor actividad
Correlación temporal: Picos de desplazamiento coinciden con incrementos de precipitación
Variabilidad espacial: Respuestas heterogéneas entre puntos de monitoreo

Patrones Identificados:

Períodos de estabilidad relativa
Episodios de deformación severa
Desplazamientos negativos (posibles subsidencias)
Activación por eventos climáticos extremos


🔍 Análisis y Discusión
Estabilidad del Terreno:
La aplicación evidencia una correlación directa entre eventos de lluvia intensa y desplazamientos del terreno. Las precipitaciones actúan como principal factor desencadenante de inestabilidad mediante:

Saturación de terrenos
Alteración de presión en poros
Reducción de resistencia al corte

Variabilidad Espacial:
Los diferentes puntos de monitoreo muestran respuestas variables, influenciadas por:

Litología local
Pendiente del terreno
Uso del suelo
Densidad urbana


⚡ Fortalezas y Limitaciones de la Aplicación
Fortalezas:

✅ Accesibilidad: Interfaz web intuitiva
✅ Flexibilidad: Carga de diferentes formatos de datos
✅ Visualización: Gráficos dinámicos con doble eje
✅ Usabilidad: No requiere conocimientos de programación

Limitaciones Identificadas:

❌ Monitoreo en tiempo real: No integra datos live
❌ Análisis espacial: Carece de mapas interactivos
❌ Alertas automáticas: No genera avisos preventivos
❌ Reportes: No produce documentos automatizados


🚀 Mejoras Propuestas
Funcionalidades Adicionales Recomendadas:
1. Integración en Tiempo Real

Conexión con estaciones meteorológicas
Sensores GNSS para alertas automáticas
Actualización continua de datos

2. Componente Geoespacial

Mapas interactivos
Capas de pendientes y litología
Análisis de uso del suelo

3. Sistema de Alertas

Umbrales de riesgo configurables
Notificaciones automáticas
Semáforo de riesgo visual

4. Herramientas Analíticas

Filtros avanzados por fecha/área
Análisis estadístico integrado
Predicciones basadas en tendencias

5. Funcionalidades Colaborativas

Reportes ciudadanos
Plataforma comunitaria
Generación automática de informes


📈 Impacto y Aplicaciones
Gestión del Riesgo Geológico:

Toma de decisiones informada
Planificación territorial mejorada
Prevención de desastres más efectiva
Seguridad poblacional incrementada

Usuarios Objetivo:

Científicos y investigadores
Autoridades locales
Planificadores urbanos
Comunidades en riesgo


🎯 Conclusiones
La aplicación desarrollada representa un avance significativo en la democratización del acceso a herramientas de análisis geotécnico. Aunque constituye una base sólida para la visualización de datos DInSAR, su potencial se maximizaría mediante la incorporación de funcionalidades orientadas a la toma de decisiones operativas y la prevención de riesgos.
Valor Agregado:

Herramienta educativa para estudiantes de geología
Plataforma de análisis para profesionales
Base tecnológica para sistemas de monitoreo más complejos

Recomendaciones:

Implementar las mejoras propuestas de manera gradual
Validar resultados con datos de campo
Capacitar a usuarios finales en interpretación de datos
Establecer protocolos de respuesta ante alertas


📚 Referencias Técnicas
Tecnologías Documentadas:

Streamlit: Framework de aplicaciones web para Python
DInSAR: Interferometría Diferencial de Radar de Apertura Sintética
Matplotlib: Biblioteca de visualización científica
Pandas: Análisis y manipulación de datos estructurados

Datos de Prueba:

Período: Enero 2015 - Julio 2019
Ubicación: Ciudad Victoria
Fuente: Análisis DInSAR previos
Formato: Excel (.xlsx) con múltiples columnas de puntos de medición


Este documento constituye la documentación técnica completa del proyecto de aplicación DInSAR desarrollado como proyecto integrador para la carrera de Geología.
