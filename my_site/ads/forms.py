from django import forms
from .models import AD

class AdForm(forms.ModelForm):
    class Meta:
        model = AD
        # Поля, которые пользователь ЗАПОЛНЯЕТ САМ.
        # Мы НЕ добавляем сюда author и is_active, их мы пропишем кодом автоматически!
        fields = ['category', 'title', 'description', 'price']
