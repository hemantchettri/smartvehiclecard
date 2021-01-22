from django.urls import path
from customer import views

 

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),
]