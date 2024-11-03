import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from io import StringIO
from scipy.stats import gaussian_kde
import folium
from streamlit_folium import st_folium
from folium.plugins import HeatMap
import geopandas as gpd
from branca.colormap import LinearColormap

st.sidebar.image("Figuras/logo.png", use_column_width=True)

st.title("Dashboard de Análisis de Datos")

# Crear el menú en la barra lateral
st.sidebar.title("Navegación")
pagina_seleccionada = st.sidebar.radio("Ir a", ["Inicio", "Visualización de Datos", "Limpieza de Datos", "EDA", "Propiedades en Mapas"])

# Páginas individuales
if pagina_seleccionada == "Inicio":
    st.header("Inicio")
    st.write("Bienvenido al dashboard de análisis de datos.")
    st.subheader("¿Quienes somos?")
    st.write("Inmobiliaria Inversiones Duomo, con sede en el corazón de Milán, es una empresa líder especializada en la venta y gestión de propiedades en esta icónica ciudad italiana.\
        Nuestro objetivo es ofrecer a nuestros clientes una experiencia integral en el mercado inmobiliario, facilitando tanto la adquisición de propiedades de alto valor como la  \
             optimización de su rendimiento a través del alquiler vacacional. Nos distinguimos por nuestro profundo conocimiento del mercado local y por brindar soluciones personalizadas \
            que maximizan la rentabilidad y el valor de cada inversión. En Inversiones Duomo, unimos la tradición y la modernidad para convertir cada propiedad en una oportunidad de \
                éxito en una de las ciudades más dinámicas de Europa.")

elif pagina_seleccionada == "Visualización de Datos":
    st.header("Visualización de Datos")
    # Ejemplo de análisis
    st.write("El objetivo de este trabajo es realizar una exploración y visualización exhaustiva de los datos descargados de Inside Airbnb para la ciudad de Milán, Italia. \
             Este análisis tiene como propósito entender la estructura de las tablas, sus campos y el contenido de los datos, proporcionando una base comprensible para comprender \
                el mercado de alquiler vacacional.")
    ####----------------------------------------------------------CALENDAR
    st.subheader("\nInformación general del DataFrame 'Calendar':")
    df_calendar = pd.read_csv('data/calendar.csv')
    st.write("Primeras finalas:")
    st.write(df_calendar.head())
    # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_calendar.info(buf=buffer)
    info_str = buffer.getvalue()

    # Mostrar la información de la tabla en Streamlit
    st.text("Información del DataFrame 'df_calendar':")
    st.text(info_str)
    
    # Mostrar estadísticas descriptivas
    st.write("Estadísticas Descriptivas:")
    st.write(df_calendar.describe())
    
    st.write("Visualización de valores nulos")
    st.image("Figuras/nulos_calendar.png", caption="Visualización de valores nulos", use_column_width=True)
    
    #if st.button("Volver al principio"):
     #   st.experimental_rerun()
    
     ####----------------------------------------------------------LISTING
    st.subheader("\nInformación general del DataFrame 'Listings':")
    df_list = pd.read_csv('data/listings.csv')
    st.write("Primeras finalas:")
    st.write(df_list.head())
    # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_list.info(buf=buffer)
    info_str = buffer.getvalue()

    # Mostrar la información de la tabla en Streamlit
    st.text("Información del DataFrame 'Listings':")
    st.text(info_str)
    
    # Mostrar estadísticas descriptivas
    st.write("Estadísticas Descriptivas:")
    st.write(df_list.describe())
    
    st.write("Visualización de valores nulos")
    st.image("Figuras/nulos_list.png", caption="Visualización de valores nulos", use_column_width=True)
    
         ####----------------------------------------------------------LISTING DETAILED
    st.subheader("\nInformación general del DataFrame 'Listings Detailed':")
    df_list_de = pd.read_csv('data/listings_detailed.csv')
    st.write("Primeras finalas:")
    st.write(df_list_de.head())
    # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_list_de.info(buf=buffer)
    info_str = buffer.getvalue()

    # Mostrar la información de la tabla en Streamlit
    st.text("Información del DataFrame 'Listings Detailed':")
    st.text(info_str)
    
    # Mostrar estadísticas descriptivas
    st.write("Estadísticas Descriptivas:")
    st.write(df_list_de.describe())
    
    st.write("Visualización de valores nulos")
    st.image("Figuras/nulos_list_de.png", caption="Visualización de valores nulos", use_column_width=True)
    
         ####----------------------------------------------------------NEIGHBOURHOODS
    st.subheader("\nInformación general del DataFrame 'Neighbourhoods':")
    df_list_de = pd.read_csv('data/neighbourhoods.csv')
    st.write("Primeras finalas:")
    st.write(df_list_de.head())
    # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_list_de.info(buf=buffer)
    info_str = buffer.getvalue()

    # Mostrar la información de la tabla en Streamlit
    st.text("Información del DataFrame 'Neighbourhoods':")
    st.text(info_str)
    
    # Mostrar estadísticas descriptivas
    st.write("Estadísticas Descriptivas:")
    st.write(df_list_de.describe())
    
    st.write("Visualización de valores nulos")
    st.image("Figuras/nulos_neigh.png", caption="Visualización de valores nulos", use_column_width=True)
     ####----------------------------------------------------------REVIEWS SUMMARY
    st.subheader("\nInformación general del DataFrame 'Reviews_summary':")
    df_rev_su = pd.read_csv('data/reviews_summary.csv')
    st.write("Primeras finalas:")
    st.write(df_rev_su.head())
    # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_rev_su.info(buf=buffer)
    info_str = buffer.getvalue()

    # Mostrar la información de la tabla en Streamlit
    st.text("Información del DataFrame 'Reviews_summary':")
    st.text(info_str)
    
    # Mostrar estadísticas descriptivas
    st.write("Estadísticas Descriptivas:")
    st.write(df_rev_su.describe())
    
    st.write("Visualización de valores nulos")
    st.image("Figuras/nulos_rev_su.png", caption="Visualización de valores nulos", use_column_width=True)
    
     ####----------------------------------------------------------REVIEWS detailed
    st.subheader("\nInformación general del DataFrame 'Reviews_detailed':")
    df_rev_de = pd.read_csv('data/reviews_detailed.csv')
    st.write("Primeras finalas:")
    st.write(df_rev_de.head())
    # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_rev_de.info(buf=buffer)
    info_str = buffer.getvalue()

    # Mostrar la información de la tabla en Streamlit
    st.text("Información del DataFrame 'Reviews_detailed':")
    st.text(info_str)
    
    # Mostrar estadísticas descriptivas
    st.write("Estadísticas Descriptivas:")
    st.write(df_rev_de.describe())
    
    st.write("Visualización de valores nulos")
    st.image("Figuras/nulos_rev_deta.png", caption="Visualización de valores nulos", use_column_width=True)

elif pagina_seleccionada == "Limpieza de Datos":##################################################################
    st.header("Limpieza de Datos")
    st.write("En esta etapa se realiza principalmente tareas como: identificar y corregir errores, eliminar duplicados, manejar valores nulos y anomalías en los datos.")
    st.write("Estandarizaron unidades, como eliminar simbolos $ de la columna 'price' crear una nueva columna con valores binarios para la columna 'available', \
        asegurando que todos los datos sigan el mismo estándar.")
    df_list = pd.read_csv('data_clean/listings.csv')
    st.subheader("Resultados de eliminación de limpios de la columna 'listing' como ejemplo")
    st.write(df_list.isnull().sum())
    
    df_calendar = pd.read_csv('data_clean/calendar.csv')
    st.subheader("Resultados de ajuste de columna 'price' ")
    st.write("De esta columna fue eliminada el simbolo $ de todos los campos y ajustado el tipo de datos a 'float', también se realizaron ajustes similares a otras columnas de diversas tablas")
     # Capturar la salida de .info() en un string
    buffer = StringIO()
    df_calendar.info(buf=buffer)
    info_str = buffer.getvalue()
    st.text(info_str)
    
    st.subheader("Nuevo DataSet")
    st.write("Para calculos posteriores de precios de inversión y tiempo de retorno de inversión, fue creado un nuevo DataSet con datos filtrados y nuevas columnas")
    df_sub = pd.read_csv('data_clean/df_sub.csv')
    st.write("Primeras finalas:")
    st.write(df_sub.head())



elif pagina_seleccionada == "EDA":
    st.header("Gráficos Estáticos")
    st.write("El Análisis Exploratorio de Datos (EDA) para los datos de la ciudad de Milán permite entender patrones clave en el mercado \
        de alquileres vacacionales. Este proceso incluye examinar la disponibilidad, precios, reseñas y ubicación de propiedades, proporcionando insights \
            valiosos para identificar tendencias y oportunidades de inversión en la región.")

    st.write("Visualización de precios por tipo de inmueble")
    st.image("Figuras/distribución de precio por tipo de propiedad.png", caption="Visualización de precios por tipo de inmueble", use_column_width=True)
    
    st.write("Distribución de precio por vecindario")
    st.image("Figuras/distribución de precio por vecindario.png", caption="Distribución de precio por vecindario", use_column_width=True)
    
    st.write("Ocupación promedio por mes")
    st.image("Figuras/ocupación promedio por mes.png", caption="Ocupación promedio por mes", use_column_width=True)
    
    st.write("Precio por noche")
    st.image("Figuras/precio por noche.png", caption="Precio por noche", use_column_width=True)
    
    st.write("Promedio de reseña y calificación por propiedad")
    st.image("Figuras/promedio de resena y calificación x propiedad.png", caption="Promedio de reseña y calificación por propiedad", use_column_width=True)

elif pagina_seleccionada == "Propiedades en Mapas":########################
    st.header("Gráficos Estáticos y Dinámicos")
    st.write("Aquí se muestran gráficos en mapas con datos de inversión y tiempo de retorno")
    
    st.write("Mapa de calor hubicación de propiedades")
    st.image("Figuras/mapa de calor de hubicación  latitud y logitud.png", caption="Mapa de calor hubicación de propiedades", use_column_width=True)
    #---------------------------------------------------------------------
    df_list_de = pd.read_csv('data_clean/listings_detailed.csv')
    
    latitudes = df_list_de['latitude'].dropna()
    longitudes = df_list_de['longitude'].dropna()

    # Calcular densidad con KDE (estimación de densidad de kernel)
    xy = np.vstack([latitudes, longitudes])
    kde = gaussian_kde(xy, bw_method=0.1)  
    density = kde(xy)

# Crear pares de coordenadas con densidad para el mapa de calor
    heat_data = [[lat, lon, d] for lat, lon, d in zip(latitudes, longitudes, density)]

# Crear el mapa con centro en la media de las coordenadas
    centro_lat = latitudes.mean()
    centro_lon = longitudes.mean()
    mapa = folium.Map(location=[centro_lat, centro_lon], zoom_start=12)

    HeatMap(heat_data, radius=10, blur=15, max_zoom=1).add_to(mapa)

    # Mostrar el mapa en Streamlit
    st.title("Mapa de Calor de Densidad de Propiedades en Milán")
    st_folium(mapa, width=500, height=350)  
#------------------------------------------------------------------------------
df_sub = pd.read_csv('data_clean/df_sub.csv')
fig = px.scatter_mapbox(
    df_sub,
    lat='latitude',
    lon='longitude',
    size='price',
    zoom=11,
    mapbox_style='carto-positron',
    title='AirBnb - Distribución de Locales en Milán',
    template="plotly_dark",
    size_max=20,
    animation_frame='property_type'
)

st.plotly_chart(fig, use_container_width=True)
#---------------------------------------------------------------------------
df_sub_12 = df_sub[(df_sub['tiempo_retorno'] >= 4) & (df_sub['tiempo_retorno'] <= 10)]
map2 = folium.Map(location=[45.46427, 9.18951], zoom_start=13)
for coord in df_sub_12.itertuples(index=False):
    folium.Marker(
    location=(coord.latitude, coord.longitude),
    tooltip=f"Inversión: {coord.costo_total_inversion:.2f}€ \n\n Tiempo de Retorno: {coord.tiempo_retorno:.2f} años"
).add_to(mapa).add_to(map2)
st.title("Mapa de Calor de Densidad de Propiedades en Milán")
st_folium(mapa, width=700, height=500) 

