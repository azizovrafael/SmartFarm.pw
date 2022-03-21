from rest_framework import generics, status, filters
from rest_framework.parsers import MultiPartParser
from .models import Arduino_Data
from .serializer import Arduino_Serializer
from rest_framework.response import Response


# class Arduino_View(generics.ListCreateAPIView):
#     parser_classes = (MultiPartParser,)
#     queryset = Arduino_Data.objects.all()
#     serializer_class = Arduino_Serializer
#
#     def post(self, request, *args, **kwargs):
#         queryset = Arduino_Data.objects.all()
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # data = serializer.save()
#             # data.id = len(queryset)+1
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Arduino_View(generics.ListCreateAPIView):
    filter_backends = (filters.SearchFilter,)
    search_fields = ['id']
    queryset = Arduino_Data.objects.all()
    serializer_class = Arduino_Serializer