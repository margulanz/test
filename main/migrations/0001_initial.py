# Generated by Django 4.2.1 on 2023-06-11 10:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScoreIQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('took_at', models.DateTimeField()),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(50)])),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test')),
            ],
        ),
        migrations.CreateModel(
            name='ScoreEQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('took_at', models.DateTimeField()),
                ('sequence', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^[абвгд]*$', 'Только set(а,б,в,г,д) допустимы')])),
                ('login', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.test')),
            ],
        ),
    ]
