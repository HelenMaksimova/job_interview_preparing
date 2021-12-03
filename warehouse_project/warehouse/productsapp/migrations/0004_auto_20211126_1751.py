# Generated by Django 3.2.9 on 2021-11-26 14:51

import django.contrib.sites.managers
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('productsapp', '0003_auto_20211125_0939'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='category',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('on_site', django.contrib.sites.managers.CurrentSiteManager()),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='site',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sites.site'),
        ),
        migrations.AddField(
            model_name='product',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(related_name='products', to='productsapp.Category', verbose_name='разделы'),
        ),
    ]
