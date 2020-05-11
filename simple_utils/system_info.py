import os
import sys
import platform
import time
import datetime
print("USer::",os.getlogin(),"\nPid",os.getpid())
print("Current Time::",datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
print("Loading System Info ... \n ",
        "System_version = ", sys.version)                 
print("CPU Count = ",os.cpu_count())

print("platform == ",sys.platform)
print("platform::",platform.uname())

print("processor info  ",platform.processor())
