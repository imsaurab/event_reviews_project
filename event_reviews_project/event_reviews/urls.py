from django.urls import path
from .views import ReviewListCreateAPIView, ReviewRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('events/<int:event_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('events/<int:event_id>/reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-detail'),
    ]