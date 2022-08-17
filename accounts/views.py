from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse


class SignupView(CreateView):
    form_class =UserCreationForm
    template_name = "registration/signup.html"
    success_url = reverse('login')
