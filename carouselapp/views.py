from rest_framework import generics, status
from rest_framework.response import Response

from .models import CarouselItem
from .serializers import CarouselItemSerializer


class CarouselItemListCreateView(generics.ListCreateAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "success": True,
            "error": False,
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "error": False,
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "error": True,
            "message": "Invalid data.",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)


class CarouselItemListAPIView(generics.ListAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "success": True,
            "error": False,
            "data": serializer.data
        })

    def create(self, request, *args, **kwargs):
        return Response({
            "success": False,
            "error": True,
            "message": "Method 'POST' not allowed on this endpoint."
        }, status=status.HTTP_405_METHOD_NOT_ALLOWED)



class CarouselItemDeleteView(generics.DestroyAPIView):
    queryset = CarouselItem.objects.all()
    serializer_class = CarouselItemSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        self.perform_destroy(instance)

        return Response({
            "success": True,
            "error": False,
            "detail": "Carousel item deleted successfully.",
            "deleted_item": serializer.data
        }, status=status.HTTP_204_NO_CONTENT)


