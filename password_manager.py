from cryptography.fernet import Fernet # module use to encrypt the text


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


def load_key():
    file =  open("key.key", "rb")
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)




def view():
    with open("passwords.txt",'r') as f:
        for line in f.readlines():
            data= line.rstrip() #rstrip will strip off the \n that we arw using while inserting the new account and password
            username , password = data.split('|')
            print("User: ",username,"Password: ",fer.decrypt(password.encode()).decode())
        
def add():
    name = input("Account Name :- ")
    pwd = input("Password :- ")
    
    with open("passwords.txt",'a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+'\n')


while True:
    mode = input("Would you like to add a new password or view existing password or press q to quit :- ").lower()
    
    if mode =='q':
        break
    
    if mode=="view":
        view()
        
    elif mode =="add":
        add()
        
    else:
        print("Invalid ! mode is not supported")
