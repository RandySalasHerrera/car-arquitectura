# Generated by Django 3.2.6 on 2023-06-19 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CursoScraped',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Course Scraped',
                'verbose_name_plural': 'Course Scrapeds',
                'ordering': ['-name'],
            },
        ),
    ]
