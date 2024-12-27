from flask_login import LoginManager
from models import Admin

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(user_id)
