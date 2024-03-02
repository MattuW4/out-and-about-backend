from django.urls import path
from attending import views

urlpatterns = [
    path('attending/', views.AttendList.as_view()),
    path('attending/<int:pk>/', views.AttendDetail.as_view()),
]