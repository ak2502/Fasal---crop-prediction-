from django.db import models

class soil(models.Model):
    SOIL_TYPE = [
        ('Black' , 'black soil'),
        ('Alluvial' , 'alluvial soil'),
        ('Loamy' , 'loamy soil'),
        ('Red' , 'red soil'),
    ]
    soil_type = models.CharField(max_length=8,choices=SOIL_TYPE)

    def __str__(self):
        return self.soil_type