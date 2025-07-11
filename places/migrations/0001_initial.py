from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description_short', models.TextField(blank=True, verbose_name='Краткое описание')),
                ('description_long', models.TextField(blank=True, verbose_name='Описание')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('images', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинки')),
            ],
        ),
    ]