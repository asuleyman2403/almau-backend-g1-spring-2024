from django import forms


class CreateProductForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(min_length=0, max_length=3000, required=False)
    amount = forms.IntegerField(min_value=1, required=True)
    price = forms.IntegerField(min_value=1, required=True)




