# Generated by Django 4.0.5 on 2022-06-19 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='date_posted',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='updated_at',
            new_name='date_updated',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]