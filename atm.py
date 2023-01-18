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


atm = ATM()
atm.create_account()