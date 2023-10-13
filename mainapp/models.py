from django.db import models

MALE = 'Male'
FEMALE = 'Female'    
DEFAULT = 'Default'

GENDER = (
    (MALE,'Male'), 
    (FEMALE, 'Female'),
    (DEFAULT, 'Default')
    )

class Car(models.Model):
    mark = models.CharField(max_length=127, verbose_name='Mарка авто')
    year = models.DateField(verbose_name='Дата выпуска')
    color = models.CharField(max_length=127, verbose_name='Цвет авто')
    horse_power = models.PositiveIntegerField(default=0, verbose_name='Объём')

    def __str__(self):
        return f'{self.mark} {self.year} {self.color} {self.horse_power}'

    class Meta:
        verbose_name = 'Машину'
        verbose_name_plural = 'Машины'



class Person(models.Model):
    name = models.CharField(max_length=127)
    email = models.EmailField()
    last_name = models.CharField(max_length=127)
    age = models.PositiveIntegerField(default=0)
    gender = models.CharField(max_length=127,choices=GENDER)
    
    def __str__(self):
        return self.name