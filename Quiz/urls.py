from django.contrib import admin
from django.urls import path
from quizapp.views import Home, QuizView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),
    path('<int:pk>/', QuizView.as_view(), name='quiz'),
]
