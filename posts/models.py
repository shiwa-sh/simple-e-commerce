from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.TextField()
    created_at = models.DateField("data published")
    modified_at = models.DateField("data published")
    discount = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
