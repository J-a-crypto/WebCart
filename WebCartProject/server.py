from flask import Flask, request, jsonify,render_template,redirect,url_for,session
from sql_connection import get_sql_connection
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Japupalo2003'
#SQL Authentication
connection = get_sql_connection()

cart=[]

def get_all_products(connection):
    cursor = connection.cursor()
    
    query = ("SELECT * FROM shop.products")
    
    cursor.execute(query)
    
    response = []
    
    for(id, name, description, price, imageURL,company) in cursor:
        response.append(
            {
            'id': id,
            'name': name,
            'description' : description,
            'price' : price,
            'imageURL' : imageURL,
            'company' : company,
            }
        )
    return response
@app.route('/')
def index():
    return redirect(url_for('get_products'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'Japupalo' and password == '123':
            session['logged_in'] = True
            return redirect(url_for('get_products'))
        else:
            error_message = "Incorrect Username or Password. Please try again!"
    
    return render_template('index.html', error_message = error_message)

@app.route('/get_products', methods=['GET'])
def get_products():
   if 'logged_in' not in session or not session['logged_in']:
       return redirect(url_for('login'))
   
   products = get_all_products(connection)
   return render_template('browse.html', products=products)

  # API endpoint to handle adding products to cart
@app.route('/add_to_cart/<int:index>')
def add_to_cart(index):
    selected_product = index
    cart.append(selected_product)
    return jsonify({'message': 'Added to cart successfully'})


#still trying to figure this out with the new examples we got
#I don't think this works because the products is in the function get_products, not global
def calculate_cart_total(Products):
    total_price = sum(product["price"] for product in Products)
    return f'Total Price: ${total_price: .2f}'



if __name__ == '__main__':
    app.run(debug=True)
    
