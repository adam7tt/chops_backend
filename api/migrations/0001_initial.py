# Generated by Django 2.2.5 on 2019-11-13 19:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Citation',
            fields=[
                ('citation_id', models.AutoField(primary_key=True, serialize=False, verbose_name='citation_id')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('date', models.DateField(verbose_name='date')),
                ('abstract', models.TextField(verbose_name='abstract')),
                ('paper', models.TextField(verbose_name='paper')),
                ('date_entered', models.DateTimeField(auto_now=True, verbose_name='date_entered')),
                ('keywords', models.ManyToManyField(to='api.Keyword')),
            ],
        ),
        migrations.CreateModel(
            name='Academic',
            fields=[
                ('academic_id', models.AutoField(primary_key=True, serialize=False, verbose_name='academic_id')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('citations', models.ManyToManyField(to='api.Citation')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Department')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.University')),
            ],
        ),
    ]
