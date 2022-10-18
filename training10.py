#import numpy as np, cv2

'''x = np.array([1,2,3,5,10],np.float32)
y = np.array([2,5,7,2,9]).astype("float32")

mag=cv2.magnitude(x,y)
ang=cv2.phase(x,y)
p_mag, p_ang=cv2.cartToPolar(x,y)
x2, y2 = cv2.polarToCart(p_mag, p_ang)

print("[x] 형태 : %s 원소 : %s" % (x.shape,x))
print("[mag]형태 : %s 원소 : %s" % (mag.shape,mag))

print(">>>열벡터를 1행에 출력하는 방법")
print("[m_mag]=%s" % mag.T)
print("[p_mag]=%s" % np.ravel(p_mag))
print("[p_ang]=%s" % np.ravel(p_ang))
print("[x_mat2]=%s" % x2.flatten())
print("[y_mat2]=%s" % y2.flatton())'''

'''def mat_access1(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k = mat[i,j]
            mat[i,j]=k*2

def mat_access2(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            k=mat.item(i,j)
            mat.itemset((i,j),k*2)

mat1=np.arange(10).reshape(2,5)
mat2=np.arange(10).reshape(2,5)

print("언소 처리 전: \n%s\n" % mat1)
mat_access1(mat1)
print("원소 처리 후 : \n%s\n" % mat1)

print("원소 처리 전 : \n%s\n" % mat2)
mat_access2(mat2)
print("원소 처리 후 : \n%s\n" % mat2)'''

'''import numpy as np
import cv2

image=np.zeros((200,400),np.uint8)
image[:]=200

title1, title2 = 'Position1','Position2'
cv2.nameWindow(title1,cv2.WINDOW_AUTOSIZE)
cv2.nameWindow(title2)
cv2.moveWindow(title1,150,150)
cv2.moveWindow(title2,400,50)

cv2.imshow(title1, image)
cv2.imshow(title2,image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import numpy as np
import cv2

def onChange(value):
    global image, tilte

    add_value=value-int(image[0][0])
    print("추가 화소값:",add_value)
    image=image+add_value
    cv2.imshow(title, image)

image=np.zeros((300,500),np.uint8)
cv2.imshow(title,image)

cv2.createTrackbar('Brightness',title,image[0][0], 255, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



'''blue, green, red = (255,0,0),(0,255,0),(0,0,255)
image = np.zeros((400,600,3),np.uint8)
image[:]=(255,255,255)

pt1, pt2 = (50,50),(250,150)
pt3,pt4=(400,150),(500,50)
roi = (50,200,200,100)


cv2.line(image,pt1,pt2,red)
cv2.line(image,pt3,pt4, green,3, cv2.LINE_AA)'''
''' image = np.zeros((200,400),np.uint8)
 image[:]=200

 title1, title2 = 'Position1','Position2'
 cv2.nameWindow(title1,cv2.WINDOW_AUTOSIZE)
 cv2.nameWindow(title2)
 cv2.moveWindow(title1,150,150)
 cv2.moveWindow(title2, 400,50)

 cv2.imshow(title1,image)
 cv2.imshow(title2, image)
 cv2.waitKey(0) #키 이벤트 대기
 cv2.destroyAllWindows() #열린 모든 윈도우 '''

'''import numpy as np
import cv2

image = np.zeros((200,300),np.uint8)
image.fill(255)

title1, title2 ='AUTOSIZE','NORMAL'
cv2.nameWindow(title1, image)
cv2.nameWindow(title2, cv2.WINDOW_NORMAL)

cv2.imshow(title1, image)
cv1.imshow(title2, image)
cv2.resizeWindow(title, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import numpy as np
import cv2

def on Change(value):       #트랙바 콜백 함수
    global image, title     #전역 변수 참조

    add_value = value - int(image[0][0])    #트랙바 값과 영상 화소값 처분
    print("추가 화소값:",add_value)
    image = image + add_value       #행렬과 스칼라 덧셈 수행
    cv2.imshow(title, image)

image = np.zeros((300,500),np.uint8)    #영상 생성

title = 'Trackbar Event'
cv2.imshow(title, image)

cv2.createTrackbar('Brightness', title,image[0][0],255,onChange)    #트랙바 콜백 함수 등록
cv2.waitKey(0)
cv2.destroyAllWindows()     #열린 모든 윈도우 제거'''

'''import numpy as np
import cv2

blue, green, red = (255,0,0),(0,255,0),(0,0,255)
image = np.zeros((400,600,3),np.uint8)
image[:]=(255,255,255)

pt1, pt2 = (50,50),(250,150)
pt3, pt4 = (400,150),(500,50)
roi=(50,200,200,100)

cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)

cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
cv2.rectangle(image,(400,200,100,100),green,cv2.FILLED)

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''import cv2

capture = cv2.VideoCapture(0)   #0번 카메라 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

fps =29.97      #초당 프레임 수
delay = round(1000/fps) #프레임 간 지연시간
size = (600, 360)   #동영상파일 해상도
fourcc =  cv2.VideoWriter_fourcc(*'DX50')   #압축코덱 설정

#카메라 속성 실행창에  출력
print("width x height:", size)
print("VideoWriterfourcc: %s" % fourcc)
print("delay: %2d ms", % delay)
print("fps: %.2f" % fps)

capture.set(cv2.CAP_PROP_ZOOM,1)    #카메라 속성 지정
capture.set(cv2.CAP_PROP_FRAME_WIDTH, sizez[0]) #해상도 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

#동영상파일 개방 및 코덱, 해상도 설정
writer = cv2.VideeoWriter("images/video_file.avi", fourcc, fps, size)
if writer.isOpended() == False: rraise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read() #카메라 영상 받기
    if not ret: break
    if cv2.waitKey(delay) >= 0: break

    writer.write(frame) #프레임을 동영상으로 저장
    cv2.imshow("View Frame from camera", frame)

writer.release()
capture.release()'''
'''def put_string(frame, tetxt, pt, value, color=(120,200,90)):    #문자열 출력
    text += str(value)
    shade == (pt[0]+2, pt[1] + 2)
    font =cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7,(0,0,0),2) #그림자 효과
    cv2.putText(frame, text, pt  , font, 0,7, color,2)  #글자적기

capture = cv2.VideoCapture(0)       #0번 카메라 연결
if capture.isOpensed() == False:       #카메라 연결 예외처리
    raise Exception("카메라 연결 안됨")

print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))'''

import numpy as np, cv2, math

def calc_hsi(bgr):  #한 화소 hsi  계산함수
    B, G, R = float(bgr[0]), float(bgr[1]), float(bgr[2]) #float형 변환
    bgr_sum=(R+G+B)
    #색상계산
    tmp1 = ((R-G) + (R-B)) * 0.5
    tmp2 = math.sqrt((R-G)*(R-G)+(R-B)*(G-B))
    angle = math.acos(tmp1 / tmp2) * (180 / np.pi) if tmp2 else 0 #각도

    H = angel if B <= G else 360 - angle    #색상
    S = 1.0 -3 * min([R,G,B]) / bgr_sum if bgr_sum else 0 #채도
    I = bgr_sum / 3 #명도
    return (H/2, S*255, I)   3원소 튜플로 변환

def bgr2hsi(image): #BGR 컬러 - HSI컬러 변환 함수
    hsv=[[calc_hsi(pixel) for pixel in row]for row in image] #2차원 배열 순회
    return cv2.convertScaleAbs(np.array(hsv))

BGR_img = cv2.imread("images/color_space.jpg", cv2.IMREAD_COLOR) #컬러영상 읽기
if BGR_img is None: raise Exception("영상 읽기 오류")

HSI_img = bgr2hsi(BGR_img)      #BGR-HSI변환
HSV_img = cv2.cvtColor(BGR_img, cv2.COLOR_BGR2HSV)  #OpenCV함수
Hue, Saturation, Intensity = cv2.split(HSI_img) #채널 분리
Hue2, Saturation2, Internsity2 = cv2.split(HSV_img) #채널분리

titles = ['BGR_img', 'Hue', 'Saturation', 'Intensity']
[cv2.imshow(t, eval(t)) for t in titles]    #User 구현 결과 영상표시
[cv2.imshow('OpenCV_'+t, eval(t+'2'))for t in titles[1:]]   #OpenCV 결과 영상 표시
cv2.waitKey(0)















