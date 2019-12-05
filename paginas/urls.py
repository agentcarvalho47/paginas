from django.urls import path
from .views import HomePageView, CadastroCreateView, LoginPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cadastro', CadastroCreateView.as_view(), name='cadastro'),
    path('login', LoginPageView.as_view(), name='login'),

]