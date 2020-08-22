from django.shortcuts import render, redirect
from questions.models import Question
from django.contrib import auth
from random import choice

# Homepage
def home(request):
    questions = Question.objects
    count = Question.objects.filter(status="PUB").count()
    if count > 0:
        random_question = choice(Question.objects.filter(status="PUB"))
        return render(request, "home.html", {"question": random_question})
    else:
        return render(
            request, "home.html", {"question": "What's your favorite question?"}
        )

