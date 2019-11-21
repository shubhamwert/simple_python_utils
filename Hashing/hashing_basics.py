#Creating a simple hash table
class HashTable:
    def __init__(self,name,size,probing_mehtod="__Linear"):
        self.name=name
        self.size=size
        self.__bucket=[[0 for i in range(2)] for j in range(size)]
        self.probingMehtod=probing_mehtod

        print("Empty bucket initiated named ",name)
    def _detectCollision(self,location):
        if(self.__bucket[location][1]==0):
            return False
        else:
            return True

    def _InsertAtLoc(self,data,location):
        if(self._detectCollision(location)):
            print("Collision detected")
            self._HandelCollision(data,location)
        else:
            self.__bucket[location][0]=data
            self.__bucket[location][1]=1
            
            print("data inserted at location ",location)
    def InsertData(self,data):
        newdata=hash(data)
        location=newdata%self.size
        self._InsertAtLoc(data,location)
    def getBucket(self):
        return self.__bucket
    def _HandelCollision(self,data,location):
        self._Linear(data,location)

    def _Linear(self,data,location):
        for i in range(location,self.size):
            if(self.__bucket[i][1]==0):
                self.__bucket[i][0]=data
                self.__bucket[i][1]=1
                print("Data Inserted at location ",i)
                return True
        for i in range(location):
            if(self.__bucket[i][1]==0):
                self.__bucket[i][0]=data
                self.__bucket[i][1]=1
                print("Data Inserted at location ",i)
                return True
        print("Unable to insert data ...")
        return False
    
    def Linear_Search(self,data):
        datahash=hash(data)
        location=datahash%self.size
        for i in range(location,self.size):
            if(self.__bucket[i][0]==data):
                print(data," found at location ",i)
                return True
        for i in range(location):
            if(self.__bucket[i][0]==data):
                print(data," found at location ",i)
                return True
        print("Data not found in bucket")
        return False
def test():    
    a=HashTable("Mbucket",5)
    a.InsertData("shubham")
    a.InsertData("shubham1")
    a.InsertData("shubham2")
    a.InsertData("shubham3")
    a.InsertData("shubha3")
    a.Linear_Search("shubham3")
    a.Linear_Search("shubham")
    a.Linear_Search("shub")
    print(a.getBucket())
if __name__ == "__main__":
    test()
    

