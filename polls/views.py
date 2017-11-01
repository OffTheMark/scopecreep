from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic

from .forms import LoginForm


@login_required
def index(request):
    return render(request, 'polls/index.html', {})


class LoginView(generic.FormView):
    template_name = "polls/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = User.objects.get(username=username)

        if user is not None and user.check_password(password):
            login(self.request, user)

        return super().form_valid(form)
