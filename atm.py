import re


class ATM:
    """
    Collect user's personal information and generate an account number
    """

    def create_account(self):

        print('--------Please enter your passport number--------')
        print('Passport number should like the following example')
        print('Example: 141234567/ 151234567, G12345678, P1234567')
        passport_number = input('Please enter your passport number here: ')
        regex = re.match('(^(14|15)\d{7})|(^[DEGPS]\d{7,8}$)', passport_number)
        if not regex:
            print('Please enter the right passport number')
            return False
        
        print()
        print('--------Please enter your phone number--------')
        print('-------Phone number should start with 08------')
        phone_number = input('Please enter your phone number: ')
        regex = re.match('08[35679][0-9]{7}$', phone_number)
        if not regex:
            print('Please enter the right phone number')
            return False

        print()
        print('--------Please enter your full name--------')
        username = input('Pleaase enter your full name: ')
        regex = re.match('^[a-zA-Z]+ [a-zA-Z]+$', username)
        if not regex:
            print('Please enter your name correctly')
            return False

        print()
        print('--------Please enter your password--------')
        password = input('Please enter your password(4 digits): ')
        regex = re.match('\d{4}', password)
        if not regex:
            print('Incorrect! your password should contains 4 digits')
            return False
        confirm = input('Please confirm your password: ')
        if password != confirm:
            print('The confirmation password is not identical!')
            


atm = ATM()
atm.create_account()