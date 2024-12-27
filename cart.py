from models import Order
from models import db

class Cart:
    def __init__(self):
        self.items = []

    def numerated_items(self):
        return enumerate(self.items)
    
    def add_item(self,item):
        if item.id not in [item.id for item in self.items]:
            self.items.append(item)
        
    def clear(self):
        self.items.clear()

    def delete_item(self,number):
        self.items.pop(number)

    def get_price(self):
        price = 0
        for item in self.items:
            price += item.price
        return price

    def count(self):
        return len(self.items)


    def create_order(self,form_data):
        order = Order(name=form_data.get("name"),
                      last_name=form_data.get("last_name"),
                      price=self.get_price(),
                      phone_or_email=form_data.get("phone_or_email"))
        for item in self.items:
            order.items.append(item)
        db.session.add(order)
        db.session.commit()
        return order
        
    

def get_cart(session):
    if "cart" not in session:
        session["cart"] = Cart()
    return session["cart"]




