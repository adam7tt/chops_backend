# Generated by Django 2.2.5 on 2019-12-08 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20191205_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='wordcloud',
            field=models.TextField(default=None, max_length=2048, verbose_name='wordcloud'),
        ),
    ]
