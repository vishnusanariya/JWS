# Generated by Django 4.0.1 on 2022-03-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_deal_id_alter_deal_deal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='job_image',
            field=models.ImageField(upload_to='profile_pics'),
        ),
    ]
