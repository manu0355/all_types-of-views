from listviews.models import Category, Book
from listviews.serializer import CategorySerializer, Bookserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def get_book(request):
    query_book = Book.objects.all()
    serializer = Bookserializer(query_book, many=True)
    return Response(serializer.data, status = status.HTTP_200_OK)
@api_view(['POST'])
def post_book(request):
    serializer = Bookserializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response("please enter valid details", status = status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_book(request,pk):
    book_query = Book.objects.get(pk=pk)
    serializer = Bookserializer(book_query, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    return Response("please update correct information", status = status.HTTP_400_BAD_REQUEST)