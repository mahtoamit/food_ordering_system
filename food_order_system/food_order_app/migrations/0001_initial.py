# Generated by Django 4.2.13 on 2024-06-12 10:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hotel_name', models.CharField(max_length=255)),
                ('hotel_reg_num', models.CharField(max_length=255)),
                ('hotel_gst_num', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('mobile_num', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('number_of_table', models.IntegerField()),
                ('owner_name', models.CharField(max_length=255)),
                ('subscription_status', models.BooleanField(default=False)),
                ('subscription_plan', models.CharField(max_length=255)),
                ('subscription_start_date', models.DateTimeField()),
                ('subscription_end_date', models.DateTimeField()),
                ('subscription_payment_mode', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyTable',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('table_number', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
                ('food_order', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_order_app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('food_item_name', models.CharField(max_length=255)),
                ('full_price', models.FloatField()),
                ('half_price', models.FloatField()),
                ('category_name', models.CharField(max_length=255)),
                ('food_type', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_order_app.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food_order_app.hotel')),
            ],
        ),
    ]
