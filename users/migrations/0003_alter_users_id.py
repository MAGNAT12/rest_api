# Generated by Django 4.2.8 on 2024-08-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_username_users_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.CharField(max_length=500, primary_key=True, serialize=False),
        ),
    ]
