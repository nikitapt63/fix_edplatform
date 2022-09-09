# Generated by Django 4.0.6 on 2022-08-23 17:56

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import Eduplatform_site.mixins


class Migration(migrations.Migration):

    dependencies = [
        ("learning", "0001_create_course_model"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("topic_name", models.CharField(max_length=50)),
                ("content", models.TextField(null=True)),
                ("numbering", models.IntegerField(validators=[django.core.validators.MinValueValidator(0, "Min number value!")])),
                ("course", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="learning.course")),
            ],
            options={
                "verbose_name": "course_topic",
                "verbose_name_plural": "course_topics",
                "ordering": ["numbering"],
            },
            bases=(models.Model, Eduplatform_site.mixins.DateTimeMixinModel),
        ),
    ]
