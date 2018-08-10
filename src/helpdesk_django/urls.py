from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='tickets/', permanent=False), name='index'),
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
]
