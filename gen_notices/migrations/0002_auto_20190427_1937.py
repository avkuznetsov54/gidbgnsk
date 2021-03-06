# Generated by Django 2.2 on 2019-04-27 12:37

from django.db import migrations, models
import gen_notices.models


class Migration(migrations.Migration):

    dependencies = [
        ('gen_notices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticetemplate',
            name='emails_developer',
            field=models.CharField(help_text='1) Сперва для проверки впишите тестовую почту, после тестирования измените на почту застройщика.<br>2) Если у застройщика больше чем одна почта, то напишите почты через запятую без пробелов.', max_length=200, verbose_name='Email(s) застройщика'),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='file_null_notice',
            field=models.FileField(help_text='Укажите файл пустого уведомления, будет скачиваться при нажатию на кнопку "Скачать пустое".<br>Используйте .docx формат.', upload_to=gen_notices.models.generate_filename, verbose_name='Файл пустого уведомления'),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='file_template',
            field=models.FileField(help_text='Выберите подготовленный файл, для генерации уведомления.<br>Используйте .docx формат.', upload_to=gen_notices.models.generate_filename, verbose_name='Файл шаблона уведомления'),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='nick_name',
            field=models.CharField(help_text='Используйте латинские буквы.<br>Пример: yasniy_bereg_form_1', max_length=150, unique=True, verbose_name='Название уведомления'),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='office_is_active',
            field=models.BooleanField(default=True, help_text='Если нужен выбор офиса, занесите сначало офисы в "Настройка уведомлений" -> "Офисы/РОПы/emails".<br>Если включить выбор офиса станет обязателен.', verbose_name='Выбор офиса'),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='type_for_lawyer_is_active',
            field=models.BooleanField(default=False, help_text='Если есть необходимость отправлять копию ипотечному специалисту.<br>Внесите email специалиста в разделе "Настройка уведомлений" -> "Доп. значения".', verbose_name='Отправлять ипотечному специалисту или нет (наличные/ипотека)'),
        ),
        migrations.AlterField(
            model_name='noticetemplate',
            name='type_for_notice_choice',
            field=models.CharField(blank=True, choices=[('uvedd', 'Уведомление'), ('bronn', 'Бронирование'), ('uvedd_bronn', 'Уведомление или Бронирование')], help_text='Определяет тип уведомления.<br>Если выбрать пункт "Уведомление или Бронирование", то нужно будет указать тип при заполнении формы пользователем.', max_length=50, verbose_name='Уведомление или бронирование'),
        ),
    ]
