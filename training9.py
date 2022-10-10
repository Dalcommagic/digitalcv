import numpy as np, cv2

'''m1=np.full((3,6),10,np.uint8)
m2=np.full((3,6),50,np.uint8)
m_mask=np.zeros(m1.shape, np.uint8)
m_mask[:, 3:] = 1

m_add1 = cv2.add(m1,m2)
m_add2=cv2.add(m1,m2,mask=m_mask)

m_div1 =cv2.divide(m1, m2)
m1 = m1.astype(np.float32)
m2=np.float32(m2)
m_div2=cv2.divide(m1,m2)

titles=['m1','m2','m_mask','m_add1','m_add2','m_div1','m_div2']
for title in titles:
    print("[%s]= \n%s \n"%(title, eval(title)))'''

v1 = np.array([1,2,3],np.float32)
v2 = np.array([[1],[2],[3]],np.float32)
v3 = np.array([[1,2,3]],np.float32)

v_exp = cv2.exp(v1)
m_exp=cv2.exp(v2)
m_exp=cv2.exp(v3)
v_log=cv2.log(v1)
m_sqrt=cv2.sqrt(v2)
m_pow=cv2.pow(v3,3)

#행렬 정보 결과 출력
print("[v1형태: %s 원소: %s" % (v1.shape, v1))
print("[v2형태: %s 원소: %s" % (v2.shape, v2))
print("[v3형태: %s 원소: %s" % (v3.shape, v3))
print()

#행렬 정보 결과 출력 - openCV 결과는 행렬로 반환됨
print("[v1_exp] 자료형 %s 형태 : " % (type(v1_exp),v1_exp.shape))
print("[v2_exp] 자료형 %s 형태 : " % (type(v2_exp),v2_exp.shape))
print("[v3_exp] 자료형 %s 형태 : " % (type(v3_exp),v3_exp.shape))
print()

#열벡터를 1행에 출력하는 예시
print("[log]=",log.T)
print("[sqrt=",np.ravel(sqrt))
print("[pow]=",pow.flatten())



