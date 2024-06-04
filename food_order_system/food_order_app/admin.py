from django.contrib import admin
from .models import VacancyTable, FoodCategory, FoodItems, UserData, TableAnalytics

# Register your models here.

@admin.register(VacancyTable)
class VacancyTableAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_no', 'status')
    list_filter = ('status',)
    search_fields = ('table_no', 'status')

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'category_name', 'added_by', 'created_at', 'updated_at')
    search_fields = ('category_name', 'added_by')

@admin.register(FoodItems)
class FoodItemsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'food_item_name', 'category_id', 'price', 'created_at', 'updated_at')
    list_filter = ('category_id',)
    search_fields = ('food_item_name',)

@admin.register(UserData)
class UserDataAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'mobile_no', 'user_id', 'role', 'created_at', 'updated_at')
    search_fields = ('email', 'mobile_no', 'user_id', 'role')

@admin.register(TableAnalytics)
class TableAnalyticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'table_no', 'customer_name', 'total_amt', 'payment_mode', 'created_at', 'updated_at')
    list_filter = ('table_no', 'payment_mode')
    search_fields = ('table_no', 'customer_name')

