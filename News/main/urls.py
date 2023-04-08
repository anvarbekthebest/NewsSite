from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index, contact, BlogSingle, categories, CategoryDetail


urlpatterns = [
    path('', index, name="index"),
    path('categories/', categories, name="category"),
    path('singlenews/<slug:slug>', BlogSingle.as_view(), name="single"),
    path('contact/', contact, name="contact"),
    path("cat/<slug:cat_slug>/", CategoryDetail.as_view(), name="cat_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
