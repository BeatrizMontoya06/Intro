import streamlit as st
from PIL import Image
import datetime

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Bea's Webspace 2000s",
    page_icon="✨",
    layout="wide"
)

# ---------------------------------------------------------
# ESTILOS RETRO AÑOS 2000 (CSS PERSONALIZADO)
# ---------------------------------------------------------
retro_css = """
<style>
    /* Fondo retro y tipografía */
    .stApp {
        background-color: #0b021a;
        background-image: radial-gradient(#2b0938 15%, transparent 16%), radial-gradient(#15002b 15%, transparent 16%);
        background-size: 30px 30px;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Encabezados brillantes tipo Y2K */
    h1, h2, h3, h4 {
        color: #ff007f !important;
        text-shadow: 2px 2px #00ffff, 0 0 10px #ff007f;
        font-family: 'Comic Sans MS', 'Chalkboard SE', cursive, sans-serif !important;
    }

    /* Cajas y marcos estilo tarjeta 2000s */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 8px;
    }

    /* Botones retro */
    .stButton>button {
        background: linear-gradient(180deg, #ff007f 0%, #7b00ff 100%);
        color: #ffffff !important;
        border: 2px solid #00ffff !important;
        box-shadow: 3px 3px 0px #00ffff;
        font-weight: bold;
        text-transform: uppercase;
        border-radius: 0px !important;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 5px 5px 0px #00ffff;
        color: #ffff00 !important;
    }

    /* Estilo para las cajas de comentarios y chat */
    .comment-box {
        background-color: #1a0033;
        border: 2px dashed #ff007f;
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 5px;
    }

    /* Banner con movimiento */
    .marquee {
        width: 100%;
        background-color: #ff007f;
        color: #ffffff;
        padding: 5px;
        font-weight: bold;
        border: 2px solid #00ffff;
        text-shadow: 1px 1px #000;
        margin-bottom: 20px;
    }
</style>
"""
st.markdown(retro_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# BARRERA / BANNER SUPERIOR ANIMADO (MARQUESINA)
# ---------------------------------------------------------
st.markdown(
    '<div class="marquee"><marquee behavior="scroll" direction="left">'
    '★ Bienvenid@ a mi rincón en la web ★ Interfaces Multimodales ★ Backend & Frontend ★ ¡Deja tu comentario abajo! ★'
    '</marquee></div>', 
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# ENCABEZADO PRINCIPAL
# ---------------------------------------------------------
st.title("✨ ~* Welcome to Bea's Blog *~ ✨")
st.write("---")

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR) - BIOGRAFÍA Y FOTO DE PERFIL
# ---------------------------------------------------------
with st.sidebar:
    st.header("👤 PERFIL / SOBRE MÍ")
    
    # -----------------------------------------------------
    # [ZONA 1: TU FOTO / ROSTRO DE PERFIL]
    # Reemplaza 'tu_foto.jpg' por la ruta de tu foto de perfil.
    # -----------------------------------------------------
    try:
        foto_perfil = Image.open('mono.jpg') # Cambia 'mono.jpg' por la foto de tu cara
        st.image(foto_perfil, caption='Bea @ 2000s Web', use_container_width=True)
    except Exception:
        st.info("📌 [AQUÍ VA TU FOTO DE CARA/PERFIL] - Pon la ruta de tu imagen en el código.")

    st.subheader("★ Datos Personales ★")
    # -----------------------------------------------------
    # [ZONA 2: INFORMACIÓN SOBRE TI]
    # -----------------------------------------------------
    st.markdown("""
    * **Nombre:** Bea
    * **Rol:** Diseño de Narrativas 3D/2D/ANG
    * **Especialidad:**  Unity, Maya
3D, Figma y Adobe Creative Cloud
    * **Estado actual:** 🟢 Diseño Sonoro/Mapping
    * **Música favorita:** Beakcore 🎧
    * **Ubicación:** Medayork 🌐
    """)
    
    st.write("---")
    st.subheader("🔗 Mis Redes / Contacto")
    # -----------------------------------------------------
    # [ZONA 3: ENLACES A TUS REDES O PROYECTOS ENLACE]
    # -----------------------------------------------------
    st.markdown("- [Instagram](#) *(https://www.instagram.com/cloo.vie/)*")


# ---------------------------------------------------------
# CONTENIDO PRINCIPAL EN NAVEGACIÓN POR PESTAÑAS (TABS)
# ---------------------------------------------------------
tab_inicio, tab_proyectos, tab_multimodal, tab_comentarios = st.tabs([
    "🏠 Inicio / Blog", 
    "🚀 Mis Proyectos", 
    "🎛️ Demo Multimodal", 
    "💬 Librito de Visitas (Comentarios)"
])

# ---------------------------------------------------------
# PESTAÑA 1: INICIO Y ENTRADAS DEL BLOG
# ---------------------------------------------------------
with tab_inicio:
    st.header("📝 ÚLTIMAS ENTRADAS DEL BLOG")
    
    # -----------------------------------------------------
    # [ZONA 4: PRIMERA ENTRADA DEL BLOG]
    # -----------------------------------------------------
    st.subheader("📅 Entrada #1: Interfaces Multimodales y Desarrollo Web")
    st.caption("Publicado el: 29 de Septiembre, 2026")
    
    st.write("""
    ¡Hola! En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales. 
    Puedo realizar sin problemas tanto el **Backend** como el **Frontend** de los proyectos. 
    Las interfaces multimodales permiten combinar texto, visión, audio y sensores para enriquecer 
    la experiencia del usuario a niveles totalmente interactivos.
    """)
    
    # Imagen destacada del blog
    try:
        img_blog = Image.open('mono.jpg')
        st.image(img_blog, caption='Evolución de las Interfaces Multimodales', width=450)
    except Exception:
        st.info("📌 [AQUÍ VA UNA IMAGEN DESTACADA DEL BLOG]")

    st.write("---")

    # -----------------------------------------------------
    # [ZONA 5: SEGUNDA ENTRADA / ESPACIO PARA OTRA PUBLICACIÓN]
    # -----------------------------------------------------
    st.subheader("📅 Entrada #2: Mi visión del desarrollo")
    st.caption("Publicado recientemente")
    st.write("""
    Escribe aquí tus reflexiones, aprendizajes, eventos a los que hayas asistido 
    o cualquier actualización que quieras dar a tus visitantes.
    """)

# ---------------------------------------------------------
# PESTAÑA 2: PORTAFOLIO DE PROYECTOS
# ---------------------------------------------------------
with tab_proyectos:
    st.header("🛠️ GALERÍA DE PROYECTOS")
    st.write("Aquí puedes ver algunos de mis trabajos más recientes:")
    
    col_proj1, col_proj2 = st.columns(2)
    
    # -----------------------------------------------------
    # [ZONA 6: PROYECTO 1]
    # -----------------------------------------------------
    with col_proj1:
        st.subheader("🤖 Proyecto 1: App Multimodal")
        # st.image('ruta_proyecto_1.jpg')  <-- Descomenta para poner foto de tu proyecto
        st.write("""
        **Descripción:** Una aplicación que integra procesamiento de imágenes y voz en tiempo real.
        
        **Tecnologías:** Python, Streamlit, IA Multimodal.
        """)
        st.button("Ver Demo 1 🔗", key="proj1_btn")

    # -----------------------------------------------------
    # [ZONA 7: PROYECTO 2]
    # -----------------------------------------------------
    with col_proj2:
        st.subheader("💻 Proyecto 2: Backend + Frontend")
        # st.image('ruta_proyecto_2.jpg')  <-- Descomenta para poner foto de tu proyecto
        st.write("""
        **Descripción:** Arquitectura completa de microservicios con panel visual interactivo.
        
        **Tecnologías:** FastAPI, React, Streamlit, SQL.
        """)
        st.button("Ver Demo 2 🔗", key="proj2_btn")

# ---------------------------------------------------------
# PESTAÑA 3: DEMO DE TU CÓDIGO INTERACTIVO
# ---------------------------------------------------------
with tab_multimodal:
    st.header("🎛️ PRUEBA INTERACTIVA DE COMPONENTES")
    st.write("Aquí puedes interactuar con los controles que construí en esta demo:")
    
    # Entrada de texto interactiva
    texto = st.text_input('Escribe algo en mi terminal retro:', '¡El desarrollo web retro es genial!')
    st.success(f'✏️ **Texto ingresado:** {texto}')

    st.write("---")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Column #1: Experiencia de Usuario")
        st.write("Las interfaces multimodales mejoran enormemente la interacción.")
        resp = st.checkbox('¿Estás de acuerdo?')
        if resp:
            st.write('✅ ¡Correcto! La flexibilidad es clave.')

    with col2:
        st.subheader("Column #2: Modalidades")
        modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ('Visual', 'Auditiva', 'Táctil'))
        if modo == 'Visual':
            st.write('👁️ La vista es fundamental para la interpretación gráfica.')
        elif modo == 'Auditiva':
            st.write('🎧 La audición permite respuestas inmediatas sin pantalla.')
        elif modo == 'Táctil':
            st.write('✋ El tacto y la hápitca crean inmersión física.')

    st.write("---")
    st.subheader("Uso de Botones Interactivos")
    if st.button('¡Presiona el Botón Neón!'):
        st.balloons()
        st.write('🎉 ¡Gracias por interactuar conmigo!')
    else:
        st.write('👆 Presiona el botón para lanzar un efecto.')

# ---------------------------------------------------------
# PESTAÑA 4: LIBRO DE VISITAS / SECCIÓN DE COMENTARIOS
# ---------------------------------------------------------
with tab_comentarios:
    st.header("💬 LIBRO DE VISITAS / GUESTBOOK")
    st.write("¡Déjame un mensaje en mi muro como en los 2000s!")

    # Inicializar estado del historial de comentarios
    if 'comentarios' not in st.session_state:
        st.session_state['comentarios'] = [
            {"nombre": "RetroFan2000", "fecha": "2026-09-28", "mensaje": "¡Me encanta el diseño de tu blog! Saludos."},
            {"nombre": "WebDev_Guru", "fecha": "2026-09-29", "mensaje": "Genial cómo combinaste Streamlit con temática Y2K."}
        ]

    # Formulario de nuevo comentario
    with st.form(key='form_comentarios'):
        nombre_usuario = st.text_input("Tu Nombre / Nickname:", placeholder="Ej: CyberUser_99")
        mensaje_usuario = st.text_area("Tu Mensaje:", placeholder="Escribe tu mensaje aquí...")
        submit_button = st.form_submit_button(label='Publicar Comentario 🚀')

    if submit_button:
        if nombre_usuario.strip() != "" and mensaje_usuario.strip() != "":
            nuevo_comentario = {
                "nombre": nombre_usuario,
                "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mensaje": mensaje_usuario
            }
            st.session_state['comentarios'].insert(0, nuevo_comentario)
            st.success("✨ ¡Comentario publicado con éxito!")
        else:
            st.warning("⚠️️ Por favor completa tu nombre y el mensaje antes de publicar.")

    st.write("---")
    st.subheader("📜 Comentarios de los Visitantes")

    # Desplegar lista de comentarios
    for c in st.session_state['comentarios']:
        st.markdown(f"""
        <div class="comment-box">
            <b>👤 {c['nombre']}</b> <small>({c['fecha']})</small><br>
            💬 <i>"{c['mensaje']}"</i>
        </div>
        """, unsafe_allow_html=True)
