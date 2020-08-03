from django.urls import path
from .views import ProfileView, ProfileDetailView

urlpatterns = [
    path ('profile', ProfileView.as_view() ),
    path('profile/<str:id>', ProfileDetailView.as_view())
]


