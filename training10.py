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

import numpy as np
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
cv2.destroyAllWindows()











