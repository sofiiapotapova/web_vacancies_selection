from django_elasticsearch_dsl import Document, Index
from .models import Vacancy

vacs = Index('vacs')


@vacs.doc_type
class VacDocument(Document):
    class Django:
        model = Vacancy

        fields = [
            'title_of_vacancy',
            'description',
            'city_of_vacancy',
            'salary',
            'web_site',
            'percent'
        ]