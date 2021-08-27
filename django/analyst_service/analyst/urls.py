from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('post/create/', PostCreateView.as_view()),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    path('post/all/', PostListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/all/', UserListView.as_view()),
    path('like/create/', LikeCreateView.as_view()),
    path('like/all/', LikeListView.as_view()),
    path('like/list/', get_like),
    path('transaction/create/', TransactionCreateView.as_view()),
    path('transaction/all/', TransactionListView.as_view()),
    path('user/update/', UserUpdateView.as_view()),

]