import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# img = cv2.imread("C:\\Users\\Danger_Harsh\\Desktop\\AI\\img1.jpg")
vid = cv2.VideoCapture(0,cv2.CAP_DSHOW)

var = 0
while True:
    var = var + 1

    if var%5 == 0:
        text= "Hello There"

    else :
        text = "I Am Harsh"
    alwaystrue , frame = vid.read()

    grayimg = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)

    face_cord = trained_face_data.detectMultiScale(grayimg)

    for (x,y,w,h) in face_cord :
        cv2.rectangle( frame , (x ,y) ,(x+w ,y+h), (randrange(255),randrange(255),randrange(255)),2)

        # font = cv2.FONT_HERSHEY_PLAIN
        # cv2.putText(frame , text , (x+10,y-10),font,2,(0,0,0) ,5 )
    

    cv2.imshow("My first AI project" , frame)
    k = cv2.waitKey(1)

    if k==81 or k==113 or k== 112:
        break  

vid.release
