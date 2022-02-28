from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel
# from teacherApp.models import Teacher
import teacherApp.models
from subjectApp.models import Subject

@register_snippet
class Section(models.Model):
    grade_id=models.AutoField(primary_key=True)
    grade=models.IntegerField(unique=True)
    section_head=models.OneToOneField(
        teacherApp.models.Teacher,
        null=True,
        on_delete=models.CASCADE,
    )
    subject=models.ManyToManyField(Subject)

    panels=[
        FieldPanel('grade'),
        FieldPanel('section_head'),
        FieldPanel('subject'),
    ]

    def __str__(self):
        return str(self.grade)
