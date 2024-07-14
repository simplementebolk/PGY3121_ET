from django.shortcuts import render, redirect, get_object_or_404
from .models import RankedAccount,CartItem,ContactForm, Comuna
from .forms import ContactForm

def index(request):
    return render(request, 'shop/index.html')

def buy(request):
    return render(request, 'shop/views/nav/buy.html')

def eloboost(request):
    return render(request, 'shop/views/main/eloboost.html')

def coaching(request):
    return render(request, 'shop/views/main/coaching.html')

def riot_points(request):
    return render(request, 'shop/views/main/riot_points.html')

def confirmacion(request):
    return render(request, 'shop/views/nav/confirmacion.html')

def accounts(request):
    cuentas_rankeadas = RankedAccount.objects.all()

    context = {
        'cuentas_rankeadas': cuentas_rankeadas,
    }
    return render(request, 'shop/views/main/accounts.html', context)

def add_to_cart(request, account_id):
    account = RankedAccount.objects.get(pk=account_id)
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
    cart_item, created = CartItem.objects.get_or_create(
        account=account,
        session_key=session_key,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def view_cart(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.subtotal() for item in cart_items)
    context = {
        'cart_items': cart_items,
        'total': total,
    }
    return render(request, 'shop/views/main/cart.html', context)

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)
    cart_item.delete()
    return redirect('cart')

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirigir a la vista 'confirmacion'
            return render(request, 'shop/views/nav/confirmacion.html')  # Ajusta 'confirmacion' al nombre de tu vista o URL
    else:
        form = ContactForm()

    comunas = Comuna.objects.all()
    context = {
        'form': form,
        'comunas': comunas,
    }
    return render(request, 'shop/views/nav/contact_us.html', context)