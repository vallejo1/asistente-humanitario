import streamlit as st

st.set_page_config(page_title="Asistente Humanitario", layout="centered")

st.title("🤝 Asistente para Proyectos Humanitarios")
st.write("Bienvenido, Jesús. Este asistente te ayudará a gestionar iniciativas con impacto social.")

st.header("📋 Registro de Proyecto")
nombre = st.text_input("Nombre del proyecto")
descripcion = st.text_area("Descripción")
ubicacion = st.text_input("Ubicación geográfica")
fecha_inicio = st.date_input("Fecha de inicio")

if st.button("Guardar proyecto"):
    st.success(f"Proyecto '{nombre}' guardado exitosamente.")
