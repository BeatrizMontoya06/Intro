import streamlit as st
from PIL import Image, ImageEnhance, ImageOps
import datetime
import os

# ---------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA (ESTILO Y2K / FRUTIGER AERO + ABEJAS)
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

    /* Marco estilo marco de fotos / Cyber Profile Y2K */
    .y2k-photo-frame {
        border: 3px solid #ff007f;
        box-shadow: 0 0 15px #ff007f, 4px 4px 0px #00ffff;
        padding: 6px;
        background: linear-gradient(135deg, #1a0033 0%, #2b0938 100%);
        border-radius: 8px;
        text-align: center;
        margin-bottom: 15px;
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
# FUNCIÓN PARA PROCESAR LA FOTO EN ESTILO Y2K / VINTAGE DIGICAM
# ---------------------------------------------------------
def aplicar_estilo_y2k(imagen):
    # Aumentar contraste y saturación estilo cámara digital de los 2000s
    enhancer_sat = ImageEnhance.Color(imagen)
    img_y2k = enhancer_sat.enhance(1.35)
    
    enhancer_contrast = ImageEnhance.Contrast(img_y2k)
    img_y2k = enhancer_contrast.enhance(1.2)
    
    return img_y2k

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
# BARRA LATERAL (SIDEBAR) - BIOGRAFÍA, FOTO Y2K Y AUDIO LOCAL
# ---------------------------------------------------------
with st.sidebar:
    st.header("👤 PERFIL / SOBRE MÍ")
    
    # Cargar y procesar la foto con estilo Y2K
    nombre_foto = 'mono.jpeg' if os.path.exists('mono.jpeg') else 'mono.jpg'
    
    if os.path.exists(nombre_foto):
        img_original = Image.open(nombre_foto)
        img_y2k = aplicar_estilo_y2k(img_original)
        
        st.markdown('<div class="y2k-photo-frame">', unsafe_allow_html=True)
        st.image(img_y2k, caption='★ Bea @ Y2K Cyber Space ★ 🐝', use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("📌 [AQUÍ VA TU FOTO DE CARA/PERFIL - 'mono.jpeg']")

    # -----------------------------------------------------
    # MÚSICA DE FONDO (DESDE ARCHIVO LOCAL)
    # -----------------------------------------------------
    st.write("---")
    st.subheader("🎵 Background Music")
    
    archivo_musica = "musica.mp3"
    
    if os.path.exists(archivo_musica):
        st.audio(archivo_musica, format="audio/mp3", loop=True)
        st.caption("🎧 Sonando desde los archivos locales.")
    else:
        st.info("📌 Coloca tu archivo de canción como `musica.mp3` en la misma carpeta para reproducirla aquí.")

    st.write("---")
    st.subheader("★ Datos Personales ★")
    st.markdown("""
    * **Nombre:** Beatriz Montoya Arenas[cite: 1]
    * **Rol:** Diseñadora Interactiva / Narrativas 3D/2D/ANG[cite: 1]
    * **Especialidad:** Unity, Maya 3D, Figma y Adobe Creative Cloud[cite: 1]
    * **Estado actual:** 🟢 Diseño Sonoro / Projection Mapping
    * **Música favorita:** Frutiger Aero, IDM & Breakcore 🎧
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
tab_inicio, tab_multimodal, tab_comentarios = st.tabs([
    "🏠 Inicio / Blog 🐝", 
    "🎛️ Demo Multimodal ✨", 
    "💬 Librito de Visitas 📜"
])

# ---------------------------------------------------------
# PESTAÑA 1: INICIO Y ENTRADAS DEL BLOG
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
    
    Fácilmente puedo desarrollar tanto frontend como backend, integrando herramientas como Unity, Maya, 
    TouchDesigner y diseño sonoro en Reaper para llevar las interfaces a otro nivel[cite: 1].
    """)
    
    if os.path.exists(nombre_foto):
        img_blog = Image.open(nombre_foto)
        st.image(aplicar_estilo_y2k(img_blog), caption='Evolución de las Interfaces Multimodales & Experiencias Híbridas', width=420)

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
# PESTAÑA 2: DEMO INTERACTIVA
# ---------------------------------------------------------
with tab_multimodal:
    st.header("🎛️ PRUEBA INTERACTIVA DE COMPONENTES")
    st.write("Prueba los elementos interactivos incorporados en la interfaz:")
    
    # Entrada de texto interactiva
    texto = st.text_input('Escribe algo en la terminal retro de Bea 🐝:', '¡Las experiencias inmersivas son el futuro!')
    st.success(f'✏ **Texto en consola:** {texto}')

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
            st.write('🎧 La audición potencia la atmósfera e inmersión de la interfaz.')
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
# PESTAÑA 3: LIBRO DE VISITAS / COMENTARIOS
# ---------------------------------------------------------
with tab_comentarios:
    st.header("💬 LIBRO DE VISITAS / GUESTBOOK 🐝")
    st.write("¡Déjame un mensaje en el panal como en los 2000s!")

    # Historial de comentarios
    if 'comentarios' not in st.session_state:
        st.session_state['comentarios'] = [
            {"nombre": "RetroFan2000", "fecha": "2026-09-28", "mensaje": "¡Amé la estética Y2K de la foto de perfil y la página!"},
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
