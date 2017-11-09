from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import LoginForm, SignupForm
from .models import Topic


def index(request):
    return render(request, 'polls/index.html', {})


class SigninView(generic.FormView):
    template_name = "polls/signin.html"
    form_class = LoginForm

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = User.objects.get(username=username)

        if user is not None and user.check_password(password):
            login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("polls:index")


def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse("polls:index"))


class SignupView(generic.FormView):
    template_name = "polls/signup.html"
    form_class = SignupForm

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        user = User.objects.create_user(username, email=email, password=password)
        login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse("polls:index")


class TopicsView(generic.ListView, LoginRequiredMixin):
    template_name = "polls/topics.html"
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.all()


class TopicView(generic.DetailView, LoginRequiredMixin):
    template_name = "polls/topic.html"
    model = Topic


def delete_topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    if request.user == topic.submitter:
        Topic.objects.get(pk=topic_id).delete()
    return render(request, 'polls/topics.html')
