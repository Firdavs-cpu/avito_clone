from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# Задаем пространство имен для приложения (чтобы ссылки не путались)
app_name = 'ads'

urlpatterns = [
    # Пустой путь '' означает главную страницу нашего приложения (http://127.0.0)
    path('', views.index, name='index'),
    path('ad/<int:pk>/', views.ad_detail, name='ad_detail'),
    path('register/', views.RegisterView.as_class_view() if hasattr(views.RegisterView, 'as_class_view') else views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='ads/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='ads:index'), name='logout'),
]
