# Generated by Django 4.2 on 2023-04-23 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_paid_curse'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(blank=True, default=0, verbose_name='Стоимость курса'),
            preserve_default=False,
        ),
    ]