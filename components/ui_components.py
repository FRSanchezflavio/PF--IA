"""
Componentes de interfaz de usuario para la aplicación
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Dict, List
from config.settings import COLORS, SIDEBAR_INFO

def render_header():
    """Renderizar el header de la aplicación"""
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0;">
        <h1 style="color: #1976D2; font-size: 3rem; margin-bottom: 0;">
            🎯 Analizador de Sentimientos
        </h1>
        <h2 style="color: #424242; font-size: 1.5rem; font-weight: 300;">
            Análisis Inteligente de Reseñas de Productos
        </h2>
        <hr style="width: 50%; margin: 2rem auto; border: 2px solid #1976D2;">
    </div>
    """, unsafe_allow_html=True)

def render_description():
    """Renderizar la descripción de la aplicación"""
    st.markdown("""
    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                padding: 2rem; border-radius: 10px; color: white; margin: 2rem 0;">
        <h3 style="margin-top: 0; color: white;">🚀 Potencia tu Negocio con IA</h3>
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Esta aplicación utiliza <strong>Inteligencia Artificial avanzada</strong> para analizar 
            el sentimiento de reseñas de productos, proporcionando insights valiosos sobre la 
            percepción del cliente que te ayudarán a <strong>mejorar tu estrategia comercial</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_sidebar():
    """Renderizar la barra lateral con información"""
    with st.sidebar:
        st.markdown(f"""
        <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #1976D2; margin-top: 0;">{SIDEBAR_INFO['title']}</h3>
            {SIDEBAR_INFO['content']}
        </div>
        """, unsafe_allow_html=True)
        
        # Información adicional
        st.markdown("---")
        st.markdown("### 📊 Estadísticas de Uso")
        if 'analysis_count' not in st.session_state:
            st.session_state.analysis_count = 0
        
        st.metric("Análisis Realizados", st.session_state.analysis_count)
        
        # Información del desarrollador
        st.markdown("---")
        st.markdown("""
        ### 👨‍💻 Desarrollado por
        **Proyecto Final - Curso de IA**  
        *Integración de IA en Aplicaciones Web*
        """)

def render_input_section():
    """Renderizar la sección de entrada de datos"""
    st.markdown("### 📝 Ingresa la Reseña del Producto")
    
    # Crear tabs para diferentes formas de entrada
    tab1, tab2 = st.tabs(["✍️ Escribir Reseña", "📋 Ejemplos"])
    
    with tab1:
        review_text = st.text_area(
            "Escribe o pega aquí la reseña del producto que quieres analizar:",
            height=150,
            placeholder="Ejemplo: 'Este producto es increíble, la calidad es excelente y llegó muy rápido. Lo recomiendo 100%'",
            help="Puedes incluir reseñas en español o inglés"
        )
        
        # Contador de caracteres
        char_count = len(review_text) if review_text else 0
        st.caption(f"Caracteres: {char_count}")
    
    with tab2:
        st.markdown("#### 💡 Ejemplos de Reseñas")
        
        ejemplos = {
            "Reseña Positiva": "Este producto superó mis expectativas. La calidad es excelente, el envío fue rápido y el servicio al cliente muy atento. Definitivamente lo recomiendo y volveré a comprar.",
            "Reseña Negativa": "Muy decepcionado con esta compra. El producto llegó dañado, la calidad es pésima y el servicio al cliente no respondió a mis quejas. No lo recomiendo para nada.",
            "Reseña Neutral": "El producto está bien, cumple con lo básico. El precio es justo aunque podría mejorar en algunos aspectos. El envío fue dentro del tiempo esperado."
        }
        
        for titulo, ejemplo in ejemplos.items():
            if st.button(f"Usar: {titulo}", key=f"ejemplo_{titulo}"):
                st.session_state.ejemplo_seleccionado = ejemplo
                st.rerun()
        
        # Si hay un ejemplo seleccionado, mostrarlo
        if hasattr(st.session_state, 'ejemplo_seleccionado'):
            st.text_area(
                "Ejemplo seleccionado:",
                value=st.session_state.ejemplo_seleccionado,
                height=100,
                disabled=True
            )
            if st.button("Usar este ejemplo"):
                review_text = st.session_state.ejemplo_seleccionado
    
    return review_text

def render_provider_selection():
    """Renderizar la selección de proveedor de IA"""
    st.markdown("### 🤖 Selecciona el Proveedor de IA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        provider = st.selectbox(
            "Elige el modelo de IA:",
            options=["OpenAI", "Groq"],
            help="OpenAI GPT-3.5: Más preciso | Groq: Más rápido"
        )
    
    with col2:
        st.info(f"""
        **{'🎯 OpenAI GPT-3.5' if provider == 'OpenAI' else '⚡ Groq Llama-3'}**
        
        {'Análisis más detallado y preciso' if provider == 'OpenAI' else 'Procesamiento ultra-rápido'}
        """)
    
    return provider.lower()

def render_analysis_results(analysis_result: Dict):
    """Renderizar los resultados del análisis"""
    if not analysis_result:
        return
    
    st.markdown("## 📊 Resultados del Análisis")
    
    # Métricas principales
    col1, col2, col3 = st.columns(3)
    
    sentimiento = analysis_result.get('sentimiento_general', 'No disponible')
    puntuacion = analysis_result.get('puntuacion', 0)
    
    # Determinar color basado en sentimiento
    if sentimiento.lower() == 'positivo':
        color = COLORS['positive']
        emoji = "😊"
    elif sentimiento.lower() == 'negativo':
        color = COLORS['negative']
        emoji = "😞"
    else:
        color = COLORS['neutral']
        emoji = "😐"
    
    with col1:
        st.markdown(f"""
        <div style="background: {color}20; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: {color}; margin: 0;">{emoji} {sentimiento}</h3>
            <p style="margin: 0;">Sentimiento General</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: #1976D220; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: #1976D2; margin: 0;">⭐ {puntuacion}/10</h3>
            <p style="margin: 0;">Puntuación</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        # Calcular nivel de confianza basado en la puntuación
        if puntuacion >= 8 or puntuacion <= 2:
            confianza = "Alta"
            confianza_color = COLORS['positive']
        elif puntuacion >= 6 or puntuacion <= 4:
            confianza = "Media"
            confianza_color = COLORS['neutral']
        else:
            confianza = "Baja"
            confianza_color = COLORS['negative']
        
        st.markdown(f"""
        <div style="background: {confianza_color}20; padding: 1rem; border-radius: 10px; text-align: center;">
            <h3 style="color: {confianza_color}; margin: 0;">🎯 {confianza}</h3>
            <p style="margin: 0;">Confianza</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Gráfico de puntuación
    render_score_chart(puntuacion)
    
    # Aspectos detallados
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### ✅ Aspectos Positivos")
        aspectos_positivos = analysis_result.get('aspectos_positivos', [])
        if aspectos_positivos:
            for aspecto in aspectos_positivos:
                st.markdown(f"• {aspecto}")
        else:
            st.info("No se identificaron aspectos positivos específicos")
    
    with col2:
        st.markdown("### ❌ Aspectos Negativos")
        aspectos_negativos = analysis_result.get('aspectos_negativos', [])
        if aspectos_negativos:
            for aspecto in aspectos_negativos:
                st.markdown(f"• {aspecto}")
        else:
            st.info("No se identificaron aspectos negativos específicos")
    
    # Recomendaciones
    st.markdown("### 💡 Recomendaciones")
    recomendaciones = analysis_result.get('recomendaciones', [])
    if recomendaciones:
        for i, recomendacion in enumerate(recomendaciones, 1):
            st.markdown(f"**{i}.** {recomendacion}")
    else:
        st.info("No hay recomendaciones específicas disponibles")
    
    # Resumen ejecutivo
    st.markdown("### 📋 Resumen Ejecutivo")
    resumen = analysis_result.get('resumen', 'No disponible')
    st.markdown(f"""
    <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1976D2;">
        <p style="margin: 0; font-size: 1.1rem; line-height: 1.6;">{resumen}</p>
    </div>
    """, unsafe_allow_html=True)

def render_score_chart(score: int):
    """Renderizar gráfico de puntuación"""
    st.markdown("### 📈 Visualización de Puntuación")
    
    # Crear gráfico de gauge
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Puntuación de Sentimiento"},
        gauge={
            'axis': {'range': [None, 10]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 3], 'color': COLORS['negative']},
                {'range': [3, 7], 'color': COLORS['neutral']},
                {'range': [7, 10], 'color': COLORS['positive']}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': score
            }
        }
    ))
    
    fig.update_layout(height=300)
    st.plotly_chart(fig, use_container_width=True)

def render_footer():
    """Renderizar el footer de la aplicación"""
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #666;">
        <p>🚀 <strong>Analizador de Sentimientos con IA</strong> | Desarrollado con ❤️ usando Streamlit</p>
        <p><small>© 2024 - Proyecto Final Curso de IA | Integración de IA en Aplicaciones Web</small></p>
    </div>
    """, unsafe_allow_html=True)

def show_loading_animation():
    """Mostrar animación de carga"""
    return st.empty()

def render_error_message(error: str):
    """Renderizar mensaje de error"""
    st.error(f"""
    🚨 **Error en el Análisis**
    
    {error}
    
    **Posibles soluciones:**
    - Verifica que hayas configurado correctamente las API keys
    - Asegúrate de que el texto no esté vacío
    - Intenta con el otro proveedor de IA
    """)

def render_success_message():
    """Renderizar mensaje de éxito"""
    st.success("✅ **¡Análisis completado exitosamente!** Los resultados se muestran a continuación.")
    
    # Incrementar contador
    st.session_state.analysis_count += 1