#%%
import mysql.connector
from mysql.connector import errorcode
import numpy as np
#%%
def creacion_bbdd(query, contrasena, nombre_bbdd=None):
    if nombre_bbdd is not None:
        cnx = mysql.connector.connect (
            user = "root",
            password = contrasena,
            host = "127.0.0.1")
        mycursor = cnx.cursor()

        try:
            mycursor.execute(query)
            print (mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error code", err.errno)
            print("SQLSTATE", err.sqlstate) 
            print("Message", err.msg)
    else:
            cnx = mysql.connector.connect (
            user = "root",
            password = contrasena,
            host = "127.0.0.1",
            database = nombre_bbdd)

            mycursor = cnx.cursor()

            try:
                mycursor.execute(query)
                print (mycursor)
            except mysql.connector.Error as err:
                print(err)
                print("Error code", err.errno)
                print("SQLSTATE", err.sqlstate) 
                print("Message", err.msg)

#%%
def creacion_tablas(query, contrasena, nombre_bbdd=None):
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
def convertir_tipos(lista_tuplas):
    lista_tuplas_convertidas = []
    for tupla in lista_tuplas:
        tupla_convertida = tuple(
            int(value) if isinstance(value, np.integer) else
            float(value) if isinstance(value, np.floating) else
            value for value in tupla
        )
        lista_tuplas_convertidas.append(tupla_convertida)
    return lista_tuplas_convertidas