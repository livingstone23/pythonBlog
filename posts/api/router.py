from rest_framework.routers import DefaultRouter
from posts.api.views import PostModelViewSet

# from posts.api.views import PostViewSet

router_post = DefaultRouter()

# router_post.register(prefix='posts', basename='posts', viewset=PostViewSet)
router_post.register(prefix='posts', basename='posts', viewset=PostModelViewSet)
