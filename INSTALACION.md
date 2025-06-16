# 🛠️ Guía de Instalación - Analizador de Sentimientos

## 📋 Requisitos del Sistema

### Requisitos Mínimos
- **Sistema Operativo**: Windows 10/11, macOS 10.14+, Ubuntu 18.04+
- **Python**: Versión 3.8 o superior
- **RAM**: Mínimo 4GB (recomendado 8GB)
- **Espacio en disco**: 500MB para dependencias
- **Conexión a Internet**: Para APIs de IA

### Cuentas Necesarias
- Cuenta de OpenAI (opcional): https://platform.openai.com/
- Cuenta de Groq (opcional): https://console.groq.com/
- **Nota**: Necesitas al menos una de las dos para que funcione la aplicación

## 🚀 Instalación Paso a Paso

### Paso 1: Verificar Python

```bash
# Verificar versión de Python
python --version

# Si no tienes Python o tienes una versión anterior a 3.8:
# Descarga desde: https://www.python.org/downloads/
```

### Paso 2: Descargar el Proyecto

**Opción A: Desde GitHub (recomendado)**
```bash
git clone https://github.com/tu-usuario/sentiment-analyzer.git
cd sentiment-analyzer
```

**Opción B: Descarga directa**
1. Descarga el archivo ZIP del proyecto
2. Extrae los archivos
3. Abre terminal en la carpeta extraída

### Paso 3: Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### Paso 4: Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt

# Si tienes problemas, instala una por una:
pip install streamlit>=1.28.0
pip install openai>=1.0.0
pip install groq>=0.4.0
pip install python-dotenv>=1.0.0
pip install pandas>=2.0.0
pip install plotly>=5.15.0
pip install requests>=2.31.0
```

### Paso 5: Configurar Variables de Entorno

1. **Localiza el archivo `.env`** en la carpeta del proyecto

2. **Abre el archivo `.env`** con un editor de texto

3. **Configura tus API Keys:**

```env
# OpenAI API Key (opcional pero recomendado)
OPENAI_API_KEY=tu_openai_api_key_aqui

# Groq API Key (opcional, alternativa gratuita)
GROQ_API_KEY=tu_groq_api_key_aqui
```

### Paso 6: Obtener API Keys

#### OpenAI (Recomendado para mejor precisión)

1. Ve a https://platform.openai.com/
2. Crea una cuenta o inicia sesión
3. Ve a "API Keys" en el menú lateral
4. Haz clic en "Create new secret key"
5. Copia la key y pégala en el archivo `.env`
6. **Importante**: Agrega créditos a tu cuenta en "Billing"

#### Groq (Gratuito con límites)

1. Ve a https://console.groq.com/
2. Crea una cuenta con Google/GitHub
3. Ve a "API Keys"
4. Crea una nueva key
5. Copia la key y pégala en el archivo `.env`

### Paso 7: Verificar Instalación

```bash
# Ejecutar verificación rápida
python -c "import streamlit; print('Streamlit OK')"
python -c "import openai; print('OpenAI OK')"
python -c "import groq; print('Groq OK')"
```

### Paso 8: Ejecutar la Aplicación

```bash
# Ejecutar la aplicación
streamlit run app.py
```

**¡La aplicación debería abrirse automáticamente en tu navegador!**
- URL local: http://localhost:8501

## 🔧 Solución de Problemas Comunes

### Error: "ModuleNotFoundError"

```bash
# Reinstalar dependencias
pip install --upgrade -r requirements.txt
```

### Error: "Python no reconocido"

**Windows:**
1. Agregar Python al PATH del sistema
2. Reiniciar terminal
3. Verificar con `python --version`

**macOS/Linux:**
```bash
# Usar python3 en lugar de python
python3 --version
python3 -m pip install -r requirements.txt
python3 -m streamlit run app.py
```

### Error: "No API Key configurada"

1. Verifica que el archivo `.env` existe
2. Verifica que las API keys están correctamente escritas
3. Reinicia la aplicación

### Error: "API Key inválida"

1. Verifica que copiaste la key completa
2. Verifica que la cuenta tiene créditos (OpenAI)
3. Genera una nueva API key

### Error: "Puerto 8501 ocupado"

```bash
# Usar puerto diferente
streamlit run app.py --server.port 8502
```

### La aplicación se abre pero no responde

1. Verifica tu conexión a internet
2. Verifica que las API keys son válidas
3. Revisa la consola por errores

## 🚀 Optimización del Rendimiento

### Para mejor rendimiento:

```bash
# Instalar versión optimizada de pandas
pip install --upgrade pandas

# Limpiar caché de Streamlit
streamlit cache clear
```

## 🔄 Actualización

```bash
# Actualizar dependencias
pip install --upgrade -r requirements.txt

# Limpiar caché después de actualizar
streamlit cache clear
```

## 🐳 Instalación con Docker (Avanzado)

```bash
# Construir imagen
docker build -t sentiment-analyzer .

# Ejecutar contenedor
docker run -p 8501:8501 sentiment-analyzer
```

## 📱 Acceso desde Dispositivos Móviles

Una vez ejecutando localmente:
1. Encuentra tu IP local: `ipconfig` (Windows) o `ifconfig` (Mac/Linux)
2. Accede desde móvil: `http://TU_IP:8501`

## ☁️ Deployment en Streamlit Cloud

1. Sube tu código a GitHub
2. Ve a https://share.streamlit.io/
3. Conecta tu repositorio
4. Configura variables de entorno en "Advanced settings"
5. Deploy automático

## 💡 Consejos Adicionales

### Para Desarrollo:
```bash
# Ejecutar en modo debug
streamlit run app.py --logger.level debug
```

### Para Producción:
```bash
# Ejecutar optimizado
streamlit run app.py --server.runOnSave false
```

### Configuración Avanzada:
Crear archivo `.streamlit/config.toml`:
```toml
[server]
port = 8501
enableCORS = false

[theme]
primaryColor = "#1976D2"
backgroundColor = "#FFFFFF"
```

## 📞 Soporte

Si tienes problemas:

1. **Revisa esta guía** completa
2. **Consulta el README.md** para más detalles
3. **Revisa los logs** en la consola
4. **Contacta al desarrollador** con detalles del error

---

✅ **¡Instalación Completa!** Ya puedes empezar a analizar sentimientos con IA.