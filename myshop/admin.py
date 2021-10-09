from django.contrib import admin
from .models import*
from parler.admin import TranslatableAdmin
# Register your models here.
from django.utils.safestring import mark_safe
# @admin.register(Category)
@admin.register(Brend)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','slug']
    prepopulated_fields={'slug':("title",)}

# @admin.register(SubCategory)
# class SubCategoryAdmin(admin.ModelAdmin):
#     list_display=['title','slug']
#     prepopulated_fields={'slug':("title",)}
# class ProductImagesAdmin(admin.TabularInline):
#     model=ProductImages

class ProductAdminQuantityFilter(admin.SimpleListFilter):
    title="Soni bo'yicha saralash!"
    parameter_name='quantity'
    def lookups(self,request,model_admin):
        return (
            ('Kam','Kam qolganlar'),
            ('Normal','Normal'),
            ("Ko'p","Ko'p qolganlar"),
        )
    def queryset(self,request,queryset):
        if self.value()=='Kam':
            return queryset.filter(quantity__lte=5)
        if self.value()=='Normal':
            return queryset.filter(quantity__gt=5,quantity__lte=20)
        if self.value()=="Ko'p":
            return queryset.filter(quantity__gt=20)
        
# @admin.register(Pruduct)
# class ProductAdmin(admin.ModelAdmin):
#     list_display=['title','soni','price']
#     list_filter=[ProductAdminQuantityFilter]
#     prepopulated_fields={'slug':("title",)}
#     inlines=[ProductImagesAdmin]
#     def soni(self,instnec):
#         if instnec.quantity==0:
#             return mark_safe("<b style='color:red'>To'gagan</b>")
#         else:
#             return instnec.quantity
# @admin.register(CartProduct)
@admin.register(CartProducts)
class CartProductAdmin(admin.ModelAdmin):
    list_display=['product','price','qty']
# @admin.register(Cart)
@admin.register(Carts)
class CartAdmin(admin.ModelAdmin):
    list_display=['Savat','total_price','total_quantity']
    def Savat(self,instnec):
        return "Savat"


class OrderItemAdmin(admin.TabularInline):
    model=OrderItems
    raw_fields=['product']
    extra=1

@admin.register(Orders)
class OrderAdmin(admin.ModelAdmin):
    list_display=['name','phone','province','district']
    list_filter=['paid','create_date','updated_date']
    inlines=[OrderItemAdmin]
# admin.site.register(Banner)


# -------------------------
@admin.register(Yangiliklar)
@admin.register(Banner)
@admin.register(Provinces)
@admin.register(Districts)
class FactAdmin(TranslatableAdmin):
    list_display=['title']
@admin.register(Rang)
@admin.register(Categorys)
@admin.register(SubCategorys)
class CategorAdmin(TranslatableAdmin):
    list_display=['title','slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }

class ProductImageAdmin(admin.TabularInline):
    model=ProductImage
@admin.register(Product)
class TavarAdmin(TranslatableAdmin):
    list_display=['title','soni','price']
    list_filter=[ProductAdminQuantityFilter]
    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }
    inlines=[ProductImageAdmin]
    def soni(self,instnec):
        if instnec.quantity==0:
            return mark_safe("<b style='color:red'>Yo'q</b>")
        else:
            return instnec.quantity

# -------------------------