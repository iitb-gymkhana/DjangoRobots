# Generated by Django 3.0 on 2019-12-16 06:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('robots', '0005_url_reverse_proxy_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.fields.NOT_PROVIDED, to=settings.AUTH_USER_MODEL, verbose_name='creator'),
        ),
    ]
