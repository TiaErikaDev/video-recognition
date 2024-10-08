import cv2
from simple_facerec import SimpleFacerec


# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

#Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name  in zip(face_locations, face_names):
        top, left, bottom, right = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        rect_name = cv2.putText(frame, name, (right, top - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 2)
        cv2.rectangle(rect_name, (left, top), (right, top - 40), (0, 0, 200), 4)

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()