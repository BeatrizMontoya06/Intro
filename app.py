import streamlit as st
from PIL import Image
import datetime

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA (ESTILO Y2K + ABEJAS)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Bea's Hive Webspace 🐝✨",
    page_icon="🐝",
    layout="wide"
)

# ---------------------------------------------------------
# ESTILOS RETRO AÑOS 2000 (CSS PERSONALIZADO CON DETALLES AMARILLO/NEÓN)
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
        color: #ffcc00 !important;
        text-shadow: 2px 2px #ff007f, 0 0 10px #ffcc00;
        font-family: 'Comic Sans MS', 'Chalkboard SE', cursive, sans-serif !important;
    }

    /* Cajas y marcos estilo tarjeta 2000s */
    div[data-testid="stVerticalBlock"] > div {
        border-radius: 8px;
    }

    /* Botones retro */
    .stButton>button {
        background: linear-gradient(180deg, #ffcc00 0%, #ff007f 100%);
        color: #000000 !important;
        border: 2px solid #00ffff !important;
        box-shadow: 3px 3px 0px #00ffff;
        font-weight: bold;
        text-transform: uppercase;
        border-radius: 0px !important;
        transition: all 0.2s ease;
    }
    
    .stButton>button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 5px 5px 0px #ff007f;
        color: #ffffff !important;
    }

    /* Estilo para las cajas de comentarios y publicaciones */
    .comment-box {
        background-color: #1a0033;
        border: 2px dashed #ffcc00;
        padding: 12px;
        margin-bottom: 12px;
        border-radius: 6px;
    }

    /* Banner con movimiento (Marquesina retro) */
    .marquee {
        width: 100%;
        background-color: #ffcc00;
        color: #000000;
        padding: 6px;
        font-weight: bold;
        border: 2px solid #ff007f;
        text-shadow: 0px 0px #fff;
        margin-bottom: 20px;
    }
</style>
"""
st.markdown(retro_css, unsafe_allow_html=True)

# ---------------------------------------------------------
# MARQUESINA ANIMADA DE BIENVENIDA
# ---------------------------------------------------------
st.markdown(
    '<div class="marquee"><marquee behavior="scroll" direction="left">'
    '🐝 Bienvenid@ a Bea\'s Hive 🐝 Diseño Interactivo ★ Experiencias Inmersivas ★ Arte, Narrativa & Tecnología ★ ¡Deja tu mensaje en el panal! 🍯'
    '</marquee></div>', 
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# ENCABEZADO PRINCIPAL
# ---------------------------------------------------------
st.title("🐝 ✨ ~* Welcome to Bea's Blog *~ ✨ 🐝")
st.write("---")

# ---------------------------------------------------------
# BARRA LATERAL (SIDEBAR) - BIOGRAFÍA Y FOTO DE PERFIL
# ---------------------------------------------------------
with st.sidebar:
    st.header("👤 PERFIL / SOBRE MÍ")
    
    # Foto de perfil
    try:
        foto_perfil = Image.open('mono.jpg')
        st.image(foto_perfil, caption='Bea @ 2000s Web 🐝', use_container_width=True)
    except Exception:
        st.info("📌 [AQUÍ VA TU FOTO DE CARA/PERFIL - 'mono.jpg']")

    st.subheader("★ Datos Personales ★")
    st.markdown("""
    * **Nombre:** Beatriz Montoya Arenas[cite: 1]
    * **Rol:** Diseñadora Interactiva / Narrativas 3D/2D/ANG[cite: 1]
    * **Especialidad:** Unity, Maya 3D, Figma y Adobe Creative Cloud[cite: 1]
    * **Estado actual:** 🟢 Diseño Sonoro / Projection Mapping
    * **Música favorita:** Breakcore 🎧
    * **Ubicación:** Medayork 🌐 *(Medellín, Col)*[cite: 1]
    """)
    
    st.write("---")
    st.subheader("🛠️ Software & Tools")
    st.markdown("""
    * **3D e Interacción:** Unity, Maya[cite: 1]
    * **Diseño/Creatividad:** Touch Designer, Adobe CC, Affinity, Canva, Capcut[cite: 1]
    * **Audio & Prod:** Reaper, Microsoft Office[cite: 1]
    """)

    st.write("---")
    st.subheader("🔗 Mis Redes / Contacto")
    st.markdown("- [Instagram](https://www.instagram.com/cloo.vie/) 📸 (`@cloo.vie`)")
    st.markdown("- **Email:** bmontoya03@hotmail.com[cite: 1]")


# ---------------------------------------------------------
# CONTENIDO PRINCIPAL POR PESTAÑAS (TABS)
# ---------------------------------------------------------
tab_inicio, tab_proyectos, tab_multimodal, tab_comentarios = st.tabs([
    "🏠 Inicio / Blog 🐝", 
    "🚀 Mis Proyectos 🍯", 
    "🎛️ Demo Multimodal ✨", 
    "💬 Librito de Visitas 📜"
])

# ---------------------------------------------------------
# PESTAÑA 1: INICIO Y ENTRADAS DEL BLOG (BASADO EN TU HOJA DE VIDA)
# ---------------------------------------------------------
with tab_inicio:
    st.header("📝 ÚLTIMAS ENTRADAS DEL PANAL")
    
    # Entrada #1
    st.subheader("📅 Entrada #1: Interfaces Multimodales y Convergencia Digital")
    st.caption("Publicado el: 29 de Septiembre, 2026")
    
    st.write("""
    ¡Hola! En este espacio me dedico a explorar la convergencia entre arte, narrativa y tecnología[cite: 1]. 
    Como diseñadora interactiva, mi enfoque radica en crear ecosistemas digitales y experiencias inmersivas 
    que integran elementos análogos y digitales para generar impacto social y cultural[cite: 1].
    
    Facilmente puedo desarrollar tanto frontend como backend, integrando herramientas como Unity, Maya, 
    TouchDesigner y diseño sonoro en Reaper para llevar las interfaces a otro nivel[cite: 1].
    """)
    
    try:
        img_blog = Image.open('mono.jpg')
        st.image(img_blog, caption='Evolución de las Interfaces Multimodales & Experiencias Híbridas', width=450)
    except Exception:
        st.info("📌 [IMAGEN DESTACADA 'mono.jpg']")

    st.write("---")

    # Entrada #2
    st.subheader("📅 Entrada #2: Proyección Urbana y Experiencias Híbridas")
    st.caption("Publicado recientemente desde la Universidad EAFIT[cite: 1]")
    st.write("""
    En mis últimos desarrollos académicos y personales he estado trabajando en la articulación de propuestas 
    expositivas con proyección urbana[cite: 1]. La combinación de cerámica física con arte digital virtual 
    demuestra cómo los entornos tangibles e intangibles pueden fusionarse para contar historias profundas[cite: 1].
    """)

# ---------------------------------------------------------
# PESTAÑA 2: PORTAFOLIO DE PROYECTOS (DE TU HOJA DE VIDA)
# ---------------------------------------------------------
with tab_proyectos:
    st.header("🛠️ GALERÍA DE PROYECTOS & EXPERIENCIAS")
    st.write("Proyectos destacados estructurados y conceptualizados:")
    
    col_proj1, col_proj2 = st.columns(2)
    
    # Proyecto Galeria A
    with col_proj1:
        st.subheader("🎨 Galería A")
        st.caption("Experiencia Inmersiva sobre Conciencia Social (Ago 2025 – Nov 2025)[cite: 1]")
        st.write("""
        * **Liderazgo integral:** Diseño y desarrollo de una experiencia inmersiva orientada al impacto social[cite: 1].
        * **Estrategia técnica:** Definición y estructuración técnica de la propuesta interactiva[cite: 1].
        * **Gestión:** Flujos de trabajo bajo presión garantizando excelencia[cite: 1].
        """)
        st.button("Ver detalle de Galería A 🔗", key="proj1_btn")

    # Proyecto Balegries
    with col_proj2:
        st.subheader("🏺 Balegries")
        st.caption("Experiencia Artística Híbrida (Jun 2022 – Nov 2022)[cite: 1]")
        st.write("""
        * **Narrativa digital:** Integración de cerámica física con arte digital en un entorno híbrido único[cite: 1].
        * **Espacio virtual:** Desarrollo y despliegue interactivo para la visualización de obras artísticas[cite: 1].
        * **Proyección urbana:** Colaboración interdisciplinaria para exposiciones en la ciudad[cite: 1].
        """)
        st.button("Ver detalle de Balegries 🔗", key="proj2_btn")

# ---------------------------------------------------------
# PESTAÑA 3: DEMO INTERACTIVA
# ---------------------------------------------------------
with tab_multimodal:
    st.header("🎛️ PRUEBA INTERACTIVA DE COMPONENTES")
    st.write("Prueba los elementos interactivos incorporados en la interfaz:")
    
    # Entrada de texto interactiva
    texto = st.text_input('Escribe algo en la terminal retro de Bea 🐝:', '¡Las experiencias inmersivas son el futuro!')
    st.success(f'✏️️ **Texto en consola:** {texto}')

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
            st.write('👁️ La vista es fundamental para la interpretación gráfica y el mapping.')
        elif modo == 'Auditiva':
            st.write('🎧 La audición y el Breakcore potencian el ambiente inmersivo.')
        elif modo == 'Táctil':
            st.write('✋ El tacto con elementos análogos aporta tridimensionalidad.')

    st.write("---")
    st.subheader("Uso de Botones Interactivos")
    if st.button('¡Presiona el Botón Neón!'):
        st.balloons()
        st.write('🎉 ¡Gracias por interactuar conmigo!')
    else:
        st.write('👆 Presiona el botón para lanzar un efecto.')

# ---------------------------------------------------------
# PESTAÑA 4: LIBRO DE VISITAS / COMENTARIOS
# ---------------------------------------------------------
with tab_comentarios:
    st.header("💬 LIBRO DE VISITAS / GUESTBOOK 🐝")
    st.write("¡Déjame un mensaje en el panal como en los 2000s!")

    # Historial de comentarios
    if 'comentarios' not in st.session_state:
        st.session_state['comentarios'] = [
            {"nombre": "RetroFan2000", "fecha": "2026-09-28", "mensaje": "¡Me encanta la temática de abejas y Y2K!"},
            {"nombre": "EAFIT_Visitor", "fecha": "2026-09-29", "mensaje": "Increíble portafolio de experiencias inmersivas. ¡Éxitos desde Medayork!"}
        ]

    # Formulario
    with st.form(key='form_comentarios'):
        nombre_usuario = st.text_input("Tu Nombre / Nickname:", placeholder="Ej: BeeUser_99")
        mensaje_usuario = st.text_area("Tu Mensaje:", placeholder="Escribe tu mensaje aquí...")
        submit_button = st.form_submit_button(label='Publicar en el Panal 🐝🚀')

    if submit_button:
        if nombre_usuario.strip() != "" and mensaje_usuario.strip() != "":
            nuevo_comentario = {
                "nombre": nombre_usuario,
                "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "mensaje": mensaje_usuario
            }
            st.session_state['comentarios'].insert(0, nuevo_comentario)
            st.success("✨ ¡Comentario publicado con éxito en el panal!")
        else:
            st.warning("⚠ Por favor completa tu nombre y el mensaje antes de publicar.")

    st.write("---")
    st.subheader("📜 Mensajes Recibidos")

    for c in st.session_state['comentarios']:
        st.markdown(f"""
        <div class="comment-box">
            <b>🐝 {c['nombre']}</b> <small>({c['fecha']})</small><br>
            💬 <i>"{c['mensaje']}"</i>
        </div>
        """, unsafe_allow_html=True)
