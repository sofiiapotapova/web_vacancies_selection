from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, vacs):
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = vacs['instance']

    if app_label == 'core':
        if model_name == 'vacancy':
            instances = instance.vacancies.all()
            for _instance in instances:
                registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, vacs):
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = vacs['instance']

    if app_label == 'core':
        if model_name == 'vacancy':
            instances = instance.vacancies.all()
            for _instance in instances:
                registry.delete(_instance, raise_on_error=False)
