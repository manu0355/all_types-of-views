from listviews.models import Category, Book
from listviews.serializer import CategorySerializer, Bookserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

"""mixins supports python only and its also called multiple inheritance"""

"""a class that contains methods for use by other classes without having to be the parent class of those other classes"""
#only class based view

class Listbookmixin(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class Detailsbookmixin(mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):

    queryset = Book.objects.all()
    serializer_class = Bookserializer
                        
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)