from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
	path('albums/', views.albums, name='albums'),
    # ex: /polls/5/
    path('albums/<int:album_id>/', views.detail, name='detail'),
]
