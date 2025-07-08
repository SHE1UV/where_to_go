from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20220905_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=200, null=True, verbose_name='ID места'),
        ),
    ]