# Django E-Commerce Website

A simple single-vendor e-commerce website built with Django, SQLite, HTML, CSS, JavaScript, and Bootstrap.

This project allows users to browse products, view product details, add products to a session-based shopping cart, update quantities, checkout, and place orders. The admin panel is used to manage products, categories, customers, and orders.

---

## Features

### Product Management
- Product listing page
- Product detail page
- Product categories
- Product images
- Product price and description
- Stock quantity management
- Featured products

### Shopping Cart
- Add products to cart
- Increase product quantity
- Decrease product quantity
- Remove products from cart
- Automatic subtotal calculation
- Automatic cart total calculation
- Session-based cart

### Checkout
- Customer name input
- Phone number input
- Delivery address input
- Order summary
- Stock availability validation
- Order creation
- Automatic stock reduction after successful order
- Cart is cleared after placing an order
- Order success page

### Admin Panel
- Manage product categories
- Add/edit/delete products
- Manage product prices
- Manage product stock
- Mark products as featured
- View customers
- View addresses
- View placed orders

### Frontend
- Bootstrap 5 responsive design
- Responsive product cards
- Responsive cart page
- Responsive checkout page
- Navigation bar
- Footer
- Home page
- Product search using JavaScript

---

## Technologies Used

- Python
- Django 6.1.1
- SQLite
- HTML5
- CSS3
- JavaScript
- Bootstrap 5.3.3
- Pillow
- python-dotenv

---

## Project Structure


```text
django-ecommerce/
│
├── accounts/
│   ├── migrations/
│   ├── models.py
│   ├── admin.py
│   └── ...
│
├── products/
│   ├── migrations/
│   ├── static/
│   │   └── products/
│   │       └── js/
│   │           └── script.js
│   │
│   ├── templates/
│   │   └── products/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── product_list.html
│   │       ├── product_detail.html
│   │       ├── cart.html
│   │       ├── checkout.html
│   │       └── order_success.html
│   │
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── shared/
│   ├── migrations/
│   └── models.py
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md

###Database Models

The project uses SQLite as the database.

ProductCategory

Stores product categories.

Main fields:

Category name
Category slug
Product

Stores product information.

Main fields:

Category
Product name
Price
Description
Image
Quantity
Featured status
###Customer

Stores customer information and connects customers with Django users.

###Address

Stores customer delivery address information.

###Order

Stores placed order information.

Main fields:

Customer
Product
Quantity
Total price
Created date

```
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/df0e78f3-467b-4ba3-ab86-1fd6e787f593" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/392e4c3b-abb5-40b0-9448-f18c58a77826" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/fed0e328-22c3-46d4-9ea6-82ce5bf4a6d4" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/8f15da3c-cdf2-4c4d-b456-e276c8e14208" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/b8f6c17b-ead7-4105-8203-f32917e229dd" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/eb0d37e5-4f8c-4629-b3a0-3cd14321510e" />
<img width="1920" height="1040" alt="image" src="https://github.com/user-attachments/assets/9dc6330c-6e4d-40ff-afab-5fb495524294" />






