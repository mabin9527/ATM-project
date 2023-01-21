import re
import random
import gspread
from google.oauth2.service_account import Credentials
from user import User
from card import Card

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ATM_project')

spreadsheets = SHEET.worksheet('client_info')


class ATM:
    """
    pass
    """
    def create_account(self):
        """
        Collect user's personal information and generate an account number
        Inser all information to google spreadsheet
        """

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
            for i in range(2, 0, -1):
                confirm = input(f'Incorrect! {i} times left: ')
                if password == confirm:
                    break
            else:
                print('Incorrect! Retruning to previous menu')
                return False
        print()
        print('--------Please enter your predeposit--------')
        balance = input('Please enter your amount: ')
        regex = re.match('[1-9][0-9]+$', balance)
        if not regex:
            print('Please enter correct amount of predeposit')
            return False

        while True:
            account_number = random.randrange(10000000, 100000000)
            acc_number = spreadsheets.col_values(4)
            if account_number != acc_number:
                break
        print(f'Congralations! Your account number is {account_number}')

        card = Card(account_number, password, balance)
        user = User(passport_number, username, phone_number, card)
        data = [
            user.passport_number, user.username, user.phone_number,
            user.card.account_number, user.card.password,
            user.card.balance, user.card.card_lock
            ]
        spreadsheets.append_row(data)

    def lodgement(self):
        """
        Account number, password, card lock have to be checked 
        before lodgement
        """
        if not self.__public_check_account_number():
            return False
            
    def __public_check_account_number(self):

        """
        Check if input account number from users matches
        saved account number.
        """
        try:
            account_number = int(input('Please enter your account number: '))
            saved_account_number = spreadsheets.col_values(4)
            saved_account_number.pop(0)
            saved_account_number = [int(x) for x in saved_account_number]
            if account_number in saved_account_number:
                print('Your account number is correct!')
                return True
        except ValueError:
            print('Please enter numbers for your account number!')
        print("Your account number doesn't exist!")
        return False

    def __public_verify_password(self, account_number):
        """
        Verity password entered by user and password saved in database
        """
        account_number_row = spreadsheets.find(account_number).row
        account_number_col = spreadsheets.find(account_number).col
        account_password = spreadsheets.cell(
            account_number_row, account_number_col+1
            ).value
        password = input('Please enter your password: ')
        if account_password != password:
            for i in range(2, 0, -1):
                password = input(f'Incorrect! {i} times left: ')
                if password == account_password:
                    break
            else: 
                print('Your card has been blocked! Please contact us')
                return False
            return True