# Generated by Django 4.0 on 2021-12-31 06:19

from django.conf import settings
from django.core.management import call_command
from django.db import migrations, models
import django.db.models.deletion
import uuid

appLabel = 'resume'

def loadTechnologyFixtures(apps, schema_editor):
	call_command('loaddata', 'technology', app_label=appLabel)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academyType', models.CharField(max_length=15)),
                ('subject', models.CharField(max_length=30)),
                ('instituteName', models.CharField(max_length=30)),
                ('passingYear', models.CharField(max_length=10)),
                ('result', models.DecimalField(decimal_places=2, max_digits=2)),
            ],
        ),
        migrations.CreateModel(
            name='OtherSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resumeId', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='candidate.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologyCode', models.CharField(max_length=20)),
                ('technologyName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ResumeAndTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField()),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.resume')),
                ('technology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.technology')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeAndOtherSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otherSkills', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.otherskills')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.resume')),
            ],
        ),
        migrations.CreateModel(
            name='ResumeAndAcademicRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicRecord', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.academicrecord')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='resume.resume')),
            ],
        ),
        migrations.RunPython(loadTechnologyFixtures),
    ]
