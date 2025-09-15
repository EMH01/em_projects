# EM Projects - Repositorio de Proyectos de Machine Learning e IA

## ⚠️ Aviso Importante

Este repositorio contiene proyectos desarrollados hace algún tiempo. **Es importante tener en cuenta que las tecnologías, librerías y estrategias utilizadas pueden haber evolucionado considerablemente** desde su creación. Algunas dependencias podrían estar desactualizadas o requerir ajustes para funcionar con las versiones más recientes de las librerías.

Se recomienda revisar y actualizar las dependencias antes de ejecutar cualquier proyecto.

## 📁 Descripción de Proyectos

Este repositorio contiene una colección de proyectos de inteligencia artificial, machine learning y desarrollo de aplicaciones organizados por carpetas:

### 🎨 **CartoonizerApp_Streamlit_OpenCV**
Aplicación web desarrollada con Streamlit que aplica efectos de dibujo animado a imágenes utilizando OpenCV. Incluye interfaz simple para cargar imágenes y procesarlas.
- **Tecnologías**: Streamlit, OpenCV, NumPy
- **Funcionalidad**: Conversión de imágenes a estilo cartoon/dibujo animado

### 🤖 **Chatbot_Streamlit_OpenAI**
Chatbot interactivo que utiliza la API de OpenAI con capacidad de procesar documentos PDF/TXT. Incluye sistema de autenticación y memoria persistente mediante base de datos Supabase.
- **Tecnologías**: Streamlit, OpenAI API, Supabase, Sumy NLP
- **Funcionalidad**: Chat conversacional con documentos, análisis de contenido

### 🐱🐶 **Images_Classifier**
Notebook que demuestra el entrenamiento de un modelo clasificador de imágenes para distinguir entre gatos y perros, implementado en Google Colab.
- **Tecnologías**: PySpark, Pillow, NumPy, Google Colab
- **Funcionalidad**: Clasificación binaria de imágenes

### 🏆 **Pytorch_Classifier_Cifar10**
Implementación de clasificación del dataset CIFAR-10 utilizando el modelo VGG19 preentrenado con PyTorch. Incluye entrenamiento, evaluación y métricas de rendimiento.
- **Tecnologías**: PyTorch, Torchvision, TorchMetrics, VGG19
- **Funcionalidad**: Clasificación de 10 categorías de imágenes
- **Resultados**: 94.41% precisión en evaluación, 93.96% en pruebas

### 🎵 **Search_Covers**
Aplicación para búsqueda de covers musicales similares mediante análisis de letras extraídas de videos de YouTube. Utiliza embeddings y búsqueda por similitud.
- **Tecnologías**: Gradio, OpenAI Whisper, SentenceTransformers, FAISS, PyTubeFix
- **Funcionalidad**: Extracción de letras, búsqueda de similitudes, gestión de base de datos

### 🌤️ **WeatherAPP**
Asistente virtual para consultas meteorológicas desarrollado con FlowiseAI y desplegado en HuggingFace Spaces. Incluye interfaz de chat y autenticación.
- **Tecnologías**: Python, FlowiseAI, HuggingFace, Gradio, GraphQL, Docker
- **Funcionalidad**: Consultas meteorológicas actuales y pronósticos

### 🔬 **Trabajo de Diploma**
Investigación sobre Inteligencia Artificial Explicable enfocada en la interpretación de decisiones de modelos de clasificación de imágenes como VGG19, utilizando funciones de perturbación.
- **Tecnologías**: Redes neuronales, funciones de perturbación, Food101 dataset
- **Funcionalidad**: Generación de mapas de relevancia para explicabilidad de modelos

### 📊 **topic detection and polarity calculation**
Paquete de componentes de Procesamiento de Lenguaje Natural (NLP) para análisis de sentimientos y detección de tópicos en textos en español.
- **Tecnologías**: Python, K-means clustering, SpanishSentiWordNet
- **Funcionalidad**: Análisis de polaridad, agrupamiento de tópicos, procesamiento de texto

### 🧠 **Turing_Test**
Sistema conversacional DocuGenius Assistant basado en documentos, construido con Streamlit, LangChain y modelos GPT de OpenAI para casos prácticos de pruebas de Turing.
- **Tecnologías**: Streamlit, LangChain, OpenAI GPT, Python
- **Funcionalidad**: Asistente conversacional inteligente basado en documentos

## 📋 **Archivos Individuales**

### 📓 **Demo_Test_Windshield.ipynb**
Notebook de demostración para pruebas y experimentos diversos.

### 🎯 **Zero_Shot_Example.ipynb**
Ejemplo práctico de implementación de técnicas de Zero Shot Learning.

## 🚀 Instrucciones Generales de Uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/EMH01/em_projects.git
   cd em_projects
   ```

2. **Navegar al proyecto específico:**
   ```bash
   cd [nombre_del_proyecto]
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
   *Nota: Verificar compatibilidad de versiones antes de la instalación*

4. **Seguir las instrucciones específicas** en el README de cada proyecto.

## ⚙️ Consideraciones Técnicas

- **Python**: La mayoría de proyectos requieren Python 3.7+
- **Entornos**: Algunos proyectos están optimizados para Google Colab
- **APIs**: Varios proyectos requieren claves de API (OpenAI, Supabase, etc.)
- **Dependencias**: Revisar compatibilidad con versiones actuales de librerías

## 🔄 Estado de Mantenimiento

Este repositorio se mantiene como archivo histórico de proyectos. Para uso en producción, se recomienda:
- Actualizar todas las dependencias a versiones estables recientes
- Revisar y modernizar el código según las mejores prácticas actuales
- Verificar la compatibilidad con las últimas versiones de frameworks
- Actualizar documentación y instrucciones de instalación

## 📞 Contacto

Para preguntas o colaboraciones relacionadas con estos proyectos, puedes contactar al autor a través de GitHub.

---

*Repositorio mantenido por EMH01 - Colección de proyectos de IA y Machine Learning*