# Generated by Django 4.2.6 on 2023-10-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videolar', '0003_rename_ekonomi_haberler_alter_haberler_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ekonomi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200)),
                ('aciklama', models.TextField()),
                ('eklenme_tarih', models.DateTimeField(auto_now_add=True)),
                ('kapak', models.ImageField(default='Ekonomi.png', upload_to='images')),
            ],
            options={
                'verbose_name': 'Ekonomi',
                'verbose_name_plural': 'Ekonomi',
            },
        ),
    ]