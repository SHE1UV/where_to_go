from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_alter_image_ordinal_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='place_id',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Картинки'),
        ),
    ]