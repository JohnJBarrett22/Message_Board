from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('board', views.board),
    path('post', views.post),
    path('comment', views.comment),
    path('deleteMessage/<int:id>', views.deleteMessage),
    path('deleteComment/<int:id>', views.deleteComment)
]
