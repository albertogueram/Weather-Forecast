import streamlit as st
import plotly.express as px
from backend import get_data

try:
    # Cabecera de la pagina
    st.title("Prevision del Tiempo")
    lat = st.text_input("Latitud: ")
    lon = st.text_input("Longitud: ")
    dias = st.slider("Prevision en dias:", min_value=1, max_value=5,
                     help="Selecciona el numero de dias a visualizar")

    # Backend Data
    st.subheader(f"Temperaturas en los proximos {dias} dias en "
                 f"Latitud: {lat}º, Longitud: {lon}º")
    cnt = dias * 8
    filtered_data = get_data(lat, lon, cnt)

    # Plot
    temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
    dates = [dict["dt_txt"] for dict in filtered_data]
    figure = px.line(x=dates, y=temperatures, labels={"x":"Fecha", "y":"Temperatura(ºC)"})
    st.plotly_chart(figure)

    st.subheader(f"Descripcion del Tiempo")
    for i in filtered_data:
        tiempo = i["dt_txt"]
        descripcion = i["weather"][0]["description"]
        st.markdown(f"{tiempo} - {descripcion}")


except KeyError:
    pass









