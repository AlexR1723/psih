from django.db import models


# Create your models here.

class AnswerLevel1(models.Model):
    quest = models.ForeignKey('QuestionLevel1', models.DO_NOTHING, blank=True, null=True, verbose_name='Вопрос')
    area = models.ForeignKey('Areas', models.DO_NOTHING, blank=True, null=True, verbose_name='Сфера')
    text = models.TextField(blank=True, null=True, verbose_name='Ответ')

    # is_check = models.BooleanField(blank=True, null=True, verbose_name='Это проверочный вопрос?')

    class Meta:
        managed = False
        db_table = 'answer_level_1'
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Areas(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name='Сфера')

    class Meta:
        managed = False
        db_table = 'areas'
        verbose_name = 'Сфера'
        verbose_name_plural = 'Сферы'

    def __str__(self):
        return self.text


class QuestionLevel1(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name='Вопрос')

    class Meta:
        managed = False
        db_table = 'question_level_1'
        verbose_name = 'Вопрос ур.1'
        verbose_name_plural = 'Вопросы ур.1'

    def __str__(self):
        return str(self.id) + ' ' + self.text


class CheckQuestion(models.Model):
    first_quest = models.ForeignKey('QuestionLevel1', models.DO_NOTHING, db_column='first_quest', blank=True, null=True,
                                    verbose_name='Первый вопрос', related_name='first_question')
    second_quest = models.ForeignKey('QuestionLevel1', models.DO_NOTHING, db_column='second_quest', blank=True,
                                     null=True, verbose_name='Второй вопрос', related_name='second_question')

    class Meta:
        managed = False
        db_table = 'check_question'
        verbose_name = 'Проверочный вопрос'
        verbose_name_plural = 'Проверочные вопросы'


class QuestionLevel2(models.Model):
    area = models.ForeignKey('Areas', models.DO_NOTHING, blank=True, null=True, verbose_name='Сфера')
    text = models.TextField(blank=True, null=True, verbose_name='Вопрос')

    class Meta:
        managed = False
        db_table = 'question_level_2'
        verbose_name = 'Вопрос ур.2'
        verbose_name_plural = 'Вопросы ур.2'


class QuestionLevel3(models.Model):
    area = models.ForeignKey('Areas', models.DO_NOTHING, blank=True, null=True, verbose_name='Сфера')
    text = models.TextField(blank=True, null=True, verbose_name='Вопрос')

    class Meta:
        managed = False
        db_table = 'question_level_3'
        verbose_name = 'Вопрос ур.3'
        verbose_name_plural = 'Вопросы ур.3'


class Conclusions(models.Model):
    text = models.TextField(blank=True, null=True, verbose_name='Текст')
    first_area = models.ForeignKey('Areas', models.DO_NOTHING, db_column='first_area', blank=True, null=True,
                                   verbose_name='Первая сфера', related_name='first_area')
    second_area = models.ForeignKey('Areas', models.DO_NOTHING, db_column='second_area', blank=True, null=True,
                                    verbose_name='Вторая сфера', related_name='second_area')

    class Meta:
        managed = False
        db_table = 'conclusions'
        verbose_name = 'Вывод'
        verbose_name_plural = 'Выводы'


class CheckTable(models.Model):
    date = models.DateTimeField(blank=True, null=True, verbose_name='Дата')
    count = models.IntegerField(blank=True, null=True, verbose_name='Количество сфер')

    class Meta:
        managed = False
        db_table = 'check_table'
        verbose_name = 'Error'
        verbose_name_plural = 'Errors'


class Results(models.Model):
    file = models.FileField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'results'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
