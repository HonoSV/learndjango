# Generated by Django 2.0.1 on 2018-02-16 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20180216_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfoex',
            name='user_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup'),
        ),
    ]
