# Generated by Django 2.0.6 on 2018-11-06 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20181106_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentprofile',
            name='student_class',
            field=models.CharField(choices=[('JSS1', 'jss1'), ('JSS2', 'jss2'), ('JSS3', 'jss3'), ('SS1', 'ss1'), ('SS2', 'ss2'), ('SS3', 'ss3')], default='JSS1', max_length=50),
        ),
    ]
