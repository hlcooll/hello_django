# from django.db import models
#
# # Create your models here.
# class Publisher(models.Model):
#     name=models.CharField(max_length=30,verbose_name='名字')
#     address=models.CharField("地址",max_length=50)
#     number=models.CharField("编号",max_length=60)
#     website=models.URLField("网址")
#
#     class Meta:
#         verbose_name='资产'
#         verbose_name_plural=verbose_name
#
#     def __str__(self):
#         return self.name
#


from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=30, verbose_name='领用人')
    computer = models.CharField("主机箱", max_length=50)
    display = models.CharField("显示器", max_length=60)
    keyboard = models.CharField("键盘", max_length=50)
    mouse = models.CharField("鼠标", max_length=60)
    memory = models.CharField("内存", max_length=50)
    status = models.CharField("状态", max_length=60)

    class Meta:
        verbose_name = '资产'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class hardware(models.Model):
    number=models.CharField(max_length=30,verbose_name='编号')
    address=models.CharField("日期",max_length=50)
    product_name=models.CharField("商品名称",max_length=60)
    commodity_brand=models.CharField("商品品牌",max_length=50)
    unit_price=models.CharField("单价",max_length=60)
    quantity=models.CharField("数量",max_length=50)
    amount=models.CharField("金额",max_length=60)
    tis=models.CharField("安装情况 /领用人",max_length=50)
    status=models.CharField("状态",max_length=60)
    norc=models.CharField("可领用数",max_length=50)

    class Meta:
        verbose_name='硬件'
        verbose_name_plural=verbose_name
