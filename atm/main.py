import time as t

user_balance = 97432.50
user_name = "Mr John Doe"
user_pin = 1234
user_verification = False

print("""
\n
\t\t\t         _             
\t\t\t        | |            
\t\t\t  __ _  | |_   _ __ ___  
\t\t\t / _` | | __| | '_ ` _ \ 
\t\t\t| (_| | | |_  | | | | | |
\t\t\t \__,_|  \__| |_| |_| |_|
\n
""")

print("Welcome to your bank account", user_name, end="\n\n")


print("USER VERIFICATION INITIATED...\n")
input_pin = int(input("Please enter your 4-digit PIN > "))
num_of_tries = 3
while (num_of_tries != 0):

    if input_pin == user_pin:
        print("\nUSER AUTHORIZED!🎊\n")
        user_verification = True

    else:
        num_of_tries -= 1
        print("PIN incorrect! Number of tries left - ",
              num_of_tries, end="\n\n")

else:
    print("USER VERIFICATION FAILED! \n Exiting...")
    user_verification = False
    t.sleep(2)
    print("Exited!\n\n")
