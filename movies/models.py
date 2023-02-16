from django.db import models


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True)
    added_by = models.EmailField(max_length=127)
    rating = models.CharField(
        max_length=20,
        choices=RatingChoices.choices,
        default=RatingChoices.G,
    )
    synopsis = models.TextField(null=True)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
        null=True,
    )

    users = models.ManyToManyField(
        "users.User",
        related_name="movie_orders",
        through="movies.MovieOrder",
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user_movie_orders",
    )
    movie = models.ForeignKey(
        "movies.Movie",
        on_delete=models.CASCADE,
        related_name="movie_orders",
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
