from . import views
from django.urls import path


urlpatters = [
    path('', views.PostList.as_view(), name='home'),
]
