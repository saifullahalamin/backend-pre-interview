# Generated by Django 2.1 on 2019-09-21 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=254)),
                ('name', models.CharField(max_length=254)),
                ('unit', models.CharField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
