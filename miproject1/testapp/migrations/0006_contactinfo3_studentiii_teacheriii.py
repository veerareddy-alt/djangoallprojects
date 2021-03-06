# Generated by Django 3.0.6 on 2020-06-15 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_contactinfo2_studentii_teacherii'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StudentIII',
            fields=[
                ('contactinfo3_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.ContactInfo3')),
                ('rollno', models.IntegerField()),
                ('marks', models.IntegerField()),
            ],
            bases=('testapp.contactinfo3',),
        ),
        migrations.CreateModel(
            name='TeacherIII',
            fields=[
                ('contactinfo3_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.ContactInfo3')),
                ('subjects', models.CharField(max_length=30)),
                ('salary', models.FloatField()),
            ],
            bases=('testapp.contactinfo3',),
        ),
    ]
