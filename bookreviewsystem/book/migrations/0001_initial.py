# Generated by Django 5.2.4 on 2025-07-16 21:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('genre', models.CharField(choices=[('fiction', 'Fiction'), ('non_fiction', 'Non-Fiction'), ('science', 'Science'), ('technology', 'Technology'), ('history', 'History')], max_length=20)),
                ('isbn', models.CharField(max_length=13, unique=True, verbose_name='ISBN')),
                ('publication_date', models.DecimalField(decimal_places=2, default=0, max_digits=3, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
