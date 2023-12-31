# Generated by Django 4.2.7 on 2023-11-29 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('cover', models.FileField(blank=True, null=True, upload_to='fimapp/cover')),
            ],
        ),
    ]
