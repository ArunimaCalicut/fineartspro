# Generated by Django 4.0 on 2021-12-15 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_no', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('leader_name', models.CharField(max_length=100)),
                ('total_score', models.FloatField()),
            ],
        ),
    ]