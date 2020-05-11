#Robinhood hashing
class RobinHashing:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.__bucket=[[0 for i in range(3)] for i in range(size)]
    
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
            self.__bucket[location][2]=0
            
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
        dist=0
        for i in range(location,self.size):
            if(self.__bucket[i][1]==0):
                self.__bucket[i][0]=data
                self.__bucket[i][1]=1
                self.__bucket[i][2]=i-location+dist
                print("Data Inserted at location ",i)
                return
            else: 
                if(self.__bucket[i][2]>i-location+dist):
                    temp=self.__bucket[i][0]
                    self.__bucket[i][0]=data
                    self.__bucket[i][1]=1
                    t2=self.__bucket[i][2]
                    self.__bucket[i][2]=i-location+dist
                    location=i
                    dist=t2
                    print("Data Swapped at location ",i)

                    data=temp
        print("reversed check")
        i=location
        while i>=0:
            if(self.__bucket[i][1]==0):
                self.__bucket[i][0]=data
                self.__bucket[i][1]=1
                self.__bucket[i][2]=location-i+dist
                print("Data Inserted at location ",i)
                return
            else: 
                if(self.__bucket[i][2]>location-i+dist):
                    temp=self.__bucket[i][0]
                    self.__bucket[i][0]=data
                    self.__bucket[i][1]=1
                    t2=self.__bucket[i][2]
                    self.__bucket[i][2]=location-i+dist
                    dist=t2
                    location=i
                    print("Data Swapped at location ",i)

                    data=temp
            i=i-1




        # for i in range(location):
        #     if(self.__bucket[i][1]==0):
        #         self.__bucket[i][0]=data
        #         self.__bucket[i][1]=1
        #         self.__bucket[i][2]=location-i
        #         print("Data Inserted at location ",i)
        #         return
        print("current distance = ",location-i+dist)
        print("Unable to insert current  data, Bucket might be full ...")
    
    def LinearSearch(self,data):
        data_hash=hash(data)
        dist=0
        location=data_hash%self.size
        for i in range(location,self.size):
            if(data==self.__bucket[i][0]):
                print(data," found at location at ",i)
                return
            else:
                if(self.__bucket[i][2]>dist):
                    break
            dist=dist+1
        dist=0
        i=location
        while i>=0:
            if(data==self.__bucket[i][0]):
                print(data," found at location at ",i)
                break
            else:
                if(self.__bucket[i][2]>dist):
                    break    
            i=i-1
            dist=dist+1 
        print("Data not found")



def test():
    a=RobinHashing("Mtable",5)
    for i in ["Hello","ello","yellow","jellow","pellow","mellow"]:
        a.InsertData(i)
        print(a.getBucket())
    for i in ["Hello","yellow","UUU"]:
        a.LinearSearch(i)
    

if __name__ == "__main__":
    test()