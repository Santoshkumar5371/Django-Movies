# Generated by Django 5.0 on 2023-12-13 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=100)),
                ('heroname', models.CharField(max_length=100)),
                ('heroinename', models.CharField(max_length=100)),
            ],
        ),
    ]
