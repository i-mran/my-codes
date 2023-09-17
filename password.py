
 

def validpassword():
    password=input("Enter the password:")
    n=len(password)
    symbols=",.!@$%^&*()_+?><:\|/~`"
    digits="0,1,2,3,4,5,6,7,8,9"
    if(len(password)<8):
        print("invalid password:")
    if(n<=10):
        has_upper=False
        has_lower=False
        has_digit=False
        has_symbol=False
    if(password[0].isupper()):
         has_upper=True
    if(password[1:].islower()):
        has_lower=True
    for digit in digits:
        if digit in password:
           has_digit=True
    for symbol in symbols:
        if symbol in password:
            has_symbols=True
    if(has_lower==True&has_upper==True&has_digit==True&has_symbols==True):
        print("valid password:")
    else:
        print("Try again")
validpassword()
            
