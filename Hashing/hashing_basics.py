#Creating a simple hash table
import sys
class HashTable:
    def __init__(self,name,size,probing_mehtod="__Linear"):
        self.name=name
        self.size=size
        self.__bucket=[[0 for i in range(2)] for j in range(size)]
        self.probingMehtod=probing_mehtod

        print("Empty bucket initiated named ",name)
    def __detectCollision(self,location):
        if(self.__bucket[location][1]==0):
            return False
        else:
            return True

    def __InsertAtLoc(self,data,location):
        if(self.__detectCollision(location)):
            print("Collision detected")
            self.__HandelCollision(data,location)
        else:
            self.__bucket[location][0]=data
            self.__bucket[location][1]=1
            
            print("data inserted at location ",location)
    def InsertData(self,data):
        newdata=hash(data)
        location=newdata%self.size
        self.__InsertAtLoc(data,location)
    def getBucket(self):
        return self.__bucket
    def __HandelCollision(self,data,location):
        self.__Linear(data,location)

    def __Linear(self,data,location):
        for i in range(location,self.size):
            if(self.__bucket[i][1]==0):
                self.__bucket[i][0]=data
                self.__bucket[i][1]=1
                print("Data Inserted at location ",i)
                return
        for i in range(location):
            if(self.__bucket[i][1]==0):
                self.__bucket[i][0]=data
                self.__bucket[i][1]=1
                print("Data Inserted at location ",i)
                return
        print("Unable to insert data ...")
    



if __name__ == "__main__":
    a=HashTable("Mbucket",5)
    a.InsertData("shubham")
    a.InsertData("shubham1")
    a.InsertData("shubham2")
    a.InsertData("shubham3")
    a.InsertData("shubha3")

    print(a.getBucket())
