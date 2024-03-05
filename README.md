# UR 미니 프로젝트 01: OpenCV를 활용한 실시간 비디오 디스플레이 및 제어 프로그램



## 소개
우리는 **OpenCV**를 활용한 미니 프로젝트를 구상했습니다. 이 간단한 프로그램은 사용자가 클릭한 지정 위치로 UR (Universal Robots) 암을 이동시키고 그 위치에서 작업을 수행합니다.
![image](https://github.com/jiloKIm/UR-MINI-PROJECT/assets/96615422/b191ac0d-94ad-4c9c-8743-e1cb3e7ec6f4)

## 구현 단계
![image](https://github.com/jiloKIm/UR-MINI-PROJECT/assets/96615422/c0fec885-83d6-4fd4-b077-772460971229)
![image](https://github.com/jiloKIm/UR-MINI-PROJECT/assets/96615422/1ea1b49c-303c-4329-890c-f24867175513)
![image](https://github.com/jiloKIm/UR-MINI-PROJECT/assets/96615422/18906040-c5a3-4a88-be94-b67d917d7b10)
![image](https://github.com/jiloKIm/UR-MINI-PROJECT/assets/96615422/a8725372-026f-411d-9440-307f31c6a9b8)

### UR 로봇으로 카메라 위치 설정
- UR 로봇에 해당하는 카메라 위치를 설정합니다.
- 사용된 카메라는 회의용 웹캠으로, 현재 UR에 설치된 카메라의 문제가 아니라 품질이 낮습니다.
- 카메라 뷰의 좌표를 UR의 좌표 시스템과 일치시키기 위해 카메라 캘리브레이션이 필수적입니다. 이는 다양한 크기의 그림 종이에 좌표를 매칭하는 것과 유사합니다.![image](https://github.com/jiloKIm/UR-MINI-PROJECT/assets/96615422/170bae6b-bf05-48cd-8c31-154f4e2960af)


### 코드 스니펫

1. **로봇 연결**
   ```python
   # 로봇 연결
   ip = '192.168.50.100'
   rob = Robot(ip)
   ```

2. **초기 설정**
   ```python
   # 초기 설정
   a = 0.5
   v = 1
   rob.set_tcp((0, 0, 0.1, 0, 0, 0))
   rob.set_payload(2, (0, 0, 0.1))
   time.sleep(0.2)

   rob.movej((0, r(-80), 0, r(-90), 0, 0), a, v)
   ```

3. **마우스 핸들러 정의 (이벤트 처리)**
   - OpenCV 이벤트 핸들러에 대한 자세한 내용: [OPEN CV 프로젝트 1: 반자동 문서 스캐너 만들기](https://blog.naver.com)
   ```python
   def mouse_handler(event, x, y, flags, param):
       global point
       if event == cv2.EVENT_LBUTTONDOWN:  # 왼쪽 마우스 버튼 클릭
           point = (x, y)  # 선택된 좌표 설정
   ```

4. **비디오 프레임 읽기**
   - 비디오 프레임에서 원을 그려 좌표를 표시하고 해당 좌표로 로봇을 이동시킵니다.
   ```python
   p = cv2.VideoCapture(0)  # 카메라 0을 사용하여 비디오 캡처 객체 생성

   cv2.namedWindow('img')
   cv2.setMouseCallback('img', mouse_handler)
   while True:
       ret, frame = cap.read()  # 비디오 프레임 읽기
       frame = cv2.resize(frame, (800, 600))  # 프레임 크기 조절

       if point is not None:
           cv2.circle(frame, point, 15, (0, 0, 255), 3)  # 선택된 좌표에 원 그리기

       cv2.imshow('img', frame)

       if cv2.waitKey(1) == ord('q'):  # 'q' 키를 누르면 종료
           break

   cap.release()  # 비디오 캡처 객체 해제
   cv2.destroyAllWindows()
   ```

   선택된 좌표에 따라 로봇은 사전 정의된 위치로 이동합니다. 지정된 범위 내의 좌표가 없으면 메시지가 출력됩니다.

5. **데모 비디오**


   - 시스템 작동 방식을 보여주기 위한 데모 비디오 링크: [데모 보기](https://www.youtube.com/watch?v=q2jQ3aRR7D4)

이 프로젝트는 OpenCV를 로봇 시스템과 통합하여 상호 작용적이고 반응형의 응용 프로그램을 만들 수 있는 방법을 보여줍니다.
