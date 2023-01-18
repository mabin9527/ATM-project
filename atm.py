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


atm = ATM()
atm.create_account()