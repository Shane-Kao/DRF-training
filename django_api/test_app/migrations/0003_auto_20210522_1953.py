# Generated by Django 3.2.3 on 2021-05-22 11:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0002_auto_20210522_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='testmodel',
            options={'ordering': ('-created_at',), 'verbose_name_plural': 'Test Model'},
        ),
        migrations.AddField(
            model_name='testmodel',
            name='extra_name',
            field=models.CharField(default='null', editable=False, max_length=250),
        ),
        migrations.CreateModel(
            name='ModelX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('test_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_content', to='test_app.testmodel')),
            ],
            options={
                'verbose_name_plural': 'Model X',
                'ordering': ('-created_at',),
            },
        ),
    ]
