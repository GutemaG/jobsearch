# Generated by Django 4.0.5 on 2022-06-19 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobsearch', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.employer'),
        ),
        migrations.AddField(
            model_name='application',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='jobsearch.job'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.applicant'),
        ),
    ]
