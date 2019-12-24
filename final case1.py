def flag():    
    muk =input("Enter 1 for Encryption and 2 for Decryption ")
    if int(muk) == 1:
        encrypt()
    elif int(muk) == 2:
        decrypt()
    else:
        print("ERROR OUTBOUND")


def encrypt():
    c= input("Enter uur text to be ENCRYPTED ")
    print("ENCRYPTING_ _ _")
    for dung in range(0,5):
        tm.sleep(1)
        print("_")

    x = c.split()

    type (x)


    res = [] 
    res[:0] = c

    ##print (str(res)) 
    


    global m
    m=[]
    global result
    result =""

    for a in range (0,len(c)):
        e= str(ord(res[a]))
        x = m.append(e)
        if a< len(c)-1:
            x= m.append("#")
        else:
            break
    ##print(m)


    for u in m:
        result +=u
    result = result##+"7071987649"
    print (result)
    print("****************************************************************************************************")
    if input("do you want to Exit, ENTER 'yes' or 'no' ")=="yes":
        print("******************************************************************************************************")
        print("SEE YOU SOON ")
    else:
        flag()

def decrypt():
    inp = input("Enter cipher")
    print("decrypting_ _ _")
    for dung in range(0,10):
        tm.sleep(1)
        print("_")
    split1 = inp.split("#")
    #print (split1)
    final = ''
    for a in split1:
        final= final + chr(int(a))
    print(final)
    print("***************************************************************************************************")
    if input("do you want to Exit, ENTER 'yes' or 'no' ")=="yes":
        print("******************************************************************************************************")
        print("SEE YOU SOON ")
    else:
        flag()
    
    
global users
users =['Shreytrivedi','teacher']
global passcodes
passcodes =['madman','teacher']




def finaly():
    i=0
    j=0
    print("***************************************************************************************************")
    user= input("Enter USER ID to Log INTO the System ")
    passcode= input("Enter PASSWORD ")
    print("CHECKING DATABASE FOR DETAILS. This may take a while_ _ _")
    for dung in range(0,5):
        tm.sleep(1)
        print("_")
    for a in range(0,3):
            if user== users[i]:
                if passcode== passcodes[i]:
                    flag()
                else:
                    i=i+1
            else :
                i=i+1
    

                
import time as tm
    
    
if input("Do you want to make a new account. Enter 'yes' or 'no' ") =="yes":
    print("PROCESSING_ _ _"),
    for dung in range(0,5):
        tm.sleep(1)
        print("_")
    newid = input("Enter new Userid ")
    newpassword =input("Enter new PASSWORD")
    users.append(newid)
    passcodes.append(newpassword)
    print("Accessing_ _ _")
    for dung in range(0,2):
        tm.sleep(0.19)
        print("_")
    print("Saving in Basebase_ _ _")
    for dung in range(0,2 ):
        tm.sleep(1)
        print("_")
    print("Saved!!!!!")
    finaly()
    
else:
    finaly()
            
        ##