print("Welcome to Citi Bank ATM")
restart = ('Y')
chance = 3
balance = 88.34
while chance >= 0:
    pin = int(input('Please Enter your 4 digit Pin: '))
    if pin == (1111):
        print('You entered your pin correctly\n')
        while restart not in ('n', 'No', 'no', 'N'):
            print('Please Press 1 for you balance\n')
            print('Please Press 2 to make a withdrawl\n')
            print('Please Press 3 to pay in\n')
            print('Please Press 4 to return card\n')
            option = int(input('What would you like to choose?'))
            if option == 1:
                print('Your balance: ', balance,'\n')
                restart = input('Would you like to go back? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('Thank you')
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much would you like?'))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print('\n you balance is now ', balance)
                    restart = input('would you like to go back?')
                    if restart in('n', 'No', 'no', 'N'):
                        print('Thank you')
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print('Invalid Amount please retry\n')
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(input('please enter desired amount: '))

            elif option == 3:
                pay_in = float(input('How much would you like to enter? '))
                balance = balance + pay_in
                print('\n Your balance is now: ', balance)
                restart = input('Would you like to go back? ')
                if restart in('n', 'No', 'N', 'no'):
                    print('Thank You')
                    break
            elif option == 4:
                print('Please wait while your card is returning....\n')
                print('Thank you for your time and services')
                break
            else:
                print('Please enter a correct number. \n')
                restart = ('y')

    elif pin != ('1111'):
        print("Incorret Passcode")
        chance = chance - 1
        if chance == 0:
            print('\n No more tries ')
            break
