from django.shortcuts import render, get_object_or_404, redirect
from .models import AD, AdImage, Category
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required # Защита от гостей
from .forms import AdForm
from django.forms import inlineformset_factory

def index(request):
    all_ads = AD.objects.filter(is_active=True).select_related('author', 'category').prefetch_related('images').order_by('-created_at')
    category_slug = request.GET.get('category')
    if category_slug:
        all_ads = all_ads.filter(category__slug=category_slug)

    categories = Category.objects.all()
    context = {
        'ads': all_ads,
        'categories': categories,
        'current_category': category_slug
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




# Декоратор @login_required не пустит гостя на страницу добавления. Его перекинет на вход
@login_required
def ad_create(request):
    # Создаем фабрику формсет. Связываем модель AD с моделью AdImage. 
    # fields=['image'] означает, что мы просим только поле выбора файла. extra=3 — даем 3 поля для фото.
    AdImageFormSet = inlineformset_factory(AD, AdImage, fields=['image'], extra=3)

    if request.method == 'POST':
        form = AdForm(request.POST)
        # В формсет передаем и POST (текст), и FILES (картинки!)
        formset = AdImageFormSet(request.POST, request.FILES)
        
        if form.is_valid() and formset.is_valid():
            # Сохраняем объявление, привязываем автора
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
            
            # Привязываем загруженные картинки к только что созданному объявлению
            formset.instance = ad
            formset.save()
            
            return redirect('ads:index')
    else:
        form = AdForm()
        formset = AdImageFormSet() # Пустой набор форм для картинок при открытии страницы

    # Передаем и форму, и формсет в HTML
    return render(request, 'ads/ad_form.html', {'form': form, 'formset': formset})


