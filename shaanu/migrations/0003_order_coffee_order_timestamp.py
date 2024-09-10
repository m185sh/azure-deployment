# Generated by Django 5.0.3 on 2024-09-03 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shaanu', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coffee',
            field=models.CharField(choices=[('Espresso', 'Espresso'), ('Latte', 'Latte'), ('Cappuccino', 'Cappuccino'), ('Mocha', 'Mocha')], default='Espresso', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2023-01-01'),
            preserve_default=False,
        ),
    ]
