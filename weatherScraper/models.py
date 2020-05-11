from django.db import models

# Create your models here.
class WeatherQuery(models.Model):
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.location

    class Meta:
        verbose_name_plural = "Weather Queries"