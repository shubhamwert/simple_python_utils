import hashing_basics

class ChainedHash(hashing_basics.HashTable):
    def __init__(self, name, size):
        self.name=name
        self.size=size
        self._HashTable__bucket=[[0 for i in range(2)] for j in range(size)]

    def _HandelCollision(self,data,location):
        print("Collision detected")
        self._HashTable__bucket[location].append(data)
        
    def Linear_Search(self, data):
        location=hash(data)%self.size
        for i in self._HashTable__bucket[location]:
            if(i==data):
                print(data," found at location ",location)
                return
        print("Data not found")

def test():    
    a=ChainedHash("Mbucket",5)
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
    