from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from langdetect import detect
import nltk

# Descargar recursos de NLTK si no están presentes
def download_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

# Función para detectar el idioma
def detect_language(text):
    return detect(text)

# Función para obtener stop words personalizadas
def load_stop_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        stop_words = set(file.read().splitlines())
    return stop_words

def get_custom_stop_words(language):
    if language == "es":
        return load_stop_words('spanish.txt')
    else:  # Para inglés 
        return load_stop_words('./english.txt')
    
# Función para calcular el número de oraciones en el resumen
def calculate_num_sentences(num_messages, min_sentences=2, max_sentences=10, factor=5):
    return min(max(num_messages // factor, min_sentences), max_sentences)

# Función para extraer y resumir los mensajes del asistente usando Sumy con LSA
def summarize(messages):
    download_nltk_resources()
    # Filtrar los mensajes del asistente
    mensajes_asistente = [msg["content"] for msg in messages if msg["role"] == "assistant"]
    
    # Concatenar los mensajes en un solo texto
    texto_asistente = " ".join(mensajes_asistente)
    
    language = detect_language(texto_asistente)
    # Crear el parser de texto para Sumy
    parser = PlaintextParser.from_string(texto_asistente, Tokenizer(language))
    
    # Calcular el número de frases para el resumen
    num_frases = calculate_num_sentences(len(mensajes_asistente))
    
    # Crear el resumen con LSA Summarizer
    if language == "es":
        stemmer = Stemmer("spanish")
        stop_words = get_custom_stop_words("es")
    else:
        stemmer = Stemmer("english")
        stop_words = get_custom_stop_words("en")
    
    summarizer = LsaSummarizer(stemmer)
    
    summarizer.stop_words = stop_words

    resumen = summarizer(parser.document,num_frases)
    
    # Convertir el resumen en una lista de diccionarios
    resumen_mensajes = [{"role": "assistant", "content": str(sentence)} for sentence in resumen]
    
    return resumen_mensajes

def summarize_text(text):
    download_nltk_resources()
    language = detect_language(text)
    parser = PlaintextParser.from_string(text, Tokenizer(language))
    sentences = parser.document.sentences
    num_frases = calculate_num_sentences(len(sentences))
    if language == "es":
        stemmer = Stemmer("spanish")
        stop_words = get_custom_stop_words("es")
    else:
        stemmer = Stemmer("english")
        stop_words = get_custom_stop_words("en")
    
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = stop_words
    resumen = summarizer(parser.document,num_frases)
    
    result= ""
    for sentence in resumen:
        result += f"{sentence}. " 

    return result
    
# Función para dividir el texto en fragmentos más pequeños
def split_text(text, max_tokens=3000):
    download_nltk_resources()
    sentences = text.split('. ')
    chunks = []
    current_chunk = ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_tokens:
            current_chunk += sentence + '. '
        else:
            chunks.append(current_chunk)
            current_chunk = sentence + '. '
    if current_chunk:
        chunks.append(current_chunk)
    return chunks
