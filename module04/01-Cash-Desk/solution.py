class Bill:
    """Bill represents a single bill"""
    def __init__(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount should be of type int")
        if amount < 0:
            raise ValueError("Negative amount is not supported")
        self.amount = amount

    def __str__(self):
        return "A %s$ bill" % self.amount

    def __repr__(self):
        return 'Bill(amount=%s)' % self.amount

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def __lt__(self, other):
        return self.amount < other.amount


class BatchBill:
    """BatchBill represents a batch of bills"""
    def __init__(self, batch):
        self.batch = batch

    def __len__(self):
        return len(self.batch)

    def __getitem__(self, index):
        return self.batch[index]

    def total(self):
        total = 0
        for bill in self.batch:
            total += bill.amount
        return total


class CashDesk:
    """CashDesk represents a simple cash desk"""
    def __init__(self):
        self.cash = {}

    def take_money(self, money):
        if isinstance(money, Bill):
            self.add_money_to_cash_desk(money)
        if isinstance(money, BatchBill):
            for bill in money:
                self.add_money_to_cash_desk(bill)

    def total(self):
        total = 0
        for bill in self.cash:
            bill_sum = self.cash.get(bill) * bill.__int__()
            total += bill_sum
        return total

    def inspect(self):
        result = "We have a total of %s$ in the desk" \
                 "\nWe have the following count of bills, " \
                 "sorted in ascending order:" % self.total()
        for bill in sorted(self.cash):
            result += "\n%s$ bills - %s" % (bill.__int__(), self.cash.get(bill))
        return result

    def add_money_to_cash_desk(self, money):
        if self.cash.__contains__(money):
            self.cash[money] += 1
        else:
            self.cash[money] = 1
