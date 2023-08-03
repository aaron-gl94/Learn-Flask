from flask import Flask, jsonify, request;
from products import products

app = Flask(__name__)

@app.route('/ping')
def ping():
    return jsonify({"message": "pong!"})

@app.route('/products', methods=['GET'])
def getProducts():
    return jsonify({"products": products, "message": "Product list..."})

@app.route('/product/<string:product_name>')
def getProductByName(product_name):
    print(product_name)

    product_found = [product for product in products if product['name'] == product_name]

    if (len(product_found) > 0):
        return jsonify({'product': product_found[0]})
    return jsonify({'message': 'Product not found.'})

@app.route('/product', methods=['POST'])
def addProduct():
    new_product = {
        "name": request.json['name'],
        "price": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)

    print(new_product)
    return jsonify({"message": "The product was successfully added!", "products": products})

@app.route('/product/<product_name>', methods=['PUT'])
def updateProductByName(product_name):
    product_found = [product for product in products if product['name'] == product_name]
    
    if(len(product_found) > 0):
        product_found[0]['name'] = request.json['name']
        product_found[0]['price'] = request.json['price']
        product_found[0]['quantity'] = request.json['quantity']
        return jsonify({'messages': 'The product was successfully updated!', "product": product_found[0]})
    return jsonify({'messages': "Product Not updated."})

@app.route('/product/<product_name>', methods=['DELETE'])
def deleteProductByName(product_name):
    product_found = [product for product in products if product['name'] == product_name]

    if(len(product_found) > 0):
        products.remove(product_found[0])
        return jsonify({'messages': 'The product was successfully removed!', 'products': products})
    return jsonify({'message': 'Product Not found.'})

# Initialize Server
if __name__ == '__main__':
    app.run(debug = True, port = 4000)