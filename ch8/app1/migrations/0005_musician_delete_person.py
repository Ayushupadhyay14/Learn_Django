# Generated by Django 5.2.1 on 2025-05-29 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_person_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
