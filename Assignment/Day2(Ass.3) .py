


"""""
# غلط هنا عشان لما بطلع من آخر خطوة مش هدخل أعمل الأتشكات تاني 
email = input("enter your email : ")
if "@" in email and "." in email :
    username , domain = email.split("@")
    if username and domain :
        x , y = domain.split(".")
        if x and y :
            print(f"email:{email}")
else :
    email = input("enter a valid email : ")  #آخر خطوة

print(f"email:{email}")



while True :
    email=input("enter your email :")
    if '@' in email and '.' in email :
        username, domain = email.split('@')
        if  username and domain :
            x, y = domain.split('.')
            if x and y :
                break
    else :
        print("please enter a valid email")

print(f"email:{email}")


""""""""""""

def email_validation () :
    while True :
        email=input("enter your email :")
        if '@' in email and '.' in email :
            username, domain = email.split('@')
            if  username and domain :
                 x, y = domain.split('.')
                 if x and y :
                    break
        else :
            print("please enter a valid email")
     print(f"email:{email}")
    

email_validation ()

"""""

def email_validation (x) :
    while True :
        email=x
        if '@' in email and '.' in email :
            username, domain = email.split('@')
            if  username and domain :
                 x, y = domain.split('.')
                 if x and y :
                     print(f"email:{email}")
                     break
        else :
            print("please enter a valid email")
            break
    

email_validation ("youssefmosa@gmail.com")
