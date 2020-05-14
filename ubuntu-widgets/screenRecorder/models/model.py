import cv2
import pyautogui
import ctypes
import numpy as np
from pynput.mouse import Listener

class Recorder():
    def __init__(self,file:str,codec="xvid",fps=20):
        self.codec=codec
        self.fps=fps
        self.filename=file
        self.Screen_Size=pyautogui.size()
        self.region=(0,0,pyautogui.size()[0],pyautogui.size()[1])
        self.r=[]
        self.cropping=False
        self.listner=Listener(on_click=self.selectArea)
    def setRegion(self):
        self.ConnectMouse(True)
        print("MOUSE CONNECTED")
    
    
    def selectArea(self,x, y, button,pressed):
        if pressed:
            self.r=[x,y]
            self.cropping=True
        else:
            self.r.append([x,y])
            self.cropping=False
            self.region=tuple(self.r)

    def ConnectMouse(self,state=True):
        if state:
            with self.listner as l:
                l.join()
            print('se')
            
        else:
            with self.listner as l:
                l.stop()
            

    def record(self):
        if(type(self.codec) != str):
            print("Codec must be a string")
        fourcc = cv2.VideoWriter_fourcc(*self.codec)
        out = cv2.VideoWriter(self.filename, fourcc, self.fps, self.Screen_Size)
        while True:
            frame=pyautogui.screenshot(region=self.region)
            frame=np.array(frame)

            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            out.write(frame)
            cv2.imshow("current_recording",frame)
            if cv2.waitKey(1) == ord("q"):
                break

        cv2.destroyAllWindows()
        out.release()