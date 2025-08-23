from django.db import models


# Create your models here.
class returnItemModel(models.Model):
    item_type = models.CharField(max_length=15)
    item_description = models.CharField(max_length=15)
    location_found = models.CharField(max_length=15)
    date_found = models.CharField(max_length=15)
    item_image = models.ImageField(upload_to="items", default="fallback.jpg")
    approval = models.BooleanField("approval", default=False)

    def __str__(self):
        return self.item_type
