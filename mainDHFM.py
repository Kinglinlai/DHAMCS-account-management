import DHFMread
import DHFMlogin
import DHFMtime
from DHFMweb import *
GREET = '''
 *******     **      **   ********   ****     ****
/**////**   /**     /**  /**/////   /**/**   **/**
/**    /**  /**     /**  /**        /**//** ** /**
/**    /**  /**********  /*******   /** //***  /**
/**    /**  /**//////**  /**////    /**  //*   /**
/**    **   /**     /**  /**        /**   /    /**
/*******    /**     /**  /**        /**        /**
///////     //      //   //         //         // 
'''

ADMIN_HELP = '''
=================
| help --> display this screen again
|
| stat --> display the status of the database
| 
| new  --> create a new user
|
| log  --> display the change in the database
|
| cmt  --> apply changes to the server
|
| wrt  --> change any attribute of a user, instantly effective
=================
'''
CLIENT_HELP = '''
=================
| help --> display this screen again
|
| stat --> display the status of the user
|
| pass --> change the password
|
| char --> charge for the account
=================

'''

def check(str,cata):
    if cata == "USER":
        if str == "help" or str == "stat" or str == "pass" or str == "char":
            return True
        else:
            return False
    elif cata == "ADMIN":
        if str == "help" or str == "stat" or str == "new" or str == "log" or str == "cmt" or str == "wrt":
            return True
        else:
            return False
    else:
        print('There is a problem...')
        raise SystemError("UNKNOWN")

def main():
    print(GREET)
    info = DHFMlogin.login()
    cata = info.giveCata()
    print(cata)
    
    if cata == "ADMIN":
        print(ADMIN_HELP)
    else:
        print(CLIENT_HELP)
        
    swi = True
    while swi:
        userInput = input("\n$ ")
        if userInput == "quit":
            
            return(1)
        while check(userInput,cata) == False:
            print("\nCOMMAND NOT FOUND")
            userInput = input("\n$ ")
            
        if userInput == "help":
            if cata == "ADMIN":
                print(ADMIN_HELP)
            else:
                print(CLIENT_HELP)
        elif userInput == "stat":
            print("USERNAME: %s\nLEVEL: %s\nBALANCE: %s\nDATE: %s" % (info.name,info.giveCata(),info.giveMoney(),DHFMtime.giveTime()))
        elif userInput == "pass":
            #TODO
            print('TODO')
        elif userInput == "char":
            result = html()
            # result = 50 # test
            if result != None:
                charge(info,result)
                cmt()
            else:
                print('Charge not successful, Please try again...')
                print(CLIENT_HELP)
        elif userInput == "new":
            #TODO
            print('TODO')
        elif userInput == "log":
            #TODO
            print('TODO')
        elif userInput == "cmt":
            cmt()
            print('')
        elif userInput == "wrt":
            #TODO
            print('')
        else:
            print("\n==COMMAND NOT FOUND==")
    a = input('END OF PROGRAM... TYPE ANYTHING TO QUIT')
    return(None)

def cmt():
    DHFMread.cmChange()

def charge(obj,money):
    obj.askForChange('<money>',str(int(obj.giveMoney())+int(money)))

if __name__ == '__main__':
    main()
