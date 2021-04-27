from django.contrib.auth.models import User
from django.db import models
from neomodel import StructuredNode, StringProperty, IntegerProperty, UniqueIdProperty, RelationshipTo


# Create your models here.


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


class VacancyManager(models.Manager):
    def create_vacancy(self,
                       title_of_vacancy,
                       description,
                       city_of_vacancy,
                       salary,
                       web_site):
        vacancy = self.create(title_of_vacancy=title_of_vacancy,
                              description=description,
                              city_of_vacancy=city_of_vacancy,
                              salary=salary,
                              web_site=web_site)
        return vacancy


class Vacancy(models.Model):
    title_of_vacancy = models.CharField('VacancyTitle', max_length=50)
    description = models.TextField('Description', max_length=400)
    city_of_vacancy = models.CharField('City', max_length=25)
    salary = models.IntegerField('Salary')
    web_site = models.CharField('WebSite', max_length=20)

    objects = VacancyManager()

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title_of_vacancy


class NeoCompetence(StructuredNode):
    name = StringProperty(index=True, default='competence')


class NeoVacancy(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)

    # Relations
    neo_competence = RelationshipTo(NeoCompetence, "REQUIRES")


