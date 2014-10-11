# -*- coding: utf-8 -*-
from django.db import migrations


def create_options(apps, schema_editor):
    TestModel = apps.get_model("reproduction", "TestModel")
    TestModel.objects.create(foo="Obey")
    TestModel.objects.create(foo="The")
    TestModel.objects.create(foo="Testing")
    TestModel.objects.create(foo="Goat")


class Migration(migrations.Migration):
    dependencies = [
        ('reproduction', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_options),
    ]