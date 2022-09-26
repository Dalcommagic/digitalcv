import cv2

capture = cv2.VideoCapture(0)   #카메라 연결
if capture.isOpened() is None: raise Exception("카메라 연결 안 됨")

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)          # 오토포커스 정지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 0)       # 프레임 밝기를 초기화 시킬거예요

title = "test"
cv2.namedWindow(title)

while True:
    ret, frame = capture.read()           # 카메라 영상 출력
    if not ret: break
    if cv2.waitKey(100) == 27: break      # esc 누르면 종료

    blue, green, red = cv2.split(frame) # 컬러 영상 채널 분리
    cv2.add(green[100:300, 200:300], 50, green[100:300, 200:300])

    frame = cv2.merge([blue, green, red])

    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 2)    #관심영역을 빨간색으로 표시합니다.

    cv2.imshow(title, frame)

capture.release()