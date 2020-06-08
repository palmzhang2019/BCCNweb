from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=64, verbose_name="活动名称")
    datetime_start = models.DateTimeField(verbose_name="活动开始时间") # 活动开始时间
    datetime_end = models.DateTimeField(verbose_name="活动结束时间") # 活动结束时间
    main_image = models.ImageField(upload_to="activity", null=True)
    number_people = models.PositiveIntegerField()
    address = models.CharField(max_length=128, verbose_name="活动地址")
    view_number = models.PositiveIntegerField(verbose_name="浏览数")
    collect_number = models.PositiveIntegerField(verbose_name="收藏数", default=0)
    partner = models.ManyToManyField(to="Partner") # 合作方
    important_guests = models.CharField(max_length=32)
    tag = models.CharField(max_length=32, verbose_name="标签", null=True)

    activity_type_choices = ((0, '免费'), (1, '收费'))
    activity_type = models.SmallIntegerField(choices=activity_type_choices, default=0, verbose_name="活动的费用类型")

    comment = GenericRelation("Comment")

class Partner(models.Model):
    name = models.CharField(max_length=128, verbose_name="合作方名称")
    breif = models.TextField(max_length=1024, verbose_name="合作方简介")

class ActivityDetail(models.Model):
    activity = models.OneToOneField("Activity", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="活动详情")

class Institute(models.Model):
    name = models.CharField(max_length=64, verbose_name="文章标题")
    post_datetime = models.DateTimeField(verbose_name="文章发布日期", auto_now_add=True)
    author = models.CharField(max_length=32, verbose_name="作者")
    thumb_up = models.PositiveIntegerField(verbose_name="点赞数")
    view_num = models.PositiveIntegerField(verbose_name="浏览数")
    reply_num = models.PositiveIntegerField(verbose_name="回复数")
    main_image = models.ImageField(upload_to="institute", null=True)
    tag = models.CharField(max_length=32, verbose_name="标签", null=True)

    comment = GenericRelation("Comment")

class InstituteDetail(models.Model):
    institute = models.ForeignKey("Institute", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="学院帖子详情")

class Products(models.Model):
    name = models.CharField(max_length=64, verbose_name="商品名称")
    product_img = models.ImageField(upload_to='products')
    product_type_choices = ((0, '纪念品'), (1, '书籍'), (2, '文化衫'))
    product_type = models.SmallIntegerField(choices=product_type_choices)

    post_date = models.DateField(verbose_name="发布日期", blank=True, null=True)
    status_choices = ((0, '预定中'), (1, '售卖中'), (2, '已售空'))
    status = models.SmallIntegerField(choices=status_choices)

class ProductsDetail(models.Model):
    product = models.OneToOneField("Products", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="商品描述",max_length=2048)

class ProductsParams(models.Model):
    name = models.CharField(max_length=32, verbose_name="产品的参数")
    product = models.ManyToManyField(Products, through='Params2Products')

class Params2Products(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    param = models.ForeignKey(ProductsParams, on_delete=models.CASCADE)

class Comment(models.Model):
    """通用的评论表"""
    content_type = models.ForeignKey(ContentType, blank=True, null=True, verbose_name="类型", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    p_node = models.ForeignKey("self", blank=True, null=True, verbose_name="父级评论", on_delete=models.CASCADE)
    content = models.TextField(max_length=1024)
    account = models.ForeignKey("Account", verbose_name="会员名", on_delete=models.CASCADE)
    disagree_number = models.IntegerField(default=0, verbose_name="踩")
    agree_number = models.IntegerField(default=0, verbose_name="赞同数")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name_plural = "19. 通用评论表"

# ########################### 3. 用户相关 ################################

class Account(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField("密码", max_length=64)

    uid = models.CharField(max_length=64, unique=True, help_text='微信用户绑定和CC视频统计')  # 与第3方交互用户信息时，用这个uid,以避免泄露敏感用户信息
    openid = models.CharField(max_length=128, blank=True, null=True)
    # 贝里余额
    balance = models.PositiveIntegerField(default=0, verbose_name="可提现和使用余额")

class UserAuthToken(models.Model):
    """
    用户Token表
    """
    user = models.OneToOneField(to="Account", on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)