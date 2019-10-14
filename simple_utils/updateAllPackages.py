from sys import executable
import pip
from subprocess import call,check_output

if __name__ == "__main__":
  try:
    reqs = check_output([executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    for packages in installed_packages:
        try:
            print("updating package : ",packages)
            call("pip install --upgrade "+packages,shell=True)
            

        except:
            print("Unable to install package : ",packages,"\n Try manually updating the package \n")

  except Exception as e:
       print("\nOOPS!! there seems to be a problem\nError :: ",e,"\n\n")
  finally:
      call("pip list")
  