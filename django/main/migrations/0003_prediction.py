# Generated by Django 5.1.3 on 2024-11-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('result', models.FloatField(verbose_name='Вероятность выигрыша')),
                ('section', models.CharField(max_length=256, verbose_name='Вид спорта')),
            ],
            options={
                'verbose_name': 'Предсказание',
                'verbose_name_plural': 'Предсказания',
            },
        ),
    ]