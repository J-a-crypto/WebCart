from flask import Flask, render_template, jsonify

# tech products data
techProducts = [
    {
        'name': 'Laptop',
        'description': 'Powerful laptop for all your computing needs.',
        'price': 999.99,
        'imageURL': 'https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craig-dennis-205421.jpg&fm=jpg'
        
    },
    {
        'name': 'Laptop',
        'description': 'Powerful laptop for all your computing needs.',
        'price': 999.99,
        'imageURL': 'https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craig-dennis-205421.jpg&fm=jpg'
    },
     {
        'name': 'Laptop',
        'description': 'Powerful laptop for all your computing needs.',
        'price': 999.99,
        'imageURL': 'https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craig-dennis-205421.jpg&fm=jpg'
    },
     {
        'name': 'Laptop',
        'description': 'Powerful laptop for all your computing needs.',
        'price': 999.99,
        'imageURL': 'https://images.pexels.com/photos/205421/pexels-photo-205421.jpeg?cs=srgb&dl=pexels-craig-dennis-205421.jpg&fm=jpg'
    },
    # ... other product data
]

@app.route('/')
def index():
    return render_template('product.html', products=techProducts)

# API endpoint to handle adding products to cart
@app.route('/add_to_cart/<int:index>')
def add_to_cart(index):
    
    selected_product = techProducts[index]
   
    cart = []
    cart.append(selected_product)
    return jsonify({'message': 'Added to cart successfully'})

def calculate_cart_total(techProducts):
    total_price = sum(item["price"] for item in techProducts)
    return f'Total Price: ${total_price: .2f}'

