# Generated by Django 2.2.3 on 2019-07-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_id', models.CharField(max_length=50)),
                ('u_pw', models.CharField(help_text='Enter PassWord', max_length=200)),
                ('th', models.IntegerField(help_text='Enter th')),
                ('Name', models.CharField(max_length=20)),
                ('major', models.CharField(help_text='Enter major', max_length=300)),
                ('stu_id', models.IntegerField(help_text='Enter student_id')),
                ('email', models.EmailField(max_length=254)),
                ('staff', models.BooleanField()),
            ],
        ),
    ]