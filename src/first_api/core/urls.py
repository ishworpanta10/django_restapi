
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_view.as_view(), name="test"),

]
