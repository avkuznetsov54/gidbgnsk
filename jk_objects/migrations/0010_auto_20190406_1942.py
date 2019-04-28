# Generated by Django 2.2 on 2019-04-06 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jk_objects', '0009_finishingflat_houseofobject'),
    ]

    operations = [
        migrations.AddField(
            model_name='houseofobject',
            name='jk_object',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jkobject', to='jk_objects.JkObject', verbose_name='Жилой комплекс'),
        ),
        migrations.RemoveField(
            model_name='houseofobject',
            name='bank',
        ),
        migrations.AddField(
            model_name='houseofobject',
            name='bank',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='bank', to='jk_objects.Bank', verbose_name='Банки'),
        ),
        migrations.RemoveField(
            model_name='houseofobject',
            name='finishing_flat',
        ),
        migrations.AddField(
            model_name='houseofobject',
            name='finishing_flat',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='finishingflat', to='jk_objects.FinishingFlat', verbose_name='Отделка квартиры'),
        ),
        migrations.RemoveField(
            model_name='houseofobject',
            name='payment_method',
        ),
        migrations.AddField(
            model_name='houseofobject',
            name='payment_method',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='paymentmethod', to='jk_objects.PaymentМethod', verbose_name='Способы оплаты'),
        ),
    ]