from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('post/<int:pk>', views.post, name='post'),
    path('Category/<str:foo>', views.category, name='Category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('password', views.password, name='password'),
    path('search/', views.search, name='search'),
    path('request_user/', views.request_user, name='request_user'),
    path('pro/', views.pro, name='pro'),

 

    ]
    