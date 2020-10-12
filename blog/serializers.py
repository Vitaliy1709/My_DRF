from rest_framework import serializers
from blog.models import *
from django.contrib.auth.models import User



class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='blog_post-highlight', format='html')

    class Meta:
        model = BlogPost
        fields = ['url', 'id', 'highlight', 'owner', 'title', 'slug', 'author',
                  'body', 'publish', 'created', 'updated', 'status']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='blog_post-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'blog']





class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'body', 'created', 'updated', 'active']


