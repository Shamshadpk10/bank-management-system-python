import time

class Bank:
    BankName='Mitsubishi UFJ Bank '
    BankAddress='2-1 Otemachiu, Tokyo 100-8793|'

    # Create a new account
    def __init__(self, name, number, place, balance):
        self.name = name
        self.number = number
        self.place = place
        self.balance = balance


    def balance_check(self):
        # The balance_check method displays the current balance in the account.
        print("Your Account Current Balance:", self.balance)
        print('----------------------------')

    def deposit(self, deposit_amount):

        # The deposit method allows the user to deposit money into the account.
        self.balance += deposit_amount
        print("Transaction Complete")
        print("Deposited Amount is", deposit_amount)
        print('----------------------------')
        z = int(input('Press 1 for Check Current Balance\n'
                      'Press 2 for Exit'))
        print('----------------------------')
        if z == 1:
            print("Currently Account Balance is", self.balance)
        print('----------------------------')

    def withdraw(self, withdraw_amount):
        # The withdraw method allows the user to withdraw money from the account
        if withdraw_amount <= self.balance:
            self.balance -= withdraw_amount
            print("Transaction Complete")
            print('Withdraw amount is', withdraw_amount)
            print('----------------------------')
            x = int(input('Press 1 for Check Current Balance\n'
                          'Press 2 for Exit'))
            if x == 1:
                print("Currently Account Balance is", self.balance)
            print('----------------------------')
        else:
            print('Insufficient balance. Check Your Balance')
            y = int(input('Press 1 for Check Current Balance\n'
                          'Press 2 for Exit'))
            if y == 1:
                print("Currently Account Balance is", self.balance)



    def display_info(self):
        # The display_info method prints the details of the account holder
        print("Account Details:")
        print('--------------------')
        print('Name:', self.name)
        print('Mobile numbers:', self.number)
        print('Place:', self.place)
        print('Your Current Balance:', self.balance)
        print('----------------------------')

# Initial Welcome Message
print('|-------------------------------------------------------------|')
print(f'|Welcome to { Bank.BankName }, { Bank.BankAddress } ')
print('|____________________________________________________________|')

bank = {} # The bank dictionary is used to store 1 or more user account information

while True:
    # Main Menu Options
    choice = int(input('Press 1 for New Account Create.\n'
                       'Press 2 for Login\n'
                       'Press 3 for Exit'))

    if choice == 1: # Create new account
        name = input("Enter your full name:")

        while True:
            print('*** Note- Mobile number must be 10 Digits ***')
            number = input("Enter your mobile number:")
            if number.isdigit() and len(number) == 10:
                break

        place = input('Enter your place and pincode:')

        balance = float(input('Add Account Opening amount'))

        account = Bank(name, number, place, balance) # Account is a Bank class object
        bank[name] = account

        print(f'Hello {name}! Your account Created successfully!!! ')
        print('Now You can Login Your account, Press 2 for Login ')
        print('-----------------------------------------------')

    elif choice == 2: # Login
        print('*** Note- Give your name as Username ***')
        username = input("Enter Your Username:")
        print('Please wait.\n____________\nLoading....')
        time.sleep(0.5)
        print('Loading.....')
        time.sleep(0.5)
        print('Loading................')
        time.sleep(1)
        print('')
        if username in bank:
            account = bank[username]
            print('Welcome', username, '!')
            while True:
                # User Menu Options
                choice1 = int(input('Press 1 for Check Balance\n'
                                    'Press 2 for Money Withdraw\n'
                                    'Press 3 for Money Deposit\n'
                                    'Press 4 for Account Details\n'
                                    'Press 0 for Logout'
                                    '\n----------------------------'))

                if choice1 == 1: # Check balance
                    account.balance_check()
                    print('----------------------------')

                elif choice1 == 2: # Withdraw amount
                    print('Choose your Option for Money Withdrawal')
                    a = int(input('Press 1 for 1000\n'
                                  'Press 2 for 2000\n'
                                  'Press 3 for 3000\n'
                                  'Press 4 for other amount\n----------------------------'))

                    if a == 1:
                        a = 1000
                    elif a == 2:
                        a = 2000
                    elif a == 3:
                        a = 3000
                    elif a == 4:
                        other = int(input('Enter an amount'))
                        a = other
                    else:
                        print("Invalid Input")

                    account.withdraw(a)

                elif choice1 == 3: # Deposit
                    print('Choose your Option for Money Depositing')
                    a = int(input('Press 1 for 1000\n'
                                  'Press 2 for 2000\n'
                                  'Press 3 for 3000\n'
                                  'Press 4 for other amount\n----------------------------'))

                    if a == 1:
                        a = 1000
                    elif a == 2:
                        a = 2000
                    elif a == 3:
                        a = 3000
                    elif a == 4:
                        other = int(input('Enter an amount'))
                        a = other
                    else:
                        print("Invalid Input")

                    account.deposit(a)

                elif choice1 == 4: # Account details
                    account.display_info()

                elif choice1 == 0: # Log out
                    print("Logged out successfully!!")
                    break
                else:
                    print("Invalid Input")

        else:
            print("Account not found")
            print('===============================')

    elif choice != 3:
        print("Invalid Option")

    else:
        print('')
