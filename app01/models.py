from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class Activity(models.Model):
    name = models.CharField(max_length=64, verbose_name="活动名称")
    datetime_start = models.DateTimeField(verbose_name="活动开始时间") # 活动开始时间
    datetime_end = models.DateTimeField(verbose_name="活动结束时间") # 活动结束时间
    main_image = models.ImageField(upload_to="activity", null=True)
    number_people = models.PositiveIntegerField()
    address = models.CharField(max_length=128, verbose_name="活动地址")
    orderpeople_num = models.IntegerField(verbose_name="当前报名人数", default=0)
    view_number = models.PositiveIntegerField(verbose_name="浏览数")
    collect_number = models.PositiveIntegerField(verbose_name="收藏数", default=0)
    partner = models.ManyToManyField(to="Partner") # 合作方
    important_guests = models.ManyToManyField(to="Account", related_name="important_guests")

    activity_status_choices = ((0, '正在报名'), (1, '正在进行'), (2, '已过期'))
    activity_status = models.SmallIntegerField(choices=activity_status_choices, default=0)

    activity_type_choices = ((0, '免费'), (1, '收费'))
    activity_type = models.SmallIntegerField(choices=activity_type_choices, default=0, verbose_name="活动的费用类型")
    tag = models.ManyToManyField(to="Tag", blank=True, verbose_name="标签")
    comment = GenericRelation("Comment")

    def __str__(self):
        return "活动{"+self.name+"}"

class Partner(models.Model):
    name = models.CharField(max_length=128, verbose_name="合作方名称")
    breif = models.TextField(max_length=1024, verbose_name="合作方简介")

    def __str__(self):
        return self.name + '机构'

class ActivityDetail(models.Model):
    activity = models.OneToOneField("Activity", on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(verbose_name="活动详情")

    def __str__(self):
        return "{"+self.activity.name + "}的详情"

class Tag(models.Model):
    # content_type 表示content type表
    # content_type = models.ForeignKey(ContentType, blank=True, null=True, verbose_name="类型", on_delete=models.CASCADE)
    # # object_id表示
    # object_id = models.PositiveIntegerField(blank=True, null=True)
    # content_object = GenericForeignKey('content_type', 'object_id')

    name = models.CharField(max_length=64, unique=True)
    breif = models.TextField(max_length=1024)

    def __str__(self):
        return self.name

class Institute(models.Model):
    name = models.CharField(max_length=64, verbose_name="文章标题")
    post_datetime = models.DateTimeField(verbose_name="文章发布日期", auto_now_add=True)
    author = models.ForeignKey(to="Account", verbose_name="作者", max_length=64, on_delete=models.SET_NULL, null=True, blank=True)
    thumb_up = models.PositiveIntegerField(verbose_name="点赞数")
    view_num = models.PositiveIntegerField(verbose_name="浏览数")
    reply_num = models.PositiveIntegerField(verbose_name="回复数")
    main_image = ProcessedImageField(
        upload_to="institute",
        null=True,
        processors=[ResizeToFill(600, 400)],
        format='JPEG',
        options={'quality': 75}
    )

    tag = models.ManyToManyField(to=Tag, blank=True, verbose_name="标签")
    comment = GenericRelation("Comment")

    def __str__(self):
        return self.name

class InstituteDetail(models.Model):
    institute = models.ForeignKey("Institute", on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(verbose_name="学院帖子详情")

    def __str__(self):
        return "{"+self.institute.name + "}的内容"

class InstituteRec(models.Model):
    institute = models.OneToOneField(to="Institute", on_delete=models.SET_NULL, blank=True, null=True)
    weights_choices = ((1, '低'), (2, '中'), (3, '高'))
    weights = models.SmallIntegerField(choices=weights_choices, default=2)

    def __str__(self):
        return "{推荐}" + self.institute.name

class subjectList(models.Model):
    name = models.CharField(max_length=64, unique=True)
    brief = models.TextField(verbose_name="专题的详情")
    article = models.ManyToManyField(to="Institute")
    main_image = ProcessedImageField(
        upload_to="subject",
        null=True,
        processors=[ResizeToFill(825, 300)],
        format='JPEG',
        options={'quality': 75}
    )

    def __str__(self):
        return "{" + self.name + "}专题"

class Products(models.Model):
    name = models.CharField(max_length=64, verbose_name="商品名称")
    product_img = ProcessedImageField(
        upload_to="products",
        null=True,
        processors=[ResizeToFill(800, 800)],
        format='JPEG',
        options={'quality': 75}
    )
    product_type_choices = ((0, '纪念品'), (1, '书籍'), (2, '文化衫'))
    product_type = models.SmallIntegerField(choices=product_type_choices)
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    sale_num = models.PositiveIntegerField(verbose_name="销售额", default=0)
    store_num = models.PositiveIntegerField(verbose_name="库存量", default=0)
    post_date = models.DateField(verbose_name="发布日期", blank=True, null=True)
    status_choices = ((0, '预定中'), (1, '售卖中'), (2, '已售空'))
    status = models.SmallIntegerField(choices=status_choices)
    def __str__(self):
        return "{" + self.get_product_type_display() + "}" + self.name

class ProductsDetail(models.Model):
    product = models.OneToOneField("Products", on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField(verbose_name="商品描述",max_length=2048)

    def __str__(self):
        return "{" + self.product.name + "}详情"

class ProductsParams(models.Model):
    product = models.ForeignKey(to="Products", on_delete=models.SET_NULL, blank=True, null=True)
    meta_key = models.CharField(max_length=64, verbose_name="参数名", null=True, blank=True)
    meta_value = models.CharField(max_length=255, verbose_name="参数值", null=True, blank=True)

    def __str__(self):
        return self.product.name + "{" + self.meta_key + "} " + self.meta_value

class Params2Products(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, blank=True)
    param = models.ForeignKey(ProductsParams, on_delete=models.SET_NULL, null=True, blank=True)

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
    weights_choices = ((0,"普通会员"),(1, '青铜会员'), (2, '白银会员'), (3, '金牌会员'))
    weights = models.SmallIntegerField(choices=weights_choices, default=0)
    # 贝里余额
    balance = models.PositiveIntegerField(default=0, verbose_name="可提现和使用余额", null=True)

    # 多对多了
    article = models.ManyToManyField(to="Institute", blank=True, verbose_name="发布的文章")
    activity = models.ManyToManyField(to="Activity", blank=True, verbose_name="参加的活动")
    # products = models.ManyToManyField(to="Products", blank=True, verbose_name="购买的产品")

    def __str__(self):
        return self.username

class UserAuthToken(models.Model):
    """
    用户Token表
    """
    user = models.OneToOneField(to="Account", on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)