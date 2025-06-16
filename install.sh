#!/bin/bash

echo "========================================"
echo "  INSTALADOR - Analizador de Sentimientos"
echo "========================================"
echo

echo "Verificando Python..."
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "[ERROR] Python no está instalado."
        echo
        echo "Por favor instala Python 3.8 o superior:"
        echo "- Ubuntu/Debian: sudo apt update && sudo apt install python3 python3-pip"
        echo "- macOS: brew install python3"
        echo "- O descarga desde: https://www.python.org/downloads/"
        echo
        exit 1
    else
        PYTHON_CMD="python"
    fi
else
    PYTHON_CMD="python3"
fi

echo "[OK] Python encontrado"
$PYTHON_CMD --version

echo
echo "Instalando dependencias..."
$PYTHON_CMD -m pip install --upgrade pip
$PYTHON_CMD -m pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "[ERROR] Falló la instalación de dependencias"
    echo
    echo "Intenta instalar manualmente:"
    echo "$PYTHON_CMD -m pip install streamlit openai groq python-dotenv pandas plotly requests"
    echo
    exit 1
fi

echo
echo "[OK] Dependencias instaladas correctamente"
echo

echo "Verificando instalación..."
$PYTHON_CMD -c "import streamlit; print('✓ Streamlit OK')" 2>/dev/null
$PYTHON_CMD -c "import openai; print('✓ OpenAI OK')" 2>/dev/null
$PYTHON_CMD -c "import groq; print('✓ Groq OK')" 2>/dev/null
$PYTHON_CMD -c "import plotly; print('✓ Plotly OK')" 2>/dev/null

echo
echo "========================================"
echo "  INSTALACIÓN COMPLETADA"
echo "========================================"
echo
echo "SIGUIENTE PASO:"
echo "1. Configura tus API keys en el archivo .env"
echo "2. Ejecuta: streamlit run app.py"
echo
