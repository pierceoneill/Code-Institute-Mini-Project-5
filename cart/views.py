from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """A view that renders the cart contents page"""
    print('Cart from view_cart view: {}'.format(request.session.get('cart')))
    return render(request, "cart.html")
    
    
def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the cart"""
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    print('Cart from add_to_cart view: {}'.format(cart))
    if item_id in cart:
        cart[item_id] = int(cart[item_id]) + quantity
    else:
        cart[item_id] = cart.get(item_id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
    
def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    print('Cart from adjust_cart view: {}'.format(cart))
    
    if quantity > 0:
        cart[item_id] = quantity
    else:
        cart.pop(item_id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))