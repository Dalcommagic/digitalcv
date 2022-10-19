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

'''import cv2

capture = cv2.VideoCapture(0)       #카메라 연결
if capture.isOpenedd() is None: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH,400)           #카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)          #카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS,0)               #오토포커스 정지
capture.set(cv2.CAP_PROP_BRIGHTNESS,0)                #프레임 밝기를 초기화 시킬거예요

title = "test"
cv2.namedWindow(title)

while True:
    ret, frame = capture.read()             #카메라 영상 출력
    if not ret: break
    if cv2.waitKey(100) == 27: break            #esc 누르면 종료

    blue, green, red = cv2.split(frame)     #컬러 영상 채널 분리
    cv2.add(green[100:300,200:300], 50, green[100:300,200:300])

    frame = cv2.merge([blue,green, red])

    cv2.rectangle(frame,(200,100),(300,300),(0,0,255),2)            #관심영역을 빨간색으로 표시한다.

    cv2.imshow(title, frame)

capture.release()'''

'''import cv2

capture = cv2.VideoCapture(0)   #0번 카메라 연결
if catpure.isOpened() is None: raise Exception("카메라 연결 안됨")

title = "test"
cv2.namedWindow(title)

size = (640,480)    #동영상 크기
fps = 15.0      #15프레임
fourcc=cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter("images/flip_test.avi", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH,size[0])   #프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1]) #프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS,0)       #오토포커싱 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS,100)       #밝기 초기회

while True:
    ret, frame = capture.read() #카메라 영상을 받기
    if not ret: break
    if cv2.waitKey(100) == 27: break    #esc누르면 종료

    frame = cv2.flip(frame,1)
    writer.write(frame)
    cv2.imshow(title, frame)

writer.release()
capture.release()'''

'''import numpy as np, cv2

image = cv2.imread("images/color.jpg", cv2.IMREAD_COLOR)        #이미지 영상을 읽어옵니다
if image is None: raise Exception("영상 파일 읽기 오류")

mask = np.zeros(image.shape[:2], np.uint8)  #이미지크기와 같은 영상(마스크기능)
center = (190, 170)#타원의 중심
cv2.ellipse(mask,center,(50,90),0,0,360,(255,255,255), -1)
dst =cv2.add(image, image, mask=mask)

cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)'''

'''import numpy as np, cv2

image = cv2.imread("images/sum_test.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류 발생")

mask = np.zeros(image.shape[:2],np.uint8)
mask[100:200, 100,200]=255  #관심영역 200, 100좌표 설정, 200*100크기 설정

sum_value = cv2.sumElems(image) #채널별 합 구하기
mean_value1 = cv2.mean(image)   #결과 튜플로 반환
mean_value2 = cv2.mean(image,mask)

print('sum_value 자료형:', type(sum_value), type(sum_value[0]))
print("[sum_value]=", sum_value)
print("[mean_value1]=", mean_value1)
print("[mean_value2]=", mean_value2)
print()

mean, stddev=cv2.meanStdDev(image)
mean2, stddev2 =  cv2.meanStdDev(image, mask=mask)
print('mean자료형 :', type(mean), type(mean[0],[0]))
print("[mean] = ", mean.flatten())
print("[stddev]=",stddev.flatten())
print()

print("[mean2] =", mean2.flatten())
print("[stddev2] = ", stddev2.flatten())

cv2.imshow("image", image)
cv2.imshow("mask", mask)
cv2.waitKey(0)'''

import numpy as np, cv2

def bar(value):
    global alpha, beta, title, image1, image2, dst

    alpha = cv2.getTrackbarPos('image1', title) / 100
    beta = cv2.getTrackbarPos('image2', title) / 100

    image3 = cv2.addWeighted(image1, alpha, image2,beta,0)
    dst[0:h, w:w*2] = image3[0:h, 0:w]

    cv2.imshow(title, dst)

image1 = cv2.imread("images/add1.jpg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("images/add2.jpg", cv2.IMREAD_GRAYSCALE)
if image1 is None or image2 is None: raise Exception("영상 파일 읽기 오류 발생")
title = 'dst'

alpha, beta = 0.6, 0.4
image3 = cv2.addWeighted(image1, alpha, image2, beta,0)

w,h = image1.shape
dst = np.zeros((w,h*3),np.uint8)



































