from django.contrib import admin
from .models import Produk
from account.models import UserProfile

admin.site.register(Produk)
admin.site.register(UserProfile)