# forms.py
from django import forms
from .models import returnItemModel

class ReturnItemForm(forms.ModelForm):
    class Meta:
        model = returnItemModel
        fields = ['item_type', 'item_description', 'location_found', 'date_found', 'item_image']
