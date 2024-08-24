from django.shortcuts import render,redirect,HttpResponse
from .models import contact,Product,CustomerOrder
from cart.cart import Cart
from django.http import JsonResponse

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("food")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    product_id_str = str(product.id)
    if product_id_str in cart.cart:
        current_quantity = cart.cart[product_id_str]['quantity']
        if current_quantity > 1:
            cart.decrement(product=product)
        else:
            cart.remove(product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")




def index(request):
    return render(request,'index.html')


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contacts = contact(name=name,phone=phone,email=email,message=message)
        contacts.save()
        return redirect('index')
    return render(request,'contact_page.html')


def food(request):
    product = Product.objects.all()
    print(product)
    context={
        'product': product,
    }
    return render(request,'food.html',context)



def about(request):
    return render(request,'about_us.html')




def checkout(request):
    if request.method == 'POST':
        cart = request.session.get('cart',{})
        if not cart:
            return JsonResponse({"error": "your card is empty, please add something"})
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        for i in cart:
            price = cart[i]['price']
            quantity = int(cart[i]['quantity'])
            total = float(price) * int(quantity)
            CustomerOrder_instance = CustomerOrder(
                image=cart[i]['image'],
                product=cart[i]['name'],
                price=cart[i]['price'],
                quantity=cart[i]['quantity'],
                total=total,
                customer_name =name,
                phone=phone,
                address=address,
            )
            CustomerOrder_instance.save()
        request.session['cart'] = {}
        return redirect('food')
    cart = request.session.get('cart', {})
    cart_total_amount = sum(float(item['price']) * int(item['quantity']) for item in cart.values())
    context = {
        'cart': cart,
        'cart_total_amount': cart_total_amount,
    }
    return render(request, 'checkout.html', context)




def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_total_amount = sum(float(item['price']) * int(item['quantity']) for item in cart.values())

    context = {
        'cart': cart,
        'cart_total_amount': cart_total_amount,
    }
    return render(request, 'cart_detail.html',context)



def product_detail(request,id):
    product = Product.objects.filter(id = id).first()

    data={
        'product':product,
    }
    return render(request,'view_product.html',data)
