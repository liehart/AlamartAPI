from django import forms

from AlamartAPI.items.models import Item


class ItemForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Item
        fields = '__all__'
