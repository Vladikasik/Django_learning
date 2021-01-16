from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:article_id>/', views.detail, name='detail'),
]