from flask import Flask, request, jsonify
from sql_connection import get_sql_connection

app = Flask(__name__)

#SQL Authentication
connection = get_sql_connection()

@app.route('/')

@app.route('/getData', methods=['GET'])
def get_products():
    products = get_all_products(connection)
    response = jsonify(products)
    return response

def get_all_products(connection):
    cursor = connection.cursor()
    
    query = ("select products.id, products.name, products.company, ")
    
    cursor.execute(query)
    
    response =[]
    
    for(id, name, company, description, price, imageURL) in cursor:
        response.append(
            {
            'id': id,
            'name': name,
            'company' : company,
            'description' : description,
            'price' : price,
            'imageURL' : imageURL
            }
        )
    return response
    