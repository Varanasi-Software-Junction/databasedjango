
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path("",views.index),
	path("test/",views.test),
	path("insert/",views.insert),
]
