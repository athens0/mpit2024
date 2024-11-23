from django.db import models

# Create your models here.
class Match(models.Model):
    date = models.DateTimeField("Дата и время")
    team1 = models.CharField("Команда 1", max_length=256)
    team2 = models.CharField("Команда 2", max_length=256)
    score1 = models.IntegerField("Счёт 1")
    score2 = models.IntegerField("Счёт 2")
    place = models.CharField("Место проведения", max_length=256)

    def __str__(self):
        return f"{self.date} - {self.team1} {self.score1} : {self.score2} {self.team2} - {self.place}"
    
    class Meta:
        verbose_name = "Матч"
        verbose_name_plural = "Матчи"

class Team(models.Model):
    name = models.CharField("Название", max_length=256)
    staff = models.TextField("Состав")

    def __str__(self):
        return f"{self.name}"
    
    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class Prediction(models.Model):
    date = models.DateField("Дата")
    result = models.FloatField("Вероятность выигрыша")
    section = models.CharField("Вид спорта", max_length=256)

    def __str__(self):
        return f"{self.date} {self.result} {self.section}"
    
    class Meta:
        verbose_name = "Предсказание"
        verbose_name_plural = "Предсказания"