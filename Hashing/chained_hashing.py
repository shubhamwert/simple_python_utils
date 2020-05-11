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
                return True
        print("Data not found")
        return False

def test():    
    a=ChainedHash("Mbucket",5)
    for i in ["Hello","ello","yellow","jellow","pellow","mellow"]:
        a.InsertData(i)
        print(a.getBucket())
    for i in ["Hello","yellow","UUU"]:
        a.Linear_Search(i)
    print(a.getBucket())
if __name__ == "__main__":
    test()
    