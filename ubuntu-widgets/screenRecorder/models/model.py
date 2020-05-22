import cv2
import pyautogui
import ctypes
import numpy as np
from pynput.mouse import Listener
import time
class Recorder():
    def __init__(self,file:str,codec="xVid",fps=40):
        self.codec=codec
        self.fps=fps
        self.filename=file
        self.Screen_Size=pyautogui.size()
        self.region=(0,0,pyautogui.size()[0],pyautogui.size()[1])
        self.r=[]
        self.cropping=False
        self.count=0
    def setRegion(self):
        count=0
        self.ConnectMouse(True)
        print(self.r)

    def selectArea(self,x, y, button,pressed):
        print(x,y,button,pressed)
        if pressed:
            self.r=[x,y]
            self.cropping=True
        else:
            self.r.append(x)
            self.r.append(y)

            self.cropping=False
            self.region=tuple(self.r)
            self.l.stop()
            # self.Screen_Size=tuple([abs(self.region[0]-self.region[2]),abs(self.region[1]-self.region[3])])
            self.Screen_Size=pyautogui.Size(width=abs(self.region[0]-self.region[2]),height=abs(self.region[1]-self.region[3]))
    def ConnectMouse(self,state=True):
        if state:
            print("CONNECTING MOUSE")
            self.l= Listener(on_click=self.selectArea)
            self.l.start()
                
            print('se')
        


            

    def record(self):
        if(type(self.codec) != str):
            print("Codec must be a string")
        fourcc = cv2.VideoWriter_fourcc(*'MPEG')
        out = cv2.VideoWriter(self.filename, fourcc, self.fps, self.Screen_Size)
        print(self.region)
        while True:
            frame=pyautogui.screenshot(region=self.region)
            frame=np.array(frame)

            frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            cv2.imshow("current_recording",frame)
            out.write(frame)

            if cv2.waitKey(1) == ord("q"):
                break

        cv2.destroyAllWindows()
        out.release()