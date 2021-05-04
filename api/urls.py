from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('token-auth/', obtain_auth_token, name='obtain_auth_token'),
]
