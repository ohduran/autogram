# Generated by Django 2.2.5 on 2019-09-24 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={},
        ),
        migrations.AddField(
            model_name='user',
            name='para',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]