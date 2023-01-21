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
        account_number = self.__public_check_account_number()
        if not account_number:
            return
        account_number_row = spreadsheets.find(account_number).row
        account_number_col = spreadsheets.find(account_number).col
        card_lock = spreadsheets.cell(
            account_number_row, account_number_col+3
            ).value
        balance = spreadsheets.cell(
            account_number_row, account_number_col+2
        ).value
        if card_lock == 'TRUE':
            print('Your card has been blocked!')
            return
        if not self.__public_verify_password(account_number):
            return
        deposit = int(input('Please enter your deposit: '))
        if deposit % 5 != 0:
            print('Please enter correct deposit')
        else:
            print('Your lodgement is successfully!')
            spreadsheets.update_cell(
                account_number_row, account_number_col+2,
                deposit + int(balance)
                )

    def withdraw(self):
        """
        User can withdraw money by calling this function
        """
        account_number = self.__public_check_account_number()
        if not account_number:
            return
        account_number_row = spreadsheets.find(account_number).row
        account_number_col = spreadsheets.find(account_number).col
        card_lock = spreadsheets.cell(
            account_number_row, account_number_col+3
            ).value
        balance = spreadsheets.cell(
            account_number_row, account_number_col+2
        ).value
        if card_lock == 'TRUE':
            print('Your card has been blocked!')
            return
        if not self.__public_verify_password(account_number):
            return
        money = int(input('Please enter the amount you want to withdraw: '))
        if money % 5 != 0:
            print('Please enter the correct amount!')
        elif money > int(balance):
            print('Your balance is insufficient!')
        else:
            print('Your withdrawal is successfully!')
            spreadsheets.update_cell(
                account_number_row, account_number_col+2, int(balance)-money)

    def check_balance(self):
        """
        Allow user to check their account balance
        """
        account_number = self.__public_check_account_number()
        if not account_number:
            return
        account_number_row = spreadsheets.find(account_number).row
        account_number_col = spreadsheets.find(account_number).col
        card_lock = spreadsheets.cell(
            account_number_row, account_number_col+3
            ).value
        if card_lock == 'TRUE':
            print('Your card has been blocked!')
            return
        if not self.__public_verify_password(account_number):
            return
        balance = spreadsheets.cell(
            account_number_row, account_number_col+2
        ).value
        print(f'Your balance is {int(balance)}')

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
                return str(account_number)
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
                print('Your account has been blocked! Please contact us')
                spreadsheets.update_cell(
                    account_number_row, account_number_col+3, True
                    )
                return False
        print('Your password is correct!')
        return True