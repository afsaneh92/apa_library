# Generated by Django 2.2.1 on 2019-07-16 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20190716_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 16, 16, 10, 23, 981388)),
        ),
    ]
