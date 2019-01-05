import os
import numpy as np, cv2 as cv
import face_recognition

known_face_encodings = []
known_face_names = []
face_names = []
for i in os.listdir('C:\cygwin64\home\PC\FaceRecogniser\identities'):
    if i.endswith('.jpg') or i.endswith('.png'):
        face_encoding = face_recognition.face_encodings(face_recognition.load_image_file('C:\cygwin64\home\PC\FaceRecogniser\identities/'+i))[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(i[:-4])

cap = cv.VideoCapture(0)

while(cap.isOpened()):
    res, frame = cap.read()
    if res==True:
        frame = cv.flip(frame, 1)
        working_frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(working_frame)  # Top Right Bottom Left
        face_encodings = face_recognition.face_encodings(working_frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            size = cv.getTextSize(name, cv.FONT_HERSHEY_DUPLEX, 1, 1)
            cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv.rectangle(frame, (left, bottom), (left + size[0][0], bottom + size[0][1] + 5), (0, 0, 255), cv.FILLED)
            cv.putText(frame, name, (left, bottom + size[0][1]), cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1)

        cv.imshow('frame2', frame)
        k = cv.waitKey(100) & 0xFF
        if k == ord('q') or k == ord('Q') : break
    else: break
print("People identified: \n{}".format(set(face_names)))
cap.release()
cv.destroyAllWindows()
