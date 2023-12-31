# Generated by Django 4.2.5 on 2023-12-21 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=255)),
                ('field2', models.IntegerField()),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
