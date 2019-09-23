import pandas as pd
import numpy as np
import re as re


# ------------------------------

def obtener_df_indexado(df, ncol, clave=None):
    """
    Busca en datos no-None y confecciona un data frame indexado incluyendo nombres a las columnas.
    Adicionalmente puede buscar por una clave distinta de None que puede ingresarse como parámetro.

    Parameters:
    -----------
    arg : df, ncol, clave [Opcional, default = None]
    
    df -- data frame
    ncol -- nombre de columna indexada
    clave -- parámetro opcional. Clave distinta de None. Por defecto es None
    
    Returns:
    --------
    df_ret : data frame de dos dimensiones (indice & ncol).
    
    """

    l_ind = []
    l_col = []
    for i in range(len(df.index)):
        if df.iloc[i] != clave:
            l_ind.append(i)
            l_col.append(df.iloc[i][1])
    df_ret = pd.DataFrame(l_ind, columns={'indice'})
    df_ret[ncol] = pd.DataFrame(l_col)
    return df_ret


# ------------------------------

def limpiar_columna_x_clave(dic, df):
    """
    Busca las claves reconocidas en el diccionario y las reemplaza por su significado de diccionario. 
    En caso de no detectar la clave en un diccionario, reemplaza por NaN.
    
    Parameters:
    -----------
    arg : dic, df
    
    dic -- diccionario de claves a filtrar
    df -- data frame
    
    Returns:
    --------
    ret : data frame de una dimensión.
    
    """
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


# ------------------------------

def generar_df_posproduccion(nfilas):
    """
    Genera un data framne de posproduccion inicial de 'n' filas
    
    Parameters:
    -----------
    arg : nfilas
    
    nfilas -- cantidad de filas
    
    Returns:
    --------
    ret : data frame indice de posproduccion.
    
    """
    pos_pro = np.arange(0,nfilas)
    return pd.DataFrame(pos_pro, columns={'indice'})