import gspread
import time
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
    admin = Admin()
    admin.welcome()
    time.sleep(1)
    while True:
        admin.func()
        time.sleep(1)
        menu = input('Please select your options: ')
        atm = ATM()
        if menu == '1':
            atm.create_account()


if __name__ == '__main__':
    main()