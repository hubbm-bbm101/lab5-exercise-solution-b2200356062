#. Write a Boolean function that checks if a string contains ‘@’ sign and at least one ‘.’ dot
#  (disregard the order for the sake of simplicity). Use that function to check if a user input is a valid e-mail or not.
email = str(input('enter your email: '))

def f(email):
    if "@" and "." in email:
        print('this is a valid email')
    else:
        print("this is not a valid email")

f(email)



    


