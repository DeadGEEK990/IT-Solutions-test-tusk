from dal import autocomplete
from django.template.defaulttags import comment

from .models import (
    StatusCashFlow,
    TypeCashFlow,
    CategoryCashFlow,
    SubcategoryCashFlow,
    CashFlow,
)
from django.contrib import admin
from .forms import CashFlowForm


# Показывает только те подкатегории, которые относят к выбранной категории
class SubcategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = SubcategoryCashFlow.objects.all()

        category_id = self.forwarded.get("category", None)
        if category_id:
            qs = qs.filter(category_cash_flow_id=category_id)
        return qs


# Показывает только те категории, которые относятся к выбранному типу
class CategoryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = CategoryCashFlow.objects.all()

        type_id = self.forwarded.get("type_flow", None)
        if type_id:
            qs = qs.filter(type_cash_flow_id=type_id)
        return qs


@admin.register(StatusCashFlow)
class StatusCashFlowAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(TypeCashFlow)
class TypeCashFlowAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CategoryCashFlow)
class CategoryCashFlowAdmin(admin.ModelAdmin):
    list_display = ("name", "type_cash_flow")
    list_filter = ("type_cash_flow",)
    search_fields = ("name",)


@admin.register(SubcategoryCashFlow)
class SubcategoryCashFlowAdmin(admin.ModelAdmin):
    list_display = ("name", "category_cash_flow")
    list_filter = ("category_cash_flow",)
    search_fields = ("name",)


@admin.register(CashFlow)
class CashFlowAdmin(admin.ModelAdmin):
    form = CashFlowForm
    list_display = (
        "date",
        "status",
        "type_flow",
        "category",
        "subcategory",
        "amount",
        "comment",
    )
    list_filter = (
        ("date", admin.DateFieldListFilter),
        "status",
        "type_flow",
        "category",
        "subcategory",
    )
    search_fields = (
        "comment",
        "status__name",
        "type_flow__name",
        "category__name",
        "subcategory__name",
    )
