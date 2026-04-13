print("Enter 'start' to start")
s = input()
s = s.lower()
if s == 'start':
    while(s != 'stop'):
        print("Enter your password.       Write 'stop' to exit")
        s = input()
        if s == 'stop':
            print("Programm is ended")
            break
        if s.isspace():
            print("Please enter your password")
        else:

            acnt = 0
            bcnt = 0
            cnt = 0
            scnt = 0
            lcnt = 0
            ucnt = 0
            b = s.lower()
            c = s.upper()
            for i in range(len(b)):
                if b[i] >= 'a' and b[i] <= 'z':
                    acnt += 1
                elif b[i] >= '0' and b[i] <= '9':
                    bcnt += 1
                elif b[i] == ' ':
                    scnt += 1
                else:
                    cnt += 1

                if b[i] != s[i]:
                    ucnt += 1
                if c[i] != s[i]:
                    lcnt += 1
            if scnt > 0:
                print("There mustn't be spaces in password")
            else:
                print("Lenght of password:" , len(s))
                print("Number of letters:" , acnt)
                print("Number of digits:" , bcnt)
                print("Number of symbols:" , cnt)
                if acnt > 1:
                    print("Number of letters in uppercase:" ,  ucnt)
                    print("Number of letters in lowercase:" , lcnt)
                if(len(s) > 8 and ucnt > 0 and lcnt > 0 and bcnt > 0 and cnt > 0):
                    print("Password is excellent!")
                elif(len(s) > 8 and acnt> 0 and bcnt > 0 and cnt > 0):
                    print("Password is good!")
                elif len(s) > 8 and (acnt > 0 and bcnt > 0) or (acnt > 0 and cnt > 0)  or (bcnt > 0 and bcnt > 0):
                    print("Passwrod is mid")
                else:
                    print("Password is bad")
else:
    b = ''
    while b != 'start':
        print("Enter 'start' to start")
        b = input()

            




