# Generated by Django 4.2.5 on 2023-11-01 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(blank=True, max_length=100, null=True)),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='Profile')),
            ],
        ),
    ]
