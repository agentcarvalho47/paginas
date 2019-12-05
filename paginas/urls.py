from django.urls import path
from .views import HomePageView, CadastroCreateView, LoginPageView, SobrePageView, AreaAlunoPageView, LogaPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('cadastro', CadastroCreateView.as_view(), name='cadastro'),
    path('login', LoginPageView.as_view(), name='login'),
    path('sobre', SobrePageView.as_view(), name='sobre'),
    path('dashboard', AreaAlunoPageView.as_view(), name='dashboard'),
    path('sucessfull', LogaPageView.as_view(), name='sucessfull'),
    
]