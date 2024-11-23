
from django.contrib import admin
from django.urls import path
from taskWriter import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/' , views.getAllCategories),
    path('categories/<int:id>' , views.getbyId),
    path('upload/', views.upload_file, name='upload-file'),
    path('files/', views.get_files, name='get-files'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
