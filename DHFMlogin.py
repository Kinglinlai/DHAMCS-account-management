from DHFMread import giveUser, giveAll
from DHFMtime import *

def lockdown(username):
    # TODO LAI 20210615
    '''LOCKDOWN the user'''
    print('[TIP] your account has been locked down')
    print('Please contact the administrator for more information')
    return(None)


def login():
    '''A script-like function that returns a user object or -1 if failed to login'''
    swi = True
    while swi:
        attempt = giveUser(input("USERNAME:/* \n$",),giveAll())
        if attempt != -1:
            print(' */')
            user = attempt
            swi = False
        else:
            print('[TIP] USERNAME NOT FOUND')
            print('please try again\n')
    print('#username check complete#')
    swi = True
    count = 3
    while swi == True:
        print('[TIP] %s remaining attempts before LOCKDOWN' % count)
        print('TYPE "quit" to exit')
        temp = input('\nPASSWORD: /*\n$')
        if temp == 'quit':
            exit()
        attempt = user.veriKey(temp)
        if attempt:
            print('*/\n ###[Login SUCCESS]###')
            print('\nWELCOME, %s @ %s' % (user.name,giveTime()))
            return(user)
        else:
            count -= 1
            if count <= 0:
                lockdown(user.name)
                a = input('Press anything to continue......')
                return(-1)

if __name__ == '__main__':
    login()
