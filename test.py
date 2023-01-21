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
try:
    account_number = int(input('Please enter your account number: '))
    saved_account_number = spreadsheets.col_values(4)
    saved_account_number.pop(0)
    saved_account_number = [int(x) for x in saved_account_number]
    if account_number in saved_account_number:
        print('Your account number is correct!')
    else:
        print("Your account number doesn't exist!")
except ValueError:
    print('Please enter numbers for your account number!')

    


