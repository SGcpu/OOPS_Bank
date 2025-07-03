from bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sarah = BankAccount(2000, "Sarah")

Dave.get_balance()
Sarah.get_balance()

Dave.withdraw(10)

Dave.transfer(10, Sarah)

blaze = SavingAcct(1000, "Blaze")

blaze.get_balance()
blaze.deposit(100)
blaze.transfer(100, Sarah)
