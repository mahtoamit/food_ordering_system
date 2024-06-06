from django.contrib import admin
from .models import Hotel, VacancyTable, FoodCategory, FoodItem

# Register your models here.

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = (
        'hotel_name', 'hotel_reg_num', 'hotel_gst_num', 'address', 'mobile_num',
        'email', 'number_of_table', 'owner_name', 'subscription_status',
        'subscription_plan', 'subscription_start_date', 'subscription_end_date',
        'subscription_payment_mode', 'created_at', 'updated_at'
    )
    search_fields = ('hotel_name', 'owner_name', 'email', 'hotel_reg_num', 'hotel_gst_num')
    list_filter = ('subscription_status', 'subscription_plan', 'subscription_payment_mode')


@admin.register(VacancyTable)
class VacancyTableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'hotel', 'status', 'created_at', 'updated_at')
    list_filter = ('status',)
    search_fields = ('table_number', 'hotel__hotel_name')


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'hotel', 'created_at', 'updated_at')
    search_fields = ('category_name', 'hotel__hotel_name')


@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('food_item_name', 'category_name', 'hotel', 'full_price', 'half_price', 'created_at', 'updated_at')
    list_filter = ('category_name', 'hotel__hotel_name')
    search_fields = ('food_item_name', 'category_name__category_name')