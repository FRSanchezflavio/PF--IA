@echo off
echo ========================================
echo  INSTALADOR - Analizador de Sentimientos
echo ========================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado.
    echo.
    echo Por favor:
    echo 1. Ve a https://www.python.org/downloads/
    echo 2. Descarga Python 3.8 o superior
    echo 3. Instala Python (asegurate de marcar "Add to PATH")
    echo 4. Reinicia la terminal y ejecuta este script nuevamente
    echo.
    pause
    exit /b 1
)

echo [OK] Python encontrado
python --version

echo.
echo Instalando dependencias...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo [ERROR] Fallo la instalacion de dependencias
    echo.
    echo Intenta instalar manualmente:
    echo python -m pip install streamlit openai groq python-dotenv pandas plotly requests
    echo.
    pause
    exit /b 1
)

echo.
echo [OK] Dependencias instaladas correctamente
echo.

echo Verificando instalacion...
python -c "import streamlit; print('✓ Streamlit OK')" 2>nul
python -c "import openai; print('✓ OpenAI OK')" 2>nul
python -c "import groq; print('✓ Groq OK')" 2>nul
python -c "import plotly; print('✓ Plotly OK')" 2>nul

echo.
echo ========================================
echo  INSTALACION COMPLETADA
echo ========================================
echo.
echo SIGUIENTE PASO:
echo 1. Configura tus API keys en el archivo .env
echo 2. Ejecuta: streamlit run app.py
echo.
pause
