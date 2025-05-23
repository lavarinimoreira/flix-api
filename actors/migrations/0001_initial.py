# Generated by Django 5.2.1 on 2025-05-14 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('nationality', models.CharField(blank=True, choices=[('FRANCE', 'France'), ('BRAZIL', 'Brazil'), ('CHINA', 'China'), ('USA', 'United States'), ('SPAIN', 'Spain')], max_length=100, null=True)),
            ],
        ),
    ]
