from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_options_alter_place_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='ordinal_number',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Описание'),
        ),
    ]