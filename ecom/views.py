from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.contrib import messages
from ecom.models import Category, Product, Cart, Profile, User


# Create your views here.

def indexview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'index.html')

def aboutview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'about.html')

def blogdetailview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'blog-detail.html')

def blogview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'blog.html')

def contactview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'contact.html')

def homeview2(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'home-02.html')

def homeview3(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'home-03.html')

def productdetailview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'product-detail.html')

def productview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'product.html')

def cartview(request):
    # return HttpResponse("welcome to website.")
    return render(request, 'shoping-cart.html')

def home(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    cart = Cart.objects.filter(user=request.user)

    allproducts = Product.objects.all()
    trending_products = Product.objects.filter(trending=1)
    context = {'allproducts':allproducts, 'trending_products':trending_products, 'cart':cart, 'cartitems':cartitems, 'total_price':total_price}
    return render(request, "layouts/index.html", context)

def allproducts(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    cart = Cart.objects.filter(user=request.user)

    allproducts = Product.objects.all()
    context = {'allproducts':allproducts, 'cart':cart, 'cartitems':cartitems, 'total_price':total_price}
    return render(request, "products/allproducts.html", context)

def collections(request):
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    cart = Cart.objects.filter(user=request.user)

    category = Category.objects.filter(status=0)
    context = {'category':category, 'cart':cart, 'cartitems':cartitems, 'total_price':total_price}
    return render(request, 'collections.html', context)

def collectionsview(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'products/index.html', context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products': products}
        else:
            messages.error(request, "No such product found")
            return redirect('collections')
    else:
        messages.error(request, "No such category found")
        return redirect('collections')
    return render(request, "products/view.html", context)

def productlistAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    productList = list(products)

    return JsonResponse(productList, safe=False)

def searchproduct(request):
    if request.method == 'POST':
        searchedterm = request.POST.get('productsearch')
        if searchedterm == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchedterm).first()

            if product:
                return redirect('collections/'+product.category.slug+'/'+product.slug)
            else:
                messages.info(request, "No product matched your search")
                return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))

def myaccount(request):
    userprofile = Profile.objects.filter(user=request.user).first()

    currentuser = User.objects.filter(id=request.user.id).first()

    if not currentuser.first_name:
        currentuser.first_name = request.POST.get('fname')
        currentuser.last_name = request.POST.get('lname')
        currentuser.save()

    if not Profile.objects.filter(user=request.user):
        userprofile = Profile()
        userprofile.user = request.user
        userprofile.phone = request.POST.get('phone')
        userprofile.address = request.POST.get('address')
        userprofile.city = request.POST.get('city')
        userprofile.state = request.POST.get('state')
        userprofile.country = request.POST.get('country')
        userprofile.pincode = request.POST.get('pincode')
        userprofile.save()
            
    context = {'userprofile':userprofile}
    return render(request, 'profile.html', context)