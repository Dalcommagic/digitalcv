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
'''import numpy as np, cv2

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
cv2.destroyAllWindows()'''

'''import cv2

capture = cv2.VideoCapture(0)
if capture.isOpened() is None: raise Excepton("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH,400)   #카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)  #카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS,0)   #오토포커스 정지
capture.set(cv2.CAP_PROP_BRIGHTNESS,0)  #프레임 밝기를 초기화 시킨다.

title ="test"
cv2.nameWindow(title)

while True:
     ret, frame = capture.read()    #카메라 영상 출력
     if not ret: break
     if cv2.waitKey(100) == 27: break   #esc누르면 종료
     blue, green, red = cv2.split(frame)    #컬러 영상 채널 분리
     cv2.add(green[100:300,200:300], 50, green[100:300, 200:300])

     frame = cv2.merge([blue, green, red])
     cv2.rectangle(frame,(200,100), (300,300), (0,0,225),2) #관심 영역을 빨간색으로

     cv2.imshow(title, frame)

capture.release()'''


'''import numpy as np
import cv2

image = np.zeros((200,300), np.uint8)   #행렬 생성 8bit data
image = np.zeros((200,300), np.uint8)
image[:] = 0                            #흰색 바탕

title1, title2 = 'Position1', 'Position2'       #윈도우 이름
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE)        #윈도우 생성 및 크기 조정 옵션
cv2.namedwindow(title2)
cv2.moveWindow(title1,0,0)                  #첫번쨰 윈도우
cv2.moveWindow(title2,300,230)                 #2번째 창

cv2.imshow(title1, image)           #행렬 원소를 영상으로 표시
cv2.imshow(title2, image)          
cv2.waitKey(0)                         #키 이벤트 대기
cv2.destroyAllWindows()                #열린 모든 윈도우 파괴'''

'''import numpy as np, cv2

def onMouse (event, x, y, flags, param):
    global title

    if event == cv2.EVENT_RBUTTONDOWN:  #마우스 오른쪽 버튼을 눌러보면
        cv2.circle(img, (x,y), 20,(0,0,255),2)      #반지름 20짜리 원 그리기
    elif event ==cv2.EVENT_LBUTTONDOWN: #왼쪽 버튼을 누르면?
        cv2.rectangle(img,(x,y),(x+30, y+30),(255,0,0),2)   #크기가 30*30짜리 사각형 그리기

    cv2.imshow(title,img)

img = np.full((400,300,3),(255,255,255), np.uint8)
title = 'test'
cv2.imshow(title,img)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import cv2

capture =cv2.Videocapture(0)        #카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      #카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)      #카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS,0)             #오토포커스 정지
capture.set(cv2.CAP_PROP_BRIGHTNESS,0)          #프레임 밝기를 초기화 시킨다

title="test"
cv2..nameWindow(title)

while True:
    ret, frame = capture.read()     #카메라 영상 출력
    if not ret: break
    if cv2.waitKey(100) == 27: break    #esc누르면 종료

    blue, green, red = cv2.split(frame) #컬러 영상 채널 분리
    cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])

    frame = cv2.merge([blue, green,red])

    cv2.rectangel(frame, (200,100),(300,300),(0,0,255),2)   #관심영역을 빨간색으로 표시한다.

    cv2.imshow(title, frame)

capture.release()'''

















