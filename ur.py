#로봇연결
ip = '192.168.50.100'
rob = Robot(ip)

#초기 셋팅
a = 0.5
v = 1
rob.set_tcp((0, 0, 0.1, 0, 0, 0))
rob.set_payload(2, (0, 0, 0.1))
time.sleep(0.2)

rob.movej((0, r(-80), 0, r(-90), 0, 0), a, v) 


p = cv2.VideoCapture(0)  # 0번 카메라를 사용하여 비디오 캡처 객체 생성

cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_handler)
while True:
    ret, frame = cap.read()  # 비디오 프레임 읽기
    frame = cv2.resize(frame, (800, 600))  # 프레임 크기 조정

    if point is not None:
        cv2.circle(frame, point, 15, (0, 0, 255), 3)  # 선택된 좌표에 원 그리기

    cv2.imshow('img', frame)

    if cv2.waitKey(1) == ord('q'):  # 'q' 키를 누르면 종료
        break

cap.release()  # 비디오 캡처 객체 해제
cv2.destroyAllWindows()

if (651 <= point[0] <= 681) and (91 <= point[1] <= 151):
    rob.movej((r(-4.83), r(-95.48), r(-92.97), r(-80.61), r(87.87), r(40.75)), a, v)
elif (674 <= point[0] <= 704) and (157 <= point[1] <= 217):
    rob.movej((r(-17.97), r(-105.24), r(-81.39), r(-81.32), r(88.11), r(27.59)), a, v)
elif (714 <= point[0] <= 744) and (232 <= point[1] <= 292):
    rob.movej((r(-28.87), r(-118.35), r(-62.84), r(-86.98), r(88.36), r(16.75)), a, v)
elif (753 <= point[0] <= 783) and (321 <= point[1] <= 381):
    rob.movej((r(-36.10), r(-133.83), r(-36.99), r(-97.12), r(88.55), r(9.36)), a, v)
else:
    print("No point is within the specified range.")
