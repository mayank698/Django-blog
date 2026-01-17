from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from app import views as AppsView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("category/", include("app.urls")),
    path("<slug:slug>/", AppsView.blogs, name="blogs"),
    path("blogs/search/", AppsView.search, name="search"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
