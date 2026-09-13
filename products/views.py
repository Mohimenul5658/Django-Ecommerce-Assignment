from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User

from accounts.models import customer, Address
from .models import Product, Order


def home(request):
    featured_products = Product.objects.filter(is_featured=True)

    context = {
        "featured_products": featured_products,
    }

    return render(request, "products/home.html", context)


def product_list(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, "products/product_list.html", context)


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        "product": product
    }

    return render(request, "products/product_detail.html", context)


def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = request.session.get("cart", {})

    product_id = str(product.id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["cart"] = cart

    return redirect("cart")


def cart(request):
    cart_data = request.session.get("cart", {})

    cart_items = []
    total_price = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity
        total_price += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "products/cart.html", context)


def increase_quantity(request, id):
    cart = request.session.get("cart", {})
    product_id = str(id)

    if product_id in cart:

        product = get_object_or_404(Product, id=id)

        if cart[product_id] < product.quantity:
            cart[product_id] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def decrease_quantity(request, id):
    cart = request.session.get("cart", {})
    product_id = str(id)

    if product_id in cart:

        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def remove_from_cart(request, id):
    cart = request.session.get("cart", {})
    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


def checkout(request):

    cart_data = request.session.get("cart", {})

    if not cart_data:
        return redirect("cart")

    cart_items = []
    total_price = 0

    # Prepare cart information
    for product_id, quantity in cart_data.items():

        product = get_object_or_404(Product, id=product_id)

        subtotal = product.price * quantity
        total_price += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    # Place order
    if request.method == "POST":

        name = request.POST.get("name")
        phone = request.POST.get("phone")
        address_line = request.POST.get("address")

        # Check stock before creating any order
        for product_id, quantity in cart_data.items():

            product = get_object_or_404(Product, id=product_id)

            if product.quantity < quantity:

                return render(
                    request,
                    "products/checkout.html",
                    {
                        "cart_items": cart_items,
                        "total_price": total_price,
                        "error": f"Not enough stock for {product.product_name}.",
                    }
                )

        # Create user
        username = f"customer_{phone}"

        user, created = User.objects.get_or_create(
            username=username,
            defaults={
                "first_name": name,
            }
        )

        # Create address
        address = Address.objects.create(
            country="Bangladesh",
            city="Chattogram",
            postal_code="",
            address_line=address_line,
        )

        # Create customer
        customer_obj, created = customer.objects.get_or_create(
            user=user,
            defaults={
                "phone": phone,
            }
        )

        customer_obj.address.add(address)

        # Create orders and reduce stock
        for product_id, quantity in cart_data.items():

            product = get_object_or_404(Product, id=product_id)

            Order.objects.create(
                customer=customer_obj,
                product=product,
                quantity=quantity,
                total_price=product.price * quantity,
            )

            product.quantity -= quantity
            product.save()

        # Clear cart
        request.session["cart"] = {}
        request.session.modified = True

        return render(
            request,
            "products/order_success.html"
        )

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(
        request,
        "products/checkout.html",
        context
    )