from django.db import models


class Product(models.Model):
    p_name = models.CharField(max_length=255)
    p_description = models.TextField()
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.p_name
