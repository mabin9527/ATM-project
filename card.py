class Card:
    """
    Card class includes four attributes:
        account number
        card number
        account balance
        if the card has been blocked
    """

    def __init__(self, account_number, password, balance):
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.card_lock = False
        