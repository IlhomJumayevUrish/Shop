from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect,reverse
from django.views.generic.detail import DetailView
from django.utils.translation import gettext as _
from django.core.cache import cache
from .models import*
from .ajax import cart_init
def home(request):
        # request.session.clear()
        # CartProduct.objects.all().delete()
        categorys=Categorys.objects.all()
        blogs=Yangiliklar.objects.all()
        newproducts=Product.objects.all()[0:6]
        banners=Banner.objects.all()[:5]
        context={"categorys":categorys,"blogs":blogs,"newproducts":newproducts,'banners':banners}
        return render(request,'home.html',context)
def erorr(request):
        return render(request,'404.html')
def blog(request):
        return render(request,'blog.html')
def checkout(request):
        return render(request,'checkout.html')
def blog_details(request):
        return render(request,'blog-details.html')
def faq(request):
        return render(request,'faq.html')
def my_wishlist(request):
        return render(request,'my-wishlist.html')
def product_comparison(request):
        return render(request,'product-comparison.html')        
def sign_in(request):
        return render(request,'sign-in.html')
def contact(request):
        return render(request,'contact.html')
def terms_conditions(request):
        return render(request,'terms-conditions.html')
def track_orders(request):
        return render(request,'track-orders.html')
def Wrapper(request):
        return render(request,'wrapper.html')
class Subcategory_product(View):
        def get(self,request,sub_slug):
                try:
                        subcategorys=SubCategorys.objects.all()
                        subcategory=subcategorys[0]
                        for i in subcategorys:
                                if i.slug == sub_slug:
                                        subcategory=i
                                     
                except:
                        return render(request,"404.html")
                products=subcategory.Product.all()
                categorys=Categorys.objects.all()
                # print(products)
                banner=True
                for i in products:
                        if i.banner.all():
                                banner=i.banner.all()
                                break
                context={"products":products,"categorys":categorys,'banner':banner}
                return render(request,'subcategory/subcategory_product.html',context)
class ProductDetail(DetailView):
        model=Product
        template_name="prodact/detail.html"
        context_object_name="product"
def logouts(request):
    logout(request)
    return redirect('myshop:home')