from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_remove_place_place_id_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='./makemigrations', upload_to='', verbose_name='Картинки'),
        ),
    ]