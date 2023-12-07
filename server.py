from flask import Flask, request, jsonify,render_template,redirect,url_for
from sql_connection import get_sql_connection

app = Flask(__name__, static_url_path='/static')

#SQL Authentication
connection = get_sql_connection()

#This gets all the product info and puts them in a response array.
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

def filter_products_by_comapny(connection, filters):
    cursor = connection.cursor()
    query = "SELECT * FROM shop.products WHERE company IN %s"
    cursor.execute(query, (filters,))
    filtered_products = []

    for(id, name, descption, price, imageURL, company) in cursor:
        filtered_products.append(
            {
                'id': id,
                'name': name,
                'description': descption,
                'price': price,
                'imageURL':imageURL,
                'company': company
            }
        )
    return filtered_products



@app.route('/')
def index():
    return redirect(url_for('get_products'))

#This will get the array of products and ref them as products which will be used in the browse.html template.
@app.route('/get_products', methods=['GET'])
def get_products():
   products = get_all_products(connection)
   return render_template('browse.html',products=products)

@app.route('/filter_products', methods=['POST'])
def filter_products():
    filters = request.json.get('filters')
    filtered_products = filter_products_by_comapny(connection, filters)
    return jsonify(filtered_products)

  # API endpoint to handle adding products to cart
@app.route('/add_to_cart/<int:index>')
def add_to_cart(index):
    cart = []
    selected_product = request.json
    cart.append(selected_product)
    return jsonify({'message': 'Added to cart successfully'})


def calculate_cart_total(response):
    total_price = sum(item["price"] for item in response)
    return f'Total Price: ${total_price: .2f}'

if __name__ == '__main__':
    app.run(debug=True)
    
