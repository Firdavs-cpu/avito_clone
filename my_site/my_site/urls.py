from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve  # ИСПРАВЛЕНО: Импортируем встроенный обработчик файлов
from django.urls import re_path       # Импортируем обработчик регулярных выражений


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ads.urls')),
        # ИСПРАВЛЕНО: Этот маршрут будет насильно отдавать медиа-файлы в любом режиме (даве при DEBUG=False)
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

]

# ИСПРАВЛЕНО: добавляем раздачу медиа-файлов (картинок) в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
