#%%
# -----LIBRERIAS------

# Tratamiento de datos
import pandas as pd
import numpy as np
import re

# Imputación de the_null usando métodos avanzados estadísticos
from sklearn.impute import SimpleImputer
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.impute import KNNImputer

# Gestión de los warnings
import warnings
warnings.filterwarnings("ignore")

# Configuración
pd.set_option('display.max_columns', None) # para poder visualizar todas las columnas de los DataFrames

#%%

# LEER ARCHIVOS
def leer_csv(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo, index_col=0)
        return df
    except:
        print(f"El archivo '{ruta_archivo}' no se encontró.")
#%%

# EXPLORAR LOS DATAFRAME EN GENERAL 
def exploracion_df(df):
    
    print(' Filas y Columnas del DATAFRAME \n')
    print(f"El número de filas que tenemos es de {df.shape[0]}.\nEl número de columnas es de {df.shape[1]}\n")
    print('____________________________________________________________\n')
    
    print(' Nombre de todas las Columnas del DATAFRAME: \n')
    print(df.columns)
    print('____________________________________________________________\n')
    
    print('INFORMACIÓN GENERAL DEL DATAFRAME \n')
    print(df.info())
    print('____________________________________________________________\n')
    
    print('Ver los the_null del DataFrame \n')
    print(f'the_null de todo el data: --> {df.isnull().sum().mean() * 100} \n')
    for columna in df.columns:
        cantidad_valores_the_null = df[columna].isnull().mean() * 100
        print(f'La columna {columna}: {cantidad_valores_the_null}')
    print('____________________________________________________________\n')
    
    print('Valores ÚNICOS por columna:\n')
    for columna in df.columns:
        cantidad_valores_unicos = df[columna].unique()
        print(f'La columna {columna}: {len(cantidad_valores_unicos)}')
        print(f'La columna {columna}: {cantidad_valores_unicos}')
        
    print('____________________________________________________________\n')
    
    print('Valores DUPLICADOS por columna es de:\n')
    for columna in df.columns:
        cantidad_duplicados = df[columna].duplicated().sum()
        print(f'La columna {columna}: {cantidad_duplicados}')
    print('____________________________________________________________\n')
  
    print('--> RESUMEN ESTADÍSTICO \n')
    
    try:
        numeric_summary = df.describe().select_dtypes(include=['number']).T
        if not numeric_summary.empty:
            print('<<< Variables Numéricas >>> \n')
            print(f'{numeric_summary} \n')     
    except:
        print('No hay variables numéricas en el DataFrame.')
    
    try:
        categorical_summary = df.describe(include='object').T
        if not categorical_summary.empty:
            print('<<< Variables Categóricas >>> \n')
            print(f'{categorical_summary} \n')     
    except:
        print('No hay variables categóricas en el DataFrame.')
        
#%%
def limpieza_tranformacion1(df):
    # Eliminar columnas no deseadas
    columnas_a_eliminar = ["employeecount", "Department", "Over18", "StandardHours", 
                           "Salary", "NUMBERCHILDREN", "RoleDepartament", 
                           "YearsInCurrentRole", "SameAsMonthlyIncome"]
    df.drop(columns=columnas_a_eliminar, axis=1, inplace=True)

    # Convertir nombres de columnas a minúsculas
    nuevas_columnas = {columna: columna.lower() for columna in df.columns}
    df.rename(columns=nuevas_columnas, inplace=True)
    
    df["businesstravel"] = df["businesstravel"].str.replace("_", " ").str.replace("-"," ")
    
    df['dailyrate'] = df['dailyrate'].str.replace(",", ".").str.replace("$", "")
    df['dailyrate'] = df['dailyrate'].astype(float)
    
    df['distancefromhome'] = df['distancefromhome'].abs()
    
    df['educationfield'] = df['educationfield'].str.lower()
    df['jobrole'] = df['jobrole'].str.lower()
    
    df['gender'] = df['gender'].replace({0: 'Male', 1: 'Female'})
    
    df["maritalstatus"] = df["maritalstatus"].str.lower()
    df["maritalstatus"] = df["maritalstatus"].str.replace('marreid', 'married')
    
    # Rellenar los valores NA con 0 o cualquier otro valor predeterminado
    df.hourlyrate = df.hourlyrate.replace({'Not Available': 0})
    df['hourlyrate'] = df['hourlyrate'].astype(int) # Convertir la columna a enteros
    
    # Eliminar duplicados en la columna 'employeenumber' y conservar solo la primera ocurrencia
    df.drop_duplicates(subset='employeenumber', keep='first', inplace = True)
    # Limpiar la columna 'employeenumber'
    df['employeenumber'] = df['employeenumber'].astype(str).str.replace(',', '').str.strip()  
    # Convertir la columna 'employeenumber' a tipo numérico (int), manejando los posibles errores
    df['employeenumber'] = pd.to_numeric(df['employeenumber'], errors='coerce')
    # Mover la columna 'employeenumber' al principio
    df = df[['employeenumber'] + [col for col in df.columns if col != 'employeenumber']]
    
    
    df['remotework']= df['remotework'].replace({('1'):'Yes',('0') or ('False'): 'No', 'True': 'Yes', 'False': 'No'})
    
    # ----------------------------
    def cambiar_comas(cadena):
        try:
            return float(cadena.replace(',', '').replace('.', ''))
        except:
            return np.nan
    df['monthlyincome'] = df['monthlyincome'].apply(cambiar_comas)
    df['performancerating'] = df['performancerating'].apply(cambiar_comas)
    df['performancerating'] = df['performancerating'].astype(float)
    
    # Funición unica que cambia los valores de las columnas de totalworkingyears, worklifebalance
    def cambiar_comas_y_the_null(cadena):
        if pd.isnull(cadena):  # Si es un valor nulo, devuelve NaN
            return np.nan
        try:
            return float(cadena.replace(',', '.'))  # Intenta convertir la cadena a float
        except ValueError:  # Si la conversión falla, devuelve NaN
            return np.nan

    # Lista de las columnas que deseas modificar
    columnas_a_convertir = ['totalworkingyears', 'worklifebalance']

    # Aplica la función a cada columna en la lista
    for columna in columnas_a_convertir:
        df[columna] = df[columna].apply(cambiar_comas_y_the_null)
    
    # ----------------------------
    
    # Diccionario para convertir palabras a números
    word_to_number = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
        'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
        'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60,
        'seventy': 70, 'eighty': 80, 'ninety': 90
    }

    # Función para convertir cadenas a números
    def convert_to_number(age):
        try:
            # Primero intentamos convertir directamente a entero
            return int(age)
        except ValueError:
            # Si falla, intentamos convertir usando el diccionario
            words = age.split('-')
            number = 0
            for word in words:
                if word in word_to_number:
                    number += word_to_number[word]
                else:
                    return f"Error converting '{age}'"
            return number

    # Aplicar la función de conversión a la columna 'age' del DataFrame
    df['age'] = df['age'].apply(convert_to_number)

    return df       

#%%

# VER NULLS POR CATEGORIA

def tratamiento_the_null(df):
    percent_the_null = {}

    # Calcular para columnas numéricas
    colum_num = df.select_dtypes(include=np.number).columns
    print(f'Columnas Númericas: {colum_num}\n')
    for columna in colum_num:
        the_null = df[columna].isnull().sum()
        percent = (the_null / len(df)) * 100
        percent_the_null[columna] = percent

    # Calcular para columnas categóricas
    column_category = df.select_dtypes(include='object').columns
    print(f'Columnas Categóricas: {column_category}\n')
    for columna in column_category:
        the_null = df[columna].isnull().sum()
        percent = (the_null / len(df)) * 100
        percent_the_null[columna] = percent

    return percent_the_null

#%%

# IMPUTACIÓN DE NULOS
def imputacion_nulos(df):
    
    # ---> NULOS EN NÚMERICAS
    columnas_numericas = ['dailyrate', 'worklifebalance', 'performancerating']
    # Asegurarse de que las columnas existen 
    # Calcular la media para cada columna específica y rellenar los valores nulos
    for col in columnas_numericas:
        if col in df.columns:
            media = df[col].mean()
            df[col].fillna(media, inplace=True)
            df[col] = df[col].round(1)  # Redondear a un decimal
            print(f"Después del 'fillna' la columna {col.upper()} tiene {df[col].isnull().sum()} nulos")


    # ---> NULOS ATÍPICOS
    def fillna_with_median(df, column_name):
    
        # Calcular la mediana de la columna y rellenar los valores nulos
        mediana = df[column_name].median()
        df[column_name].fillna(mediana, inplace=True)

        # Comprobar los nulos después del 'fillna'
        print(f"Después del 'fillna' la columna '{column_name}' tiene {df[column_name].isnull().sum()} nulos")
    
    fillna_with_median(df, 'monthlyincome')
    fillna_with_median(df, 'totalworkingyears')
    
    # ---> NULOS CATEGÓRICAS
    columnas_categoricas = ['businesstravel', 'educationfield', 'maritalstatus', 'overtime']

    def reemplazar_nulos_por_moda(df, columnas_categoricas):
        for columna in columnas_categoricas:
            # Calcular la moda de la columna
            moda = df[columna].mode()[0]
            # Reemplazar los valores nulos por la moda
            df[columna] = df[columna].fillna(moda)
            print(f"Después del 'fillna' la columna '{columna}' tiene {df[columna].isnull().sum()} nulos")
        return df
    
    df = reemplazar_nulos_por_moda(df, columnas_categoricas)
    
    # Guardar el DataFrame limpio como un archivo CSV
    df.to_csv("DF_Totalmente_Limpio.csv", index=False)
#%%