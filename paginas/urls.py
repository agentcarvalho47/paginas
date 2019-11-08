from django.urls import path

from .views import HomePageView
from .views import SobrePageView
urlpatterns = [
    path('', HomePageView.as_view(), name ='home'),
    path('sobre', SobrePageView.as_view(), name = 'sobre')
]