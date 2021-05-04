from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<post_pk>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('posts/<int:post_pk>/comments/', CommentViewSet.as_view(  # TODO Ref-r in classbased way
    #     {'get': 'list', 'post': 'create'})),
    # path('posts/<int:post_pk>/comments/<int:pk>/', CommentViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})),
]

urlpatterns += [
    path('token-auth/', obtain_auth_token, name='obtain_auth_token'),
]
