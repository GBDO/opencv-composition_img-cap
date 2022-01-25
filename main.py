import cv2
import numpy as np
import time, argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('--video',help='Input video path')
# args = parser.parse_args()

# cap = cv2.VideoCapture(args.video if args.video else 0)

cap = cv2.VideoCapture(0)

time.sleep(3)

for i in range(60):
    ret, frame = cap.read()

fourcc= cv2.VideoWriter_fourcc(*'mp4v')
width= round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height= round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps= cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('.\캐글스터디\해리포터_투명망토_만들기\output.mp4',
                      fourcc,
                      fps,
                      (width,
                       height))

out2 = cv2.VideoWriter('.\캐글스터디\해리포터_투명망토_만들기\original.mp4',
                       fourcc,
                       fps,
                      (width,
                       height))

while(cap.isOpened()):
    ret,img = cap.read()
    if not ret:
        break
    
    ### hue= (0~179), saturation= (0~255), value= (0~255) 
    ### opencv hue color map= https://i.imgur.com/PKjgfFXm.jpg
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90,50,70])
    upper_blue = np.array([128,255,255])
    
    ### inRange 함수는 lower~upper 사이 범위의 색상을 가진 영역은 255
    ### 아닌 영역은 0으로 변환
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

    ### Red range
    # lower_red = np.array([0,120,70])
    # upper_red = np.array([10,255,255])
    # mask1 = cv2.inRange(hsv, lower_red, upper_red)

    # lower_red = np.array([170,120,70])
    # upper_red = np.array([100,255,255])
    # mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # mask1 = mask1 + mask2

    ### Black range
    #lower_black = np.array([0,0,0])
    #upper_black = np.array([255,255,80])
    #mask1 = cv2.inRange(hsv, lower_black, upper_black)

    ### 모폴로지 연산(Morphological Operation)
    ## OPEN 과 CLOSE가 있음
    # OPEN은 Erosion(침식) 후 Dilate(팽창) 진행
    # CLOSE는 Dilate(팽창) 후 Erosion(침식) 진행
    mask_cloak = cv2.morphologyEx(mask1,
                                  op= cv2.MORPH_OPEN,
                                  kernel= np.ones((3,3),np.uint8),
                                  iterations= 3)
    
    ### 이미지 팽창 
    mask_cloak = cv2.dilate(mask_cloak,
                            kernel=np.ones((3,3),np.uint8),
                            iterations=1)
    
    ###
    mask_bg =cv2.bitwise_not(mask_cloak)

    cv2.imshow('mask_cloak',mask_cloak)
    cv2.imshow('mask_mask_bg',mask_bg)

    res1 = cv2.bitwise_and(frame,frame,
                           mask= mask_cloak)

    res2 = cv2.bitwise_and(img,img,mask= mask_bg)

    result = cv2.addWeighted(src1= res1,
                             alpha= 1,
                             src2= res2,
                             beta= 1,
                             gamma= 0)

    cv2.imshow('res1',res1)
    cv2.imshow('res2',res2)
    cv2.imshow('result',result)

    # out.write(result)

    # out2.write(img)

    if cv2.waitKey(1) == ord('q'):
        break

out.release()

out2.release()

cap.release()

cv2.destroyAllWindows()