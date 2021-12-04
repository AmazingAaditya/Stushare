from django.urls import path

from . import views

urlpatterns = [
    path('find/', views.get, name="get"),
    path('find/item/<str:pk>/', views.itemView, name="itemView"),
    
    path('find/search/', views.itemSearch, name="itemSearch"),
    
    path('posts/', views.give, name="give"),
    path('posts/add/', views.itemAdd, name="itemAdd"),
    path('posts/edit/<str:pk>/', views.itemEdit, name="itemEdit"),
    path('posts/delete/<str:pk>/', views.itemDelete, name="itemDelete"),
   
]
