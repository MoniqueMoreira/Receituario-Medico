# Generated by Django 4.0.5 on 2022-06-13 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receituario', '0004_alter_clinic_cnpj_alter_doctor_crm_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clinic',
            name='id',
        ),
        migrations.AlterField(
            model_name='clinic',
            name='cnpj',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
