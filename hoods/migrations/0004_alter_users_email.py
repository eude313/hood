# Generated by Django 3.2 on 2021-10-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoods', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
