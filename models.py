from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

item_order_table = db.Table("item_order_table",
                            db.Column("item_id",db.ForeignKey("items.id")),
                            db.Column("order_id",db.ForeignKey("orders.id"))
                            )


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer,
                   primary_key=True)
    img = db.Column(db.String(200))
    name = db.Column(db.String(150))
    description = db.Column(db.Text)
    price = db.Column(db.Float)
    vendor = db.Column(db.String(200))

    def __str__(self):
        return self.name

    def get_message_text(self):
        message_text = f"""
Назва товару {self.name}
Вартість товару {self.price}
"""
        return message_text

class Admin(db.Model,
            UserMixin):
    __tablename__ = "admins"
    id = db.Column(db.Integer,
                   primary_key=True)
    login = db.Column(db.String(250),index=True)
    password = db.Column(db.String(250),index=True)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer,
                   primary_key=True)
    phone_or_email = db.Column(db.String(250),info={"label":"Телефон або email"})
    name = db.Column(db.String(250),info={"label":"Ім'я"})
    last_name = db.Column(db.String(300),info={"label":"Прізвіще"})
    date = db.Column(db.DateTime,default=datetime.now)
    price = db.Column(db.Float)
    items = db.relationship("Item",
                            secondary=item_order_table)

    def get_message_text(self):
        message_text = f"""
Від {self.name}   {self.last_name}
Було отримано {self.date}
Ціна замовлення {self.price}
Дані користувача {self.phone_or_email}
"""
        for item in self.items:
            message_text += item.get_message_text()
        return message_text




    
