# Generated by Django 3.2.22 on 2023-11-18 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('career_app', '0003_auto_20230923_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('JOB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career_app.agency')),
                ('STUDENT', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='career_app.student')),
            ],
        ),
    ]
