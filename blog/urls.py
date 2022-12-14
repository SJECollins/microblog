from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('add', views.add, name='add'),
    path('delete/<post_id>', views.delete, name='delete')
]
