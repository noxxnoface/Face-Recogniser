import numpy as np, cv2 as cv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('Identity', default = "Anonymous", type = str, help = "Name as identification for Recogniser")
args = parser.parse_args()

cap = cv.VideoCapture(0)
cap.isOpened()

while(cap.isOpened()):
    res, frame = cap.read()
    if res==True:
        identity = cv.flip(frame, 1)
        frame = np.copy(identity)
        cv.putText(frame, "press c to capture", (30,30), cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 0), 2)
        cv.putText(frame, "press q to quit", (30,50), cv.FONT_HERSHEY_SIMPLEX, .8, (255, 255, 0), 2)
        cv.imshow('frame', frame)
        k = cv.waitKey(1) & 0xFF
        if k == ord('c'):
            cv.imwrite("C:/cygwin64/home/PC/FaceRecogniser/identities/"+args.Identity+".jpg", identity)
            break
        if k == ord('q'): break
    else: break

cap.release()
cv.destroyAllWindows()
