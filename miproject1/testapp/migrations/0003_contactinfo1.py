# Generated by Django 3.0.6 on 2020-06-15 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_student1_teacher1'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
    ]
