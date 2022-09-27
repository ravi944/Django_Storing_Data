from django.db import models



class Employees(models.Model):
    c1 = (
        ('IN', 'INDIA'),
        ('USA', 'AMERICA'),
        ('RUS', 'RUSSIA'),
        ('AUSTR', 'AUSTRALIA'),
    )
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    salary = models.CharField(max_length=10)
    phone = models.CharField(max_length=11)
    country = models.CharField(max_length=20, choices=c1, default=None)

    def __str__(self):
        return self.middle_name






