from subjectApp.models import Subject
from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel

@register_snippet
class Teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    teacher=models.CharField(max_length=500)
    subject=models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        null=True
    )

    panels=[
        FieldPanel('subject'),
        FieldPanel('teacher'),
    ]

    def __str__(self):
        return self.teacher
