# coding: utf-8

from rest_framework import serializers

from .models import User, Talk


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')


class TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = ('title', 'body', 'created_at', 'status', 'author')