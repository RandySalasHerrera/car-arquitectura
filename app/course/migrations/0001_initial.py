# Generated by Django 3.2.6 on 2023-06-20 04:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('coursescraped', '0001_initial'),
        ('teacher', '0002_alter_teacher_options'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('course_scraped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coursescraped.cursoscraped')),
                ('students', models.ManyToManyField(to='student.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.teacher')),
            ],
            options={
                'verbose_name': 'Course Scraped',
                'verbose_name_plural': 'Course Scrapeds',
                'ordering': ['-id'],
            },
        ),
    ]