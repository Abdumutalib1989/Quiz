from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import Quiz, Savol, Javob, Foydalanuvchi


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

class QuizSaveView(View):
    def post(self, request, pk):
                if request:
                    questions = []
                    data = request.POST
                    data_ = dict(data.lists())

                    data_.pop('csrfmiddlewaretoken')

                    for k in data_.keys():
                        print('key: ', k)
                        question = Savol.objects.get(matn=k)
                        questions.append(question)

                    user = request.user
                    quiz = Quiz.objects.get(id=pk)

                    score = 0
                    marks = []
                    correct_answer = None

                    for q in questions:
                        a_selected = request.POST.get(q.matn)

                        if a_selected != "":
                            question_answers = Javob.objects.filter(savol=q)
                            for a in question_answers:
                                if a_selected == a.matn:
                                    if a.togri:
                                        score += 1
                                        correct_answer = a.matn
                                else:
                                    if a.togri:
                                        correct_answer = a.matn

                            marks.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
                        else:
                            marks.append({str(q): 'not answered'})

                    Foydalanuvchi.objects.create(quiz=quiz, user=user, natija=score)

                    return JsonResponse({'passed': True, 'score': score, 'marks': marks})

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        p = request.POST.get('password')
        l = request.POST.get('username')
        users = authenticate(request, username=l, password=p)
        if users is None:
            return redirect('login')
        else:
            login(request, users)
            return redirect('index')

class SignupView(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        user = User.objects.create_user(
            username=request.POST.get("username"),
            email=request.POST.get("email"),
            password=request.POST.get("password1"),
        )
        login(request, user)
        return redirect('index')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


# class ResultsView(View):
#     def get(self, request):

