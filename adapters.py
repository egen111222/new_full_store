from flask_admin.contrib.sqla import ModelView
from flask_admin.form.upload import ImageUploadField
from flask_login import current_user
from flask import redirect,url_for

class AdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth_app.login'))



class ItemView(AdminView):
    form_extra_fields = {
        'img': ImageUploadField(base_path="static")
    }
