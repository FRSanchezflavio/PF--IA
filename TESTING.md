# 🧪 Guía de Testing - Analizador de Sentimientos

## 📋 Tipos de Testing

### 1. Testing Manual
- Pruebas de interfaz de usuario
- Pruebas de funcionalidad
- Pruebas de casos extremos

### 2. Testing Automático
- Tests unitarios
- Tests de integración
- Tests de rendimiento

## 🔍 Testing Manual

### Pre-requisitos
- Aplicación instalada y funcionando
- Al menos una API key configurada
- Navegador web moderno

### Casos de Prueba Básicos

#### ✅ Caso 1: Reseña Positiva
**Entrada:**
```
"Este producto es increíble! La calidad es excelente, llegó súper rápido y el empaque era perfecto. El servicio al cliente fue muy atento cuando tuve una consulta. Definitivamente lo recomiendo 100% y volveré a comprar. ¡5 estrellas!"
```

**Resultado Esperado:**
- Sentimiento: Positivo
- Puntuación: 8-10
- Aspectos positivos identificados
- Recomendaciones relevantes

#### ✅ Caso 2: Reseña Negativa
**Entrada:**
```
"Terrible experiencia. El producto llegó dañado, la calidad es pésima y no funciona como se anuncia. El servicio al cliente es horrible, no responden. Perdí mi dinero. No lo recomiendo para nada. Muy decepcionado."
```

**Resultado Esperado:**
- Sentimiento: Negativo
- Puntuación: 1-3
- Aspectos negativos identificados
- Recomendaciones para mejorar

#### ✅ Caso 3: Reseña Neutral
**Entrada:**
```
"El producto está bien, nada especial. Cumple con lo básico pero podría ser mejor. El precio es justo. La entrega fue en tiempo normal. Es aceptable pero hay mejores opciones en el mercado."
```

**Resultado Esperado:**
- Sentimiento: Neutral
- Puntuación: 4-6
- Balance entre aspectos positivos y negativos

### Casos de Prueba Avanzados

#### 🔬 Caso 4: Texto Mixto (Positivo-Negativo)
**Entrada:**
```
"Me encanta el diseño y la funcionalidad del producto, realmente es innovador. Sin embargo, el precio me parece muy alto para lo que ofrece y la batería dura menos de lo esperado. En general, está bien pero con reservas."
```

#### 🔬 Caso 5: Texto Corto
**Entrada:**
```
"Bueno"
```

#### 🔬 Caso 6: Texto Largo
**Entrada:**
```
[Texto de 500+ palabras con múltiples aspectos]
```

#### 🔬 Caso 7: Texto en Inglés
**Entrada:**
```
"This product is amazing! Great quality and fast shipping. Highly recommended!"
```

#### 🔬 Caso 8: Texto con Emojis
**Entrada:**
```
"Excelente producto! 😍 Llegó rápido 🚚 y la calidad es top 👌 Lo recomiendo 100% ⭐⭐⭐⭐⭐"
```

### Casos de Prueba de Error

#### ❌ Caso 9: Texto Vacío
**Entrada:** [Campo vacío]
**Resultado Esperado:** Mensaje de error apropiado

#### ❌ Caso 10: Solo Espacios
**Entrada:** "     "
**Resultado Esperado:** Mensaje de error apropiado

#### ❌ Caso 11: Caracteres Especiales
**Entrada:** "!@#$%^&*()_+{}[]"
**Resultado Esperado:** Manejo apropiado o mensaje de error

## 🤖 Testing de Proveedores de IA

### Comparación OpenAI vs Groq

#### Test de Consistencia
1. Usar la misma reseña con ambos proveedores
2. Comparar resultados
3. Verificar coherencia en el análisis

#### Test de Velocidad
1. Medir tiempo de respuesta de cada proveedor
2. Documentar diferencias
3. Verificar que ambos funcionan

#### Test de Disponibilidad
1. Probar con API key válida
2. Probar con API key inválida
3. Probar sin API key
4. Verificar mensajes de error apropiados

## 📊 Checklist de Testing de UI

### Header y Navegación
- [ ] Título se muestra correctamente
- [ ] Descripción es clara y atractiva
- [ ] Sidebar funciona correctamente
- [ ] Información de "Cómo funciona" es visible

### Formulario de Entrada
- [ ] Área de texto acepta input
- [ ] Contador de caracteres funciona
- [ ] Ejemplos se cargan correctamente
- [ ] Botones de ejemplo funcionan
- [ ] Selección de proveedor funciona

### Procesamiento
- [ ] Botón "Analizar" responde
- [ ] Loading spinner aparece
- [ ] Mensajes de estado son claros
- [ ] Manejo de errores funciona

### Resultados
- [ ] Métricas se muestran correctamente
- [ ] Gráficos se renderizan
- [ ] Aspectos positivos/negativos aparecen
- [ ] Recomendaciones son relevantes
- [ ] Resumen es coherente

### Funcionalidades Adicionales
- [ ] Contador de análisis funciona
- [ ] Botón "Nuevo análisis" funciona
- [ ] Responsive design en móvil
- [ ] Colores y estilos correctos

## 🛠️ Testing Técnico

### Verificación de Dependencias

```bash
# Verificar instalación de módulos
python -c "import streamlit; print('✅ Streamlit OK')"
python -c "import openai; print('✅ OpenAI OK')"
python -c "import groq; print('✅ Groq OK')"
python -c "import plotly; print('✅ Plotly OK')"
python -c "import pandas; print('✅ Pandas OK')"
```

### Testing de Configuración

```bash
# Verificar archivo .env
python -c "
import os
from dotenv import load_dotenv
load_dotenv()
print('OpenAI Key:', '✅ Configurada' if os.getenv('OPENAI_API_KEY') else '❌ Faltante')
print('Groq Key:', '✅ Configurada' if os.getenv('GROQ_API_KEY') else '❌ Faltante')
"
```

### Testing de Conectividad

```python
# Test de conectividad OpenAI
import openai
import os
from dotenv import load_dotenv

load_dotenv()
if os.getenv('OPENAI_API_KEY'):
    try:
        openai.api_key = os.getenv('OPENAI_API_KEY')
        # Test básico
        print("✅ OpenAI conectado correctamente")
    except Exception as e:
        print(f"❌ Error OpenAI: {e}")
```

## 📈 Testing de Rendimiento

### Métricas a Medir
- **Tiempo de respuesta**: < 10 segundos típico
- **Memoria utilizada**: < 100MB
- **Carga de CPU**: Moderada durante análisis
- **Tiempo de inicio**: < 5 segundos

### Herramientas de Monitoreo

```bash
# Monitorear recursos
htop  # Linux/Mac
# o usar Task Manager en Windows

# Timing del análisis
time streamlit run app.py
```

## 🔄 Testing de Regresión

### Cada vez que hagas cambios:

1. **Verificar funcionalidad básica**
   - [ ] La app inicia correctamente
   - [ ] Análisis básico funciona
   - [ ] UI se ve correctamente

2. **Probar casos críticos**
   - [ ] Texto muy largo
   - [ ] Texto muy corto
   - [ ] Caracteres especiales
   - [ ] Múltiples análisis seguidos

3. **Verificar integraciones**
   - [ ] OpenAI funciona
   - [ ] Groq funciona
   - [ ] Gráficos se generan
   - [ ] Session state persiste

## 📋 Reporte de Testing

### Template de Reporte

```markdown
## Reporte de Testing - [Fecha]

### Resumen Ejecutivo
- Tests ejecutados: X/Y
- Tests exitosos: X
- Tests fallidos: Y
- Bugs encontrados: Z

### Detalles por Categoría

#### Funcionalidad Básica
- [✅/❌] Análisis de reseñas positivas
- [✅/❌] Análisis de reseñas negativas
- [✅/❌] Análisis de reseñas neutrales

#### Integración de IA
- [✅/❌] OpenAI responde correctamente
- [✅/❌] Groq responde correctamente
- [✅/❌] Manejo de errores de API

#### Interfaz de Usuario
- [✅/❌] Carga correcta de componentes
- [✅/❌] Navegación fluida
- [✅/❌] Responsive design

### Bugs Encontrados
1. [Descripción del bug]
   - Severidad: Alta/Media/Baja
   - Pasos para reproducir
   - Comportamiento esperado vs actual

### Recomendaciones
- [Lista de mejoras sugeridas]

### Conclusión
[Resumen general del estado de la aplicación]
```

## 🚀 Testing en Producción

### Pre-deployment Checklist
- [ ] Todos los tests manuales pasan
- [ ] Variables de entorno configuradas
- [ ] Dependencias actualizadas
- [ ] Documentación actualizada
- [ ] Sin errores en consola

### Post-deployment Testing
- [ ] App carga en URL de producción
- [ ] Funcionalidad básica opera
- [ ] APIs responden correctamente
- [ ] Logs no muestran errores críticos

## 🎯 Mejores Prácticas

### Durante el Testing
1. **Documenta todo**: Registra cada test y resultado
2. **Varía los inputs**: Prueba casos diversos
3. **Verifica edge cases**: Casos límite y extremos
4. **Prueba en diferentes navegadores**: Chrome, Firefox, Safari
5. **Testa en dispositivos móviles**: Responsive design

### Automatización Futura
- Implementar pytest para tests automáticos
- CI/CD con GitHub Actions
- Monitoring continuo en producción
- Tests de carga para escalabilidad

---

🎯 **Testing completado = App lista para producción!**