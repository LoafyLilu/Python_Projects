from django.urls import path

from . import views

urlpatterns = [
    path('', views.sailorscouts_home, name="sailorscouts_home"),
    path('scout-create/', views.sailorscouts_add, name="sailorscouts_add"),
    path('scout-list/', views.sailorscouts_list, name="sailorscouts_list"),
    path('<int:pk>/scout-detail/', views.sailorscouts_detail, name="sailorscouts_detail"),
    path('<int:pk>/scout-edit/', views.sailorscouts_edit, name="sailorscouts_edit"),
    path('<int:pk>/scout-delete/', views.sailorscouts_delete, name="sailorscouts_delete"),

]
