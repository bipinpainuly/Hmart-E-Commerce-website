from django.contrib import admin
from  .models import *

class ImageTublerinline(admin.TabularInline):
    model = Image

class TagTublerinline(admin.TabularInline):
    model = Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines=[ImageTublerinline,TagTublerinline]

class OrderItemTublerinline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTublerinline]
    list_display = ['firstname','phone', 'email','payment_id','paid','date']
    search_fields = ['firstname','email','payment_id']
    
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product,ProductAdmin)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Contact_US)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)

