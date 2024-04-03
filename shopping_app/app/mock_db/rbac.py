# RBAC configuration
roles_permissions = {
    'admin': [
        'add_product', 
        'delete_product', 
        'view_orders', 
        'add_category', 
        'delete_category', 
        'view_users', 
        'update_user',  # Assuming admins can update user details
        'view_products',  # Admins should likely also be able to view products
        'view_categories'  # And view categories
    ],
    'user': [
        'place_order', 
        'view_products', 
        'add_to_cart', 
        'view_cart',  # Assuming users need to view their cart
        'delete_from_cart',  # Assuming users might want to remove items from their cart
        'update_cart',  # Assuming users can change quantities in their cart
        'checkout',  # Assuming there's a checkout action
        'view_categories',  # Users should be able to view categories to browse products
        'update_user'  # Assuming users can update their own details
    ]
}
