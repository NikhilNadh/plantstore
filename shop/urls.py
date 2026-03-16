from django.urls import path
from . import views

urlpatterns = [

    path('', views.index_view, name='index'),  # HOME PAGE

    path('store/', views.plant_list, name='plant_list'),
    path('plant/<int:id>/', views.plant_detail, name='plant_detail'),

    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]