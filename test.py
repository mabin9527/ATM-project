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
# account_number = int(input('Please enter your account number: '))
# saved_account_number = spreadsheets.col_values(4)
# saved_account_number.pop(0)
# saved_account_number = [int(x) for x in saved_account_number]
# if account_number == saved_account_number:
#     print(account_number)
card = Card('92678223', '1234', '100')
user = User('G1234567', 'Jay Chou', '0879798188', card)
account_number_col = spreadsheets.find('92678223').col
account_number_row = spreadsheets.find('92678223').row
b = spreadsheets.cell(account_number_row, account_number_col+1).value
print(b)








# class Lodgement:
#     """
#     pass
#     """
#     def lodgement(self):
#         """
#         Account number, password, card lock have to be checked 
#         before lodgement
#         """
#         check_user = self.__public_check_account_number
#         print(check_user)
#         if not check_user:
#             return False
#         if not self.__public_verify_password(check_user):
#             return False
        
#     def __public_check_account_number(self):

#         """
#         Check if input account number from users matches
#         saved account number.
#         """
#         try:
#             account_number = int(input('Please enter your account number: '))
#             saved_account_number = spreadsheets.col_values(4)
#             saved_account_number.pop(0)
#             saved_account_number = [int(x) for x in saved_account_number]
#             if account_number in saved_account_number:
#                 print('Your account number is correct!')
#                 return account_number
#         except ValueError:
#             print('Please enter numbers for your account number!')
#         print("Your account number doesn't exist!")
#         return False

#     def __public_verify_password(self, user, account_number):
#         """
#         Verity password entered by user and password saved in database
#         """
#         account_password = user[account_number].card.password
#         password = input('Please enter your password: ')
#         if account_password != password:
#             for i in range(2, 0, -1):
#                 password = input(f'Incorrect! {i} times left: ')
#                 if password == account_password:
#                     break
#             else: 
#                 print('Your card has been blocked! Please contact us')
#                 return False
#             return True


# a = Lodgement()
# a.lodgement()   


