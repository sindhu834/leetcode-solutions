class Bank:
    def __init__(self, balance):
        # Initialize bank accounts with given balances
        self.balance = balance
        self.n = len(balance)  # number of accounts

    def transfer(self, account1, account2, money):
        # Check if both accounts exist
        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n):
            return False
        # Check if account1 has enough balance
        if self.balance[account1 - 1] < money:
            return False
        # Perform transfer
        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money
        return True

    def deposit(self, account, money):
        # Check if account exists
        if not (1 <= account <= self.n):
            return False
        # Deposit the money
        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        # Check if account exists
        if not (1 <= account <= self.n):
            return False
        # Check if there is enough balance
        if self.balance[account - 1] < money:
            return False
        # Withdraw the money
        self.balance[account - 1] -= money
        return True
