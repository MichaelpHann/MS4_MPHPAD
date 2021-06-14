from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

import stripe


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51J2MEuJ1iwsklVWMliR9x7IJGwy6qFzhzh0jQKNoX9QHskdwjEMp9PSiGBW3gWBs9PDun1NprEYPpxgzWJw2oJEW00oL3N2OCC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
