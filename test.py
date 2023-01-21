import gspread
from google.oauth2.service_account import Credentials


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
# card = Card('92678223', '1234', '100')
# user = User('G1234567', 'Jay Chou', '0879798188', card)
# a = input(':')
# account_number_col = spreadsheets.find(a).col
# account_number_row = spreadsheets.find(a).row
# b = spreadsheets.cell(account_number_row, account_number_col+1).value
# print(b)
# balance = spreadsheets.cell(
#     account_number_row, account_number_col+2
# ).value
# deposit = int(input(': '))
# if deposit % 5 != 0:
#     print('Please enter correct number')
# else:
#     balance = deposit + int(balance)
#     spreadsheets.update_cell(row, col, value)
# class ATM:
#     """
#     pass
#     """
#     def lodgement(self):
#         """
#         Account number, password, card lock have to be checked 
#         before lodgement
#         """
#         account_number = self.__public_check_account_number()
#         account_number_row = spreadsheets.find(account_number).row
#         account_number_col = spreadsheets.find(account_number).col
#         card_lock = spreadsheets.cell(
#             account_number_row, account_number_col+3
#             ).value
#         print(card_lock)
#         if not account_number:
#             return 
#         if card_lock == 'TRUE':
#             print('Your card has been blocked')
#             return
#         if not self.__public_verify_password(account_number):
#             return 

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
#                 return str(account_number)
#         except ValueError:
#             print('Please enter numbers for your account number!')
#         print("Your account number doesn't exist!")
#         return False

#     def __public_verify_password(self, account_number):
#         """
#         Verity password entered by user and password saved in database
#         """
#         # print(account_number)
#         # a = spreadsheets.find(account_number).row
#         # print(a)
#         account_number_row = spreadsheets.find(account_number).row
#         account_number_col = spreadsheets.find(account_number).col
#         account_password = spreadsheets.cell(
#             account_number_row, account_number_col+1
#             ).value
#         password = input('Please enter your password: ')
#         if account_password != password:
#             for i in range(2, 0, -1):
#                 password = input(f'Incorrect! {i} times left: ')
#                 if password == account_password:
#                     print('Your password is correct!')
#                     break
#             else: 
#                 print('Your card has been blocked! Please contact us')
#                 spreadsheets.update_cell(
#                     account_number_row, account_number_col+3, True
#                     )
#                 return False
#         else:
#             print('Your password is correct!')
#             return True


# a = ATM()
# a.lodgement()


         