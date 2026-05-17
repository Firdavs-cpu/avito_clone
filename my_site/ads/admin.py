from django.contrib import admin
from .models import Category, AD, AdImage



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Автоматически заполняет поле slug при вводе названия категории
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('name', 'slug')


class AdImageLine(admin.TabularInline):
    model = AdImage
    extra = 3


@admin.register(AD)
class AdAdmin(admin.ModelAdmin):
    # Какие поля отображать в списке всех объявлений
    list_display = ('title', 'price', 'category', 'author', 'is_active', 'created_at')
    
    # По каким полям можно кликнуть, чтобы перейти в детальный просмотр
    list_display_links = ('title',)
    
    # Фильтры в правой колонке
    list_filter = ('category', 'is_active', 'created_at')
    
    # Поля, по которым будет работать поиск
    search_fields = ('title', 'description')
    
    # Позволяет менять статус "активно/не активно" прямо из списка
    list_editable = ('is_active',)

    inlines = [AdImageLine]



