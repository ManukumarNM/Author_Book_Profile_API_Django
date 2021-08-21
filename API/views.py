from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from rest_framework import viewsets 
from .serializers import ProfileSerializer, AuthorSerializer, BookSerializer
from .models import Profile, Author, Book

# ModelViewSet is a special view that Django Rest Framework provides. It will handle GET and POST requests
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
