from django.db import models

class Review(models.Model):
    movie = models.ForeignKey('Movie', related_name='reviews', on_delete=models.CASCADE)
    reviewer_name = models.CharField(max_length=100)
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.reviewer_name} - {self.rating}/5"
