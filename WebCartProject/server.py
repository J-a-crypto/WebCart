from flask import Flask, request, jsonify,render_template,redirect,url_for,session
from sql_connection import get_sql_connection

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'Japupalo2003'
#SQL Authentication
connection = get_sql_connection()

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


def get_products_by_company(connection, company_name):
    cursor = connection.cursor()

    query = "SELECT * FROM shop.products WHERE company = %s"
    cursor.execute(query, (company_name,))

    response = []

    for (id, name, description, price, imageURL, company) in cursor:
        response.append(
            {
                'id': id,
                'name': name,
                'description': description,
                'price': price,
                'imageURL': imageURL,
                'company': company,
            }
        )

    return response

def get_product_by_id(connection, product_id):
    cursor = connection.cursor()

    query = "SELECT * FROM shop.products WHERE ProductID = %s"
    cursor.execute(query, (product_id,))

    product = cursor.fetchone()

    if product:
        id, name, description, price, imageURL, company = product
        product_details = {
            'id': id,
            'name': name,
            'description': description,
            'price': price,
            'imageURL': imageURL,
            'company': company,
        }
        return product_details

    return None
@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username == 'Japupalo' and password == '123':
            session['logged_in'] = True
            session['cart'] = []
            return redirect(url_for('get_products'))
        else:
            error_message = "Incorrect Username or Password. Please try again!"
    
    return render_template('index.html', error_message = error_message)

@app.route('/get_products', methods=['GET'])
def get_products():
   if 'logged_in' not in session or not session['logged_in']:
       return redirect(url_for('login'))
   
   company_filter = request.args.get('company')
   if company_filter:
       products = get_products_by_company(connection, company_filter)
   else:
        products = get_all_products(connection)
   return render_template('browse.html', products=products)

 
         
  # API endpoint to handle adding products to cart
@app.route('/add_to_cart/<product_id>', methods=['GET'])
def add_to_cart(product_id):
    product_id_str = str(product_id)
    product = get_product_by_id(connection, product_id_str)
    if product:
     # Initialize cart if not present in session
            
        session['cart']=[]
        session['cart'].append(product)
        
        print("cart contents:", session['cart'])
        
        return jsonify({'success': True, 'message': 'Product added to cart successfully'})
    else:
        return jsonify({'success': False, 'message': 'Product not found'}), 404
    


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():

    cart = session.get('cart',[])  # Retrieve the user's cart from the session

    total_price = sum(product['price'] for product in cart)
    
    print('Cart contents:', cart)
    app.logger.debug("cart conntents: %s", cart)
    
    if request.method == 'POST':
        # Perform checkout logic, e.g., update database, send confirmation email, etc.
        # Clear the cart after checkout
        session['cart'] = []
        return redirect(url_for('get_products'))

    return render_template('checkout.html', cart=cart, total_price=total_price)

if __name__ == '__main__':
    
    app.run(debug=True)
    
