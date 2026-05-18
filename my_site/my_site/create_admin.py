import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
django.setup()

from django.contrib.auth.models import User

# Создаем админа, только если его еще нет в базе
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'SuperPassword123')
    print("Суперпользователь успешно создан!")
else:
    print("Суперпользователь уже существует.")
