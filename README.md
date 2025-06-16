# 🎯 Analizador de Sentimientos con IA

## 📋 Descripción del Proyecto

Esta aplicación web desarrollada con **Streamlit** integra **Inteligencia Artificial** para realizar análisis de sentimientos de reseñas de productos. Utiliza modelos avanzados como **OpenAI GPT-3.5** y **Groq Llama-3** para proporcionar insights valiosos sobre la percepción del cliente.

## 🎯 Problemática

Las empresas de e-commerce reciben miles de reseñas de productos diariamente, pero analizar manualmente cada una para extraer insights valiosos es:
- ⏰ **Consumidor de tiempo**: Análisis manual toma horas
- 📊 **Poco escalable**: Imposible procesar grandes volúmenes
- 🎯 **Subjetivo**: Diferentes analistas pueden tener interpretaciones distintas
- 💸 **Costoso**: Requiere personal dedicado para análisis

## 💡 Solución Propuesta

Nuestra aplicación automatiza el análisis de sentimientos utilizando IA avanzada para:

### ✨ Características Principales
- **Análisis Automático**: Procesamiento instantáneo de reseñas
- **Puntuación Numérica**: Escala del 1 al 10 para fácil interpretación
- **Aspectos Detallados**: Identificación de puntos positivos y negativos
- **Recomendaciones**: Sugerencias accionables para mejoras
- **Visualización**: Gráficos interactivos para mejor comprensión
- **Multi-proveedor**: Soporte para OpenAI y Groq

### 🎪 Beneficios
- ⚡ **Rapidez**: Análisis en segundos vs horas manuales
- 📈 **Escalabilidad**: Procesa miles de reseñas automáticamente
- 🎯 **Consistencia**: Análisis objetivo y estandarizado
- 💰 **Costo-efectivo**: Reduce necesidad de análisis manual
- 📊 **Insights Accionables**: Recomendaciones específicas para mejoras

## 🚀 Funcionalidades

### 🔍 Análisis de Sentimientos
- Detección automática de sentimiento (Positivo/Negativo/Neutral)
- Puntuación numérica de confianza
- Extracción de aspectos específicos mencionados

### 📊 Visualización de Resultados
- Gráficos interactivos con Plotly
- Métricas visuales de fácil interpretación
- Dashboard intuitivo y moderno

### 🤖 Integración de IA
- Soporte para múltiples proveedores (OpenAI, Groq)
- Prompts optimizados para análisis de reseñas
- Manejo inteligente de errores y fallbacks

## 🛠️ Tecnologías Utilizadas

- **Frontend**: Streamlit
- **IA**: OpenAI GPT-3.5, Groq Llama-3
- **Visualización**: Plotly
- **Backend**: Python 3.8+
- **Deployment**: Streamlit Cloud

## 📁 Estructura del Proyecto

```
PF-IA/
├── app.py                 # Aplicación principal
├── requirements.txt       # Dependencias
├── .env                  # Variables de entorno
├── README.md             # Documentación
├── INSTALACION.md        # Guía de instalación
├── TESTING.md            # Guía de testing
├── config/
│   ├── __init__.py
│   └── settings.py       # Configuraciones
├── components/
│   ├── __init__.py
│   └── ui_components.py  # Componentes de UI
├── utils/
│   ├── __init__.py
│   └── ai_analyzer.py    # Lógica de análisis
└── assets/               # Recursos estáticos
```

## ⚙️ Instalación

### Requisitos Previos
- Python 3.8 o superior
- Cuenta en OpenAI y/o Groq para APIs

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/tu-usuario/sentiment-analyzer.git
   cd sentiment-analyzer
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   - Copia el archivo `.env.example` a `.env`
   - Agrega tus API keys:
   ```env
   OPENAI_API_KEY=tu_openai_api_key
   GROQ_API_KEY=tu_groq_api_key
   ```

4. **Ejecutar la aplicación**
   ```bash
   streamlit run app.py
   ```

## 🔑 Configuración de API Keys

### OpenAI
1. Ve a https://platform.openai.com/api-keys
2. Crea una nueva API key
3. Agrega créditos a tu cuenta
4. Copia la key al archivo `.env`

### Groq
1. Ve a https://console.groq.com/keys
2. Crea una nueva API key
3. Copia la key al archivo `.env`

## 🧪 Testing

Para probar la aplicación:

```bash
# Ejecutar tests básicos
python -m pytest tests/

# Testing manual con ejemplos
streamlit run app.py
```

Ver [TESTING.md](TESTING.md) para guía detallada de pruebas.

## 📊 Prompt Inicial

### Prompt Principal
```
Eres un experto analista de sentimientos especializado en reseñas de productos.

Analiza la siguiente reseña de producto y proporciona:

1. **Sentimiento General**: Positivo, Negativo o Neutral
2. **Puntuación de Sentimiento**: Del 1 al 10 (1=muy negativo, 10=muy positivo)
3. **Aspectos Positivos**: Lista los aspectos que destacan positivamente
4. **Aspectos Negativos**: Lista los aspectos que se mencionan negativamente
5. **Recomendaciones**: Sugerencias para el vendedor basadas en el análisis
6. **Resumen**: Resumen ejecutivo del análisis

Formato de respuesta en JSON...
```

### Justificación del Prompt
- **Estructura clara**: Define exactamente qué información extraer
- **Formato JSON**: Permite parsing automático y consistente
- **Múltiples dimensiones**: No solo sentimiento, sino insights accionables
- **Escalable**: Funciona con diferentes tipos de productos

## 💰 Factibilidad Económica

### Costos Estimados (por 1000 análisis)

| Proveedor | Modelo | Costo Aproximado | Ventajas |
|-----------|--------|------------------|----------|
| OpenAI | GPT-3.5-turbo | $0.50 - $1.00 | Mayor precisión |
| Groq | Llama-3-8b | $0.10 - $0.30 | Mayor velocidad |

### ROI Estimado
- **Costo manual**: $50-100 por 1000 análisis (analista humano)
- **Costo IA**: $0.10-1.00 por 1000 análisis
- **Ahorro**: 98-99% de reducción en costos
- **Tiempo**: De horas a segundos

## 🌐 Deployment

### Streamlit Cloud
1. Conecta tu repositorio GitHub
2. Configura las variables de entorno en Streamlit Cloud
3. Deploy automático

### Alternativas
- **Heroku**: Para mayor control
- **Docker**: Para containerización
- **AWS/GCP**: Para escalabilidad empresarial

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Desarrollador

**[Tu Nombre]**  
*Proyecto Final - Curso de Inteligencia Artificial*  
*Integración de IA en Aplicaciones Web*

- 📧 Email: tu@email.com
- 🔗 LinkedIn: [tu-perfil](https://linkedin.com/in/tu-perfil)
- 🐙 GitHub: [tu-usuario](https://github.com/tu-usuario)

## 🎯 Próximas Mejoras

- [ ] Soporte para múltiples idiomas
- [ ] Análisis de emociones específicas
- [ ] Integración con APIs de e-commerce
- [ ] Dashboard de analytics avanzado
- [ ] Exportación de reportes PDF
- [ ] API REST para integración externa

---

⭐ **¡Si te gusta este proyecto, dale una estrella!** ⭐