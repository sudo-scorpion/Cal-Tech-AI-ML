from flask_restx import Namespace, Resource, fields
from app.services.product_service import add_product, get_all_products, update_product, delete_product

# Define the namespace
product_ns = Namespace('products', description='Product related operations.')

# Model for product data
product_model = product_ns.model('Product', {
    'id': fields.Integer(readOnly=True, description='The product unique identifier'),
    'name': fields.String(required=True, description='The product name'),
    'category_id': fields.Integer(required=True, description='The category id the product belongs to'),
    'price': fields.Float(required=True, description='The product price')
})

@product_ns.route('/')
class ProductList(Resource):
    @product_ns.marshal_list_with(product_model)
    def get(self):
        """List all products"""
        return get_all_products()

    @product_ns.expect(product_model)
    @product_ns.marshal_with(product_model, code=201)
    def post(self):
        """Create a new product"""
        data = product_ns.payload
        return add_product(data['name'], data['category_id'], data['price']), 201

@product_ns.route('/<int:id>')
@product_ns.response(404, 'Product not found')
@product_ns.param('id', 'The product identifier')
class Product(Resource):
    @product_ns.doc('delete_product')
    def delete(self, id):
        """Delete a product by id"""
        return delete_product(id)

    @product_ns.expect(product_model)
    @product_ns.marshal_with(product_model)
    def put(self, id):
        """Update a product by id"""
        data = product_ns.payload
        return update_product(id, data['name'], data['category_id'], data['price'])
