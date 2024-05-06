# Generated by Django 5.0.1 on 2024-01-21 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rxApp', '0002_contact_nurse_physician_telemedicines_visa'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/physician/')),
            ],
        ),
        migrations.RemoveField(
            model_name='physician',
            name='resume',
        ),
        migrations.AddField(
            model_name='physician',
            name='resumes',
            field=models.ManyToManyField(to='rxApp.phyfile'),
        ),
    ]