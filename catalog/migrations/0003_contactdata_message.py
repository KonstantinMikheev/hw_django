# Generated by Django 5.0.7 on 2024-08-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_contactdata_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdata',
            name='message',
            field=models.TextField(blank=True, help_text='Введите Ваш запрос.', null=True, verbose_name='Запрос пользователя'),
        ),
    ]
