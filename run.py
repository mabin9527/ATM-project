import time
import gspread
from google.oauth2.service_account import Credentials
from admin import Admin
from atm import ATM

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('ATM_project')


def main():
    """
    Users can select their options from this function
    """
    admin = Admin()
    admin.welcome()
    time.sleep(1)
    while True:
        admin.func()
        time.sleep(1)
        menu = input('Please select your options:\n')
        atm = ATM()
        if menu == '1':
            atm.create_account()
        elif menu == '2':
            atm.lodgement()
        elif menu == '3':
            atm.withdraw()
        elif menu == '4':
            atm.check_balance()
                    

if __name__ == '__main__':
    main()
