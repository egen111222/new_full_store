
from wtforms_alchemy import ModelForm
from models import Admin,Order

class AdminForm(ModelForm):
    class Meta:
        model = Admin

class OrderForm(ModelForm):
    class Meta:
        model = Order
        exclude = ['price']

