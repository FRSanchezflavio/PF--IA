"""
Aplicación principal de análisis de sentimientos con IA
"""
import streamlit as st
import sys
import os
from pathlib import Path

# Agregar el directorio raíz al path para importaciones
root_dir = Path(__file__).parent
sys.path.append(str(root_dir))

# Importar módulos locales
try:
    from utils.ai_analyzer import analyzer
    from components.ui_components import (
        render_header,
        render_description,
        render_sidebar,
        render_input_section,
        render_provider_selection,
        render_analysis_results,
        render_footer,
        render_error_message,
        render_success_message,
        show_loading_animation
    )
    from config.settings import APP_TITLE, APP_DESCRIPTION
except ImportError as e:
    st.error(f"Error importando módulos: {e}")
    st.stop()

# Configuración de la página
st.set_page_config(
    page_title="Analizador de Sentimientos IA",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/tu-usuario/sentiment-analyzer',
        'Report a bug': 'https://github.com/tu-usuario/sentiment-analyzer/issues',
        'About': """
        # Analizador de Sentimientos con IA
        
        Esta aplicación utiliza Inteligencia Artificial para analizar el sentimiento 
        de reseñas de productos, proporcionando insights valiosos para mejorar 
        la experiencia del cliente.
        
        **Desarrollado con:**
        - Streamlit
        - OpenAI GPT-3.5
        - Groq Llama-3
        - Python
        """
    }
)

# CSS personalizado
st.markdown("""
<style>
    /* Estilos generales */
    .main {
        padding-top: 2rem;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Estilos para botones */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Estilos para inputs */
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #e1e5e9;
        transition: border-color 0.3s ease;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Estilos para selectbox */
    .stSelectbox > div > div {
        border-radius: 10px;
    }
    
    /* Animación de carga */
    .loading-spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    
    .spinner {
        width: 40px;
        height: 40px;
        border: 4px solid #f3f3f3;
        border-top: 4px solid #667eea;
        border-radius: 50%;
        animation: spin 1s linear infinite;
    }
    
    @keyframes spin {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    /* Estilos para métricas */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
        border: 1px solid #e1e5e9;
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Función principal de la aplicación"""
    
    # Inicializar session state
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'analysis_count' not in st.session_state:
        st.session_state.analysis_count = 0
    if 'last_review' not in st.session_state:
        st.session_state.last_review = ""
    
    # Renderizar sidebar
    render_sidebar()
    
    # Renderizar header y descripción
    render_header()
    render_description()
    
    # Verificar proveedores disponibles
    available_providers = analyzer.get_available_providers()
    
    if not available_providers:
        st.error("""
        🚨 **Configuración Requerida**
        
        Para usar esta aplicación, necesitas configurar al menos una API key:
        
        1. **OpenAI**: Obtén tu API key en https://platform.openai.com/api-keys
        2. **Groq**: Obtén tu API key en https://console.groq.com/keys
        3. Agrega la API key al archivo `.env` en la carpeta del proyecto
        
        **Ejemplo del archivo .env:**
        ```
        OPENAI_API_KEY=tu_api_key_aqui
        GROQ_API_KEY=tu_api_key_aqui
        ```
        """)
        st.stop()
    
    # Mostrar proveedores disponibles
    st.success(f"✅ Proveedores disponibles: {', '.join(available_providers)}")
    
    # Sección de entrada
    st.markdown("---")
    review_text = render_input_section()
    
    # Verificar si hay ejemplo seleccionado
    if hasattr(st.session_state, 'ejemplo_seleccionado') and not review_text:
        review_text = st.session_state.ejemplo_seleccionado
    
    # Selección de proveedor
    provider = render_provider_selection()
    
    # Botón de análisis
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        analyze_button = st.button(
            "🚀 Analizar Sentimiento",
            type="primary",
            use_container_width=True,
            help="Haz clic para analizar el sentimiento de la reseña"
        )
    
    # Procesar análisis
    if analyze_button:
        if not review_text or not review_text.strip():
            st.warning("⚠️ Por favor, ingresa una reseña para analizar.")
            return
        
        # Mostrar loading
        with st.spinner("🤖 Analizando sentimiento... Por favor espera"):
            try:
                # Realizar análisis
                result = analyzer.analyze_sentiment(review_text, provider)
                
                # Guardar resultado
                st.session_state.analysis_result = result
                st.session_state.last_review = review_text
                
                # Mostrar mensaje de éxito
                render_success_message()
                
            except Exception as e:
                render_error_message(str(e))
                return
    
    # Mostrar resultados si existen
    if st.session_state.analysis_result:
        st.markdown("---")
        render_analysis_results(st.session_state.analysis_result)
        
        # Opción para nuevo análisis
        st.markdown("---")
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔄 Realizar Nuevo Análisis", use_container_width=True):
                st.session_state.analysis_result = None
                st.session_state.last_review = ""
                if hasattr(st.session_state, 'ejemplo_seleccionado'):
                    del st.session_state.ejemplo_seleccionado
                st.rerun()
    
    # Footer
    render_footer()

def check_requirements():
    """Verificar que todos los módulos necesarios estén instalados"""
    required_modules = [
        'streamlit',
        'openai',
        'groq',
        'plotly',
        'pandas',
        'python-dotenv'
    ]
    
    missing_modules = []
    for module in required_modules:
        try:
            __import__(module.replace('-', '_'))
        except ImportError:
            missing_modules.append(module)
    
    if missing_modules:
        st.error(f"""
        🚨 **Módulos Faltantes**
        
        Los siguientes módulos no están instalados:
        {', '.join(missing_modules)}
        
        **Para instalar:**
        ```bash
        pip install {' '.join(missing_modules)}
        ```
        
        O ejecuta:
        ```bash
        pip install -r requirements.txt
        ```
        """)
        return False
    
    return True

if __name__ == "__main__":
    # Verificar requisitos
    if check_requirements():
        main()
    else:
        st.stop()