from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('new/', views.new, name="new"),
    path('create/', views.create),
    path('<int:my_number>/', views.show),
    path('<int:my_number>/edit', views.edit),
    path('<int:my_number>/delete', views.destroy)
]