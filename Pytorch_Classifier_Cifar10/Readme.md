# Clasificación de CIFAR-10 con VGG19 Preentrenado

Este proyecto utiliza el modelo preentrenado VGG19 para clasificar el conjunto de datos CIFAR-10. El modelo VGG19 es una red neuronal profunda ampliamente utilizada para tareas de clasificación de imágenes. En este proyecto, utilizamos PyTorch para la implementación del modelo y entrenamiento.

## Descripción

El conjunto de datos CIFAR-10 contiene 60,000 imágenes de 32x32 píxeles en 10 categorías, con 6,000 imágenes por categoría. Las categorías son:

- Aeroplano
- Automóvil
- Pájaro
- Gato
- Ciervo
- Perro
- Sapo
- Caballo
- Barco
- Camión

El objetivo de este proyecto es usar el modelo VGG19 preentrenado para clasificar estas imágenes en las categorías correspondientes.

## Tecnologías

- **PyTorch**: Framework de aprendizaje profundo utilizado para la construcción y entrenamiento del modelo.
- **Torchvision**: Librería de visión por computadora que proporciona implementaciones de modelos preentrenados y conjuntos de datos.
- **Google Colab**: Entorno de desarrollo que permite usar GPUs para el entrenamiento del modelo.
- **TorchMetrics**: Librería para calcular métricas como la precisión durante el entrenamiento y la evaluación.

## Requisitos

1. **Python 3.10+**
2. **PyTorch**
3. **Torchvision**
4. **TorchMetrics**
5. **Google Colab (opcional, pero recomendado para usar GPU)**

## Instalación

Clona este repositorio e instala las dependencias necesarias.

```bash
git clone <URL del repositorio>
cd <directorio del repositorio>
pip install -r requirements.txt
```

## Cargar y Preprocesar Datos

El conjunto de datos CIFAR-10 se descarga automáticamente usando `torchvision.datasets.CIFAR10`. Se aplican transformaciones a las imágenes para ajustarlas al tamaño y los valores esperados por el modelo VGG19.

## Entrenamiento del Modelo

Se carga el modelo preentrenado VGG19, se modifica la última capa para que tenga 10 salidas (una por cada clase de CIFAR-10) y se entrena con el conjunto de datos de entrenamiento.

```python
model = models.vgg19_bn(pretrained=True)
model.classifier[6] = nn.Linear(4096, 10)
model.to(device)
```

### Función de Entrenamiento

El modelo se entrena utilizando el optimizador SGD y la función de pérdida `CrossEntropyLoss`. Se entrena por un número determinado de épocas:

```python
train(model, train_loader, num_epochs=4)
```

## Evaluación y Pruebas

Una vez entrenado el modelo, se evalúa en el conjunto de validación y prueba. La precisión de la clasificación se calcula utilizando `torchmetrics.Accuracy`.

```python
evaluate(model, eval_loader)
test(model, test_loader)
```

## Resultados

- **Precisión de Evaluación**: 94.41%
- **Precisión de Prueba**: 93.96%

## Guardar el Modelo

Después de completar el entrenamiento, el modelo entrenado se guarda en Google Drive para su posterior uso:

```python
torch.save(model, '/content/gdrive/My Drive/Colab Notebooks/modelCompleteVGG19.pth')
```

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacer un fork del repositorio y enviar un pull request con las mejoras.

