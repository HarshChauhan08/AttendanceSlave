# Generated by Django 3.2.9 on 2022-09-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentEmail', models.CharField(max_length=50)),
                ('studentPassword', models.CharField(max_length=50)),
            ],
        ),
    ]
