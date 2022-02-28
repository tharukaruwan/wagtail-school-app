from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel

@register_snippet
class Subject(models.Model):
    subject_id=models.AutoField(primary_key=True)
    subject_name=models.CharField(unique=True,max_length=500)
    
    panels=[
        FieldPanel('subject_name'),
    ]

    def __str__(self):
        return self.subject_name
