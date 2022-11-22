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

        while (user_verification == True):
            print("\t\t0. Logout and Exit")
            print("\t\t1. Check Bank Balance 💵 ")
            print("\t\t2. Withdraw Money 💰 ")
            print("\t\t3. Deposit Money 💰 ")
            print("\t\t4. Change PIN 🔑 ")
            print("\t\t5. Account INFO 🧑‍🦰 ")

            choice = int(
                input(f"\nHow may we serve u {user_name} (enter a choice) : "))
            print("\n")

            if choice == 0:
                print("Exiting...")
                t.sleep(2)
                print("You have been logged out. Thank you!\n\n")
                break

            elif choice in (1, 2, 3, 4, 5):

                if choice == 1:
                    print("Loading Account Balance...")
                    t.sleep(1.5)
                    print("Your current balance is Rs.",
                          user_balance, end="\n\n\n")
                    break

                elif choice == 2:
                    print("Opening Cash Withdrawal...")
                    t.sleep(1.5)

                    while (True):
                        withdraw_amt = float(
                            input("Enter the amount you wish to withdraw > "))

                        if withdraw_amt > user_balance:
                            print("Can't withdraw Rs.", withdraw_amt)
                            print("Please enter a lower amount!")
                            continue

                        else:
                            print("Withdrawing Rs.", withdraw_amt)
                            confirm = input("Confirm? Y/N > ")
                            if confirm in ('Y', 'y'):
                                user_balance -= withdraw_amt
                                print("Amount withdrawn - Rs.", withdraw_amt)
                                print("Remaining balance - Rs.",
                                      user_balance, end="\n\n\n")
                                break

                            else:
                                print("Cancelling transaction...")
                                t.sleep(1)
                                print("Transaction Cancelled!\n\n")
                                break
                    break

                elif choice == 3:
                    print("Loading Cash Deposit...")
                    t.sleep(1.5)

                    deposit_amt = float(
                        input("Enter the amount you wish to deposit > "))
                    print("Depositing Rs.", deposit_amt)
                    confirm = input("Confirm? Y/N > ")

                    if confirm in ('Y', 'y'):
                        user_balance += deposit_amt
                        print("Amount deposited - Rs.", deposit_amt)
                        print("Updated balance - Rs.",
                              user_balance, end="\n\n\n")
                    else:
                        print("Cancelling transaction...")
                        t.sleep(1)
                        print("Transaction Cancelled!\n\n")

                    break

                elif choice == 4:
                    print("Loading PIN Change...")
                    t.sleep(1.5)

                    pin_new = int(input("Enter your new PIN > "))

                    print("Changing PIN to", pin_new)
                    confirm = input("Confirm? Y/N > ")
                    if confirm in ('Y', 'y'):
                        user_pin = pin_new
                        print("PIN changed successfully! \n\n")
                    else:
                        print("Cancelling PIN change...")
                        t.sleep(1)
                        print("Process Cancelled!\n\n")

                    break

                else:
                    print(f'Account Name . {user_name}')
                    print(f'Account PIN : {user_pin}')
                    print(f'Account Balance : {user_balance} \n\n')
                    break

            else:
                print("Invalid input!")
                print("\t\t0. Enter 0 to Logout and Exit!")
                continue

    else:
        num_of_tries -= 1
        print("PIN incorrect! Number of tries left - ",
              num_of_tries, end="\n\n")

else:
    print("USER VERIFICATION FAILED! \n Exiting...")
    user_verification = False
    t.sleep(2)
    print("Exited!\n\n")
