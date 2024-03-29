import pandas as pd
import numpy as np
import re as re


# ------------------------------
# Listado de funciones utilizadas para la recuperación de datos regex
# ------------------------------

def obtener_df_indexado_booleano(df, ncol, clave=None):
    """
    Busca en datos no-None y confecciona un data frame indexado incluyendo nombre a la columna. Si detecta un valor != None entonces reemplaza el valor por 1.00
    Adicionalmente puede buscar por una clave distinta de None que puede ingresarse como parámetro.
    A diferencia de 'obtener_df_indexado', 'obtener_df_indexado_booleano' operara sobre estructuras de datos simples como un str o int

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
            l_col.append(1.00)
    df_ret = pd.DataFrame(l_ind, columns={'indice'})
    df_ret[ncol] = pd.DataFrame(l_col)
    return df_ret


# ------------------------------

def obtener_df_indexado_simple(df, ncol, clave=None):
    """
    Busca en datos no-None y confecciona un data frame indexado incluyendo nombres a las columnas.
    Adicionalmente puede buscar por una clave distinta de None que puede ingresarse como parámetro.
    A diferencia de 'obtener_df_indexado', 'obtener_df_indexado_simple' operara sobre estructuras de datos simples como un str o int

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
            l_col.append(df.iloc[i])
    df_ret = pd.DataFrame(l_ind, columns={'indice'})
    df_ret[ncol] = pd.DataFrame(l_col)
    return df_ret

# ------------------------------

def registrar_recupero(valor, colu, df_recup):
    """
    Registra cantidad de valores recuperados de un feature en particular.
    Devuelve un data frame con los valores recuperados.
    Adicionalmente deja un archivo.csv a modo de syslog
    
    Parameters:
    -----------
    arg : valor, colu
    
    valor -- cant datos recuperados del feature
    colu -- nombre de columna (feature)
    df_recup -- data frame con valores recuperados por columna
    
    Returns:
    --------
    ret : data frame de una dimensión y archivo.csv
    
    """
    if df_recup.size == 0:     
        #recup = pd.DataFrame([valor], columns=[colu])
        df_recup = pd.DataFrame([valor], columns=[colu])
#         print('primer dato en df')
    elif colu not in df_recup.columns:
        df_recup[colu] = [valor+1]
#         print('columna creada')
    else:
        df_recup[colu] = [valor+2]
#         print('columna existente')
    df_recup.to_csv(r'../data/valores_recuperados.csv', encoding='utf-8')
    return df_recup

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
    serie_2 = pd.to_numeric(serie_1, errors='coerse', downcast='float') # coerse: pasa a los no-numericos como Nan's
    return pd.DataFrame(serie_2)

# ------------------------------

def busca_claves(pattern, columna, df_aux):
    """
    Busca las claves según pattern, dentro de una columna de un dataframe.
    
    Parameters:
    -----------
    pattern, columna, df_aux
    
    dipattern -- patrón de regex
    columna -- nombre de característica
    df -- data frame
    
    Returns:
    --------
    ret : data frame de una dimensión.
    
    """
    regex = re.compile(pattern, flags = re.IGNORECASE)
    m = pd.DataFrame([regex.findall(n) for n in df_aux[columna]])
    return m[0]

# ------------------------------
# Reemplaza NaN's por el valor de la clave ingresada
# Entrada: clave, df
# Salida: DataFrame

def reemplaza_nan(clave, df):
    """
    Reemplaza una clave específica por NaN en todo el dataframe
    
    Parameters:
    -----------
    clave, df
    
    clave -- clave de busqueda
    df -- data frame
    
    Returns:
    --------
    ret : data frame modificado por clave.
    """
    
    return df.replace(np.nan,clave)


# ------------------------------

def reemplaza_x_por_valor(dic, df, valor=None):
    """
    Reemplaza valores según claves dentro de un diccionario.
    
    Parameters:
    -----------
    arg : dic, df, valor
    
    dic -- diccionario de claves
    df -- dataframe
    valor -- valor a incluir en el reemplazo. Por defecto = None
    
    Returns:
    --------
    ret : dataframe modificado según claves
    
    """
    df_temp = [x if x not in dic else dic.get(x) for x in df]
    return df_temp

# ------------------------------

def agregar_columna(columna, df_original, df_nuevo):
    """
    Incorpora columnas dentro de un dataframe_01 a partir de la columna del dataframe_02
    
    Parameters:
    -----------
    arg : nfilas
    
    nfilas -- cantidad de filas
    
    Returns:
    --------
    ret : dataframe.
    
    """
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


# ------------------------------

def existe_clave(key, columna, df_aux):    
    """
    Verifica existencia de una key dentro de la columna de un data frame
    
    Parameters:
    -----------
    arg : key, columna, df_aux
    
    key -- clave de búsqueda
    columna -- nombre de columna a realizar la búsqueda
    df_aux -- data frame de búsqueda
    
    Returns:
    --------
    ret : cantidad de valores encontrados
    """
    
    m = []
    for frase in df_aux[columna]:
        if key in frase:
            m.append(True)
        else:
            m.append(False)
    return sum(m)

# ------------------------------

def crear_csv(nombre, df):
    """
    Crea archivo csv con el contenido de un dataframe identificado por un nombre.
    
    Parameters:
    -----------
    arg : nombre, df
    
    nombre -- nombre de archivo
    df -- data frame a persistir
    
    Returns:
    --------
    ret : cantidad de valores encontrados
    """
    
    ruta = '../data/'+nombre
    df.to_csv(ruta, encoding='utf-8')
    return print('[LOG] Se ha creado el archivo: ',nombre)