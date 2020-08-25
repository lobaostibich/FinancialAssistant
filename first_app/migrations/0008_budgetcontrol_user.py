# Generated by Django 3.1 on 2020-08-25 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0007_remove_budgetcontrol_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetcontrol',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]