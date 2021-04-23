from django.db import models


# Create your models here.


class User(models.Model):
    first_name = models.CharField('Name', max_length=30)
    last_name = models.CharField('Surname', max_length=30)
    city = models.CharField('City', max_length=20)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = 'Пользователи'


class Competence(models.Model):
    ONE = '1'
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    LEVEL_OF_COMPETENCE = (
        (ONE, "begginer"),
        (TWO, "low"),
        (THREE, "middle"),
        (FOUR, "upper"),
        (FIVE, "pro")
    )

    person = models.ForeignKey(User, on_delete=models.RESTRICT)
    title_of_competence = models.CharField('CompetenceTitle', max_length=50)
    level_of_competence = models.CharField(max_length=2, choices=LEVEL_OF_COMPETENCE,
                                           default=ONE)

    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = 'Компетенции'

    def __str__(self):
        return self.title_of_competence


class Vacancy(models.Model):
    title_of_vacancy = models.CharField('VacancyTitle', max_length=50)
    description = models.TextField('Description', max_length=400)
    city_of_vacancy = models.CharField('City', max_length=25)
    salary = models.IntegerField('Salary')
    web_site = models.CharField('WebSite', max_length=20)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title_of_vacancy