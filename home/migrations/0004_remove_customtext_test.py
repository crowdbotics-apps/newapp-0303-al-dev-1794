# Generated by Django 2.2.10 on 2020-03-03 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_customtext_test"),
    ]

    operations = [
        migrations.RemoveField(model_name="customtext", name="test",),
    ]
