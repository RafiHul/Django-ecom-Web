from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('rafih/admoon/', admin.site.urls),
    path('',include('core.urls')),
    path('',include('account.urls')),
    path('',include('purchase.urls')),
    path('items/',include("items.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
