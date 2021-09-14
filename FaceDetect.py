import cv2
#Use algorithm for face detection
face_cascade = cv2.CascadeClassifier('face_detector.xml')

#Uses image from within folder
img = cv2.imread('Faces.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
cv2.imwrite("face_detected.png", img)
print('Successfully Saved')
