from django.db import models

class TshirtProperty(models.Model):
    title = models.CharField(max_length=30, null=False)
    slug = models.CharField(max_length=30, null=False, unique=True)
    class Meta:
        abstract = True


    def __str__(self):
        return self.title



class Occasion(TshirtProperty):
    pass



class Idealfor(TshirtProperty):
    pass


class NeckType(TshirtProperty):
    pass

class Sleeve(TshirtProperty):
    pass

class Brand(TshirtProperty):
    pass


class Color(TshirtProperty):
    pass



class Tshirt(models.Model):
    tshirt_name = models.CharField(max_length=50 , null=False)
    discription = models.CharField(max_length=100 , blank=True)
    discount = models.IntegerField()
    image = models.ImageField(upload_to = 'upload/image' ,blank=False )
    image2 = models.ImageField(upload_to = 'upload/image' ,blank=True )
    image3 = models.ImageField(upload_to = 'upload/image' ,blank=True )
    image4 = models.ImageField(upload_to = 'upload/image' ,blank=True )
    occasion = models.ForeignKey(Occasion , on_delete=models.CASCADE)
    deal_for = models.ForeignKey(Idealfor, on_delete=models.CASCADE)
    neck_type = models.ForeignKey(NeckType, on_delete=models.CASCADE)
    sleeve = models.ForeignKey(Sleeve, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

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
    tshirt = models.ForeignKey(Tshirt , on_delete=models.CASCADE)
    size = models.CharField(choices=SIZES , max_length=5)









