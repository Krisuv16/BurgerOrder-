from django import forms
from .models import Burger,Size

# class BurgerForms(forms.Form):
#     topping1 = forms.CharField(label = "Topping1", max_length=150)
#     topping2 = forms.CharField(label = "Topping2", max_length=150)
#     size = forms.ChoiceField(label = "Size", choices=[('Small','Small'),('Medium','Medium'),('Large','Large')])
    
class BurgerForms(forms.ModelForm):
    class Meta:
        model = Burger
        fields = ['topping1','topping2','size']
        labels = {'topping1' : 'Topping 1', 'topping2':'Topping 2', 'size':'Size'}
class MultipleBurgerForms(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=12)