# Generated by Django 4.0.3 on 2022-04-29 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_shoppingitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]