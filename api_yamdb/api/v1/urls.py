from django.urls import include, path
from rest_framework import routers

from api.v1.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                          ReviewViewSet, TitleViewSet, UserViewSet,
                          obtain_token, signup)

router = routers.DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register('users', UserViewSet, basename='user')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')

auth_patterns = [
    path('signup/', signup, name='signup'),
    path('token/', obtain_token, name='token')
]

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(auth_patterns))
]
