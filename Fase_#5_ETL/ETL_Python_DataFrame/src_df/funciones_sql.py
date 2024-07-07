import mysql.connector

def creacion_bbdd_tablas (query, contrasena,nombre_bbdd = None):
    if nombre_bbdd is not None:
        cnx = mysql.connector.connect (
            user = "root",
            password = contrasena,
            host = "VER CUAL PONER")
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
            host = "VER CUAL PONER",
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


def insertar_datos(query, contrasena, nombre_bbdd, lista_tuplas):
            cnx = mysql.connector.connect (
            user = "root",
            password = contrasena,
            host = "VER CUAL PONER")
             
            mycursor = cnx.cursor()

            try:
                  mycursor.executemany(query, lista_tuplas)
                  cnx.commit()
                  print(mycursor.rowcount, "registros insertados")
                  cnx.close()
            except mysql.connector.Error as err:
                print(err)
                print("Error code", err.errno)
                print("SQLSTATE", err.sqlstate) 
                print("Message", err.msg)
                  