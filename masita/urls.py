
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("masita", views.home, name="home"),
]
if settings.DEBUG:
   from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)




