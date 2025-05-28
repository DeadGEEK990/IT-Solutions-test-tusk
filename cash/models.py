from django.db import models


class StatusCashFlow(models.Model):
    """Модель статуса ДДС"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class TypeCashFlow(models.Model):
    """Модель типа ДДС"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CategoryCashFlow(models.Model):
    """Модель категории ДДС"""

    name = models.CharField(max_length=255)
    type_cash_flow = models.ForeignKey(
        TypeCashFlow, on_delete=models.PROTECT, related_name="categories"
    )

    def __str__(self):
        return self.name


class SubcategoryCashFlow(models.Model):
    """Модель подкатегории ДДС"""

    name = models.CharField(max_length=255)
    category_cash_flow = models.ForeignKey(
        CategoryCashFlow, on_delete=models.PROTECT, related_name="subcategories"
    )

    def __str__(self):
        return self.name


class CashFlow(models.Model):
    """Модель ДДС"""

    date = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        StatusCashFlow, on_delete=models.PROTECT, related_name="cash_flows"
    )
    type_flow = models.ForeignKey(
        TypeCashFlow, on_delete=models.PROTECT, related_name="cash_flows"
    )
    category = models.ForeignKey(
        CategoryCashFlow, on_delete=models.PROTECT, related_name="cash_flows"
    )
    subcategory = models.ForeignKey(
        SubcategoryCashFlow, on_delete=models.PROTECT, related_name="cash_flows"
    )
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    comment = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.date.date()} - {self.amount} ₽"
