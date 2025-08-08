import streamlit as st

st.title("🤝 Asistente para Proyectos Humanitarios")

nombre = st.text_input("Nombre del proyecto")
descripcion = st.text_area("Descripción")
ubicacion = st.text_input("Ubicación")
fecha = st.date_input("Fecha de inicio")

if st.button("Guardar"):
    st.success(f"Proyecto '{nombre}' guardado.")
