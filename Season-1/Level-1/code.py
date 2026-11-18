'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    payments = total = Decimal(0)

    for item in order.items:
        amount = Decimal(str(item.amount))
        if not amount.is_finite() or abs(amount) > 100_000:
            if item.type == 'payment':
                continue
            return "Invalid item amount"
        if amount != amount.quantize(Decimal('0.01')):
            return "Invalid item amount"

        if item.type == 'payment':
            payments += amount
        elif item.type == 'product':
            if amount <= 0:
                return "Invalid product price"
            if type(item.quantity) is not int or not 1 <= item.quantity <= 100:
                return "Invalid product quantity"
            total += amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if abs(payments) > 1_000_000 or total > 1_000_000:
        return "Total amount payable for an order exceeded"

    net = payments - total
    if net != 0:
        return f"Order ID: {order.id} - Payment imbalance: ${net:.2f}"
    else:
        return "Order ID: %s - Full payment received!" % order.id
