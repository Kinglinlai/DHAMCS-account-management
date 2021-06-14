start ='/* '
end = ' */'
a = ["Menu","Setting","Pizza","Python"]

def prt(string):
    print(start+str(string)+end)

def prtList(listIn):
    head = '''#################################################'''
    br = '''==========================='''
    count = 1
    print(head)
    if listIn == []:
        return(None)
    
    for x in listIn:
        print(br)
        print('# '+ str(count) + ' ' + str(x))
        count += 1
    print(br)
    return(None)
