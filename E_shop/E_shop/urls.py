
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME, name='home'),
    path('base/', views.BASE, name='base'),
    path('products/', views.PRODUCT, name='products'),
    
    path('search/', views.SEARCH, name='search'),
    path('products/<str:id>', views.PRODUCT_DETAIL_PAGE, name='product_detail'),
    path('contact/', views.CONTACT_Page, name='contact'),
    path('register/', views.Handle_Register, name='register'),
    path('login/', views.Handle_Login, name='login'),
    path('logout/', views.Handle_Logout, name='logout'),
    
    
    
    # cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('cart/checkout/',views.CHECK_OUT,name='checkout'),
    path('cart/checkout/placeorder/',views.PLACE_ORDER, name='place_order'),
    path('success',views.success, name='success'),
    path('Your_Order',views.Your_Order, name='your_order'),
    path('about_us',views.About_Us, name='about_us'),
    path('blog',views.Blog, name='blog'),
    path('blog/single_blog',views.Single_Blog, name='single_blog'),

    
    
    
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

