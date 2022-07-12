'''from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Application, Job

@receiver(post_save, sender=Application)
def update_job(sender, updated, **kwargs):

'''