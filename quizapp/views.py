from django.shortcuts import render
from django.views import View
from .models import Quiz, Savol, Javob

class Home(View):
    def get(self, request):
        quiz = Quiz.objects.all()
        return render(request, 'index.html', {"quiz":quiz})

class QuizView(View):
    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        return render(request, 'quiz.html', {"quiz":quiz})