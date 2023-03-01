from .forms import SignUpForm
from django.contrib.auth import login as auth_login
from django.views.generic import CreateView,UpdateView,TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
# Create your views here.

class HelloView(TemplateView):
    template_name = "users_accounts/hello.html"



class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "users_accounts/signup.html"
    success_url=reverse_lazy('home')


class UserUpdateView(UpdateView):
    model=User
    template_name='users_accounts/my_account.html'
    fields=('first_name','last_name','email')
    success_url=reverse_lazy('my_account')
    def get_object(self):
        return self.request.user