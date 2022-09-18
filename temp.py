import re

def valid_email():
    matcher='^[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    email=input('enter the email id: ')
    if re.search(matcher,email):
        file_data=open('database.txt','a')
        file_data.write('\n')
        file_data.write(email)
        file_data.write('\n')
        file_data.write(email)
        file_data.close()
        valid_password()
        
    else:
        print('invalid email try again')
        valid_email() 
        
        
def valid_password():
    password=input('enter the password: ')
    l,h,d,s=0,0,0,0
    if len(password)>5 and len(password)<16:
        for i in password:
            if i.islower():
                l+=1
            elif i.isupper():
                h+=1
            elif i.isdigit():
                d+=1
            elif i in '!@#$%^&*()_{}[]':
                s+=1
        if l>0 and h>0 and d>0 and s>0 and l+h+d+s==len(password):
            file_data=open('database.txt','a')
            file_data.write(' ')
            file_data.write(password)
            file_data.close()
            
        else:
            print('incorrect password try again')
            valid_password()
            
    else:
        print('incorrect password try again')
        valid_password()
        

def login():       
    press=input('select login_username/forgot_password: ')
      
    if press=='login_username':
        filename = 'database.txt'
        with open(filename) as match:
            matcher= match.read()
        name=input('enter the username: ')
        passs=input('enter the password: ')
        full=name+' '+passs
        if full in matcher:
            print('successful login')    
        else:
            print('username not present, register new username')
            valid_email()
    elif press=='forgot_password':
        filename = 'database.txt'
        with open(filename) as match:
            matcher= match.read()
        name=input('enter the username: ')
        if name in matcher:
            print('provide a new password to login')
            file_data=open('database.txt','a')
            file_data.write('\n')
            file_data.write(name)
            file_data.close()
            valid_password()
            
        else:
            print('username not present, register new username')
            valid_email()
            
print(valid_email())
print(login())
      

  
