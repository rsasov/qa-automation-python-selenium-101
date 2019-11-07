ZERO = 0


class Bill:

    def __init__(self, amount):
        self.checkParameter(amount)
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return 'Bill(amount=%s)' % self.amount

    def __int__(self):
        return int(self.amount)

    def __eq__(self, other):
        return self.__class__ == other.__class__ and self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def checkParameter(self, amount):
        if not isinstance(amount, int):
            raise TypeError("Amount should be int")
        if amount < ZERO:
            raise ValueError("Negative amount for Bill is not supported")


class BatchBill:

    def __init__(self, batch):
        self.batch = batch

    def __len__(self):
        return len(self.batch)

    def __getitem__(self, index):
        return self.batch[index]

    def total(self):
        total = ZERO
        for bill in self.batch:
            total += bill.amount
        return total


class CashDesk:

    def __init__(self):
        self.cash = []

    def take_money(self, money):
        if isinstance(money, Bill):
            self.cash.append(money)
        if isinstance(money, BatchBill):
            self.cash.extend(money)

    def total(self):
        total = ZERO
        for bill in self.cash:
            total += bill.amount
        return total

    def inspect(self):
        result = "We have a total of {}$ in the desk" \
                 "\nWe have the following count of bills, " \
                 "sorted in ascending order:".format(self.total())
        self.cash.sort(key=Bill.__int__)
        for element in range(ZERO, len(self.cash)):
            bill = self.cash[element]
            if self.cash.index(bill) < element:
                continue
            result += "\n{}$ bills - {}".format(bill.__int__(), self.cash.count(bill))
        return result
