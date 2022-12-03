from django.contrib import admin
from django.urls import include, path
from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# If you're intending to use the browsable API you'll probably also want to add REST framework's login and logout views
urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('catalog/', include('catalog.urls')),

     ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
