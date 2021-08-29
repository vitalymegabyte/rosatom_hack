from django.contrib import admin

# Register your models here.
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'latitude', 'longitude', 'gender', 'age')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'post')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'place', 'sum')


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('id', 'post',)


@admin.register(Realty)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'sum', 'place', 'latitude', 'longitude', 'square')

# @admin.register(Quotes)
# class QuotesAdmin(admin.ModelAdmin):
#     list_display = ('pair', 'quote', 'is_full')
#
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ('external_id', 'name', 'numQuestionProfile', 'typeOfProfile')