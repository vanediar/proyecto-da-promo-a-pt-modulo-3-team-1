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

#Traer queries creacion de BBDD y tablas
#%%
query.query_creacion_bbdd
# %%
bbdd.creacion_bbdd_tablas(query.query_creacion_bbdd, "admin")
bbdd.creacion_bbdd_tablas(query.query_personal_employee, "admin", "abc_corporation")
bbdd.creacion_bbdd_tablas(query.query_job_satisfaction, "admin", "abc_corporation")
bbdd.creacion_bbdd_tablas(query.query_job_data, "admin", "abc_corporation")
#%%
df = pd.read_csv("nombre csv")
df.head()

#%%
datos_tabla_employee = list(set(zip(df["poner las columnas"].values)))
datos_job_satisfaction = list(set(zip(df["poner las columnas"].values)))
datos_job_data = list(set(zip(df["poner las columnas"].values)))

#Insertar datos
bbdd.insertar_datos(query.query_insertar_employee, "admin", "abc_corporation", datos_tabla_employee )
bbdd.insertar_datos(query.query_insertar_employee, "admin", "abc_corporation", datos_job_satisfaction)
bbdd.insertar_datos(query.query_insertar_employee, "admin", "abc_corporation", datos_job_data)