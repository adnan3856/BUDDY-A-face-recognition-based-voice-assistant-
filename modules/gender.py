import cv2 as cv
import sys

faceProto = "datasets/opencv_face_detector.pbtxt"
faceModel = "datasets/opencv_face_detector_uint8.pb"
genderProto = "datasets/gender_deploy.prototxt"
genderModel = "datasets/gender_net.caffemodel"

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
genderList = ['Male', 'Female']

genderNet = cv.dnn.readNet(genderModel, genderProto)
faceNet = cv.dnn.readNet(faceModel, faceProto)

def getFaceBox(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    bboxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            bboxes.append([x1, y1, x2, y2])
            cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn, bboxes

cap = cv.VideoCapture(0)
padding = 20
hasFrame, frame = cap.read()
if hasFrame != True:
    raise ValueError("Can't read frame")
# cv.imwrite('img2.png', frame)
# cv.imshow("img1", frame)
# cv.waitKey()

frameFace, bboxes = getFaceBox(faceNet, frame)

if not bboxes:
    print("No face Detected, Restart the Application")
    sys.exit()

for bbox in bboxes:
    # print(bbox)
    face = frame[max(0,bbox[1]-padding):min(bbox[3]+padding,frame.shape[0]-1),max(0,bbox[0]-padding):min(bbox[2]+padding, frame.shape[1]-1)]
    blob = cv.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
    genderNet.setInput(blob)
    genderPreds = genderNet.forward()
    gender = genderList[genderPreds[0].argmax()]
    # print("Gender : {}, conf = {:.3f}".format(gender, genderPreds[0].max()))
    genderConfidence = format(round(genderPreds[0].max() * 100,2))
    genderValue = format(gender)
    print(genderValue)
    print(genderConfidence)


cap.release()
cv.destroyAllWindows()

