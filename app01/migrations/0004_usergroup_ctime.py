# Generated by Django 2.0.1 on 2018-02-16 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20180216_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]