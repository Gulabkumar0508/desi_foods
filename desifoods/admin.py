from django.contrib import admin
from .models import contact,Product,CustomerOrder

class contactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone' , 'email')

admin.site.register(contact,contactAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','description')

admin.site.register(Product,ProductAdmin)



class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name','product', 'quantity','total','address')

admin.site.register(CustomerOrder,CustomerOrderAdmin)