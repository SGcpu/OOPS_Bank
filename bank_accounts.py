class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' balance - ${self.balance:.2f} ")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.get_balance()
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Complete!")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer..🚀')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransfer Completed!\n\n**********')
        except BalanceException as error:
            print(f'\nTransfer incomplete! {error}')


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete!")
        self.get_balance()
        

class SavingAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName) 
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw Completed!")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")