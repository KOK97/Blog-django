# Generated by Django 4.2.6 on 2023-10-16 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blogpost_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=10),
        ),
    ]
