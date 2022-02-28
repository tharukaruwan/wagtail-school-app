from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
from sectionApp.models import Section
from teacherApp.models import Teacher

@register_snippet
class Class(models.Model):
    class_id=models.AutoField(primary_key=True)
    class_name=models.CharField(unique=False,max_length=1)
    section=models.ForeignKey(
        Section,
        on_delete=models.CASCADE
    )
    class_teacher=models.OneToOneField(
        Teacher,
        null=True,
        on_delete=models.CASCADE,
    )

    panels=[
        FieldPanel('class_name'),
        FieldPanel('section'),
        FieldPanel('class_teacher'),
    ]

    def __str__(self):
        return self.class_name
