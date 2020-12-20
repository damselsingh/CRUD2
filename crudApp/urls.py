from django.urls import path, include
from crudApp import views

urlpatterns = [
    path('',views.home.as_view(), name="home"),
    path('delete/<int:id>/', views.data_delete.as_view(), name="deletedata"),
    path('update/<int:id>/', views.update_data.as_view(), name="updatedata"),
]
