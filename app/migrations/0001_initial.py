# Generated by Django 3.2.9 on 2021-12-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GROCERY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('B', 'BOUGHT'), ('NA', 'NOT AVAILABLE'), ('P', 'PENDING')], max_length=3)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
