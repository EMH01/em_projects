import cv2

def image_to_cartoon(image):
    grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplicar desenfoque mediano para suavizar la imagen
    smoothGrayScale = cv2.medianBlur(grayScaleImage, 5)

    # Recuperar los bordes para el efecto de dibujo animado
    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255, 
                                    cv2.ADAPTIVE_THRESH_MEAN_C, 
                                    cv2.THRESH_BINARY, 5, 5)

    # Aplicar filtro bilateral para eliminar ruido 
    # y mantener los bordes afilados según sea necesario
    colorImage = cv2.bilateralFilter(image, 9, 1000, 1000)

    # # Ajustar la saturación de la imagen
    # satImage = cv2.convertScaleAbs(colorImage, alpha=1.7, beta=0)

    # # Ajustar el contraste de la imagen
    # satImage = cv2.convertScaleAbs(satImage, alpha=1.5, beta=10)

    # Enmascarar la imagen de bordes con nuestra imagen "BEAUTIFY"
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    
    return cartoonImage

# # # Probando
# img = cv2.imread("/media/esther/Estudios/Probando Streamlit/prueba.jpg")
# img = cv2.resize(img, (400, 600))
# result = image_to_cartoon(img)

# # # Mostrar la imagen resultante en una ventana emergente
# cv2.imshow("Result", result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
