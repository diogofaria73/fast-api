from infrastructure.routes.blog_routes import get_routes as get_blog_routes
from infrastructure.routes.blog_routes import post_routes as post_blog_routes

router_list = [
    get_blog_routes,
    post_blog_routes
]
