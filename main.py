from flask import Flask
from dotenv import load_dotenv
import os
from models import db
from models import Item,Order
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from adapters import ItemView,AdminView
from item_part import item_app
from auth_lib import login_manager
from auth_part import auth_app
from flask_session import Session
from cart_part import cart_app
from mail_lib import mail,send_message
from flask_wtf.csrf import CSRFProtect

load_dotenv()

app = Flask(__name__,
            static_url_path="")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DB"]
app.config['FLASK_ADMIN_SWATCH'] = os.environ["DB_THEME"]
app.secret_key = os.environ["SECRET_KEY"]
app.config["SESSION_TYPE"] = os.environ["SESSION_TYPE"]

app.config["MAIL_SERVER"] = os.environ["MAIL_SERVER"]
app.config["MAIL_PORT"] = os.environ["MAIL_PORT"]
app.config["MAIL_USERNAME"] = os.environ["MAIL_USERNAME"]
app.config["MAIL_PASSWORD"] = os.environ["MAIL_PASSWORD"]
app.config["MAIL_USE_SSL"] = os.environ["MAIL_USE_SSL"]


csrf = CSRFProtect(app)
Session(app)

login_manager.init_app(app)
mail.init_app(app)


db.init_app(app)
with app.app_context():
    db.create_all()

    


app.register_blueprint(item_app)
app.register_blueprint(auth_app)
app.register_blueprint(cart_app,url_prefix="/cart")

admin = Admin(app,
              name='Інтернет Магазин',
              template_mode='bootstrap3')
admin.add_view(ItemView(Item, db.session))
admin.add_view(AdminView(Order, db.session))

if __name__ == "__main__":
    app.run()
