from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField



class Slider(models.Model):
    img = models.ImageField(upload_to = 'upload/image' ,blank=False)
    
    class Meta:
        verbose_name_plural = 'SLIDER'


class TshirtProperty(models.Model):
    title = models.CharField(max_length=30, null=False)
    slug = models.CharField(max_length=30, null=False, unique=True)
    class Meta:
        abstract = True


    def __str__(self):
        return self.title



class Occasion(TshirtProperty):
    class Meta:
        verbose_name = 'occasions'
        verbose_name_plural = 'OCCASION'



class Idealfor(TshirtProperty):
    class Meta:
        verbose_name = "Idealfor"
        verbose_name_plural = "IDEAL FOR"


class NeckType(TshirtProperty):
    class Meta:
        verbose_name_plural = 'NECK TYPE'
  

class Sleeve(TshirtProperty):
    class Meta:
        verbose_name_plural = 'SLEEVE'
   

class Brand(TshirtProperty):
    class Meta:
        verbose_name_plural = 'BRAND'
 


class Color(TshirtProperty):

    class Meta:
        verbose_name_plural = 'COLOR'
  



class Tshirt(models.Model):
    tshirt_name = models.CharField(max_length=50 , null=False)
    slug = models.CharField(max_length=50)
    discription = models.CharField(max_length=100 , blank=True)
    discount = models.IntegerField()
    image = models.ImageField(upload_to = 'upload/image' ,blank=False )
    image2 = models.ImageField(upload_to = 'upload/image' ,blank=True )
    image3 = models.ImageField(upload_to = 'upload/image' ,blank=True )
    image4 = models.ImageField(upload_to = 'upload/image' ,blank=True )
    occasion = models.ForeignKey(Occasion , on_delete=models.CASCADE)
    Ideal_for = models.ForeignKey(Idealfor, on_delete=models.CASCADE)
    neck_type = models.ForeignKey(NeckType, on_delete=models.CASCADE)
    sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    class Meta:
        # verbose_name = 'Child'
        verbose_name_plural = 'TSHIRT'

    def __str__(self):
        return f'{self.tshirt_name}'


class Sizevariant(models.Model):
    SIZES = (
        ('S','SMALL'),
        ('M','MEDIUM'),
        ('L','LARGE'),
        ('XL','EXTRA LARGE'),
        ('XXL','EXTRA EXTRA LARGE'),
    )
    price = models.IntegerField()
    tshirt = models.ForeignKey(Tshirt ,on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES , max_length=5)
    def __str__(self):
        return f'{self.size} - {self.tshirt.tshirt_name}'


class Cart(models.Model):
    sizeVariant = models.ForeignKey(Sizevariant , on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.sizeVariant.tshirt.tshirt_name
    
    class Meta:
        # verbose_name = 'Child'
        verbose_name_plural = 'CART'

class Order(models.Model):
    # orderStatus = (
    #     ('PANDING','pending'),
    #     ('PLACED','placed'),
    #     ('CANCELED','canceled'),
    #     ('COMPLETE','complet'),
    # )

    paymentMethod = (
        ('COD','cod'),
        ('ONLINE','online'),
    )
    
    # order_status = models.CharField(choices=orderStatus , max_length=15)
    payment_method  = models.CharField(choices=paymentMethod , max_length=15)
    shiping_address  = models.CharField(max_length=100 , null=False)
    phone  = models.CharField(max_length=10, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.IntegerField(null=False)
    date = models.DateTimeField(null=False , auto_now_add=True)


    class Meta:
        verbose_name_plural = 'ORDER'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)  
    size = models.ForeignKey(Sizevariant, on_delete=models.CASCADE)  
    quantity = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    date = models.DateTimeField(null=False , auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ORDER ITEMS'

    def __str__(self):
        return self.tshirt.tshirt_name


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)  
    date = models.DateTimeField(null=False , auto_now_add=True)
    payment_status = CharField(max_length=15 , default='FAILED')
    payment_id = models.CharField(max_length=60)
    payment_request_id = models.CharField(max_length=60 , unique=True, null=False )

    class Meta:
        verbose_name_plural = 'PAYMENT'

