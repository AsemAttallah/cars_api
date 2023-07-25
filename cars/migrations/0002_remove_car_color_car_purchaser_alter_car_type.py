# Generated by Django 4.2.3 on 2023-07-25 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='color',
        ),
        migrations.AddField(
            model_name='car',
            name='purchaser',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]