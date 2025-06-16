"""
Configuraciones de la aplicación
"""
import os
from dotenv import load_dotenv

# Importar streamlit para secrets (producción)
try:
    import streamlit as st
    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False

# Cargar variables de entorno
load_dotenv()

# Configuraciones de API (compatibilidad desarrollo/producción)
if STREAMLIT_AVAILABLE and hasattr(st, 'secrets'):
    # Producción (Streamlit Cloud)
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
else:
    # Desarrollo local
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Configuraciones de la aplicación
APP_TITLE = "🎯 Analizador de Sentimientos - Reseñas de Productos"
APP_DESCRIPTION = """
Esta aplicación utiliza Inteligencia Artificial para analizar el sentimiento de reseñas de productos,
proporcionando insights valiosos sobre la percepción del cliente.
"""

# Configuraciones de modelos
OPENAI_MODEL = "gpt-3.5-turbo"
GROQ_MODEL = "llama3-8b-8192"

# Prompt principal para análisis de sentimientos
SENTIMENT_ANALYSIS_PROMPT = """
Eres un experto analista de sentimientos especializado en reseñas de productos.

Analiza la siguiente reseña de producto y proporciona:

1. **Sentimiento General**: Positivo, Negativo o Neutral
2. **Puntuación de Sentimiento**: Del 1 al 10 (1=muy negativo, 10=muy positivo)
3. **Aspectos Positivos**: Lista los aspectos que destacan positivamente
4. **Aspectos Negativos**: Lista los aspectos que se mencionan negativamente
5. **Recomendaciones**: Sugerencias para el vendedor basadas en el análisis
6. **Resumen**: Resumen ejecutivo del análisis

Formato de respuesta en JSON:
{
    "sentimiento_general": "string",
    "puntuacion": number,
    "aspectos_positivos": ["string"],
    "aspectos_negativos": ["string"],
    "recomendaciones": ["string"],
    "resumen": "string"
}

Reseña a analizar:
"""

# Configuraciones de UI
SIDEBAR_INFO = {
    "title": "ℹ️ Cómo Funciona",
    "content": """
    ### 🔍 Análisis Inteligente de Sentimientos
    
    **Características Principales:**
    - Análisis de sentimientos con IA avanzada
    - Puntuación numérica del 1 al 10
    - Identificación de aspectos positivos y negativos
    - Recomendaciones personalizadas
    - Visualización de resultados
    
    **Cómo Usar:**
    1. Ingresa la reseña del producto
    2. Selecciona el proveedor de IA
    3. Haz clic en "Analizar Sentimiento"
    4. Revisa los resultados detallados
    
    **Qué Esperar:**
    - Análisis completo en segundos
    - Insights accionables
    - Visualización clara de resultados
    """
}

# Configuraciones de colores
COLORS = {
    "positive": "#4CAF50",
    "negative": "#F44336",
    "neutral": "#FF9800",
    "primary": "#1976D2",
    "secondary": "#424242"
}