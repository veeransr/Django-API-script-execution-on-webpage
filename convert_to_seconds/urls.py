from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.convert_to_seconds),
    path('snippet', views.snippet_details),
    path('external', views.external),

]
