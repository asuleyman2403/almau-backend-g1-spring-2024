from django import forms


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
