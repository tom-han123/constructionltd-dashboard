# Generated by Django 4.1.5 on 2023-01-30 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="acc_register",
            fields=[
                (
                    "admin_id",
                    models.AutoField(
                        db_column="User ID", primary_key=True, serialize=False
                    ),
                ),
                ("phone", models.CharField(db_column="Phone", max_length=50)),
                ("password", models.CharField(db_column="Password", max_length=50)),
            ],
        ),
    ]
