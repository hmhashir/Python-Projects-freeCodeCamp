class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, desc=''):
        self.ledger.append({'amount': amount, 'description': desc})

    def withdraw(self, amount, desc=''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': desc})
        return True

    def get_balance(self):
        return sum(transaction['amount'] for transaction in self.ledger)

    def transfer(self, amount, category):
        if self.withdraw(amount, f'Transfer to {category.name}'):
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        stars = (30 - len(self.name)) // 2
        title = '*' * stars + self.name + '*' * stars
        result = title + '\n'
        
        for transaction in self.ledger:
            desc = transaction['description'][:23]
            amount = transaction['amount']
            result += f"{desc:<23}{amount:>7.2f}\n"
        
        result += f"Total: {self.get_balance():.2f}"
        return result


def create_spend_chart(categories):
    spending = []
    for category in categories:
        total = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total += abs(transaction['amount'])
        spending.append(total)

    total_spent = sum(spending)

    percentages = []
    for spent in spending:
        if total_spent == 0:
            percentages.append(0)
        else:
            percent = int((spent / total_spent) * 100)
            percentages.append((percent // 10) * 10)

    chart = 'Percentage spent by category\n'
    num_cats = len(categories)

    for level in range(100, -1, -10):
        chart += f"{level:>3}| "
        for percent in percentages:
            chart += 'o  ' if percent >= level else '   '
        chart += '\n'

    # Fix 1: num_cats * 3 + 1, not + 2
    chart += '    ' + '-' * (num_cats * 3 + 1) + '\n'

    max_len = max(len(category.name) for category in categories)
    for i in range(max_len):
        chart += '     '   # Fix 2: 5 spaces, not 4
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + '  '
            else:
                chart += '   '
        chart += '\n'

    return chart.rstrip('\n')


# Test
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

print(food)
print()
print(create_spend_chart([food, clothing]))