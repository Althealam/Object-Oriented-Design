# Order and Orderitem

# order->items(list)->orderitem("Apple")
#                   ->orderitem("Banana")
class OrderItem:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

class Order:
    def __init__(self):
        # Order内部唯一持有OrderItem的引用
        self.items = []
    
    def add_item(self, product_name, price):
        self.items.append(OrderItem(product_name, price))
    
    def total_price(self):
        return sum(item.price for item in self.items)

order = Order()
order.add_item("Apple", 3)
order.add_item("Banana", 2)
print(order.items)
