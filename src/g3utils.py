import pandas as pd
import numpy as np
import re as re


# ------------------------------
# Busca las claves reconocidas en el diccionario y reemplaza por su significado. En caso de no detectar la clave en un diccionario, reemplaza por NaN.
# El reemplazo x NaN se hace para poder realizar operaciones.
# Entrada: diccionario con claves a buscar, DataFrame
# Salida: DataFrame

def limpiar_columna_x_clave(dic, df):
    serie_1 = pd.Series([x if x not in dic else dic.get(x) for x in df])
    serie_2 = pd.to_numeric(serie_1, errors='coerse', downcast='float') # coerse: pasa a NaN los no-numericos
    return pd.DataFrame(serie_2)

# ------------------------------
# Busca claves segun pattern en columna dentro de dataFrame 
# Entrada: pattern, columna, df
# Salida: DataFrame

def busca_claves(pattern, columna, df_aux):
    regex = re.compile(pattern, flags = re.IGNORECASE)
    m = pd.DataFrame([regex.findall(n) for n in df_aux[columna]])
    return m[0]

# ------------------------------
# Reemplaza NaN's por el valor de la clave ingresada
# Entrada: clave, df
# Salida: DataFrame

def reemplaza_nan(clave, df):
    return df.replace(np.nan,clave)

# ------------------------------
# Confecciona DataFrame limpio y definitivo para su uso
# Entrada: nueva columna, df1, df2
# Salida: DataFrame

def agregar_columna(columna, df_original, df_nuevo):
    df_original[columna] = df_nuevo
    return  df_original