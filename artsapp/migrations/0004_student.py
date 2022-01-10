# Generated by Django 4.0 on 2021-12-21 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artsapp', '0003_alter_group_total_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='student', serialize=False, to='artsapp.login')),
                ('name', models.CharField(max_length=100)),
                ('roll_no', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('semester', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='artsapp.group')),
            ],
        ),
    ]