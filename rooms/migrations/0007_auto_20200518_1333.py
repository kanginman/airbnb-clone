# Generated by Django 2.2.5 on 2020-05-18 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_auto_20200518_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='roomType',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rooms', to='rooms.RoomType'),
        ),
    ]
