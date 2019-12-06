from django.views.generic import TemplateView, CreateView
from .models import Aluno
class HomePageView(TemplateView):
    template_name = "home.html"
# Create your views here.
class CadastroCreateView(CreateView): 
	model = Aluno
	template_name = 'cadastro.html' 
	fields = ['nome', 'email', 'senha', 'matricula']
class LoginPageView(TemplateView):
    template_name = "login.html"    
class SobrePageView(TemplateView):
	template_name = "sobre.html"
class AreaAlunoPageView(TemplateView):
	template_name = "areaaluno.html"
class LogaPageView(TemplateView):
	template_name = "logged.html"	
class AreaProfPageView(TemplateView):
	template_name = "areaprof.html"	

