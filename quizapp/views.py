from django.http import JsonResponse
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

class QuizDataView(View):
    def get(self, request, pk):
        quiz = Quiz.objects.get(id=pk)
        savollar = Savol.objects.filter(quiz=quiz)
        questions = []
        for s in savollar:
            answears = []
            javoblar = Javob.objects.filter(savol=s)
            for j in javoblar:
                answears.append(j.matn)
            questions.append({str(s):answears})
        return JsonResponse({
            'data': questions,
            'time': quiz.davomiyligi,
        })