# Generated by Django 2.2 on 2019-04-25 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=20)),
                ('actor', models.CharField(max_length=20)),
                ('ms', models.CharField(max_length=50)),
            ],
        ),
    ]
