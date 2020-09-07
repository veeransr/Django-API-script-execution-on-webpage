from django.urls import path
from . import views


# from django.conf.urls import url

urlpatterns = [
    path('', views.area_of_triangle),
    path('snippet', views.snippet_details),
    path('result', views.result_for_Triangle_area.as_view(), name = 'result'),
    # path('output', views.output, name='script'),
    path('external', views.external),


]
