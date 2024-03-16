from django.db import models

# Create your models here.
class Contact_Us_db(models.Model):
    name = models.CharField(max_length=30 , verbose_name="نام کاربر")
    phone = models.IntegerField(verbose_name="تلفن")
    email = models.EmailField(max_length=100 , verbose_name="ایمیل")
    text =  models.TextField(verbose_name="متن پیام")
    date =  models.DateField(auto_now_add=True , verbose_name="تاریخ ارسال" , null=True)
    readed_by_admin = models.BooleanField(default=False , verbose_name="خوانده شده توسط ادمین" , null=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name ="ارتباط با ما"
        verbose_name_plural = "ارتباط با ما ها"
class Producdt(models.Model):
    title = models.CharField(max_length=50 , verbose_name="سربرگ محصول")
    name = models.CharField(max_length=50 , verbose_name="نام محصول")
    image = models.ImageField(upload_to="media" ,verbose_name="تصویر محصول")
    price = models.IntegerField(verbose_name="قیمت محصول")
    description = models.TextField(verbose_name="توضیحات محصول")
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = 'محصولات'
class Tag(models.Model):
    product = models.ForeignKey(Producdt , on_delete=models.CASCADE)
    tag = models.CharField(max_length=50 ,verbose_name="تگ فارسی")
    tag_url = models.CharField(max_length=50 , verbose_name="تگ انگلیسی محصول")

class NewsUser(models.Model):
    Email = models.EmailField(verbose_name="ایمیل")
    def __str__(self):
        return f"{self.Email}"
    class Meta:
        verbose_name = 'کاربر دنبال کننده'
        verbose_name_plural = "کاربر های دنبال کننده"