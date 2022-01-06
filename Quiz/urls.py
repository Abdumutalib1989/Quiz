from django.contrib import admin
from django.urls import path
from quizapp.views import Home, QuizView, QuizDataView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
    path('<int:pk>/data/', QuizDataView.as_view(), name='quiz-data'),
    # path('<int:pk>/save/', QuizSaveView.as_view(), name='quiz-save'),
]
