from django import forms
from .models import Product


class CreateProductForm(forms.Form):
    name = forms.CharField(min_length=1, max_length=255, required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Enter product name'
                                                         }))
    description = forms.CharField(min_length=0, max_length=3000, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter description'
                                                                }))
    amount = forms.IntegerField(min_value=1, required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'placeholder': 'Enter product amount'
                                                              }))
    price = forms.IntegerField(min_value=1, required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Enter price in KZT'
                                                             }))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price', 'amount', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter posts title'}),
            'price': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Type something...'}),
            'amount': forms.TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': 'Type something...'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type something...'}),
            'category': forms.Select(attrs={'class': 'form-select'})
        }


