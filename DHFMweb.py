import webbrowser
QR = 'qrcode.png'

def test():
    url = 'testPic.jpg'
    webbrowser.open(url)
    return None

def html():
    a = input("Please enter the money you want to charge this time:\n$ ")
    while True:
        try:
            a = int(a)
        except:
            a = input('Invalid Input\n$ ')
        else:
            break
    print('Processing//////')
    webbrowser.open(QR)
    temp = input("Enter anything to complete......")
    return a


