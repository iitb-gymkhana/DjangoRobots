# Generated by Django 3.0 on 2019-12-15 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('robots', '0004_auto_20191214_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='reverse_proxy_initial',
            field=models.CharField(default='', max_length=20),
        ),
    ]