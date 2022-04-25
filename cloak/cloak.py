import cv2
cap=cv2.VideoCapture(0)

while cap.isOpened():
    ret,back=cap.read()
    if ret==True:
        cv2.imshow("image",back)
        if cv2.waitKey(5)==ord("q"):
            #when q is pressed , click the image, save the image
            cv2.imwrite('image.jpg', back)
            break
cap.release()
cv2.destroyAllWindows()

