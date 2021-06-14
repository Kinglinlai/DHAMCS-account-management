from readByTag import *


f = open("data.py")
Rdata = f.read()

def removal(str):
    res = ""
    for c in range(len(str)):
        if str[c] != "\n":
            res += str[c]
    return(res)

class dataBase:
    data = ""

    def __init__(self):
        self.data = removal(Rdata)

    def userList(self):
        return(rbt(self.data,"<name>"))
            
        
class user:
    name = ""
    stat = ""
    id = 0
    cata = "user"
    __key = ""
    email = ""

    def __init__(self,name,stat,id,key,email):
        self.name = name
        self.stat = stat
        self.id = id
        self.key = key
        self.email = email

    def veriKey(self,str):
        if str == self.key:
            return(True)
        else:
            return(False)
        
    def giveCata(self):
        return(self.cata)
        
class admin(user):
    cata = "admin"
    def __init__(self,name,stat,id,key,email):
        user.__init__(self,name,stat,id,key,email)
    
    
class stuff(user):
    cata = "stuff"
    def __init__(self,name,stat,id,key,email):
        user.__init__(self,name,stat,id,key,email)

class client(user):
    cata = "client"
    def __init__(self,name,stat,id,key,email):
        user.__init__(self,name,stat,id,key,email)

def LocateNchange(tag,ID,content,data):
    oldone=giveIndex(data,tag)
    res = data.replace(data[oldone[ID][0]:oldone[ID][1]],content,1)
    return res
