#200행 300행의 행렬을 2개 만들어서 다음과 같이 배치해보자.
'''import numpy as np
import cv2

image= np.zeros((200,300), np.uint8)
image = np.zeros((200,300), np.uint8)
image[:] = 0

title1, title2 = 'Position1','Position2'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)    #크기설정 불가
cv2.namedWindow(title2)
cv2.moveWindow(title1,0,0)
cv2.moveWindow(title2,300,230)

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''
import numpy as np, cv2

#마우스 이벤트 제어 프로그램 작성
def onMouse(event, x, y, flags, param):
    global title

    if event == cv2.EVENT_RBUTTONDOWN:  #만약 마우스 오른쪽 버튼을 누르면
        cv2.circle(img,(x,y), 20,(0,0,255),2)   #반지름 20짜리 원 그리기
    elif event ==cv2.EVENT_LBUTTONDOWN: #왼쪽 버튼을 누르면?
        cv2.rectangle(img,(x,y),(x+30,y+30),(255,0,0),2) #크기가 30*30짜리 사각형 그리기

    cv2.imshow(title, img)

img = np.full((400,300,3),(255,255,255),np.uint8)
title = 'test'
cv2.imshow(title,img)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
















