from collections import namedtuple
Customer = namedtuple('Customer', ['name', 'fidelity'])


class LineItem:
    def __init__(self, product, quantity, price) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None) -> None:
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discont = 0
        else:
            discont = self.promotion(self)
        return self.total() - discont

    def __repr__(self) -> str:
        return f'<Order total: {self.total()} due: {self.due()}>'


def fidelity_promo(order):
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

# we can add new promo strategy here


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [
    LineItem('banana', 4, .5),
    LineItem('apple', 10, 1.5),
    LineItem('watermellon', 5, 5.0),
]

print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))


print(globals())
