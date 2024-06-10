# Proyecto de Optimización de Talento

Con el objetivo de reducir la rotación de empleados y mejorar la satisfacción en el trabajo, la empresa ABC Corporation nos ha contratado para desarrollar un proyecto de análisis de datos y experimentación A/B de gran alcance. Nuestra misión es identificar factores clave que influyen en la satisfacción en el trabajo y, en última instancia, en la retención de empleados.

En este proyecto, presentaremos los resultados de nuestro análisis exploratorio de datos, diseñaremos un experimento A/B para probar hipótesis críticas y analizaremos los resultados para proporcionar a ABC Corporation información valiosa que informe sus decisiones estratégicas.

## ¿Quién es ABC Corporation?

ABC Corporation, fundada en 1980 en California, es una consultora tecnológica especializada en ofrecer soluciones de inteligencia artificial (IA) y aprendizaje automático (machine learning) a empresas de diversos sectores. Su enfoque principal radica en automatizar y optimizar procesos empresariales mediante tecnologías de vanguardia.
La empresa se distingue por tener un equipo multidisciplinario que abarca expertos en UX/UI, marketing, analistas, científicos de datos y otros campos relevantes.

## Fases del Proyecto

### Fase 1: Análisis Exploratorio de Datos (EDA)

Realizar un análisis exploratorio detallado del conjunto de datos para comprender sus características y familiarizarnos con la información disponible.

### Fase 2: Transformación de los Datos

Realizar la limpieza, normalización, conversión de tipos de datos y aplicación de reglas empresariales específicas para preparar los datos para el análisis. Esto incluye:
- Reemplazar valores de la columna `Gender` por "Male" y "Female".
- Convertir columnas de tipo string a tipo numérico donde sea necesario.
- Eliminar valores duplicados y corregir valores inconsistentes.
- Corregir errores tipográficos en columnas categóricas.
- Eliminar columnas redundantes.

### Fase 3: Diseño de BBDD e Inserción de los Datos

Crear la estructura de la base de datos y realizar la inserción de datos inicial:
- Definir la estructura de la base de datos, identificando tablas, claves primarias y foráneas.
- Crear la base de datos utilizando herramientas aprendidas en el módulo 2.
- Insertar los datos de los empleados en la base de datos.

### Fase 4: Problema de A/B Testing

Determinar la relación entre el nivel de satisfacción en el trabajo y la rotación de empleados:
- Crear dos grupos basados en el nivel de satisfacción en el trabajo.
- Calcular la tasa de rotación en cada grupo.
- Realizar un análisis estadístico para determinar diferencias significativas.
- Analizar los resultados y calcular la magnitud de la relación.

### Fase 5: Creación de una ETL

Automatizar la extracción, transformación y carga de datos:
- Desarrollar funciones para extraer datos desde diversas fuentes.
- Aplicar las transformaciones necesarias para garantizar la calidad de los datos.
- Crear la base de datos y desarrollar funciones para la inserción de datos transformados.

### Fase 6: Reporte de los Resultados

Generar un informe detallado con visualizaciones en Python:
- Crear un informe completo con análisis descriptivos y visualizaciones.
- Presentar tendencias, áreas de mejora y fortalezas dentro de la empresa.

## Los Datos

Las columnas del DataFrame incluyen:
- `Age`, `Attrition`, `BusinessTravel`, `DailyRate`, `Department`, `DistanceFromHome`, `Education`, `EducationField`, `EmployeeCount`, `EmployeeNumber`, `EnvironmentSatisfaction`, `Gender`, `HourlyRate`, `JobInvolvement`, `JobLevel`, `JobRole`, `JobSatisfaction`, `MaritalStatus`, `MonthlyIncome`, `MonthlyRate`, `NumCompaniesWorked`, `Over18`, `OverTime`, `PercentSalaryHike`, `PerformanceRating`, `RelationshipSatisfaction`, `StandardHours`, `StockOptionLevel`, `TotalWorkingYears`, `TrainingTimesLastYear`, `WorkLifeBalance`, `YearsAtCompany`, `YearsInCurrentRole`, `YearsSinceLastPromotion`, `YearsWithCurrManager`, `SameAsMonthlyIncome`, `DateBirth`, `Salary`, `RoleDepartament`, `NumberChildren`, `RemoteWork`.

Cada columna proporciona información valiosa sobre los empleados, desde datos demográficos hasta detalles laborales y niveles de satisfacción.
