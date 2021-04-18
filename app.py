from flask import Flask, jsonify, request

#crear el servidor e inicializarlo:
app = Flask(__name__)

from products import products

#comenzamos entragando datos, creando productos:
@app.route('/ping')
def ping():
    return jsonify({"message": "pong"})

@app.route('/products', methods = ['GET'])
def getProducts():
    return jsonify({'products': products, 'message': 'Products list'})

@app.route('/products/<string:product_name>', methods = ['GET'])
def getProduct(product_name):
    #recorremos la lista de productos con un bucle y comparamos
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({'message': 'Product not found'})

@app.route('/products', methods = ['POST'])
def addProduct():
    newProduct = {
        "name" : request.json['name'],
        "price":  request.json['price'],
        "quantity":  request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({"message": "Product added sucessfully", "products": products})

@app.route('/products/<string:product_name>', methods = ['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if(len(productFound)) > 0:
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'Product updated',
            'product': productFound[0]
            })
    return jsonify({'message': 'Product not found'})

@app.route('/products/<string:product_name>', methods = ['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if len(productFound[0]) > 0:
        products.remove(productFound[0])
        return jsonify({
            'message': 'Product deleted',
            'products': products
        })
    return jsonify({'message': 'Product not found'})


if __name__ == '__main__':
    app.run(debug=True, port=4000)

