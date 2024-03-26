class Coffee:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.orders if order.coffee == self]

    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)


class Customer:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not 1 <= len(name) <= 15:
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    def orders(self):
        return [order for order in Order.orders if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be an instance of Coffee")
        if not isinstance(price, (int, float)) or not 1.0 <= price <= 10.0:
            raise ValueError("Price must be a number between 1.0 and 10.0")
        new_order = Order(self, coffee, price)
        Order.orders.append(new_order)
        return new_order


class Order:
    orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.price = price
        self.__class__.orders.append(self)
