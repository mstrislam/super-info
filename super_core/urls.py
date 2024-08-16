

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static, settings
from info.views import HomeView, ContactView, PublicDetailView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name = 'home-list'),
    path('home_search/', HomeView.as_view(), name= 'home-search'),
    path('contact/', ContactView.as_view(), name = 'contact-list'),
    path('public_detail/<int:pk>', PublicDetailView.as_view(), name = 'detail-list')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

