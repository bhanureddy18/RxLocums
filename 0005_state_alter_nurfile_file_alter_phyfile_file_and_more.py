# Generated by Django 5.0.1 on 2024-01-24 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('rxApp', '0004_nurfile_telefile_visafile_remove_contact_resume_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='nurfile',
            name='file',
            field=models.FileField(upload_to='Nurses/'),
        ),
        migrations.AlterField(
            model_name='phyfile',
            name='file',
            field=models.FileField(upload_to='physician/'),
        ),
        migrations.AlterField(
            model_name='telefile',
            name='file',
            field=models.FileField(upload_to='telemedicines/'),
        ),
        migrations.AlterField(
            model_name='visafile',
            name='file',
            field=models.FileField(upload_to='visas/'),
        ),
        migrations.CreateModel(
            name='StateAssignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rxApp.state')),
            ],
            options={
                'unique_together': {('state', 'content_type', 'object_id')},
            },
        ),
    ]
