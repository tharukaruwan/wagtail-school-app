# Generated by Django 4.0.2 on 2022-02-28 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0001_initial'),
        ('teacherApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subjectApp.subject'),
        ),
    ]
