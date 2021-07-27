from listviews.models import Category, Book
from listviews.serializer import CategorySerializer, Bookserializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

class Bookview(APIView):
     
    def get(self, request, *args, **kwargs):
        pagination_class = PageNumberPagination
        book_query = Book.objects.all()
        serializer = Bookserializer(book_query, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        
        serializer = Bookserializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response ("please enter valid book details", status = status.HTTP_406_NOT_ACCEPTABLE)
        
        

class Singlebookview(APIView):
    def get(self, request,pk):
        try:
            book_query = Book.objects.get(pk=pk)
            serializer = Bookserializer(book_query)
        except Book.DoesNotExist:
            return Response("entered book out of range", status = status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.data, status= status.HTTP_200_OK)
        
    
    def put(self, request,pk):
        book_query = Book.objects.get(pk=pk)
        serializer = Bookserializer(book_query, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response ("please enter valid book details", status = status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        login_required = authenticate(password=12345, username="bookview")
        if (login_required is not None):
            book_query = Book.objects.get(pk=pk)
            book_query.delete()
            return Response({"message":"successfully deleted by admin"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("please login before you delete the record")


class Booklistview(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    pagination_class = PageNumberPagination
    