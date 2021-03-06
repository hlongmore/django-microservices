# Generated by Django 2.1.2 on 2019-03-25 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microservices', '0003_auto_20190325_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='start_method',
            field=models.CharField(blank=True, choices=[('spawn', 'spawn'), ('fork', 'fork'), ('forkserver', 'forkserver')], default='fork', help_text='Start method for multiprocessing module', max_length=20, null=True),
        ),
    ]
