import cv2

classifier = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

image = cv2.imread('photos/pessoas3.jpg')
imageGray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

facesDetected = classifier.detectMultiScale(imageGray, scaleFactor=1.1)
print(len(facesDetected))
print(facesDetected)

for(x, y, l, a) in facesDetected:
    cv2.rectangle(image, (x,y), (x + l, y + a), (255, 0, 255), 2)

cv2.imshow("Found", image)
cv2.waitKey()
