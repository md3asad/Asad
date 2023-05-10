import cv2
from simple_facerec import SimpleFacerec
#encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images")

#load camera
cap = cv2.VideoCapture(0)
while True:
    rect, frame = cap.read()
    def rescale_frame(frame, percent=75):
        width = int(frame.shape[1] * percent / 100)
        height = int(frame.shape[0] * percent / 100)
        dim = (width, height)
        print(width,height)
        return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    #detect faces
    face_locations,face_names = sfr.detect_known_faces(frame)
    for face_loc,name in zip(face_locations,face_names):
        y1,x1,y2,x2 =  face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 0), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)


    frame150 = rescale_frame(frame, percent=150)
    cv2.imshow('frame150', frame150)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()