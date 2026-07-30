from django.urls import path
from . import views # . => current dir
app_name='myApp'
urlpatterns=[
    path('', views.index, name='index'),
    
    path('<int:id>/',views.detail, name='detail'),
    path('add/',views.create_item, name='create_item'),
]