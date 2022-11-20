from django.contrib import admin
from django.urls import include, path
from polls import views
from catalog import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    #path('', views.index, name='index'),
     ]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
