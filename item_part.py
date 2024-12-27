from flask import Blueprint,render_template
from models import db
from models import Item

item_app = Blueprint('item_app', __name__,
                     template_folder='templates')

@item_app.route("/")
def view_items():
    items = db.paginate(Item.query,per_page=20)
    return render_template("items.html",
                           items=items)


@item_app.route("/<int:item_number>")
def view_item(item_number):
    item = Item.query.filter(Item.id == item_number).first()
    return render_template("item.html",
                           item=item)
