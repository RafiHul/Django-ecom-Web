# Generated by Django 4.2.5 on 2023-11-15 02:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasehistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(blank=True)),
                ('address', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('total_paid', models.IntegerField(blank=True)),
                ('is_paid', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('product_name', models.ForeignKey(db_column='product_name', on_delete=django.db.models.deletion.CASCADE, related_name='product_name', to='core.produk')),
            ],
        ),
    ]
