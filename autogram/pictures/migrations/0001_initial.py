# Generated by Django 2.2.5 on 2019-09-27 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owners', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('times_used', models.IntegerField(default=0)),
                ('name', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to='pictures/')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='owners.Owner')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
