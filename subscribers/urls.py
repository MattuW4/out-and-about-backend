from django.urls import path
from subscribers import views

urlpatterns = [
    path('subscribers/', views.SubsciberList.as_view()),
    path('subscribers/<int:pk>/', views.SubscriberDetail.as_view())
]


