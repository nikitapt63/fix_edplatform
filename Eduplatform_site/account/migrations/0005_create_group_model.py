# Generated by Django 4.0.6 on 2022-08-23 17:55

import django.db.models.deletion
from django.db import migrations, models

import Eduplatform_site.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0004_create_photo_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Group",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("group_name", models.CharField(max_length=50)),
                ("student", models.ManyToManyField(blank=True, to="account.student")),
                ("teacher", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="account.teacher")),
            ],
            options={
                "verbose_name": "students_group",
                "verbose_name_plural": "students_groups",
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]
