# Generated by Django 2.2.10 on 2020-03-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_customtext_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='onefiled',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
