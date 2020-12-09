from django.shortcuts import render
from rest_framework import generics
from management.models import Book
from .serializers import BookSerializer
class BookAPIView(generics.ListAPIView):
    queryset: object = Book.objects.all()
    serializer_class = BookSerializer


# Create your views here.
