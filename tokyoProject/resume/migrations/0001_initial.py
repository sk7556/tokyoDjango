# Generated by Django 5.0.1 on 2024-02-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('career', models.TextField()),
                ('role', models.TextField()),
                ('salary', models.TextField()),
                ('intro', models.TextField()),
                ('information', models.TextField()),
                ('certificate', models.TextField()),
                ('photo', models.ImageField(upload_to='resume/')),
            ],
        ),
    ]
