from DHFMtime import *


#OOP
class user:
    name = ""
    stat = ""
    id = 0
    cata = ""
    __key = ""
    __email = ""

    # Constructor
    def __init__(self,name,stat,id,key,email,money):
        self.name = name
        self.stat = stat
        self.id = id
        self.__key = key
        self.__email = email
        self.__money = money
        
    # Test if key is valid
    def veriKey(self,str):
        if str == self.__key:
            return(True)
        else:
            return(False)

    # Reads
    def giveMoney(self):
        return self.__money
    
    def giveCata(self):
        return("USER")

    def prtAll(self):
        print("#####","\nUSERNAME: ",self.name,"\nID: ",self.id,"\nemail: ",self.__email,"\n\nMONEY: RMB￥",self.__money)
        print("\n#####")

    # Writes
    def askForChange(self,element,tovalue):
        wrt = '<change>'+'<id>'+self.id+'<id>'+'<element>'+str(element)+'<element>'+'<tovalue>'+str(tovalue)+'<tovalue>'+'<date>'+str(giveTime())+'<date>'+'<change>'
        file = open('buffer.DHFM',mode = 'a')
        file.write(wrt)
        file.close
        print('%s has been changed to %s' % (element,tovalue))
        return None
        
class admin(user):
    name = ""
    stat = ""
    id = 0
    cata = ""
    __key = ""
    __email = ""
    
    def __init__(self,name,stat,id,key,email,money):
        user.__init__(self,name,stat,id,key,email,money)

    # Reads
    def giveCata(self):
        return("ADMIN")

    # Writes
    def cm(self):
        cmChange()
        return None


#Functions
def giveAll():
    '''return str of all data'''
    f = open("data.txt")
    Rdata = f.read()
    f.close()
    return Rdata

def giveIndex(str,i):
    '''
    GIVEINDEX
    Search and return the position of the tag
    For example, giveIndex('<msg>hello<msg><msg>yy<msg><s1><s1>','<msg>')
    -> [[5,10],[20,22]]
    '''
    ilen = len(i)
    strlen = len(str)
    count = 0
    result = []
    beg = 0
    for element in range(len(str)):
        #print('Checking index %s' % element) 
        if str[element] == i[0] and (element + ilen-1) < strlen:
            #print('We got something~ %s' % str[element + ilen-1])
            if str[element + ilen-1]  == i[-1]:
                temp = rbi(str,[[element,element + ilen]])
                if temp[0] == i:
                    if count == 0:
                        #print('The segment is a beginner %s' % (element + ilen))
                        count = 1
                        beg = element + ilen
                    elif count == 1:
                        #print('The segment is an end %s' % (element))
                        count = 0
                        result.append([beg,element])
    return result
                    

def rbi(str,index):
    '''
    READ BY INDEX
    index: [[(inclusive start index),(exclusive end index)],[(start index),(end index)],...]
    returns a list of data
    For example, rbi('1234567890',[[0,2],[1,3],[2,10]])
    ->['12', '23', '34567890']
    '''
    result = [];
    for indexs in index:
        start = indexs[0]
        end = indexs[1]
        result.append(str[start : end])
    return(result)

def rbt(str,identifier):
    '''
    READ BY TAG
    Given a string, returns a list of data
    For example, rbt('<msg>hello<msg><msg>yy<msg><s1><s1>','<msg>')
    -> ['hello','yy']
    '''
    result = [];
    
    base = str
    i = identifier
    
    index = giveIndex(str,i)
    result = rbi(str,index)
    
    return(result)

def giveUser(name,data):
    '''return a class in the dataBase or -1 if not found'''
    nameList = rbt(data,'<name>')
    res = -1
    for x in range(len(nameList)):
        if nameList[x] == name:
            res = cstru(x)
            break
    return res

def cstru(index):
    res = None
    raw = rbt(giveAll(),"<d>")[index]
    # name,stat,id,cata,key,email
    if rbt(raw,'<cata>')[0] == "user":
        res = user(rbt(raw,'<name>')[0],rbt(raw,'<stat>')[0],rbt(raw,'<id>')[0],rbt(raw,'<key>')[0],rbt(raw,'<email>')[0],rbt(raw,'<money>')[0])
    else:
        res = admin(rbt(raw,'<name>')[0],rbt(raw,'<stat>')[0],rbt(raw,'<id>')[0],rbt(raw,'<key>')[0],rbt(raw,'<email>')[0],rbt(raw,'<money>')[0])
    return res

def LocateNchange(tag,ID,content,data):
    print('elements are: \n%s\n%s\n%s\n%s' % (tag,ID,content,data))
    oldone=giveIndex(data,tag)
    ID = int(ID)
    pre = data[0:oldone[ID][0]]
    aft = data[oldone[ID][1]:]
    data =  pre + str(content) + aft
    return data


    

def tryToWrt():
    
    '''Write the change into the database
    return -1 if something went wrong
    return 1 if everything works Alright and change is commited and logged
    '''
    process = open("buffer.DHFM")
    toDoList = rbt(process.read(),'<change>')
    for chg in range(len(toDoList)):
        print('Try No.%s' % chg)
        #try:
        trytag = rbt(toDoList[chg],'<element>')[0]
        tryid = rbt(toDoList[chg],'<id>')[0]
        trycontent = rbt(toDoList[chg],'<tovalue>')[0]
        trydata = process.read()
        #print(trytag,tryid,trycontent,trydata)
        org = open('data.txt')
        file = org.read()
        org.close
        
        temp = LocateNchange(trytag,tryid,trycontent,file)
        
        file = open("data.txt",mode = 'w')
        file.write(temp)
        file.close()
        file = open("buffer.DHFM",mode = 'w')
        file.close()
        '''except:
            process.close()
            return(-1)'''
    process.close()
    return(1)

def cmChange():
    a = open("buffer.DHFM")
    content = a.readline()
    date = giveTime()
    res = tryToWrt()
    if res == 1:
        print("Everything works just fine.")
        print("Change has been made @ %s" % date)
    elif res == -1:
        print("Unsuccessful try @ %s" % date)
