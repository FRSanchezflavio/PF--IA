#!/bin/bash

echo "========================================"
echo "  EJECUTAR - Analizador de Sentimientos"
echo "========================================"
echo

echo "Verificando configuración..."

if [ ! -f .env ]; then
    echo "[ADVERTENCIA] Archivo .env no encontrado"
    echo
    echo "Creando archivo .env básico..."
    cat > .env << EOL
# Variables de entorno para la aplicación
# Obtén tu API key desde: https://platform.openai.com/api-keys
OPENAI_API_KEY=tu_openai_api_key_aqui

# Obtén tu API key desde: https://console.groq.com/keys
GROQ_API_KEY=tu_groq_api_key_aqui
EOL
    echo
    echo "[IMPORTANTE] Edita el archivo .env y agrega tus API keys reales"
    echo
fi

# Detectar comando Python
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
elif command -v python &> /dev/null; then
    PYTHON_CMD="python"
else
    echo "[ERROR] Python no encontrado"
    exit 1
fi

echo "Verificando dependencias..."
$PYTHON_CMD -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[ERROR] Dependencias no instaladas"
    echo "Ejecuta primero: ./install.sh"
    exit 1
fi

echo "[OK] Todo listo!"
echo
echo "Iniciando aplicación..."
echo "La aplicación se abrirá automáticamente en tu navegador."
echo "Para detener la aplicación, presiona Ctrl+C"
echo

$PYTHON_CMD -m streamlit run app.py
