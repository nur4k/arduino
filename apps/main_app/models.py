from django.db import models


class Driver(models.Model):
    fio = models.CharField(verbose_name='ФИО', max_length=155, null=True, blank=True)
    car_number = models.CharField(verbose_name='Номер машины', max_length=20, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.fio} -- {self.car_number}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None) -> None:
        self.car_number = self.car_number.upper()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class Item(models.Model):
    transmitter_id = models.CharField(verbose_name='ID передатчика', max_length=50, null=True, blank=True)  # Добавленное поле
    latitude = models.FloatField(verbose_name='Широта', null=True)  # Широта
    longitude = models.FloatField(verbose_name='Долгота', null=True)  # Долгота
    direction = models.FloatField(verbose_name='Направле', null=True)  # Направление
    speed = models.FloatField(verbose_name='Скорость', null=True)  # Скорость
    timestamp = models.DateTimeField(verbose_name='Дата и время', auto_now_add=True)  
    driver = models.OneToOneField(Driver, on_delete=models.CASCADE, null=True, blank=True)  # Связь OneToOne с моделью Location

    def __str__(self) -> str:
        return f'{self.transmitter_id} -- {self.speed}'
