"""
Módulo de análisis de sentimientos con IA
"""
import json
import logging
from typing import Dict, Optional, Union
import openai
from groq import Groq
from config.settings import (
    OPENAI_API_KEY, 
    GROQ_API_KEY, 
    OPENAI_MODEL, 
    GROQ_MODEL,
    SENTIMENT_ANALYSIS_PROMPT
)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SentimentAnalyzer:
    """
    Clase para análisis de sentimientos usando diferentes proveedores de IA
    """
    
    def __init__(self):
        """Inicializar el analizador con los clientes de IA"""
        self.openai_client = None
        self.groq_client = None
        
        # Inicializar OpenAI si hay API key
        if OPENAI_API_KEY:
            try:
                openai.api_key = OPENAI_API_KEY
                self.openai_client = openai
                logger.info("Cliente OpenAI inicializado correctamente")
            except Exception as e:
                logger.error(f"Error inicializando OpenAI: {str(e)}")
        
        # Inicializar Groq si hay API key
        if GROQ_API_KEY:
            try:
                self.groq_client = Groq(api_key=GROQ_API_KEY)
                logger.info("Cliente Groq inicializado correctamente")
            except Exception as e:
                logger.error(f"Error inicializando Groq: {str(e)}")
    
    def analyze_with_openai(self, review_text: str) -> Dict:
        """
        Analizar sentimiento usando OpenAI GPT
        
        Args:
            review_text (str): Texto de la reseña a analizar
            
        Returns:
            Dict: Resultado del análisis de sentimientos
        """
        if not self.openai_client or not OPENAI_API_KEY:
            raise ValueError("OpenAI no está configurado correctamente")
        
        try:
            prompt = f"{SENTIMENT_ANALYSIS_PROMPT}\n{review_text}"
            
            response = self.openai_client.chat.completions.create(
                model=OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "Eres un experto analista de sentimientos."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            # Extraer y parsear la respuesta
            content = response.choices[0].message.content
            logger.info(f"Respuesta de OpenAI recibida: {len(content)} caracteres")
            
            return self._parse_ai_response(content)
            
        except Exception as e:
            logger.error(f"Error en análisis con OpenAI: {str(e)}")
            raise Exception(f"Error procesando con OpenAI: {str(e)}")
    
    def analyze_with_groq(self, review_text: str) -> Dict:
        """
        Analizar sentimiento usando Groq
        
        Args:
            review_text (str): Texto de la reseña a analizar
            
        Returns:
            Dict: Resultado del análisis de sentimientos
        """
        if not self.groq_client or not GROQ_API_KEY:
            raise ValueError("Groq no está configurado correctamente")
        
        try:
            prompt = f"{SENTIMENT_ANALYSIS_PROMPT}\n{review_text}"
            
            response = self.groq_client.chat.completions.create(
                model=GROQ_MODEL,
                messages=[
                    {"role": "system", "content": "Eres un experto analista de sentimientos."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=1000
            )
            
            # Extraer y parsear la respuesta
            content = response.choices[0].message.content
            logger.info(f"Respuesta de Groq recibida: {len(content)} caracteres")
            
            return self._parse_ai_response(content)
            
        except Exception as e:
            logger.error(f"Error en análisis con Groq: {str(e)}")
            raise Exception(f"Error procesando con Groq: {str(e)}")
    
    def _parse_ai_response(self, content: str) -> Dict:
        """
        Parsear la respuesta de la IA y extraer el JSON
        
        Args:
            content (str): Respuesta de la IA
            
        Returns:
            Dict: Datos parseados del análisis
        """
        try:
            # Buscar JSON en la respuesta
            start_json = content.find('{')
            end_json = content.rfind('}') + 1
            
            if start_json != -1 and end_json != 0:
                json_str = content[start_json:end_json]
                result = json.loads(json_str)
                
                # Validar estructura mínima
                required_fields = ['sentimiento_general', 'puntuacion', 'resumen']
                if all(field in result for field in required_fields):
                    return result
                else:
                    logger.warning("Respuesta JSON incompleta, usando parsing alternativo")
                    return self._fallback_parsing(content)
            else:
                logger.warning("No se encontró JSON válido, usando parsing alternativo")
                return self._fallback_parsing(content)
                
        except json.JSONDecodeError as e:
            logger.error(f"Error parseando JSON: {str(e)}")
            return self._fallback_parsing(content)
    
    def _fallback_parsing(self, content: str) -> Dict:
        """
        Parsing alternativo cuando el JSON falla
        
        Args:
            content (str): Respuesta de la IA
            
        Returns:
            Dict: Estructura básica de análisis
        """
        # Análisis básico de sentimiento basado en palabras clave
        content_lower = content.lower()
        
        # Determinar sentimiento básico
        positive_words = ['positivo', 'bueno', 'excelente', 'recomendado', 'satisfecho']
        negative_words = ['negativo', 'malo', 'terrible', 'decepcionado', 'insatisfecho']
        
        positive_count = sum(1 for word in positive_words if word in content_lower)
        negative_count = sum(1 for word in negative_words if word in content_lower)
        
        if positive_count > negative_count:
            sentiment = "Positivo"
            score = 7
        elif negative_count > positive_count:
            sentiment = "Negativo"
            score = 3
        else:
            sentiment = "Neutral"
            score = 5
        
        return {
            "sentimiento_general": sentiment,
            "puntuacion": score,
            "aspectos_positivos": ["Análisis automático - revisar manualmente"],
            "aspectos_negativos": ["Análisis automático - revisar manualmente"],
            "recomendaciones": ["Revisar análisis manual por error en procesamiento"],
            "resumen": content[:200] + "..." if len(content) > 200 else content
        }
    
    def analyze_sentiment(self, review_text: str, provider: str = "openai") -> Dict:
        """
        Método principal para análisis de sentimientos
        
        Args:
            review_text (str): Texto de la reseña
            provider (str): Proveedor de IA ("openai" o "groq")
            
        Returns:
            Dict: Resultado del análisis
        """
        if not review_text.strip():
            raise ValueError("El texto de la reseña no puede estar vacío")
        
        logger.info(f"Iniciando análisis con {provider} para texto de {len(review_text)} caracteres")
        
        try:
            if provider.lower() == "openai":
                return self.analyze_with_openai(review_text)
            elif provider.lower() == "groq":
                return self.analyze_with_groq(review_text)
            else:
                raise ValueError(f"Proveedor {provider} no soportado. Use 'openai' o 'groq'")
                
        except Exception as e:
            logger.error(f"Error en análisis de sentimientos: {str(e)}")
            raise e
    
    def get_available_providers(self) -> list:
        """
        Obtener lista de proveedores disponibles
        
        Returns:
            list: Lista de proveedores configurados
        """
        providers = []
        if self.openai_client and OPENAI_API_KEY:
            providers.append("OpenAI")
        if self.groq_client and GROQ_API_KEY:
            providers.append("Groq")
        return providers

# Instancia global del analizador
analyzer = SentimentAnalyzer()