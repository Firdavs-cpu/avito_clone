from django.shortcuts import render
from .models import AD

def index(request):
    all_ads = AD.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('images').order_by('-created_at')
    context = {
        'ads': all_ads
    }
    # Указываем путь 'ads/index.html' вместо просто 'index.html'
    return render(request, 'ads/index.html', context)
