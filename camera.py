import cv2

camera = cv2.VideoCapture(0)
classificador = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')

while True:
    check, img = camera.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    objetos = classificador.detectMultiScale(imgGray, minSize=(30, 30), scaleFactor=1.5, minNeighbors=7)

    for (x, y, w, h) in objetos:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 7)

    cv2.imshow('Imagem', img)
    cv2.waitKey(1)
