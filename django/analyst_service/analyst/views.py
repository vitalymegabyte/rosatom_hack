from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics

from .serializers import *


class PostCreateView(generics.CreateAPIView):
    """
    API View for creating posts
    """
    serializer_class = PostDetailSerializer


class PostListView(generics.ListAPIView):
    """
    API View for listing posts
    """
    serializer_class = PostListSerializer
    queryset = Post.objects.all()


class UserCreateView(generics.CreateAPIView):
    """
    API View for creating users
    """
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    """
    API View for listing users
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()


class LikeCreateView(generics.CreateAPIView):
    """
    API View for creating likes
    """
    serializer_class = LikeSerializer


class LikeListView(generics.ListAPIView):
    """
    API View for listing likes
    """
    serializer_class = LikeSerializer
    queryset = Like.objects.all()


class RealtyCreateView(generics.CreateAPIView):
    """
    API View for creating realty
    """
    serializer_class = RealtySerializer


class RealtyListView(generics.ListAPIView):
    """
    API View for listing realty
    """
    serializer_class = RealtySerializer
    queryset = Realty.objects.all()


class HashCreateView(generics.CreateAPIView):
    """
    API View for creating hash-tags
    """
    serializer_class = HashSerializer


class HashListView(generics.ListAPIView):
    """
    API View for listing hash-tags
    """
    serializer_class = HashSerializer
    queryset = Hashtag.objects.all()


class TransactionCreateView(generics.CreateAPIView):
    """
    API View for creating transactions
    """
    serializer_class = TransactionSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    API View for view detail user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostDetailView(generics.RetrieveAPIView):
    """
    API View for view detail post
    """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class TransactionListView(generics.ListAPIView):
    """
    API View for listing transactions
    """
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()


class UserUpdateView(generics.UpdateAPIView):
    """
    API View for update detail user
    """
    serializer_class = UserSerializer


def get_like(request) -> JsonResponse:
    """
    Function for getting list of likes on a separate hashtag
    :param request:
    :return: Response
    """
    hash_id = request.GET.get('hash_id')
    res = {}

    for i in Hashtag.objects.filter(id=hash_id):
        for like in Like.objects.filter(post=i.post):
            res.update({
                f'{like.id}': {
                    'user_id': like.user.id,
                    'date': like.date,
                    'post_id': like.post.id,
                }
            })

    return JsonResponse(res)


def get_posts(request) -> JsonResponse:
    """
    Function for getting list of post with hash-tags
    :param request:
    :return: Response
    """

    res = []

    for post in Post.objects.all():
        hashs = []
        for hash in Hashtag.objects.filter(post=post.id):
            hashs.append(hash.text)

        res.append({
            'id': post.id,
            'image': 'http://188.225.57.152:8005/media/' + f'{str(post.image)}',
            'title': f'{str(post.title)}',
            'text': post.text,
            'hashtags': hashs,

        })

    return JsonResponse({"res": res}, json_dumps_params={'ensure_ascii': False})


def get_post(request) -> JsonResponse:
    """
    Function for getting post by id with hash-tags
    :param request:
    :return: Response
    """

    post_id = request.GET.get('post_id')
    res = {}
    hashs = []
    post = Post.objects.get(id=post_id)

    for hash in Hashtag.objects.filter(post=post.id):
        hashs.append(hash.text)

    res.update({
        'id': post.id,
        'image': 'http://188.225.57.152:8005/media/' + f'{str(post.image)}',
        'title': f'{str(post.title)}',
        'text': post.text,
        'hashtags': hashs,

    })

    return JsonResponse(res, json_dumps_params={'ensure_ascii': False})
