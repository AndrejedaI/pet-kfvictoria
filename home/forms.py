from django import forms
from .models import Brand, Category


class ProductFilterForm(forms.Form):
    brand = forms.ModelMultipleChoiceField(
        queryset=Brand.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'cu_chbox'}),
        label='Бренд'
    )

    category = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'cu_chbox'}),
        label='Категория'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].label_from_instance = lambda obj: obj.name  # ← ключ