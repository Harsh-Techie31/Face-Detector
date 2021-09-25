import cv2
from random import randrange

# trained_face_data = cv2.CascadeClassifier('AI\\haarcascade_frontalface_default.xml')
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# img = cv2.imread("C:\\Users\\Danger_Harsh\\Desktop\\AI\\vk1.jpg")
img = cv2.imread('C:\\Users\\Danger_Harsh\\Desktop\\AI\\img1.jpg')

grayimg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

face_cord = trained_face_data.detectMultiScale(grayimg)

# print(face_cord)
# for item in face_cord:
for (x,y,w,h) in face_cord :
    cv2.rectangle(img , (x ,y) ,(x+w ,y+h), (0,255,0),4)

cv2.imshow("My first AI project" ,img)
cv2.waitKey()  

print("gg")