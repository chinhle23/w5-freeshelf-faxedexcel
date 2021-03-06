# Generated by Django 2.1.7 on 2019-03-17 15:09
# see migration 0012 for a full explanation
# adding categories in this migration

from django.db import migrations
import csv
import os.path
from django.conf import settings
from django.core.files import File
from django.utils.text import slugify

def load_author_data(apps, schema_editor):
    """
    Read a CSV file full of categories and insert them into the database
    """
    Author = apps.get_model('freeshelfapp', 'Author')

    datapath = os.path.join(settings.BASE_DIR, 'initial_data')
    datafile = os.path.join(datapath, 'authors.csv')

    with open(datafile) as file: 
        reader = csv.DictReader(file)
        for row in reader:
            author_name = row['name']
            if Author.objects.filter(name=author_name).count():
                continue
            author = Author(
                name=row['name'],
            )
            author.save()
            base_slug = slugify(row['name'])
            slug = base_slug
            n = 0
            while Author.objects.filter(slug=slug).count():
                n += 1
                slug = base_slug + "-" + str(n)
            author.slug = slug
            author.save()
            
class Migration(migrations.Migration):

    dependencies = [
        ('freeshelfapp', '0014_auto_20190317_0726'),
    ]

    operations = [
        migrations.RunPython(load_author_data)
    ]
