# Generated by Django 2.2.10 on 2020-03-03 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_homepage_onefiled'),
    ]

    operations = [
        migrations.AddField(
            model_name='customtext',
            name='final_field',
            field=models.DateField(blank=True, null=True),
        ),
    ]
