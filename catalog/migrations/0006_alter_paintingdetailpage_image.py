# Generated by Django 3.2.8 on 2021-10-31 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('catalog', '0005_auto_20211031_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paintingdetailpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]