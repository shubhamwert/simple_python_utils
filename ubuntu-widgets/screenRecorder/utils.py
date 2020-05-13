'''contains utilities for detecting mouse , capturing video or screen shot'''
import cv2
import pyautogui
import ctypes
import numpy as np
def getScreenShot(Screen_size=pyautogui.size()):
    img=pyautogui.screenshot(region=(0,0,Screen_size[0],Screen_size[0]))
    
    img=np.array(img)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    cv2.imshow("image",img)
    cv2.imwrite('screenshot.png',img)
    print("screen shot taken")
    return True
def record(Screen_Size=pyautogui.size(),codec="xvid",fps=20):
    if(type(codec) != str):
        print("Codec must be a string")
    fourcc = cv2.VideoWriter_fourcc(*codec)
    out = cv2.VideoWriter("output.avi", fourcc, fps, Screen_Size)
    while True:
        frame=pyautogui.screenshot(region=(0,0,Screen_Size[0],Screen_Size[1]))
        frame=np.array(frame)

        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        out.write(frame)
        cv2.imshow("current_recording",frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()
    out.release()