import cv2
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('F:\\voice assistant\\face_recognition\\trainer\\trainer.yml')
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml");
# indicate id counter
id = 0
confidence =0
# names related to ids: example ==> none: id=0,  etc
names = ['Unknown','Adnan','Aman']
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height
# Define min window size to be recognized as a face
minW = 0.1 * cam.get(3)
minH = 0.1 * cam.get(4)
has_image, img = cam.read()
img = cv2.flip(img, 1)  # Flip vertically
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(int(minW), int(minH)),)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

    # If confidence is less than 100 ==> "0" : perfect match
    if (confidence < 50 ): #and confidence < 100
        id = names[id]
        # print(id)
    else:
        id = "unknown"

print(id)
print(confidence)
authorized_name=id
authorized_confidence= round(confidence,2)
cam.release()
cv2.destroyAllWindows()

