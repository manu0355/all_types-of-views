from listviews.models import Category, Book
from listviews.serializer import CategorySerializer, Bookserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# from django.db import IntegrityError



class Bookviewset(viewsets.ModelViewSet):
    serializer_class = Bookserializer
    def get_queryset(self):
        query_book = Book.objects.all()
        return query_book
    
    #single view
    def retrieve(self, request,pk, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        # params_list = params['pk'].split('-')
        book = Book.objects.filter(b_name = params['pk'])
        serializer = Bookserializer(book,many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        book_request = request.data
        new_book = Book.objects.create(b_name= book_request['b_name'], author = book_request['author'])
        new_book.save()
        serializer = Bookserializer(new_book)
        return Response(serializer.data, status= status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        pass