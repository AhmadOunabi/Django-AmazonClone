# Generated by Django 4.2.2 on 2023-08-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='user-icon-human-person-sign-vector-20444565.jpg', upload_to='accounts'),
        ),
    ]
