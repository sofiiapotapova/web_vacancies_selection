from django.db import models

# Create your models here.


class User(models.Model):
    # id = models.AutoField()
    first_name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Surname', max_length=30)
    city = models.CharField('City', max_length=20)
    # email = models.EmailField()

    def __str__(self):
        return self.first_name


