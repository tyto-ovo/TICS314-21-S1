import pandas as pd
import numpy as np

# Hay varias opciones mas para  poner como parametro
#  Documentation: https://pandas.pydata.org/pandas-docs/stable/reference/index.html
df = pd.read_csv('./data/vgsales.csv')


# Print Solo head del data frame, 
print(df.head())


# Antes de empezar a manipular la data en si, debemos limpiar el dataframe

# Podemos ver en el csv que hay una columna que no tiene nada, por lo que es innecesaria
# Deberiamos eliminarla utilizando drop y df.column (Selecciona una columna utilizando el index de ella)
df = df.drop(df.columns[0], axis=1)
print(df.head())



# Ahora queremos revizar si hay o no hay valores nulos en la data
# Cuando tenemos artos datos podria ser bueno simplemente eliminar la columna. Sin embargo, hay casos en los que deberiamos reemplazarlos por algun valor predeterminado (como por ejemplo el 0)


# Para ver si hay valores nulos podemos utilizar la siguiente funciones de pandas
print(f'Shape : {df.shape}')
print(df.info())

# Para verificar cuales columnas tienen valores nulos y en que cantidad utilizamos isnull
print(df.isnull().sum())
df = df.dropna()

# Verificamos si los valores de la data se eliminaron realmente
print(df.isnull().sum())


# ---------- Ahora que ya limpiamos los valores nulos de la data, podemos empezar a trabajarla


# Agregar columna de total de ventas
df['Global_Sales'] = df['NA_Sales'] + df['EU_Sales'] + df['JP_Sales'] + df['Other_Sales'] 
print(df.head())

# Ordenar por Global Sales (El que vendio mas a nivel mundial)
# Default esta en ascending = True
Sorted_df = df.sort_values(by = 'Global_Sales', ascending = False)

print(Sorted_df.head())


# Las tenemos ordenadas, pero el index no esta ordenado. Ademas nos gustaria añadirle el ranking (Puesto de cada pelicula)

Sorted_df = Sorted_df.reset_index(drop = True)
print(Sorted_df)

Sorted_df.insert(0, 'Ranking', range(1, len(Sorted_df) + 1))
print(Sorted_df)

# Podemos ver el juego que mas se vendio en general



# --------- Ahora tenemos lista la data para hacer analisis --------------

# Que queremos hacer con la data? Un buen approach puede ser intentar revisar que 
# Plataforma es la que mas vendio durante el año

Plataforms_df = Sorted_df.groupby(by = ['Platform'])['Global_Sales'].sum().reset_index(name ='Total Amount').sort_values(by = 'Total Amount', ascending = False)
print(Plataforms_df) 


# ------- Otro analisis de los datos: quiero saber los 5 compañias que mas publicaron juegos de deporte --------

# Selecciono solo los juegos (filas) que son del genero de deportes
Sports_df = Sorted_df[Sorted_df['Genre'] == 'Sports']
print(Sports_df)

# Agrupo por Publisher y veo quien es el que ha publicado mas juegos de deporte

# Creo columna de puros ceros
Sports_df['Counter'] = np.ones(len(Sports_df)) 

# Agrupo segun publisher y cuento la columna Counter
Sports_df = Sports_df.groupby(by = ['Publisher'])['Counter'].count().reset_index(name = 'Sport Games').sort_values(by = 'Sport Games', ascending = False).reset_index(drop = True)

print(Sports_df.head())
