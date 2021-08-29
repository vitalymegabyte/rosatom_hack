from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from .views import *

urlpatterns = [
    path('post/create/', PostCreateView.as_view(), ),
    path('post/detail/<int:pk>/', PostDetailView.as_view()),
    path('post-hash/', get_posts),
    path('post-hash/detail', get_post),
    path('post/all/', PostListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/all/', UserListView.as_view()),
    path('user/detail/<int:pk>/', UserDetailView.as_view()),
    path('like/create/', LikeCreateView.as_view()),
    path('like/all/', LikeListView.as_view()),
    path('hash/create/', HashCreateView.as_view()),
    path('hash/all/', HashListView.as_view()),
    path('like/list/', get_like),
    path('transaction/create/', TransactionCreateView.as_view()),
    path('transaction/all/', TransactionListView.as_view()),
    path('realty/all/', RealtyListView.as_view()),
    path('user/update/', UserUpdateView.as_view()),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='redoc'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
]
