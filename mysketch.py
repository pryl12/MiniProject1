import cv2
import numpy as np

#sketch generating function
def sketch(image):
    #convert image to gray scale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #clean up image using gaussian blur
    img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)

    #Extract edges
    canny_edges = cv2.Canny(img_blur, 10,70)

    #Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)
while True:
        ret, frame = cap.read()
        cv2.imshow('live sketcher',sketch(frame))
        if cv2.waitKey(1) == 99:   #13 is Enter key
            cv2.imwrite('C:\\Users\\Public\\Pictures\\Sample Pictures\\capture.jpg',sketch(frame))
        if cv2.waitKey(1) == 13:
            break
#Release camera and close windows
cap.release()
cv2.destroyAllWindows()