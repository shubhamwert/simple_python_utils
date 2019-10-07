import multiprocessing 


def function1(a,result):
    for num in a:
        result.value=result.value+num*num

def calrslt(a):
    divider=int(len(a)/2)
    result=multiprocessing.Value('i')
    result.value=0
    p1=multiprocessing.Process(target=function1,args=(a[0:divider+1],result))
    p2=multiprocessing.Process(target=function1,args=(a[divider+1:len(a)+1],result))
    p1.start()
    p2.start()
    for i in range(1,10):
        print("doing something else.",end="")
        for j in range(1,10):
            print(".",end="")
        print("\n")
    p1.join()
    p2.join()
    print(result.value)



   

    
if __name__ == "__main__":
    myNums=[1,2,3,4,5,6,7]
    
    divider=int(len(myNums)/2)
    calrslt(myNums)
    