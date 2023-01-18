class User:
    """
    User class contains four attributes:
        passport number
        username
        phone number
        card attributes
    """

    def __init__(self, passport_number, username, phone_number, card):
        self.passport_number = passport_number
        self.username = username
        self.phone_number = phone_number
        self.card = card