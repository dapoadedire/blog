# Generated by Django 4.1.4 on 2022-12-23 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_post_sub_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="sub_title",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
