#%%
import pandas as pd
from src_df import soporte_funciones as sf
from src_df import soporte_queries_bbdd as query
from src_df import funciones_sql as bbdd
#%%
#%%
df_read = sf.leer_csv('HR_RAW_DATA.csv')
df_read
#%%
sf.exploracion_df(df_read)

#%%
df_limpio = sf.limpieza_tranformacion1(df_read)
#%%
percent_the_null = sf.tratamiento_the_null(df_limpio)

# IMPRIMIR EL RESULTADO DEL TRATAMIENTO DE LOS NULOS
print("<< Porcentaje de valores nulos por columna >>: \n")
for columna, porcentaje in percent_the_null.items():
    print(f"{columna}: {porcentaje:.2f}%")

# %%
sf.imputacion_nulos(df_limpio)
#%%
nuevo_df = sf.leer_csv('DF_Totalmente_Limpio.csv')
nuevo_df.sample(10)
#%%
sf.exploracion_df(nuevo_df)

##QUERIES CREACION DE BBDD Y TABLES EN SQL
# Llamamos el DF
#%%
df = pd.read_csv("/home/v_fischer/Adalab/proyecto-da-promo-a-pt-modulo-3-team-1/Fase1_y_2_EDA&Limpiza_Data/df_transformado_limpio.csv")
df.head()

#creamos una variable para almacena el nimbre de la BBDD
#%%
nombre_bbdd = "abc_corporation"

#Creamos la BBDD
# %%
bbdd.creacion_bbdd(query.query_creacion_bbdd, "AlumnaAdalab")
#%%
bbdd.creacion_tablas(query.query_personal_employee, "AlumnaAdalab", nombre_bbdd)
bbdd.creacion_tablas(query.query_job_satisfaction, "AlumnaAdalab", nombre_bbdd)
bbdd.creacion_tablas(query.query_job_data, "AlumnaAdalab", nombre_bbdd)

#Insertar datos
#%%
datos_tabla_employee = list(set(zip(df["employeenumber"].values, df["age"].values, df["education"].values, df["educationfield"].values, df["gender"].values, 
                                    df["maritalstatus"].values, df["datebirth"].values)))
datos_job_satisfaction = list(set(zip(df["employeenumber"].values, df["attrition"].values, df["businesstravel"].values, df["distancefromhome"].values, df["environmentsatisfaction"].values, 
                                    df["jobinvolvement"].values, df["jobsatisfaction"].values, df["numcompaniesworked"].values, df["overtime"].values, df["relationshipsatisfaction"].values, df["worklifebalance"].values)))
datos_job_data = list(set(zip(df["employeenumber"].values, df["dailyrate"].values, df["hourlyrate"].values, df["joblevel"].values, df["jobrole"].values, 
                                    df["monthlyincome"].values, df["monthlyrate"].values, df["percentsalaryhike"].values, df["performancerating"].values, df["stockoptionlevel"].values,
                                    df["totalworkingyears"].values, df["trainingtimeslastyear"].values, df["yearsatcompany"].values, df["yearssincelastpromotion"].values, df["yearswithcurrmanager"].values, df["remotework"].values)))
#%%
#Convertimos los tipos de datos a datos compatibles con SQL
datos_tabla_employee_convert = bbdd.convertir_tipos(datos_tabla_employee)
datos_job_satisfaction_convert = bbdd.convertir_tipos(datos_job_satisfaction)
datos_job_data_convert = bbdd.convertir_tipos(datos_job_data)
#%%
bbdd.insertar_datos(query.query_insertar_employee, "AlumnaAdalab", nombre_bbdd, datos_tabla_employee_convert )
bbdd.insertar_datos(query.query_insertar_job_satisfaction, "AlumnaAdalab", nombre_bbdd, datos_job_satisfaction_convert)
bbdd.insertar_datos(query.query_insertar_job_data, "AlumnaAdalab", nombre_bbdd, datos_job_data_convert)
