# Generated by Django 2.2 on 2020-02-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maid', '0003_auto_20200206_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='residents',
            name='type',
            field=models.CharField(choices=[('tenant', 'tenant'), ('owner', 'owner')], max_length=10),
        ),
    ]
