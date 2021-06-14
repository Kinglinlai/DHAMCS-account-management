

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
    return(result)
                    

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

def rbtStr(str,identifier):
    temp = rbt(str,identifier)
    return(temp[0])



