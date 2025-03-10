# Generated by Django 5.1.3 on 2024-11-25 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vaccine',
            name='animal',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='application_date',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='next_application_date',
        ),
        migrations.RemoveField(
            model_name='vaccine',
            name='vaccine_name',
        ),
        migrations.AddField(
            model_name='vaccine',
            name='name',
            field=models.CharField(default='Vacuna desconocida', max_length=100),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='VaccineApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_applied', models.DateField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vaccine_applications', to='animals.animal')),
                ('vaccine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.vaccine')),
            ],
        ),
    ]
