from django.db import models
import uuid

# Define models

class Hotel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel_name = models.CharField(max_length=255)
    hotel_reg_num = models.CharField(max_length=255)
    hotel_gst_num = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    mobile_num = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    number_of_table = models.IntegerField()
    owner_name = models.CharField(max_length=255)
    subscription_status = models.BooleanField(default=False)
    subscription_plan = models.CharField(max_length=255)
    subscription_start_date = models.DateTimeField()
    subscription_end_date = models.DateTimeField()
    subscription_payment_mode = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.hotel_name


class VacancyTable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    status = models.CharField(max_length=255)
    food_order = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Table {self.table_number} at {self.hotel.hotel_name}"


class FoodCategory(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    category_name = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Categories at {self.hotel.hotel_name}"


class FoodItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    food_item_name = models.CharField(max_length=255)
    full_price = models.FloatField()
    half_price = models.FloatField()
    category_name = models.CharField(max_length=255)
    food_type = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.food_item_name
