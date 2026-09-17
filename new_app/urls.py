from django.urls import path

from new_app import views

urlpatterns = [
path('abc',views.home,name='home'),
path('menu_data',views.menu_data,name='menu_data'),
path('',views.menu_view,name='menu_view'),
path('new',views.new,name='new'),
]