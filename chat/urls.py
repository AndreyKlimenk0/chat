from django.urls import path
from chat import views

urlpatterns = [
    path('messages/', views.MessageView.as_view()),
    path('messages/<int:pk>/', views.MessageDetailView.as_view()),
    path('messages/unread/', views.UnReadMessageView.as_view())
]
