from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('eventportal.urls')),
    path('jet/', include('jet.urls', 'jet')), 
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('members.urls'))
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
