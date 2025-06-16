@echo off
echo ========================================
echo  EJECUTAR - Analizador de Sentimientos
echo ========================================
echo.

echo Verificando configuracion...

if not exist .env (
    echo [ADVERTENCIA] Archivo .env no encontrado
    echo.
    echo Creando archivo .env basico...
    echo # Variables de entorno para la aplicacion > .env
    echo # Obten tu API key desde: https://platform.openai.com/api-keys >> .env
    echo OPENAI_API_KEY=tu_openai_api_key_aqui >> .env
    echo. >> .env
    echo # Obten tu API key desde: https://console.groq.com/keys >> .env
    echo GROQ_API_KEY=tu_groq_api_key_aqui >> .env
    echo.
    echo [IMPORTANTE] Edita el archivo .env y agrega tus API keys reales
    echo.
)

echo Verificando dependencias...
python -c "import streamlit" 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Dependencias no instaladas
    echo Ejecuta primero: install.bat
    pause
    exit /b 1
)

echo [OK] Todo listo!
echo.
echo Iniciando aplicacion...
echo La aplicacion se abrira automaticamente en tu navegador.
echo Para detener la aplicacion, presiona Ctrl+C
echo.

python -m streamlit run app.py

pause
