from django.db import models

class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel/')


    def __str__(self):
        return self.caption or str(self.id)
