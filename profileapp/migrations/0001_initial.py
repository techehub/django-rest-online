# Generated by Django 3.0.8 on 2020-07-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
