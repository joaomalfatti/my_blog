# Generated by Django 4.2 on 2023-04-16 21:30

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=ckeditor.fields.RichTextField(),
        ),
    ]