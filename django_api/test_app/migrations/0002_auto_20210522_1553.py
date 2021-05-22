# Generated by Django 3.2.3 on 2021-05-22 07:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('created_at',)},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='testmodel',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]