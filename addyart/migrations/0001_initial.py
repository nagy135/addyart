# Generated by Django 2.2.9 on 2020-02-22 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='addyart_catalog', serialize=False, to='cms.CMSPlugin')),
                ('alternate', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='addyart_detail', serialize=False, to='cms.CMSPlugin')),
                ('test', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('title', models.CharField(default=None, max_length=50, null=True)),
                ('description', models.TextField(default='Product description...', max_length=20000, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='addyart/static/products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='addyart.Category')),
            ],
        ),
    ]
