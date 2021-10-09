from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib import messages
from .models import*
import datetime
from .task import*
from django.template.loader import render_to_string, get_template
from django.core.mail import send_mail
from projectshop.settings import EMAIL_HOST_USER
from django.utils.html import strip_tags
def cart_init(request,delete=None):
    cart_id=request.session.get('cart_id')
    if delete:
        del request.session['cart_id']
        cart=Carts.objects.get(id=cart_id)
        return True
    today=datetime.date.today()
    t=datetime.timedelta(days=2)
    two_days_ego=today-t
    if not cart_id:
        cart=Carts.objects.create()
        cart_id=cart.id
        request.session['cart_id']=cart_id
        request.session.set_expiry(60*60*24*2)
        c=Carts.objects.filter(create_date__lte=two_days_ego).delete()
    cart=Carts.objects.get(id=cart_id)
    return cart
def cart_add(request):
    product_id=int(request.GET.get('data'))
    product=Product.objects.get(id=product_id)
    qty=request.GET.get('qty')
    if not qty:
        qty=1
    qty=int(qty)
    cart=cart_init(request)
   
    try:
        cart_product=cart.products.get(product=product)
        cart_product.qty+=qty
        cart_product.price+=product.price*qty
        cart_product.save()
        cart.total_price+=product.price*qty
        cart.total_quantity+=qty
        cart.save()
        return JsonResponse({'status':"Tavar  qo'shildi"})
    except:
        cart.products.create(product=product,price=product.price*qty,qty=qty)
        cart.total_price+=product.price*qty
        cart.total_quantity+=qty
        cart.save()
        return JsonResponse({'status':" Tavar qo'shildi"})
class cart_detail(View):
    def get(self,request):
        cart=cart_init(request)
        products=cart.products.all()
        province=Provinces.objects.all()
        return render(request,"shopping-cart.html",{"products":products,"cart":cart,"province":province})
    def post(self,request):
        province_id=request.POST.get("province_id")
        district_id=request.POST.get("district_id")
        province=Provinces.objects.get(id=int(province_id))
        district=Districts.objects.get(id=int(district_id))
        mahalla=request.POST.get("mahalla")
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        orders=Orders.objects.create(name=name,phone=phone,email=email, mahalla=mahalla,province=province,district=district)
        cart=cart_init(request)
        for i in cart.products.all():
            OrderItems.objects.create(order=orders,product=i.product,price=i.price,qty=i.qty)
        ordrt_email_send(orders.id,email)
        #-------------------------
        cart.clear()
        # send_mail(title,xabar,EMAIL_HOST_USER,[email],fail_silently=False)

        cart_init(request,delete=True)
        messages.success(request, "Tavarlar buyurtma qilindi!")
        return redirect('myshop:shopping-cart')


    
def cart_delete(request):
    cartproduct_id=int(request.GET.get('data'))
    cart=cart_init(request)
    try:
        cart_product=cart.products.get(id=cartproduct_id)
        cart.total_price-=cart_product.price
        cart.total_quantity-=cart_product.qty
        cart.save()
        cart_product.delete()
        return JsonResponse({'status':200,"cart_total_price":cart.total_price,"cart_total_qty":cart.total_quantity})
    except:
        return JsonResponse({'status':400})
def Change_cart(request):
    try:
        qty=int(request.GET.get("qty"))
        cartproduct_id=int(request.GET.get("cartproduct_id"))
        cart=cart_init(request)
        cart_product=cart.products.get(id=cartproduct_id)
        cart.total_price+=(qty-cart_product.qty)*int(cart_product.product.price)
        cart.total_quantity+=qty-int(cart_product.qty)
        cart.save()
        cart_product.qty=qty
        cart_product.price=qty*int(cart_product.product.price)
        cart_product.save()
        # print(cart_product.price)
        return JsonResponse({'status':200,'cart_product_price':cart_product.price,"cart_total_price":cart.total_price,"cart_total_qty":cart.total_quantity})
    except:
        return JsonResponse({"status":500})
from .serialezrs import ProductSerializers,DistrictSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
def shop_cart(request):
    cart=cart_init(request)
    data={
    'total_quantity':cart.total_quantity,
    'total_price':cart.total_price,
    'products':[],
    }
    for i in cart.products.all():
        data['products'].append({
            'title':i.product.title,
            'image':i.product.image.url,
            'price':i.product.price,
            'prices':i.price,
            'qty':i.qty,
            'id':i.product.id,
            'id_cp':i.id,
        })
    return JsonResponse(data)

@api_view(['GET'])
def Search_products(request):
    data=request.GET.get("data")
    if data is None:
        return JsonResponse({'status':500})
    
    products=Product.objects.all()
    a=[]
    for i in products:
        if i.title.find(data)!=-1:
            print(i.title)
            a.append(i)
    serial=ProductSerializers(a,many=True)
    data={'products':products}
    return Response(serial.data)
@api_view(['GET'])
def District_Provice(request):
    data=request.GET.get("data")
    province=Provinces.objects.get(id=int(data))
    district=province.Tuman.all()
    serial=DistrictSerializers(district,many=True)
    data={'district':district}
    return Response(serial.data)
