from flask_restx import Namespace, Resource, fields
from app.services.category_service import add_category, get_all_categories, update_category, delete_category

# Define the namespace
category_ns = Namespace('categories', description='Category related operations.')

# Request and response model for categories
category_model = category_ns.model('Category', {
    'name': fields.String(required=True, description='The category name'),
})

@category_ns.route('/')
class CategoryList(Resource):
    @category_ns.marshal_list_with(category_model)
    def get(self):
        """List all categories"""
        return get_all_categories()

    @category_ns.expect(category_model)
    @category_ns.marshal_with(category_model, code=201)
    def post(self):
        """Create a new category"""
        data = category_ns.payload
        return add_category(data['name']), 201

@category_ns.route('/<int:id>')
@category_ns.response(404, 'Category not found')
@category_ns.param('id', 'The category identifier')
class Category(Resource):
    @category_ns.doc('delete_category')
    def delete(self, id):
        """Delete a category by id"""
        return delete_category(id)

    @category_ns.expect(category_model)
    @category_ns.marshal_with(category_model)
    def put(self, id):
        """Update a category by id"""
        data = category_ns.payload
        return update_category(id, data['name'])
