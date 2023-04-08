from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/posts/', include('posts.urls')),
    path('api/v1/topposts/', include('topposts.urls')),
    path('api/v1/comments/', include('comments.urls')),
    path('', include('main.urls')),
]