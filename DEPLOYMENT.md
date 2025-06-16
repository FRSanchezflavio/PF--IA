# 🚀 Guía de Deployment - Streamlit Cloud

## 📋 Requisitos Previos

- [x] Código funcionando localmente
- [x] Cuenta de GitHub
- [x] Cuenta de Streamlit (free)
- [x] API keys configuradas

## 🌐 Paso a Paso - Streamlit Cloud

### 1. Preparar el Repositorio

#### Crear repositorio en GitHub:
1. Ve a https://github.com/new
2. Nombre: `sentiment-analyzer-ai`
3. Descripción: `Analizador de Sentimientos con IA - Proyecto Final`
4. Público o Privado (recomendado: Público para portafolio)
5. Crear repositorio

#### Subir código:
```bash
# Inicializar git (si no está inicializado)
git init

# Agregar archivos
git add .

# Primer commit
git commit -m "🎉 Proyecto inicial: Analizador de Sentimientos con IA"

# Conectar con GitHub
git remote add origin https://github.com/TU-USUARIO/sentiment-analyzer-ai.git

# Subir código
git push -u origin main
```

### 2. Configurar Streamlit Cloud

#### Acceso a Streamlit Cloud:
1. Ve a https://share.streamlit.io/
2. Inicia sesión con GitHub
3. Autoriza la conexión

#### Crear nueva app:
1. Click en "New app"
2. Selecciona tu repositorio `sentiment-analyzer-ai`
3. Branch: `main`
4. Main file path: `app.py`
5. App URL: `sentiment-analyzer-[tu-nombre]` (personalizable)

### 3. Configurar Variables de Entorno

#### En Streamlit Cloud:
1. En la configuración de tu app
2. Ve a "Advanced settings"
3. En "Secrets", agrega:

```toml
[secrets]
OPENAI_API_KEY = "tu_openai_api_key_real"
GROQ_API_KEY = "tu_groq_api_key_real"
```

**⚠️ IMPORTANTE**: Usa tus API keys reales, no los placeholders

### 4. Modificar Código para Producción

#### Actualizar `config/settings.py`:
```python
# Agregar después de las importaciones existentes
import streamlit as st

# Actualizar la carga de variables de entorno
# Para producción (Streamlit Cloud)
if hasattr(st, 'secrets'):
    OPENAI_API_KEY = st.secrets.get("OPENAI_API_KEY")
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
else:
    # Para desarrollo local
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
```

### 5. Deploy y Verificación

#### Deploy automático:
1. Streamlit Cloud detectará cambios automáticamente
2. El deployment toma 2-5 minutos
3. Recibirás notificaciones de estado

#### Verificar deployment:
- [ ] App carga correctamente
- [ ] No hay errores en los logs
- [ ] Funcionalidad básica opera
- [ ] APIs responden correctamente

## 🔧 Solución de Problemas

### Error: "Module not found"
```bash
# Verificar requirements.txt completo
streamlit>=1.28.0
openai>=1.0.0
groq>=0.4.0
python-dotenv>=1.0.0
pandas>=2.0.0
plotly>=5.15.0
requests>=2.31.0
```

### Error: "API Key not configured"
1. Verifica que las secrets estén configuradas correctamente
2. Verifica la sintaxis en el archivo secrets
3. Redeploy la aplicación

### Error: "Import error"
1. Verifica la estructura de archivos
2. Asegúrate de que `__init__.py` existen en carpetas de módulos
3. Verifica imports relativos vs absolutos

## 📱 Alternativas de Deployment

### Heroku (Gratis con limitaciones)
```bash
# Crear Procfile
echo "web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0" > Procfile

# Deploy a Heroku
heroku create sentiment-analyzer-app
git push heroku main
```

### Railway (Fácil y rápido)
1. Ve a https://railway.app/
2. Conecta GitHub
3. Deploy automático

### Render (Alternativa gratuita)
1. Ve a https://render.com/
2. Conecta repositorio
3. Configura como Web Service

## 🔒 Mejores Prácticas de Seguridad

### Nunca hardcodees API keys:
❌ **MAL:**
```python
OPENAI_API_KEY = "sk-abcd1234..."
```

✅ **BIEN:**
```python
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
```

### Usa `.gitignore`:
```gitignore
.env
__pycache__/
*.pyc
.streamlit/secrets.toml
```

## 🎯 Optimización para Producción

### Caché para mejor rendimiento:
```python
@st.cache_data
def load_model():
    # Cargar modelo pesado
    pass

@st.cache_resource
def init_api_client():
    # Inicializar cliente API
    pass
```

### Manejo de errores robusto:
```python
try:
    result = analyze_sentiment(text)
    st.success("Análisis completado")
except Exception as e:
    st.error(f"Error: {str(e)}")
    logger.error(f"Error en producción: {e}")
```

## 📊 Monitoreo Post-Deployment

### Métricas a monitorear:
- [ ] Tiempo de respuesta
- [ ] Errores de API
- [ ] Uso de recursos
- [ ] Satisfacción del usuario

### Logs importantes:
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# En funciones críticas
logger.info(f"Análisis iniciado para texto de {len(text)} caracteres")
logger.error(f"Error en API: {str(e)}")
```

## 🔄 Pipeline de CI/CD

### GitHub Actions (opcional):
```yaml
# .github/workflows/deploy.yml
name: Test and Deploy

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m pytest tests/
```

## 📋 Checklist Final

### Pre-deployment:
- [ ] Código probado localmente
- [ ] Requirements.txt actualizado
- [ ] Variables de entorno configuradas
- [ ] Repositorio GitHub actualizado
- [ ] Documentación completa

### Post-deployment:
- [ ] App accesible públicamente
- [ ] Funcionalidad básica verificada
- [ ] No errores en logs
- [ ] APIs funcionando correctamente
- [ ] URL compartida funcionando

## 🎉 ¡Tu App Está Lista!

### URLs finales:
- **Aplicación**: https://sentiment-analyzer-[tu-nombre].streamlit.app/
- **Código fuente**: https://github.com/[tu-usuario]/sentiment-analyzer-ai
- **Documentación**: Incluida en el repositorio

### Para compartir:
1. Copia la URL de tu app
2. Prueba en navegador incógnito
3. Comparte con confianza

---

🚀 **¡Felicitaciones! Tu aplicación con IA está desplegada y lista para el mundo!**
