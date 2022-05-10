# Generated by Django 4.0.4 on 2022-05-10 15:31

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='francais : nom', max_length=255, unique=True, verbose_name='category name')),
                ('slug', models.SlugField(help_text='francais : url', max_length=255, verbose_name='category safe URL')),
                ('description', models.TextField(blank=True, help_text='francais : description', null=True, verbose_name='category description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, help_text='francais : parent', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='nautilux_app.category', verbose_name='parent of category')),
            ],
            options={
                'verbose_name': 'equipment category',
                'verbose_name_plural': 'equipment categories',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='francais : nom', max_length=255, null=True, verbose_name='equipment name')),
                ('slug', models.SlugField(help_text='francais : url', max_length=255, verbose_name='equipment safe URL')),
                ('quantity', models.IntegerField(blank=True, default=0, help_text='francais : quantité', null=True, verbose_name='equipment quantity')),
                ('categories', models.ManyToManyField(blank=True, help_text='francais : catégories', null=True, to='nautilux_app.category', verbose_name='equipment categories')),
            ],
        ),
    ]