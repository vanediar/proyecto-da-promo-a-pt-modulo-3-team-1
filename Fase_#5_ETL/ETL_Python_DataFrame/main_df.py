#%%
import pandas as pd
from src_df import soporte_funciones as sf
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