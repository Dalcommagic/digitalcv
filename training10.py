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

import numpy as np
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
cv2.destroyAllWindows()




