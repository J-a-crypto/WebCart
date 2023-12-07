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


@app.route('/')
def index():
    return redirect(url_for('get_products'))

#This will get the array of products and ref them as products which will be used in the browse.html template.
@app.route('/get_products', methods=['GET'])
def get_products():
   products = get_all_products(connection)
   return render_template('browse.html',products=products)
if __name__ == '__main__':
    app.run(debug=True)
    
