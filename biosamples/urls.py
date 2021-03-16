from django.urls import path 

from . import views 

app_name = 'biosamples'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('add', views.BiosampleView.as_view(), name='biosample-add'),
]