# Import necessary modules
from django.db import models

# Define models

class VacancyTable(models.Model):
    id = models.AutoField(primary_key=True)
    table_no = models.IntegerField(choices=[(i, i) for i in range(1, 21)])
    status = models.CharField(max_length=255)
    product_order = models.JSONField()

    def __str__(self):
        return f"Vacancy Table {self.table_no}"


class FoodCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    added_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.category_name


class FoodItems(models.Model):
    item_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(FoodCategory, on_delete=models.CASCADE, db_column='category_id')
    food_item_name = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    added_by = models.CharField(max_length=255)
    removed_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.food_item_name


class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    mobile_no = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_id


class TableAnalytics(models.Model):
    id = models.AutoField(primary_key=True)
    table_no = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    product_order = models.JSONField()
    total_amt = models.FloatField()
    payment_mode = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_received_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Analytics for Table {self.table_no}"

