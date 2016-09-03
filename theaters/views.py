from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from carts.models import CartItem, Cart
from orders.models import Order
from plays.models import Showing
from theaters.models import Organizer
# Create your views here.


# TODO: add dashboard


"""
Organizer dashboard to view all reservations for a single showing
"""

@login_required
def organizer_dashboard(request):
    organizer = Organizer.objects.get(user=request.user)
    showings = Showing.objects.filter(event__organizer=organizer)
    return render(request, 'theaters/dashboard.html', {'showings': showings})

def organizer_showing_detail(request, pk):
    organizer = get_object_or_404(Organizer, user=request.user)
    showing = Showing.objects.filter(event__organizer=organizer).get(pk=pk)
    cart = Cart.objects.filter(items=showing)
    orders = Order.objects.filter(cart=cart)
    return render(request, 'theaters/organier_showing_detail.html', {'showing': showing, 'orders': orders})