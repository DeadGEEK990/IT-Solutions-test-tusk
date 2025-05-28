from dal import autocomplete
from django import forms
from .models import CashFlow, SubcategoryCashFlow


class CashFlowForm(forms.ModelForm):
    """Модель ДДС для админки"""

    class Meta:
        model = CashFlow
        fields = "__all__"
        widgets = {
            "subcategory": autocomplete.ModelSelect2(
                url="subcategory-autocomplete",
                forward=["category"],
            ),
            "category": autocomplete.ModelSelect2(
                url="category-autocomplete",
                forward=["type_flow"],
            ),
        }
