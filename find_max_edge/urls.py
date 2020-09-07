from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.find_max_edge),
    path('snippet', views.snippet_details),
    path('external', views.external),

]
