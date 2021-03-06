# Generated by Django 3.2.3 on 2021-06-01 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Emlployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('emp_code', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.position')),
            ],
        ),
    ]
