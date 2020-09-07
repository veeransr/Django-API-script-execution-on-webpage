from django.urls import path
from . import views
# from django.conf.urls import url

urlpatterns = [
    path('', views.text_repeater),
    path('snippet', views.snippet_details),
    path('external', views.external),

]
