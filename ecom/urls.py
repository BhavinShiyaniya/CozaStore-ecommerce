from django.urls import path
from ecom.views import indexview
from ecom.views import aboutview, blogdetailview, blogview, cartview, contactview, homeview2, homeview3, productdetailview, productview, collections, collectionsview, home, productlistAjax, searchproduct, allproducts, myaccount


from ecom.controller.authview import register, loginpage, logoutpage
from ecom.controller.cart import addtocart, viewcart, updatecart, deletecartitem
from ecom.controller.wishlist import indexwish, addtowishlist, deletewishlistitem
from ecom.controller.checkout import indexcheck, placeorder, razorpaycheck, orders
from ecom.controller.order import indexorder, vieworder

urlpatterns = [
    # path('', indexview,name='index'),
    path('index/', indexview,name='index'),
    path('about/', aboutview,name='about'),
    path('contact/', contactview,name='contact'),
    path('blogdetail/', blogdetailview,name='blogdetail'),
    path('blog/', blogview,name='blog'),
    path('home2/', homeview2,name='home2'),
    path('home3/', homeview3,name='home3'),
    path('productdetail/', productdetailview,name='productdetail'),
    path('product/', productview,name='product'),
    # path('cart/', cartview,name='cart'),
    # ===============================================================
    path('', home,name='home'),
    path('home/', home,name='home'),

    path('myaccount/', myaccount,name='myaccount'),

    path('products/', allproducts,name='allproducts'),

    path('collections/', collections,name='collections'),
    path('collections/<str:slug>', collectionsview,name='collectionsview'),
    path('collections/<str:cate_slug>/<str:prod_slug>', productview,name='productview'),

    path('product-list', productlistAjax),
    path('searchproduct', searchproduct, name='searchproduct'),

    path('register/', register, name='register'),
    path('login/', loginpage, name='loginpage'),
    path('logout/', logoutpage, name='logout'),

    path('add-to-cart', addtocart, name='addtocart'),
    path('cart/', viewcart, name='cart'),
    path('update-cart', updatecart, name='updatecart'),
    path('delete-cart-item', deletecartitem, name='deletecartitem'),

    path('wishlist', indexwish, name="wishlist"),
    path('add-to-wishlist', addtowishlist, name="addtowishlist"),
    path('delete-wishlist-item', deletewishlistitem, name="deletewishlistitem"),

    path('checkout', indexcheck, name="checkout"),
    path('place-order', placeorder, name="placeorder"),
    path('proceed-to-pay', razorpaycheck),

    path('my-orders', indexorder, name="myorders"),
    path('view-order/<str:t_no>', vieworder, name="orderview"),
]