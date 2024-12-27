from flask import Blueprint,render_template,request,redirect
from forms import AdminForm
from models import Admin
from flask_login import login_user

auth_app = Blueprint('auth_app', __name__,
                     template_folder='templates')


@auth_app.route("/login",methods=["GET","POST"])
def login():
    form = AdminForm()
    if request.method == "POST":
        form_data = request.form
        user = Admin.query\
               .filter(Admin.login == form_data.get("login"))\
               .filter(Admin.password == form_data.get("password"))\
               .first()
        if user:
            login_user(user)
            return redirect("/admin")
    return render_template("login.html",
                           form=form)
