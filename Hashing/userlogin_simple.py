from chained_hashing import ChainedHash


#To do : chained hashing can cause a problem that for different user it can grant access under same password due to collsion
class User:
    def __init__(self,user_name,password):
        self.__user_name=user_name
        self.__password=hash(password)
    def getUserName(self):
        return self.__user_name
    def get_password(self):
        return self.__password
    def Login(self):
        print("Hello ",self.getUserName())
        return True
class passwordHash(ChainedHash):
    def Linear_Search(self, data : User):
        location=data.get_password()%self.size
        for i in self._HashTable__bucket[location]:
            if(i==data.getUserName()):
                
                return True
        print("Data not found")
        
        
        return False
    def InsertData(self, data : User):
        location=data.get_password()%self.size
        super(passwordHash,self)._InsertAtLoc(data.getUserName(),location)
    

if __name__ == "__main__":
   tabel=passwordHash("UserTable",5)
   while True: 

    user_name=input("Enter Your User Name : ")
    password=input("Enter Your password : ")
    user=User(user_name,password)
    if(tabel.Linear_Search(user)):
        print("Loging you In.........")
        user.Login()
        exit()
    else:
        print("You seems like a new User wanna sign up (y/n)")
        res=input()
        if(res=='y'):
            tabel.InsertData(user)
        else:
            print("Quitting system")
            exit()
            

