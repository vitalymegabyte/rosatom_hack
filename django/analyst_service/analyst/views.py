from django.shortcuts import render
from rest_framework import generics

from .models import Post, User, Like, Transaction
from .serializers import *


class PostCreateView(generics.CreateAPIView):
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer


class LikeListView(generics.ListAPIView):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserSerializer