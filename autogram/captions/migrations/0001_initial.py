# Generated by Django 2.2.5 on 2019-09-24 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times_used', models.IntegerField(default=0)),
                ('text', models.TextField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
