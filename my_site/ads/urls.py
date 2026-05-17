from django.urls import path
from . import views

# Задаем пространство имен для приложения (чтобы ссылки не путались)
app_name = 'ads'

urlpatterns = [
    # Пустой путь '' означает главную страницу нашего приложения (http://127.0.0)
    path('', views.index, name='index'),
]
