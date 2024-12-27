from flask import (Blueprint,
                   render_template,
                   session,
                   redirect,
                   url_for,
                   request)

from cart import get_cart
from models import Item,Order
from forms import OrderForm
from mail_lib import send_message
import os

cart_app = Blueprint('cart_app', __name__,
                     template_folder='templates')


@cart_app.route("/",methods=["GET","POST"])
def view_cart():
    form = OrderForm()
    cart = get_cart(session)
    if request.method == "POST":
        form_data = request.form
        order = cart.create_order(form_data)
        cart.clear()
        send_message("Нове замовлення на сайті",
                     order.get_message_text(),
                     [os.environ["MAIL_USERNAME"]])
        return render_template("thanks.html")
    return render_template("cart.html",
                           cart=cart,
                           form=form)



@cart_app.route("/add/<int:item_number>")
def add_item(item_number):
    cart = get_cart(session)
    item = Item.query.filter(Item.id == item_number).first()
    if item:
        cart.add_item(item)
    return redirect(url_for("cart_app.view_cart"))


@cart_app.route("/delete/<int:item_number>")
def delete_item(item_number):
    cart = get_cart(session)
    cart.delete_item(item_number)
    return redirect(url_for("cart_app.view_cart"))



