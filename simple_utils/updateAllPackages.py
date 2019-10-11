import sys
import os
import pip
from subprocess import call
import subprocess

if __name__ == "__main__":
  try:
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    for packages in installed_packages:
        try:
            print("updating package : ",packages)
            call("pip install --upgrade "+packages,shell=True)
            

        except:
            print("Unable to install package : ",packages,"\n Try manually updating the package \n")

  except Exception as e:
       print("OOPS!! there seems to be a problem\nError :: ",e)
  