import subprocess

while True:

    print("welcome to ~RoMa~ Essentials")
    print("~~~~~~~~~~~~---~~~~~~~~~~~~~")
    print("~~P1ck_4_(l-l01c3")
    print("1.~ l)l>\1\/3-l)373(710l\l")
    print("2.~ 1|>-63773l>\\")
    print("3.~ 1l>-l>\3537")
    print("4.~ 73x7-3l)170l>\\")
    print("5.~ l=1l_3-(l>\3470l>\\")
    print("6.~ 5l-ll_l7l)0\/\/l\l")
    print("7 ~ 1337_7l>\4l\l5l_470l>\\")
    print("9.~ 3x17 :C")
    print("OP = ")

    try:
        op = int(input(""))
        if op == 1:
            subprocess.call('wmic logicaldisk get name', shell=True)
        elif op == 2:
            subprocess.call('ipconfig/all', shell=True)
            try:
                op1=int(input("M4C? = "))
                if op1 == 1:
                    subprocess.call('getmac', shell=True)
                else:
                    print("grrr ...")
            except:
                print(" meow \-(^-^)~ ")
        elif op == 3:
            subprocess.call('ipconfig/renew', shell = True)
        elif op == 4:
            subprocess.call('notepad.exe', shell=True)
        elif op == 5:
            print("")
        elif op == 6:
            subprocess.call('shutdown -h', shell=True)
        elif op == 7:
            print("welcome to the leet translator")
            try:
                op2 = int(input(" pick a choice =\n 1.- translator\n 2.- exit\n = "))
                if op2==1:
                    alphabet = ["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
                    leet_alphabet = ["4","8","(","l)","E","l=","6","l-l","¿","l<","l_","l\/l","l\l","0","°l","l>\\","5","7","l_l","\/\/","x","^/","-/_"]
                    print(f"normal ascii alphbet = {alphabet}\nleet alphabet = {leet_alphabet}")
                elif op2 ==2:
                    print("okay")
                else:
                    print("pick a right choice")
            except:
                print("")
        elif op == 8:
            print("8")
        else:
            if op == 9:
                print("o/")
                break
    except:
        print("x-x")


'''subprocess.call('dir', shell=True)
try:
    subprocess.call('cd C:', shell =True)
except:
    subprocess.call('', shell=True) '''