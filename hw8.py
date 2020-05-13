#!/usr/bin/env python
# Assignment 8

'''
For your homework, you'll need to create a Banking class that does the following:

Tracks an initial account balance
Tracks deposits in the account
Tracks withdrawals to the account
Prints out a current balance
Prints an error message if someone tries to withdraw more money than what is currently in the account
'''

class Banking():

    # Tracks an initial account balance
    def __init__(self):
        self.initial_balance = float(input("Please input your initial balance: "))
        self.balance = self.initial_balance

    # Tracks deposits in the account
    def deposits(self, deposit_amount):
        self.deposit_amount = deposit_amount
        self.balance = self.balance + self.deposit_amount
        print("After depositing ${}, your current balance is ${}.".format(self.deposit_amount,self.balance))

    # Tracks withdrawals to the account
    # Prints out a current balance
    # Prints an error message if someone tries to withdraw more money than what is currently in the account
    def withdrawals(self, withdrawal_amount):
        self.withdrawal_amount = withdrawal_amount
        if self.balance > self.withdrawal_amount:
            self.balance = self.balance - self.withdrawal_amount
            print("After withdrawing ${}, your current balance is ${}.".format(self.withdrawal_amount, self.balance))
        else:
            print("You only have ${} in your balance, which is less than what you want to withdraw.".format(self.balance))

# Create a script that imports the Banking class and instantiates two users with balances.
import hw8
user1 = hw8.Banking()
user1.withdrawals(10)
user1.deposits(20)