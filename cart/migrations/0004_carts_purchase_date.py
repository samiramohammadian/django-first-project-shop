# Generated by Django 4.1.1 on 2022-10-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='purchase_date',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]