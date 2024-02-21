from django.db import models


class Catalog(models.Model):
    # Определите поля модели, соответствующие полям вашей таблицы
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    value = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)

    class Meta:
        managed = False  # Указывает Django не управлять созданием таблицы
        db_table = 'products'

