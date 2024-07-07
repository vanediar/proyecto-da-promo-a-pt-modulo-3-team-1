#%%
import mysql.connector
from mysql.connector import errorcode
import numpy as np
#%%
def creacion_bbdd_tablas(query, contrasena, nombre_bbdd=None):
    try:
        cnx = mysql.connector.connect(
            user="root",
            password=contrasena,
            host="127.0.0.1",
            database=nombre_bbdd  # Selección de la base de datos aquí
        )
        mycursor = cnx.cursor()

        # Selección explícita de la base de datos si nombre_bbdd no es None
        if nombre_bbdd is not None:
            mycursor.execute(f"USE {nombre_bbdd};")

        try:
            mycursor.execute(query)
            print("Consulta ejecutada con éxito")
        except mysql.connector.Error as err:
            print(f"Error al ejecutar la consulta: {err}")
            print("Error code:", err.errno)
            print("SQLSTATE:", err.sqlstate)
            print("Message:", err.msg)

        cnx.commit()  # Confirmar los cambios en la base de datos

    except mysql.connector.Error as err:
        print(f"Error de conexión a MySQL: {err}")
    finally:
        if 'mycursor' in locals():
            mycursor.close()
        if 'cnx' in locals():
            cnx.close()

#%%
def insertar_datos(query, contrasena, nombre_bbdd, lista_tuplas):
    try:
        cnx = mysql.connector.connect(
            user="root",
            password=contrasena,
            host="127.0.0.1",
            database=nombre_bbdd
        )
        mycursor = cnx.cursor()

        try:
            mycursor.executemany(query, lista_tuplas)
            cnx.commit()
            print(mycursor.rowcount, "registros insertados")
        except mysql.connector.Error as err:
            print("Error al ejecutar la consulta:", err)
            print("Error code:", err.errno)
            print("SQLSTATE:", err.sqlstate)
            print("Message:", err.msg)

    except mysql.connector.Error as err:
        print("Error de conexión a MySQL:", err)
    finally:
        if 'mycursor' in locals():
            mycursor.close()
        if 'cnx' in locals():
            cnx.close()

# %%
def convertir_tipos(dataframe):
    """
    Función para convertir los tipos de datos de las columnas de un DataFrame según las necesidades.
    
    Args:
    - dataframe (pd.DataFrame): El DataFrame que contiene los datos a ser transformados.
    
    Returns:
    - pd.DataFrame: El DataFrame con los tipos de datos convertidos según las reglas especificadas.
    """
    df = dataframe.copy()
    
    # Definir reglas de conversión según el tipo de datos
    conversion_rules = {
        np.int64: int,
        np.float64: float,
        np.int32: int  
    }
    
    # Iterar sobre las columnas del DataFrame y aplicar las conversiones
    for column, dtype in df.dtypes.items():
        if dtype in conversion_rules:
            df[column] = df[column].astype(conversion_rules[dtype])
    
    return df