from django.db import models


class Catalog(models.Model):
    # Определите поля модели, соответствующие полям вашей таблицы
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False  # Указывает Django не управлять созданием таблицы
        db_table = 'products'

