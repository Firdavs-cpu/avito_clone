from django.shortcuts import render, get_object_or_404
from .models import AD
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    all_ads = AD.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('images').order_by('-created_at')
    context = {
        'ads': all_ads
    }
    # Указываем путь 'ads/index.html' вместо просто 'index.html'
    return render(request, 'ads/index.html', context)

from django.shortcuts import render, get_object_or_404
from .models import AD


def ad_detail(request, pk):
    ad = get_object_or_404(AD.objects.prefetch_related('images'), pk=pk)
    
    context = {
        'ad': ad
    }
    return render(request, 'ads/ad_detail.html', context)


class RegisterView(generic.CreateView):
    form_class = UserCreationForm  # Используем стандартную форму регистрации Django
    template_name = 'ads/register.html'  # Путь к HTML-шаблону
    success_url = reverse_lazy('ads:login')  # Куда перенаправить после успешной регистрации (на страницу входа)
