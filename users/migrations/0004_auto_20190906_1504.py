# Generated by Django 2.2.4 on 2019-09-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190904_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='avatar/default_qz.jpg', upload_to='avatar'),
        ),
    ]