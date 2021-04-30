# Generated by Django 3.2 on 2021-04-29 10:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ask_review', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('headline', models.CharField(max_length=128)),
                ('body', models.TextField(blank=True, max_length=8192)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ask_review.ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]