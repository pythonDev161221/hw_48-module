from django import forms

from .models import CHOOSE_CATEGORY


class ProductForm(forms.Form):
    product = forms.CharField(max_length=100, required=True, label="Название")
    category = forms.ChoiceField(choices=CHOOSE_CATEGORY, required=True,
                                 label='Категория', initial=CHOOSE_CATEGORY[0][1])
    description = forms.CharField(max_length=2000, required=False, label='Описание',
                                  widget=forms.Textarea)
    balance = forms.IntegerField(required=True, label='остаток')
    price = forms.DecimalField(required=True, label='цена', max_digits=7, decimal_places=2)
