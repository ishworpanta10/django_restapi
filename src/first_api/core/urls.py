
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('', views.test_view.as_view(), name="test"),
    path('', views.PostView.as_view(), name="post"),
    path('create/', views.PostCreateView.as_view(), name="post_create"),
    path('api/', views.Post.as_view(), name="api"),
    path('both/', views.PostViewCreate.as_view(), name="both"),
    path('api/token/', obtain_auth_token, name='auth-token'),



]
