class CreditCard:
    def __init__(self, card_no):
        self.card_no=card_no
    def company(self):
        if str(self.card_no).startswith('4'):
            comp = 'Visa Card'
        elif str(self.card_no).startswith(('50', '67', '58', '63',)):
            comp = 'Maestro Card'
        elif str(self.card_no).startswith('5'):
            comp = 'Master Card'
    def lencheck(self):
        if 13 <= len(self.card_no) <= 19:
            message = "Length seems alright"

        else:
            message = "First check : Check Card number once again it must be of 13 or 16 digits long."
        return message
    