from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
admin.autodiscover()
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.button),
    path('output/', views.output, name="script"),
    path('external/', include('myapp.urls')),

    path('area_of_triangle/', include('myapp.urls')),
    path('admin/', admin.site.urls),
    path('convert_to_seconds/', include('convert_to_seconds.urls')),
    path('find_max_edge/', include('find_max_edge.urls')),
    path('text_repeater/', include('text_repeater.urls')),
    path('result/', include('myapp.urls')),
]

