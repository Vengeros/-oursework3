from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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
    action_flag = models.PositiveSmallIntegerField()
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


class Clients(models.Model):
    idclient = models.AutoField(db_column='idClient', primary_key=True,unique=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45,validators=[validate_slug])  # Field name made lowercase.
    phone = models.DecimalField(db_column='Phone', max_digits=9, decimal_places=0,validators=[MinLengthValidator(9)],unique=True)  # Field name made lowercase.
    surname = models.CharField(db_column='Surname', max_length=45,validators=[validate_slug])  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True,validators=[MinValueValidator(1),MaxValueValidator(100)])  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45,validators=[validate_email],unique=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=100,validators=[validate_slug])  # Field name made lowercase.
    creditcard = models.DecimalField(db_column='CreditCard', max_digits=16, decimal_places=0,validators=[MinLengthValidator(14),MaxLengthValidator(16)],unique=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate',auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients'
        ordering = ["name","surname"]


class Firms(models.Model):
    idfirms = models.AutoField(db_column='idFirms', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True,validators=[validate_slug],unique=True)  # Field name made lowercase.
    contactnumber = models.CharField(db_column='ContactNumber', unique=True, max_length=9, blank=True, null=True,validators=[validate_slug,MinLengthValidator(9)])  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=45, blank=True, null=True,validators=[validate_email])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'firms'


class Goods(models.Model):
    idgood = models.AutoField(db_column='idGood', primary_key=True)  # Field name made lowercase.
    uniquecode = models.CharField(db_column='Uniquecode', max_length=10,)  # Field name made lowercase.
    article = models.CharField(db_column='Article', max_length=45, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=15, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='Price', max_length=10, blank=True, null=True)  # Field name made lowercase.
    image = models.TextField(db_column='Image', blank=True, null=True)  # Field name made lowercase.
    goodtypeid = models.ForeignKey('Goodstype', models.DO_NOTHING, db_column='GoodTypeID', blank=True, null=True)  # Field name made lowercase.
    firmid = models.ForeignKey('Firms', models.DO_NOTHING, db_column='FirmID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'goods'
        ordering = ["-name"]
    def __unicode__(self):
        return self.uniquecode
    # def sort1(self):
    #     for i in self:
    #         print(i.uniquecode)


class Goodstype(models.Model):
    idgoodstype = models.AutoField(db_column='idGoodsType', primary_key=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', unique=True, max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goodstype'


class Orders(models.Model):
    idorder = models.AutoField(db_column='idOrder', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date')  # Field name made lowercase.
    idclient = models.ForeignKey(Clients, models.DO_NOTHING, db_column='idClient')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Orderslist(models.Model):
    idorderslist = models.AutoField(primary_key=True)
    idorder = models.ForeignKey(Orders, models.DO_NOTHING, db_column='idOrder')  # Field name made lowercase.
    gooduniquecode = models.CharField(db_column='goodUniquecode', max_length=10)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderslist'


class Test(models.Model):
    idtest = models.AutoField(primary_key=True)
    testcol = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True,validators=[MinValueValidator(1),MaxValueValidator(100)])
    testcol1 = models.CharField(max_length=45, blank=True, null=True,validators=[validate_slug])
    creditcard = models.CharField(max_length=45, blank=True, null=True,db_column='CreditCard',validators=[MinLengthValidator(14),MaxLengthValidator(16)])  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'test'
