# Generated by Django 5.0.4 on 2024-04-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('date', models.DateField()),
                ('position', models.CharField(max_length=50)),
                ('salary', models.IntegerField()),
            ],
        ),
    ]