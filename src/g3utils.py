import pandas as pd
import numpy as np
import re as re


# ------------------------------
# Cambia los literales numericos x floats. En caso de no detectar la clave en un diccionario, reemplaza por NaN.
# El reemplazo x NaN se hace para poder realizar operaciones.
# Mejoras: debiera recibir diccionario y lista_prop como parametros para dejar una función polimorfica. 
# Entrada: DataFrame
# Salida: DataFrame

def cambiar_x_nros(df):
    dic = {'mono': 1, 'un':1, 'uno':1, 'dos':2, 'tres':3, 'cuatro':4, 'cinco':5 ,'seis':6 ,'siete':7}
    lista_prop = ['mono','un','uno','dos','tres','cuatro','cinco','seis','siete']
    serie_1 = pd.Series([x if x not in lista_prop else dic.get(x) for x in df])
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