# Generated by Django 3.2.3 on 2021-06-08 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_reserva_res_hora_reservada'),
    ]

    operations = [
        migrations.AddField(
            model_name='boletafactura',
            name='desc_medio_pago',
            field=models.ForeignKey(default='Debito', on_delete=django.db.models.deletion.PROTECT, to='core.tipopago'),
        ),
        migrations.AlterField(
            model_name='boletafactura',
            name='desc_bol_fac',
            field=models.CharField(choices=[['Boleta', 'Boleta'], ['Factura', 'Factura']], max_length=7, verbose_name='Seleccione tipo de pago: '),
        ),
        migrations.AlterField(
            model_name='detalleservicio',
            name='desc_medio_pago',
            field=models.ForeignKey(default='Debito', on_delete=django.db.models.deletion.PROTECT, to='core.pagoservicio'),
        ),
        migrations.AlterField(
            model_name='pagoservicio',
            name='desc_medio_pago',
            field=models.ForeignKey(default='Debito', on_delete=django.db.models.deletion.PROTECT, to='core.tipopago'),
        ),
        migrations.AlterField(
            model_name='tipopago',
            name='desc_medio_pago',
            field=models.CharField(default='Debito', max_length=50, verbose_name='Ingrese el nuevo medio de pago a integrar:'),
        ),
    ]