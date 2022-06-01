from django.shortcuts import render
from rest_framework import viewsets

from titles.models import Category, Genre, Title
from .serializers import TitleSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
