# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
#
# #from blog.views import views*
#
#
#
# from blog.views import BlogPostViewSet, UserViewSet, api_root
# from rest_framework import renderers
#
# blog_post_list = BlogPostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# blog_post_detail = BlogPostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = BlogPostViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'blog_post', views.BlogPostViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]


# urlpatterns = format_suffix_patterns([
#     path('', api_root),
#     path('blog/', blog_post_list, name='blog_post-list'),
#     path('blog/<int:pk>/', blog_post_detail, name='blog_post-detail'),
#     path('blog/<int:pk>/highlight/', snippet_highlight, name='blog_post-highlight'),
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
#     # path('blog/', views.CommentList.as_view()),
#     # path('blog/<int:pk>/', views.CommentDetail.as_view()),
# ])

