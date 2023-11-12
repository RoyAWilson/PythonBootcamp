# Create a bank class - will need a wayu to deposit, withdraw and display the balance

class BANK_ACCOUNT(object):

    def __init__(self, balance=0.0):
        self.balance = balance

    def display_bal(self):
        print('Your balance is {self.balance}')

    def deposit(self):
        amount = float(input('How much would you like to deposit? '))
        self.balance = self.balance + amount
        print(f'Your new balance is £{self.balance}')

    def withdrawal(self):
        w_amount = float(input('How much would you like to withdraw? '))
        while w_amount > self.balance:
            print(f'You don not have enought funds to withdraw {
                  w_amount}, your balance is {self.balance}')
            w_amount = float(input('How much would you like to withdraw> '))
        self.balance = self.balance - w_amount
        print(f'Your new balance is {self.balance}')


Roy = BANK_ACCOUNT()
Roy.deposit()
Roy.display_bal()
Roy.withdrawal()
