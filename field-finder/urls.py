from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='finder-home'),
    path('home/', views.home, name='finder-home'),
    path('institutions/', views.institutions, name='finder-institutions'), 
    path('majors/', views.majors, name='finder-majors'), 
    path('merit/', views.merit, name='finder-merit'),  
    path('new/', views.new, name='finder-new'), 
    path('quiz/', views.quiz, name='finder-quiz'), 

]
