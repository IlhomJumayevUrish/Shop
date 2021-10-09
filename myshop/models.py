from django.db import models
from fontawesome_5.fields import IconField
from taggit.managers import TaggableManager
# from parler.models import TranslatableModel, TranslatedFields
from parler.models import TranslatableModel, TranslatedFieldsModel
from parler.models import TranslatedFields
# Create your models here.
def image_folder(product,filename):
    names="ProductsImage"
    rasm_name=product
    file_format=filename.split('.')[-1]
    file_name="{}.{}".format(rasm_name,file_format)
    rasm_image_folder="{}/{}".format(names,file_name)
    return rasm_image_folder

def image_folder_blog(blog,filename):
    names="Blog"
    rasm_name=blog
    file_format=filename.split('.')[-1]
    file_name="{}.{}".format(rasm_name,file_format)
    rasm_image_folder="{}/{}".format(names,file_name)
    return rasm_image_folder
class Brend(models.Model):
    title=models.CharField('Nomi',max_length=50)
    slug=models.SlugField('Slug',blank=True)
    def __str__(self):
        return self.title
        
class Category(models.Model):
    title=models.CharField('Nomi',max_length=50)
    slug=models.SlugField( 'Slug',blank=True)
    icon=IconField(blank=True)
    def __str__(self):
        return self.title
    def icon_class(self):
        i=str(self.icon).split(',')
        return f"fa fa-{i[1]}"

class SubCategory(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='SubCategorylar',related_name='products')
    title=models.CharField('Nomi',max_length=50)
    slug=models.SlugField(  'Slug',blank=True)
    def __str__(self):
        return self.title


class Ranglar(models.Model):
    title=models.CharField('Nomi',max_length=50)
    slug=models.SlugField(  'Slug',blank=True)
    def __str__(self):
        return self.title

class Pruduct(models.Model):
    tags=TaggableManager()
    subCategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE,verbose_name="Katalog",related_name="Product")
    title=models.CharField('Nomi',max_length=50)
    slug=models.SlugField(  'Slug',blank=True)
    image=models.ImageField(upload_to=image_folder)
    short_text=models.TextField("Short Text")
    description=models.TextField(blank=True)
    info = models.CharField("Qisqa malumot",max_length=50,blank=True)
    quantity=models.PositiveIntegerField("Soni",default=0)
    old_price=models.PositiveIntegerField("Eski narxi",default=0)
    price=models.PositiveIntegerField('Xozirgi narx',default=0)
    rating=models.PositiveIntegerField('Rating',default=0)
    add_date=models.DateField('Qushilgan sana',auto_now_add=True)
    status=models.BooleanField('Status',default=True)
    brend=models.ForeignKey(Brend,on_delete=models.PROTECT,null=True,blank=True)
    rang=models.ForeignKey(Ranglar,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title 
class ProductImages(models.Model):
    product=models.ForeignKey(Pruduct,on_delete=models.CASCADE,verbose_name='images',related_name="images")
    image=models.ImageField(upload_to=image_folder)

# -------------------------------
class Categorys(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField("Nomi", max_length=50),
        slug = models.SlugField("Slug"),
    )
    icon=IconField(blank=True)
    def __str__(self):
        return self.title
    def icon_class(self):
        i=str(self.icon).split(',')
        return f"fa fa-{i[1]}"
    # class Meta:
    #     verbose_name="Bo'lim"
    #     verbose_name_plural="Bo'limlar"
class SubCategorys(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField('Nomi',max_length=50),
        slug=models.SlugField('Slug',blank=True),
    )
    category=models.ForeignKey(Categorys,on_delete=models.CASCADE,verbose_name='SubCategorylar',related_name='products')
    def __str__(self):
        return self.title
    # class Meta:
    #     verbose_name="Qism bo'lim"
    #     verbose_name_plural="Qism bo'limlar"
class Rang(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField('Nomi',max_length=50),
        slug=models.SlugField('Slug',blank=True),
    )
    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Rang"
        verbose_name_plural="Ranglar"
class Product(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField('Nomi',max_length=50),
        info = models.CharField("Qisqa malumot",max_length=50,blank=True),
        short_text=models.TextField("Short Text"),
        description=models.TextField(blank=True),
        slug=models.SlugField('Slug',blank=True)
       
    )
    tags=TaggableManager()
    subCategory=models.ForeignKey(SubCategorys,on_delete=models.CASCADE,verbose_name="Katalog",related_name="Product")
    image=models.ImageField(upload_to=image_folder)
    quantity=models.PositiveIntegerField("Soni",default=0)
    old_price=models.PositiveIntegerField("Eski narxi",default=0)
    price=models.PositiveIntegerField('Xozirgi narx',default=0)
    rating=models.PositiveIntegerField('Rating',default=0)
    add_date=models.DateField('Qushilgan sana',auto_now_add=True)
    status=models.BooleanField('Status',default=True)
    brend=models.ForeignKey(Brend,on_delete=models.PROTECT,null=True,blank=True)
    rang=models.ForeignKey(Rang,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return self.title 
    class Meta:
        verbose_name="Tavar"
        verbose_name_plural="Tavarlar"
        ordering=['-id']

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='images',related_name="images")
    image=models.ImageField(upload_to=image_folder)
class CartProducts(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='Tavar')
    price=models.PositiveIntegerField("Jami summa",default=0)
    qty=models.PositiveIntegerField("Jami soni",default=0)
    def __str__(self):
        return self.product.title
    # class Meta:
    #     ordering=["-id"]
    #     verbose_name="Savat tavar "
    #     verbose_name_plural="Savat tavarlar "
class Carts(models.Model):
    products=models.ManyToManyField(CartProducts)
    total_price=models.PositiveIntegerField("Umumiy summa",default=0)
    total_quantity=models.PositiveIntegerField("Umumiy soni",default=0)
    create_date=models.DateField("Ochilgan sanasi",auto_now_add=True)
    def clear(self):
        self.products.all().delete()
        self.delete()
    # class Meta:
    #     verbose_name="Savat "
    #     verbose_name_plural="Savatlar "

# ---------------------

class CartProduct(models.Model):
    product=models.ForeignKey(Pruduct,on_delete=models.CASCADE,verbose_name='Tavar')
    price=models.PositiveIntegerField("Jami summa",default=0)
    qty=models.PositiveIntegerField("Jami soni",default=0)
    def __str__(self):
        return self.product.title
    class Meta:
        ordering=["-id"]
        verbose_name="Savat tavar"
class Cart(models.Model):
    products=models.ManyToManyField(CartProduct)
    total_price=models.PositiveIntegerField("Umumiy summa",default=0)
    total_quantity=models.PositiveIntegerField("Umumiy soni",default=0)
    create_date=models.DateField("Ochilgan sanasi",auto_now_add=True)
    def clear(self):
        self.products.all().delete()
        self.delete()
    class Meta:
        verbose_name="Savat"
        verbose_name_plural="Savatlar"


class Provinces(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(max_length=25)
    )
    def __str__(self):
        return self.title
    # class Meta:
    #     verbose_name="Viloyat"
    #     verbose_name_plural="Vloyatlar"

class Districts(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(max_length=25)
    )
    province=models.ForeignKey(Provinces,on_delete=models.CASCADE,verbose_name='Tuman',related_name="Tuman")
    def __str__(self):
        return self.title
    # class Meta:
    #     verbose_name="Tuman"
    #     verbose_name_plural="Tumanlar"
# class Order(models.Model):
#     name=models.CharField("Name",max_length=25)
#     phone=models.CharField("Phone",max_length=25)
#     email=models.CharField("Email",max_length=45,blank=True)
#     mahalla=models.CharField("Mahalla",max_length=100)
#     province=models.ForeignKey(Provinces,on_delete=models.CASCADE,verbose_name='Viloyat')
#     district=models.ForeignKey(Districts,on_delete=models.CASCADE,verbose_name='Tuman')
#     create_date=models.DateField("Qo'shildi",auto_now_add=True)
#     updated_date=models.DateField("O'zgartirildi",auto_now=True)
#     paid=models.BooleanField("To'landi",null=True,blank=True)
#     def __str__(self):
#         return self.name
#     class Meta:
#         verbose_name="Buyurtma"
#         verbose_name_plural="Buyurtmalar"
        
# class OrderItem(models.Model):
#     order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name="orderitm")
#     product=models.ForeignKey(Pruduct,on_delete=models.CASCADE)
#     price=models.PositiveIntegerField(default=0)
#     qty=models.PositiveIntegerField(default=0)
#     def __str__(self):
#         return self.product.title
#     class Meta:
#         verbose_name="Buyurtma tavarlar"
#         verbose_name_plural="Buyurtma tavarlari"

class Orders(models.Model):
    name=models.CharField("Name",max_length=25)
    phone=models.CharField("Phone",max_length=25)
    email=models.CharField("Email",max_length=45,blank=True)
    mahalla=models.CharField("Mahalla",max_length=100)
    province=models.ForeignKey(Provinces,on_delete=models.CASCADE,verbose_name='Viloyat')
    district=models.ForeignKey(Districts,on_delete=models.CASCADE,verbose_name='Tuman')
    create_date=models.DateField("Qo'shildi",auto_now_add=True)
    updated_date=models.DateField("O'zgartirildi",auto_now=True)
    paid=models.BooleanField("To'landi",null=True,blank=True)
    def __str__(self):
        return self.name
    # class Meta:
    #     verbose_name="Buyurtma new"
    #     verbose_name_plural="Buyurtmalar new"
        
class OrderItems(models.Model):
    order=models.ForeignKey(Orders,on_delete=models.CASCADE,related_name="orderitm")
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)
    qty=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.product.title
    # class Meta:
    #     verbose_name="Buyurtma tavarlar new"
    #     verbose_name_plural="Buyurtma tavarlari new"
class Yangiliklar(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField("Name",max_length=50),
        title=models.CharField("Title",max_length=100),
        comment=models.TextField("Comment"),
    )
    image=models.ImageField("Image",upload_to=image_folder_blog)
    vaqt=models.DateField("Vaqt",auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering=['-id']

class Banner(TranslatableModel):
    translations = TranslatedFields(
    title=models.CharField(max_length=25),
    # slug=models.CharField(max_length=25),
    name=models.CharField(max_length=100),
    chegirma=models.CharField(max_length=100),
    short_text=models.TextField(),
    )
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='banner')
    image=models.ImageField(upload_to=image_folder,null=True)
    def __str__(self):
        return self.title
    # class Meta:
    #     verbose_name="Banner"
    #     verbose_name_plural="Bannerlar"
    
# class Comment(models.Model):
