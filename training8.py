#영상채널분리
import cv2

image=cv2.imread("images/color.jpg",cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")
if image.ndim != 3: raise Exception("컬러 영상 아님")

bgr =cv2.split(image)
print("bgr 자료형:",type(bgr),type(bgr[0]),type(bgr[0][0][0]))
print("bgr 원소개수:",len(bgr))

cv2.imshow("image",image)
cv2.imshow("Blue channel",bgr[0])
cv2.imshow("Green channel",bgr[1])
cv2.imshow("Red channel",bgr[2])

cv2.waitKey(0)

#만약 numpy 객체 인덱싱 방식?
'''cv2.imshow("Blue channel",image[:,:,0])
cv2.imshow("Green channel",image[:,:,1])
cv2.imshow("Red channel",image[:,:,2])'''
