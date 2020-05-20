import models.model as m
import time

if __name__ == "__main__":
    mp=m.Recorder("hello.avi")
    mp.setRegion()
    time.sleep(5)
    mp.record()