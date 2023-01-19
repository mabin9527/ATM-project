import re
import random
import csv
from card import Card
from user import User


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

        account_number = random.randrange(10000000, 1000000000)
        print(f'Congralations! Your account number is {account_number}')
        
        card = Card(account_number, password, balance)
        user = User(passport_number, username, phone_number, card)
        header = [
            'passport_number', 'username', 'phone_number',
            'account_number', 'password', 'balance', 'card_lock'
        ]
        rows = []
        rows.append((
            user.passport_number, user.username, user.phone_number,
            user.card.account_number, user.card.password, user.card.balance,
            user.card.card_lock
            ))
        with open('data.csv', 'w') as f:
            data_csv = csv.writer(f)
            data_csv.writerrow(header)
            data_csv.writerows(rows)


atm = ATM()
atm.create_account()