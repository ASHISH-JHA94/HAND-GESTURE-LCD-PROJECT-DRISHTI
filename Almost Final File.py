import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
serial_inst = serial.Serial()

ports_list = []

for port in ports:
    ports_list.append(str(port))
    print(str(port))

val: str = input('Select Port: COM')

for i in range(len(ports_list)):
    if ports_list[i].startswith(f'COM{val}'):
        port_var = f'COM{val}'
        print(port_var)

serial_inst.baudrate = 9600
serial_inst.port = port_var
serial_inst.open()
import cv2
import mediapipe as mp
import pyttsx3
import concurrent.futures

def speak(text):
    text_speech = pyttsx3.init()
    text_speech.say(text)
    text_speech.runAndWait()

cap = cv2.VideoCapture(0)
mphands = mp.solutions.hands
hands = mphands.Hands(static_image_mode=False,max_num_hands=2,
                      min_detection_confidence=0.5,
                      min_tracking_confidence=0.5)
mpDraw = mp.solutions.drawing_utils

txt1 = "1"
txt2 = "2"
txt3 = "3"
txt4 = "4"
txt5 = "5"
txt6 = "6"
txt7 = "7"
txt8 = "8"



while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frameRGB)

    if results.multi_hand_landmarks:
        landmarks = []

        for hand_landmarks in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(frame, hand_landmarks, mphands.HAND_CONNECTIONS)

            for id, lm in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

                landmarks.append([id, cx, cy])

        if len(landmarks) == 21:
            distancex = [landmarks[i][1] for i in range(21)]
            distancey = [landmarks[i][2] for i in range(21)]


            # Condition for Victory
            if distancex[7] < distancex[11] and \
                 (distancex[11] - distancex[7]) > 5 and \
                 (distancex[16] - distancex[20]) < 0.05 and \
                 distancey[15] > distancey[7] + 50 and \
                 (distancey[5]-distancey[9]<30) and\
                 (distancex[14]-distancex[4]<20)and \
                 (distancey[0]-distancey[5]>100)and\
                 distancey[20] > distancey[7] + 40:
                cv2.putText(frame, "VICTORY", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
                
                serial_inst.write(txt1.encode('utf-8'))
                # with concurrent.futures.ThreadPoolExecutor() as executor:
                #     executor.submit(speak, "Victory")


            # Condition for lose
            if distancex[6] < distancex[10] < distancex[14] < distancex[18] and \
                    (distancex[10] - distancex[6] < 50) and (distancex[14] - distancex[10] < 50) and (distancex[18] - distancex[14] < 50) and \
                    (distancex[18] - distancex[6] > 50) and (distancey[0] - distancey[6] < 50):
                cv2.putText(frame, "lose", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
                serial_inst.write(txt2.encode('utf-8'))
                # with concurrent.futures.ThreadPoolExecutor() as executor:
                #     executor.submit(speak, "Lose")



           
            # Condition for thumbs up
            if ((distancey[4] < distancey[5]) & (distancex[5] - distancex[9] > 0) & (distancex[5] - distancex[9] < 20) & (distancex[4] -distancex[8] < 20)):
                cv2.putText(frame, "thumbs up", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
                serial_inst.write(txt3.encode('utf-8'))
                # with concurrent.futures.ThreadPoolExecutor() as executor:
                #     executor.submit(speak, "thumbs up")

            #condition for pain
            
            if ((distancey[4]-distancey[8] > 100) & (distancey[4]-distancey[8] < 130) & (distancex[0]-distancex[4] > 125) & (distancey[0]-distancey[4] < 40)):
                   cv2.putText(frame, "pain", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
                   serial_inst.write(txt4.encode('utf-8'))
                   # with concurrent.futures.ThreadPoolExecutor() as executor:
                   #  executor.submit(speak, "pain")

            #condition for Thumbs Down
            if (distancey[3] + 20 < distancey[4]):
                cv2.putText(frame, "Thumbs Down", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 2, cv2.LINE_AA)
                serial_inst.write(txt5.encode('utf-8'))
                # with concurrent.futures.ThreadPoolExecutor() as executor:
                #     executor.submit(speak, "smile")

            #condition for thief
            if ((distancey[4]-distancey[8] < 20) & (distancey[4]-distancey[8] > 0)):
                cv2.putText(frame, "thief", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255),5)
                serial_inst.write(txt6.encode('utf-8'))
            

            #condition for smile
            if ((distancex[4] -distancex[8] > 130) & (distancex[12] - distancex[8] > 100)):
                cv2.putText(frame, "Smile", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)
                serial_inst.write(txt7.encode('utf-8'))

            #condn for call me
            if (distancex[4]-distancex[20] > 180):
                    
                    cv2.putText(frame, "CALL ME", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)
                    serial_inst.write(txt8.encode('utf-8'))
                    # with concurrent.futures.ThreadPoolExecutor() as executor:
                    #     executor.submit(speak, "CALL ME")8
                    
                    
             # Condition for hot
            # if (distancex[6] < distancex[8] and distancey[12] - distancey[4] < 15 and \
            #         distancey[16] - distancey[4] < 15 and distancey[20] - distancey[4] < 15):
            #     cv2.putText(frame, "hot", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                # with concurrent.futures.ThreadPoolExecutor() as executor:
                #     executor.submit(speak, "hot")


            # #Condition for hi
            # if (distancey[4] < distancey[2] and distancey[8] < distancey[6]) and \
            #         (distancey[20] < distancey[18] and distancey[12] < distancey[10]) and \
            #         (distancey[16] < distancey[14] and (distancex[8] - distancex[12] < 15) and \
            #          (distancex[12] - distancex[16] < 15) and (distancex[16] - distancex[20] < 15)):
            #     cv2.putText(frame, "hi", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)
            #     with concurrent.futures.ThreadPoolExecutor() as executor:
            #         executor.submit(speak, "hi")


        

    cv2.imshow("frame", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()







# #NEW METHOD:


# import cv2
# import mediapipe as mp
# import time

# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # Set camera width to 1280 pixels
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # Set camera height to 720 pixels

# mpHands = mp.solutions.hands
# hands = mpHands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils
# fingercordinates=[(8,6),(12,10),(16,14),(20,18)]
# thumbcordinate=(4,2)

# while True:
#     success,img=cap.read()
#     imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#     results=hands.process(imgRGB)
#     multiLandMarks=results.multi_hand_landmarks
#     if multiLandMarks:
#         handpoints=[]
#         for handLms in multiLandMarks:
#             mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)
#             for idx, lm in enumerate(handLms.landmark):
#                 # print(id,lm)
#                 h,w,c=img.shape
#                 cx,cy=int(lm.x*w),int(lm.y*h)
#                 handpoints.append((cx,cy))
#         for point in handpoints:
#             cv2.circle(img,point,10,(0,0,255),cv2.FILLED)

#         upcount=0
#         for cordinate in fingercordinates:
#             if handpoints[cordinate[0]][1] < handpoints[cordinate[1]][1]:
#                 upcount+=1
#         if handpoints[thumbcordinate[0]][0] >handpoints[thumbcordinate[1]][0]:
#             upcount+=1

#         #condition for victory
#         if (handpoints[8][1] < handpoints[6][1]) and (handpoints[12][1] < handpoints[10][1]) :
#             if upcount==2:
#                 cv2.putText(img, "VICTORY", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)


#         # #condition for yo
#         # if (handpoints[8][1] < handpoints[6][1]) and (handpoints[20][1] < handpoints[18][1]):
#         #     if upcount==2:
#         #         cv2.putText(img, "YO", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         #condition for ok
#         if handpoints[4][1] < handpoints[2][1] and handpoints[4][1] < handpoints[5][1] and handpoints[8][1] > handpoints[5][1] and upcount == 1:
#             cv2.putText(img, "OK", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         # Condition for hi
#             if (distancey[4] < distancey[2] and distancey[8] < distancey[6]) and \
#                     (distancey[20] < distancey[18] and distancey[12] < distancey[10]) and \
#                     (distancey[16] < distancey[14]):
#                 cv2.putText(frame, txt9, (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         # condition for smile
#         if handpoints[4][1] < handpoints[2][1] and handpoints[8][0] < handpoints[6][0]:
#             if upcount == 2:
#                 cv2.putText(img, "smile", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         # condition for call me
#         if (handpoints[4][1] < handpoints[2][1] and handpoints[20][1] < handpoints[18][1]):
#             if upcount == 2:
#                 cv2.putText(img, "call me", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         # condition for hot
#         if (handpoints[8][1] < handpoints[6][1]) :
#             if upcount == 1:
#                 cv2.putText(img, "HOT", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         # condition for lose
#         if handpoints[thumbcordinate[0]][0] > handpoints[thumbcordinate[1]][0]:
#             if upcount == 1:
#                 cv2.putText(img, "LOSE", (15,250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)
#         # #condition for thumbs up
#         # if (handpoints[4][1] < handpoints[2][1] and handpoints[8][1] < handpoints[6][1]) and (handpoints[20][1] > handpoints[18][1] and handpoints[12][1] > handpoints[10][1]) and (handpoints[16][1] > handpoints[14][1]):
#         #     if upcount == 1:
#         #         cv2.putText(img, "THUMBS UP", (15,250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)

#         # condition for thief (thumb tip touching index finger tip and rest of fingers closed)
#         dist_thumb_index = abs(handpoints[4][0] - handpoints[8][0]) + abs(handpoints[4][1] - handpoints[8][1])
#         if dist_thumb_index < 60 and upcount==2:
#             cv2.putText(img, "thief", (15, 250), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 5)



#         cv2.putText(img,str(upcount),(100,150),cv2.FONT_HERSHEY_PLAIN,12,(255,0,0),12)


#     cv2.imshow("finger counter",img)
#     if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' key to exit the loop and close the window
#         break

# cap.release()
# cv2.destroyAllWindows()