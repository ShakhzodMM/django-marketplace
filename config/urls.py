from django.contrib import admin
from django.urls import path, include

# Quyidagi ikkita importni qo'shing:
from django.conf import settings                                                            
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),  # Bosh sahifa uchun
    path('users/', include('users.urls',)),  # Foydalanuvchilar uchun URL manzillarini qo'shish
    path('users/', include('django.contrib.auth.urls')),  # Foydalanuvchilar uchun URL manzillarini qo'shish
    path('products/', include('products.urls')),
]

# Ushbu qatorni urls.py faylining eng oxiriga qo'shing:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)