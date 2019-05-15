from django.contrib import admin
from django.urls import path
import wcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wcount.views.home, name='home'),
    path('about/', wcount.views.about, name='about'),
    path('result/', wcount.views.result, name='result'),
]
