from django.contrib import admin
from django.urls import path
from quizapp.views import Home, QuizView, QuizDataView, QuizSaveView, LoginView, LogoutView, SignupView, ResultsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
    path('<int:pk>/data/', QuizDataView.as_view(), name='quiz-data'),
    path('<int:pk>/save/', QuizSaveView.as_view(), name='quiz-save'),
    path('results/', ResultsView.as_view(), name='results'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),

]
