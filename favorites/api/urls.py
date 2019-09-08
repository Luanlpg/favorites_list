from django.urls import path
from django.urls import include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('user/', views.UserView.as_view()),
    path('<str:token>/client/', views.ClientListView.as_view()),
    path('<str:token>/client/<str:email>/', views.ClientDetailView.as_view()),
    path('<str:token>/client/<str:email>/list/', views.FavoritesListView.as_view()),
]
