from django.urls import path
from .views import CarouselItemListCreateView, CarouselItemListAPIView, CarouselItemDeleteView

urlpatterns = [
    path('carousel-create/', CarouselItemListCreateView.as_view(), name='carousel-list-create'),
    path('carousel-list/', CarouselItemListAPIView.as_view(), name='carousel-list'),
    path('carousel-delete/<int:pk>/', CarouselItemDeleteView.as_view(), name='carousel-delete'),

]
