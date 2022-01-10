from django import forms

from .models import CHOOSE_CATEGORY


class ProductForm(forms.Form):
    product = forms.CharField(max_length=100, required=True, label="Название")
    category = forms.ChoiceField(choices=CHOOSE_CATEGORY, required=True,
                                 label='Категория', initial=CHOOSE_CATEGORY[0])
    description = forms.CharField(max_length=2000, required=False, label='Описание',
                                  widget=forms.Textarea)
    balance = forms.IntegerField(required=True, label='остаток', min_value=0)
    price = forms.DecimalField(required=True, label='цена', max_digits=7, decimal_places=2, min_value=0)
