from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import *




def index(request):
    return render(request,'main/index.html')

def about(request):
    products = Product.objects.all()
    return render(request,'main/about.html', {'products': products})

def map(request):
    return render(request,'main/map.html')

@login_required
def profile_view(request):
    return render(request, 'web/profile.html')

class RegisterView(FormView):

    template_name = 'registration/register.html'
    success_url = reverse_lazy("web:profile")

def form_valid(self,form):
    form.save()
    return super().form_valid(form)

def product(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'main/product.html', {'product': product})

@login_required
def cart(request):
    cart_items = Cart.objects.all()
    total_cost = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'main/cart.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    cart_item, created = Cart.objects.get_or_create(client=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id)
    cart_item.delete()
    return redirect(reverse('cart'))

@login_required
def order(request):
    order_items = Order.objects.filter(user=request.user)
    return render(request, 'main/order_menu.html', {'order_items': order_items})

@login_required
def order_add(request, product_id):
    if request.method == 'POST':
        # Получаем товар по его идентификатору
        product = Product.objects.get(pk=product_id)

        # Создаем экземпляр заказа для текущего пользователя и товара
        order = Order.objects.create(
            user=request.user,
            product=product,
            status='New'  # Измените на нужный вам статус
        )

        # Удаляем все товары из корзины для текущего пользователя
        Cart.objects.filter(client=request.user).delete()

        # Перенаправляем пользователя на страницу заказов
        return redirect('order')
    else:
        # Если метод запроса не POST, возвращаем пользователя на страницу корзины
        return redirect('cart')


def wherefind(request):
    return render(request, 'main/wherefind.html')