import cv2

img = cv2.imread('img/Lenna.png')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

df = cv2.CascadeClassifier('xml/haarcascade_frontalface_default.xml')

faces = df.detectMultiScale(imgGray, scaleFactor=1.05, minNeighbors=7, minSize=(30, 30),
                            flags=cv2.CASCADE_SCALE_IMAGE)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 7)

cv2.imshow(str(len(faces))+' face(s) encontrada(s).', img)
cv2.waitKey(0)