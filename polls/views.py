from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import LoginForm, SignupForm, TopicForm
from .models import Topic, Suggestion


def index(request):
    return render(request, 'polls/index.html', {})


class SigninView(generic.FormView):
    template_name = "polls/signin.html"
    form_class = LoginForm
    redirect_field_name = "next"

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = User.objects.get(username=username)

        if user is not None and user.check_password(password):
            login(self.request, user)

        return super().form_valid(form)

    def get_success_url(self):
        url = self.request.POST.get(self.redirect_field_name)
        if url is None:
            url = reverse("polls:index")
        return url


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


class TopicsView(LoginRequiredMixin, generic.CreateView):
    template_name = "polls/topics.html"
    form_class = TopicForm
    model = Topic

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["topics"] = Topic.objects.all().order_by("date_created")
        return data

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("polls:topics")


class TopicView(LoginRequiredMixin, generic.DetailView):
    template_name = "polls/topic.html"
    model = Topic

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["suggestions"] = Suggestion.objects\
            .filter(topic=self.object)\
            .annotate(score=Coalesce(Sum("vote__opinion"), 0))\
            .order_by("-score")
        return data


class EditTopicView(LoginRequiredMixin, generic.UpdateView):
    template_name = "polls/topic/edit.html"
    form_class = TopicForm
    model = Topic

    def get_success_url(self):
        return reverse("polls:topic", kwargs={"pk": self.object.id})


def delete_topic(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    if request.user == topic.submitter:
        topic.delete()
    return HttpResponseRedirect(reverse("polls:topics"))
