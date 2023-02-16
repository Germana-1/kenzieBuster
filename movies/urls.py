from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("movies/", views.MovieView.as_view()),
    path("movies/<int:movie_id>/", views.MovieDetailView.as_view()),
    path("movies/<int:movie_id>/orders/", views.MovieOrderView.as_view()),
]
