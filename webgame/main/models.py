from django.db import models

class Users(models.Model):
    Name = models.CharField(verbose_name="Имя", max_length=200)
    Level = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Уровень")
    Experience = models.DecimalField(max_digits=20, decimal_places=2)

class Resources(models.Model):
    Resource = models.CharField(verbose_name="Ресурс", max_length=200)
    Price = models.IntegerField(verbose_name="Цена")
    Efficiency = models.IntegerField(verbose_name="Производство в мин")
    Is_created = models.BooleanField()

    def __str__(self):
        return f"{self.Resource}"
    class Meta:
         verbose_name_plural="Ресурсы"

class Users_resources(models.Model):
    Resource = models.ForeignKey('Resources', on_delete=models.DO_NOTHING)
    Sum = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Количество")
    Is_active = models.BooleanField()
    User = models.ForeignKey('Users', default='null', on_delete=models.DO_NOTHING, )
    
class Fabric(models.Model):
    name = models.CharField(verbose_name="Название", max_length=200)
    used_resource = models.ForeignKey('Resources', on_delete=models.DO_NOTHING)
    Product = models.ManyToManyField('Resources', related_name='product')
    Time = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Время изготовления")
    Level = models.IntegerField()
    User = models.ForeignKey('Users', on_delete=models.DO_NOTHING)
    is_active = models.BooleanField()

class Workers(models.Model):
    id = models.AutoField(primary_key=True)
    Level = models.IntegerField(verbose_name="Уровень")
    Price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Цена")
    Created_resource = models.ForeignKey('Resources', verbose_name="Производимый ресурс", on_delete=models.DO_NOTHING)
    User = models.ForeignKey('Users', default='null', on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.Created_resource}/{self.Level}"
