# Generated by Django 4.2.7 on 2023-11-28 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='carousel/')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
