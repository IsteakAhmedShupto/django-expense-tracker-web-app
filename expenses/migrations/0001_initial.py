# Generated by Django 4.2.6 on 2023-10-26 20:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('authors', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('published_date', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('distribution_expense', models.IntegerField(default=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
