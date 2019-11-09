class BankAccount:
    """This class is representing a bank account with the supported operations of
     withdrawing, depositing, transfers, checking balance and showing history of operations"""

    def __init__(self, name, balance, currency):
        if balance < 0 or not name or not currency:
            raise ValueError("Not enough or not supported input data")
        self.name = name
        self.account_balance = balance
        self.currency = currency
        self.account_history = ["Account was created"]

    def __str__(self):
        return "Bank account for %s with balance of %s%s" % (self.name, self.account_balance, self.currency)

    def __int__(self):
        self.account_history.append("__int__ check -> %s%s" % (self.account_balance, self.currency))
        return self.account_balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Negative amount for deposit is not supported")
        self.account_balance += amount
        self.account_history.append("Deposited %s%s" % (amount, self.currency))

    def balance(self):
        self.account_history.append("Balance check -> %s%s" % (self.account_balance, self.currency))
        return self.account_balance

    def withdraw(self, amount):
        if not self.account_balance > amount:
            self.account_history.append("Withdraw for %s%s failed" % (amount, self.currency))
            return False
        self.account_balance -= amount
        self.account_history.append("%s%s was withdrawn" % (amount, self.currency))
        return True

    def transfer_to(self, account, amount):
        if not self.currency == account.currency:
            raise TypeError("Transfer between accounts with different currencies not supported")
        if not self.account_balance > amount:
            raise TypeError("Insufficient funds")
        account.deposit(amount)
        self.account_balance -= amount
        return True

    def history(self):
        return self.account_history
