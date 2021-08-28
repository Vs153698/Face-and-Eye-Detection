import cv2
# here we read the predefined classifier
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# read an image
# img=cv2.imread("download.jpg")
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret, img = cap.read()
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.imshow("image",img)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
